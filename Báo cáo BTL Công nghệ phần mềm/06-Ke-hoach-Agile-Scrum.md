# 6. KẾ HOẠCH TRIỂN KHAI THEO MÔ HÌNH AGILE/SCRUM

## 6.1. Tại sao chọn Agile/Scrum?

### Phù hợp với đặc điểm dự án

| Đặc điểm dự án | Lý do chọn Agile/Scrum |
|---|---|
| **Yêu cầu phức tạp** | Thu thập feedback sớm từ BTC và nhân viên, điều chỉnh kịp thời |
| **Quy mô vừa phải** | Team 4-6 người, phù hợp với Scrum team lý tưởng |
| **Thời gian giới hạn** | Sprint 2 tuần, giao sản phẩm từng phần, demo liên tục |
| **Nhiều stakeholder** | BTC, nhân viên, trưởng team có nhu cầu khác nhau |

### Lợi ích mong đợi

- ✅ **Phản hồi nhanh**: Demo sau mỗi sprint, điều chỉnh kịp thời
- ✅ **Giảm rủi ro**: Phát hiện sớm vấn đề kỹ thuật và nghiệp vụ
- ✅ **Tăng tính minh bạch**: Daily standup, sprint review với stakeholder
- ✅ **Linh hoạt thay đổi**: Điều chỉnh backlog theo feedback thực tế

---

## 6.2. Cấu trúc nhóm Scrum

### Vai trò trong team

| Vai trò | Trách nhiệm | Số lượng |
|---|---|---|
| **Product Owner** | Quản lý Product Backlog, quyết định ưu tiên, chấp nhận sản phẩm | 1 |
| **Scrum Master** | Hỗ trợ team làm việc hiệu quả, giải quyết trở ngại, bảo vệ quy trình | 1 |
| **Development Team** | Lập trình, test, thiết kế UI/UX, deploy | 4-5 người |

### Phân công cụ thể

**Product Owner:**
- Thu thập yêu cầu từ BTC (stakeholder thực tế)
- Viết và ưu tiên User Stories
- Tham gia Sprint Review, chấp nhận Definition of Done

**Scrum Master:**
- Tổ chức các Scrum ceremonies (Daily, Planning, Review, Retro)
- Loại bỏ blockers cho team
- Coaching team về Agile mindset

**Development Team:**
- **Backend Developer** (2 người): FastAPI, database, business logic
- **Frontend Developer** (2 người): React, UI components, responsive
- **Full-stack** (1 người): Chatbot, integration, deployment

---

## 6.3. Quy trình Scrum

### Sprint Overview

```
Sprint 0 (1 tuần) → Sprint 1 (2 tuần) → Sprint 2 (2 tuần) → Sprint 3 (2 tuần) → Sprint 4 (2 tuần)
Setup & Planning      Module đăng ký      Phân bổ bay/xe       Gala & My Journey    Polish & Deploy
```

### Các ceremonies

| Ceremony | Thời lượng | Mục đích |
|---|---|---|
| **Sprint Planning** | 4 giờ (đầu sprint) | Chọn User Stories, chia task, cam kết sprint goal |
| **Daily Standup** | 15 phút (mỗi ngày) | Chia sẻ tiến độ, blockers, kế hoạch hôm nay |
| **Sprint Review** | 2 giờ (cuối sprint) | Demo sản phẩm cho stakeholder, thu feedback |
| **Sprint Retrospective** | 1.5 giờ (sau review) | Đánh giá quy trình, cải tiến sprint sau |

---

## 6.4. Product Backlog

### Ưu tiên theo MoSCoW

#### Must Have (Sprint 1-2)

| ID | User Story | Story Points | Sprint |
|---|---|---|---|
| US-01 | Đăng ký tham gia Team Building | 5 | 1 |
| US-04 | Dashboard theo dõi đăng ký | 5 | 1 |
| US-05 | Phân bổ chuyến bay tự động | 13 | 2 |
| US-07 | Phân xe tự động theo chặng | 13 | 2 |
| US-13 | Chuyển trạng thái kỳ TB | 3 | 1 |

**Tổng Sprint 1+2:** ~39 points

#### Should Have (Sprint 3)

| ID | User Story | Story Points | Sprint |
|---|---|---|---|
| US-09 | Chọn chỗ ngồi Gala Dinner | 21 | 3 |
| US-11 | Xem My Journey | 8 | 3 |
| US-06 | Điều chỉnh phân bổ thủ công | 8 | 3 |

**Tổng Sprint 3:** ~37 points

#### Could Have (Sprint 4)

| ID | User Story | Story Points | Sprint |
|---|---|---|---|
| US-02 | Sửa thông tin đăng ký | 3 | 4 |
| US-08 | Chỉ định Trưởng xe | 5 | 4 |
| US-12 | Chatbot RAG | 13 | 4 |
| US-14 | Xem audit log | 3 | 4 |

**Tổng Sprint 4:** ~24 points

---

## 6.5. Sprint Breakdown

### Sprint 0: Setup & Foundation (1 tuần)

**Mục tiêu:**
- Cài đặt môi trường dev
- Setup CI/CD pipeline cơ bản
- Thiết kế database schema
- Tạo project structure

**Deliverables:**
- Repository với cấu trúc frontend/backend
- Docker Compose cho local dev
- Database migration đầu tiên
- Authentication cơ bản (JWT)

---

### Sprint 1: Đăng ký & Quản lý kỳ TB (2 tuần)

**Sprint Goal:** Nhân viên có thể đăng ký tham gia, BTC có thể theo dõi

**User Stories:**
- US-01: Đăng ký tham gia (5 pts)
- US-04: Dashboard theo dõi đăng ký (5 pts)
- US-13: Chuyển trạng thái kỳ (3 pts)

**Tasks:**
- Backend: API tạo kỳ, API đăng ký, API dashboard
- Frontend: Form đăng ký nhiều bước, dashboard BTC
- Test: Unit test cho business logic đăng ký

**Definition of Done:**
- ✅ Nhân viên đăng ký được và nhận email xác nhận
- ✅ BTC thấy số lượng đã đăng ký theo team
- ✅ Code review passed, test coverage ≥ 70%

**Demo:**
- Nhân viên đăng ký flow end-to-end
- Dashboard hiển thị thống kê real-time

---

### Sprint 2: Phân bổ chuyến bay & xe (2 tuần)

**Sprint Goal:** BTC có thể phân bổ tự động chuyến bay và xe

**User Stories:**
- US-05: Phân bổ chuyến bay tự động (13 pts)
- US-07: Phân xe tự động (13 pts)

**Tasks:**
- Backend: 
  - Thuật toán phân bổ chuyến bay (greedy by team)
  - API nhập chuyến bay, preview, confirm
  - Thuật toán phân xe theo chặng
- Frontend:
  - UI nhập chuyến bay
  - Preview table với cảnh báo
  - UI cấu hình xe theo chặng
- Test: Unit test thuật toán, integration test API

**Definition of Done:**
- ✅ Phân bổ 100 người trong ≤5 giây
- ✅ Team cùng chuyến bay, không vượt slot
- ✅ Xe phân đúng điểm đón, không vượt sức chứa
- ✅ Test coverage thuật toán ≥ 80%

**Demo:**
- Import 100 người, nhập chuyến bay, phân bổ tự động
- Hiển thị kết quả và cảnh báo team bị tách
- Phân xe 4 chặng, kiểm tra logic gom theo chuyến bay

---

### Sprint 3: Gala Dinner & My Journey (2 tuần)

**Sprint Goal:** Nhân viên xem được hành trình, Team Leader chọn ghế Gala

**User Stories:**
- US-09: Chọn chỗ ngồi Gala (21 pts)
- US-11: Xem My Journey (8 pts)
- US-06: Điều chỉnh phân bổ thủ công (8 pts)

**Tasks:**
- Backend:
  - API sơ đồ Gala, bốc thăm, hold/lock ghế
  - Websocket cho real-time update ghế
  - API My Journey (aggregate data)
- Frontend:
  - Canvas 2D cho sơ đồ Gala, drag-drop bàn
  - UI chọn ghế với countdown hold
  - Dashboard My Journey mobile-first
  - UI điều chỉnh thủ công (move CBNV giữa chuyến bay)
- Test: Race condition test cho seat lock

**Definition of Done:**
- ✅ 2 team chọn cùng lúc không bị conflict
- ✅ Hold timeout 120s hoạt động đúng
- ✅ My Journey hiển thị đầy đủ: bay, xe, phòng, Gala
- ✅ Mobile responsive (iPhone SE, Pixel 5)

**Demo:**
- BTC random thứ tự team
- Team Leader chọn ghế, hold, confirm
- Nhân viên xem My Journey trên điện thoại (responsive)

---

### Sprint 4: Chatbot, Polish & Deploy (2 tuần)

**Sprint Goal:** Hoàn thiện tính năng bổ sung, chuẩn bị production

**User Stories:**
- US-12: Chatbot RAG (13 pts)
- US-02: Sửa đăng ký (3 pts)
- US-08: Chỉ định Trưởng xe (5 pts)
- US-14: Audit log (3 pts)

**Tasks:**
- Backend:
  - Tích hợp OpenAI/Anthropic cho chatbot
  - RAG với vector database (ChromaDB)
  - Tool calling cho personal journey query
  - API sửa đăng ký, audit log
- Frontend:
  - UI chatbot widget
  - Form sửa đăng ký
  - Bảng audit log với filter
- DevOps:
  - Production deployment checklist
  - Database backup/restore
  - Monitoring (logs, errors)

**Definition of Done:**
- ✅ Chatbot trả lời đúng quy định và hành trình cá nhân
- ✅ Không lộ dữ liệu người khác (security test)
- ✅ Audit log ghi đầy đủ mọi thay đổi quan trọng
- ✅ Production deploy thành công, smoke test passed

**Demo:**
- Chatbot trả lời câu hỏi về quy định và hành trình
- Sửa đăng ký, xem audit log
- Chỉ định Trưởng xe, nhận email thông báo

---

## 6.6. Velocity & Timeline

### Dự tính velocity

**Giả định:**
- Team 5 người, mỗi người ~6-8 points/sprint (làm part-time như đồ án)
- Velocity trung bình: **30-40 points/sprint**

### Timeline tổng thể

| Sprint | Thời gian | Story Points | Milestone |
|---|---|---|---|
| Sprint 0 | Tuần 1 | - | Dev environment ready |
| Sprint 1 | Tuần 2-3 | 13 | Đăng ký working |
| Sprint 2 | Tuần 4-5 | 26 | Phân bổ tự động working |
| Sprint 3 | Tuần 6-7 | 37 | Gala + My Journey working |
| Sprint 4 | Tuần 8-9 | 24 | MVP complete, deployed |

**Tổng thời gian:** ~9 tuần (2 tháng rưỡi)

---

## 6.7. Definition of Done (DoD)

### Cấp độ User Story

Một User Story được coi là Done khi:

- ✅ Code đã được viết và pass tất cả test
- ✅ Code review bởi ít nhất 1 member khác
- ✅ Unit test coverage ≥ 70% cho business logic
- ✅ Integration test passed (API end-to-end)
- ✅ UI responsive trên mobile & desktop
- ✅ Tài liệu API (nếu có endpoint mới)
- ✅ Acceptance Criteria của User Story đạt 100%
- ✅ Demo thành công cho Product Owner

### Cấp độ Sprint

Một Sprint được coi là Done khi:

- ✅ Tất cả User Stories trong sprint đạt DoD
- ✅ Sprint Review được tổ chức, stakeholder chấp nhận
- ✅ Code merged vào branch `main`
- ✅ Deploy lên staging environment thành công
- ✅ Regression test passed (không làm hỏng tính năng cũ)

---

## 6.8. Công cụ hỗ trợ

### Quản lý dự án

| Công cụ | Mục đích |
|---|---|
| **Jira / Trello** | Product Backlog, Sprint Board, Burndown Chart |
| **Confluence / Notion** | Tài liệu, Meeting notes, Retrospective |
| **Slack / Discord** | Giao tiếp team, daily standup async |

### Development

| Công cụ | Mục đích |
|---|---|
| **GitHub** | Source control, Pull Request, Code Review |
| **GitHub Actions** | CI/CD: test tự động, deploy staging |
| **Docker Compose** | Local dev environment |
| **Postman** | API testing |

### Monitoring & Quality

| Công cụ | Mục đích |
|---|---|
| **Pytest** | Backend unit & integration test |
| **Vitest / Jest** | Frontend unit test |
| **Playwright** | E2E test |
| **SonarQube** | Code quality, coverage |

---

## 6.9. Rủi ro & Biện pháp giảm thiểu

### Rủi ro kỹ thuật

| Rủi ro | Xác suất | Tác động | Biện pháp |
|---|---|---|---|
| Thuật toán phân bổ chậm (>5s) | Trung bình | Cao | Spike research thuật toán từ Sprint 1, optimize sớm |
| Gala seat lock race condition | Cao | Cao | Test kỹ, dùng database transaction lock |
| Chatbot trả lời sai hoặc lộ data | Trung bình | Rất cao | Unit test tool calling, security review |
| Team thiếu kinh nghiệm Scrum | Cao | Trung bình | Scrum Master coaching, retrospective cải tiến |

### Rủi ro quản lý

| Rủi ro | Xác suất | Tác động | Biện pháp |
|---|---|---|---|
| Member nghỉ giữa chừng | Thấp | Cao | Pair programming, knowledge sharing |
| Scope creep (stakeholder thêm yêu cầu) | Cao | Trung bình | Product Owner kiên quyết bảo vệ sprint goal |
| Deadline bị dồn (thi, deadline môn khác) | Cao | Trung bình | Buffer 1 tuần, giảm scope nếu cần |

---

## 6.10. Kết luận

Kế hoạch Agile/Scrum cho phép:

- ✅ **Giao sản phẩm sớm**: Demo working software sau Sprint 1
- ✅ **Linh hoạt thay đổi**: Điều chỉnh backlog dựa trên feedback
- ✅ **Giảm rủi ro**: Phát hiện vấn đề kỹ thuật sớm qua integration liên tục
- ✅ **Tăng chất lượng**: DoD chặt chẽ, test coverage cao
- ✅ **Team học hỏi**: Retrospective giúp cải tiến quy trình

Với kế hoạch này, team tự tin hoàn thành **MVP trong 9 tuần** với chất lượng cao, sẵn sàng deploy thực tế.