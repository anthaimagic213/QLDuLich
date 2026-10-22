"""Kiểm tra adapter TrollLLM không cần gửi request ra mạng."""

import asyncio
from types import SimpleNamespace

from app.core.config import settings
from app.rag.llm import ExtractiveLLM, OpenAICompatibleLLM, _to_openai_llm_error
from app.rag.prompts import Turn
from app.rag.runtime import get_llm


def test_provider_requires_its_own_key(monkeypatch):
    monkeypatch.setattr(settings, "LLM_PROVIDER", "openai")
    monkeypatch.setattr(settings, "LLM_API_KEY", "")
    monkeypatch.setattr(settings, "GEMINI_API_KEY", "gemini-only")
    get_llm.cache_clear()
    try:
        assert isinstance(get_llm(), ExtractiveLLM)
    finally:
        get_llm.cache_clear()


def test_openai_streams_multiple_requests_without_blocking(monkeypatch):
    monkeypatch.setattr(settings, "LLM_PROVIDER", "openai")
    monkeypatch.setattr(settings, "LLM_API_KEY", "test-key")
    monkeypatch.setattr(settings, "LLM_BASE_URL", "https://chat.trollllm.xyz/v1")
    monkeypatch.setattr(settings, "LLM_MODEL", "gpt-6.1-sol")
    get_llm.cache_clear()
    try:
        llm = get_llm()
        assert isinstance(llm, OpenAICompatibleLLM)
        assert llm.configured and llm.name == "gpt-6.1-sol"
        assert str(llm._client.base_url) == "https://chat.trollllm.xyz/v1/"

        started = asyncio.Event()
        release = asyncio.Event()
        requests = []

        async def create(**kwargs):
            requests.append(kwargs)
            if len(requests) == 2:
                started.set()
            await release.wait()

            async def chunks():
                yield SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content="Xin "))])
                await asyncio.sleep(0)
                yield SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content="chào"))])

            return chunks()

        monkeypatch.setattr(llm._client.chat.completions, "create", create)

        async def consume(question):
            return "".join([piece async for piece in llm.stream(
                system="Chỉ dùng tài liệu công khai", turns=[Turn("user", question)], hits=[]
            )])

        async def run():
            tasks = [asyncio.create_task(consume(question)) for question in ("Một", "Hai")]
            try:
                await asyncio.wait_for(started.wait(), timeout=2)
                release.set()
                return await asyncio.wait_for(asyncio.gather(*tasks), timeout=2)
            finally:
                release.set()
                for task in tasks:
                    task.cancel()

        assert asyncio.run(run()) == ["Xin chào", "Xin chào"]
        assert all(request["model"] == "gpt-6.1-sol" and request["stream"] for request in requests)
        assert [request["messages"][-1]["content"] for request in requests] == ["Một", "Hai"]
    finally:
        get_llm.cache_clear()


def test_openai_errors_do_not_leak_provider_messages():
    assert _to_openai_llm_error(SimpleNamespace(status_code=401)).code == "LLM_NOT_CONFIGURED"
    assert _to_openai_llm_error(SimpleNamespace(status_code=429)).code == "LLM_QUOTA_EXCEEDED"
    assert _to_openai_llm_error(SimpleNamespace(status_code=None)).code == "LLM_UNAVAILABLE"