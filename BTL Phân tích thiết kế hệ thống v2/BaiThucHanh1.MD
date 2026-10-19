# BÀI THỰC HÀNH 1 — Khám phá vấn đề và đề xuất hệ thống Team Building nội bộ

> **Đề tài:** Hệ thống quản lý kỳ Team Building nội bộ. **Trạng thái:** bản hoạch định để nhóm khảo sát và hoàn thiện, không phải kết quả nghiên cứu người dùng đã xác nhận.
>
> **Căn cứ:** `D:/QLDuLich/nội-dung-thực-hành-1-pttkht.md` (các nhiệm vụ 1–5, Problem Discovery Report, Business Requirement và System Request); `D:/QLDuLich/Báo cáo BTL-PTTKHT/01-Dat-van-de.md`, `02-Phan-tich-nghiep-vu.md`; `D:/QLDuLich/docs/product-overview.md` và `01-requirements.md` (bối cảnh/phạm vi sản phẩm). Các tài liệu dự án là **nguồn mô tả**, không thay thế phỏng vấn hoặc số liệu đo tại doanh nghiệp.

## 1. Executive Summary — kết luận sơ bộ

Trong kỳ Team Building nội bộ, CBNV cần biết mình đã đăng ký thành công hay chưa và, sau khi BTC công bố, cần xác định đúng thông tin di chuyển, lưu trú, lịch trình của bản thân. Tài liệu dự án mô tả hiện trạng dùng biểu mẫu, bảng tính và nhiều kênh trao đổi để tổng hợp/công bố thông tin; thay đổi ở một danh sách có thể không được phản ánh kịp ở danh sách khác. **Giả thuyết cần kiểm chứng:** sự phân tán này khiến CBNV phải đối chiếu hoặc hỏi lại BTC và tạo thêm công việc kiểm tra, trả lời, cập nhật cho BTC. Chưa có dữ liệu chứng minh mức độ ảnh hưởng, số lỗi hoặc chi phí. Nhóm sẽ khảo sát trước khi chốt đầu tư; cổng thông tin tập trung là **một phương án thử**, không phải định nghĩa của vấn đề.

**Phạm vi:** một hoặc nhiều kỳ Team Building của tổ chức; CBNV, BTC và các vai trò phối hợp. Không khảo sát bán tour công khai, thanh toán, đặt vé trực tiếp với nhà cung cấp. Trọng tâm bài thực hành là thông tin đăng ký và hành trình; phân bổ bay/xe/phòng là bối cảnh vận hành liên quan. Chatbot và ghế Gala không phải điều kiện để kiểm chứng vấn đề ưu tiên.

## 2. Background & Context — hiện trạng và nguồn thông tin

| Nội dung | Điều tài liệu mô tả | Mức độ tin cậy |
|---|---|---|
| Quy trình | BTC thu thông tin, tổng hợp đăng ký, lập danh sách bay/xe/phòng, xử lý sửa/hủy và công bố hành trình. | Mô hình As-Is trong `02-Phan-tich-nghiep-vu.md` §2.3; chưa quan sát thực địa. |
| Kênh | Biểu mẫu, bảng tính, email/nhóm trao đổi; các danh sách có thể được chỉnh riêng. | Mô tả tình huống trong `01-Dat-van-de.md` §1.2; chưa đo tần suất. |
| Người liên quan | CBNV cần đăng ký và tra cứu; BTC cần điều phối, cập nhật, giải đáp; trưởng nhóm/trưởng xe phối hợp theo vai trò. | `01-Dat-van-de.md` §1.6. |
| Tác động dự kiến | Có thể khó xác định bản cập nhật mới nhất, tra cứu bất tiện, phát sinh việc kiểm tra lại. | Rủi ro suy ra từ tài liệu; **chưa xác nhận** số lần hỏi, lỗi, thời gian hay tiền bạc. |

**Nghiên cứu cần thực hiện:** (1) phỏng vấn CBNV đã/chuẩn bị tham gia và BTC, có đại diện người đổi lịch/hủy; (2) quan sát một lượt đăng ký, công bố và một tình huống đổi chuyến; (3) đối chiếu các phiên bản biểu mẫu/danh sách, log câu hỏi và thời điểm cập nhật nếu được phép; (4) khảo sát ngắn để ước tính mức độ phổ biến sau khi đã hiểu nguyên nhân qua phỏng vấn. Xin phép, ẩn danh dữ liệu cá nhân; không thu thập/chia sẻ thông tin phòng hoặc di chuyển riêng tư ngoài phạm vi nghiên cứu.

## 3. User Needs → User Problem Statement (thực hành 1)

| Mã | Người dùng và nhu cầu (mục tiêu, không phải tính năng) | Bối cảnh/trở ngại cần tìm hiểu | Bằng chứng hiện có / tình trạng |
|---|---|---|---|
| N1 — **ưu tiên** | CBNV muốn xác nhận việc tham gia và biết thông tin hành trình **đúng, mới nhất của mình** để chuẩn bị đúng giờ/địa điểm. | Khi đăng ký, trước chuyến đi hoặc khi lịch trình thay đổi; thông tin có thể nằm ở nhiều kênh/bản danh sách. | Tài liệu mô tả nhiều danh sách và tra cứu bất tiện; **chưa xác minh** CBNV gặp trở ngại thường xuyên hoặc nguyên nhân chính là phân tán. |
| N2 | BTC muốn xác định danh sách đăng ký và phân bổ hiện hành để điều phối và xử lý thay đổi nhất quán. | Sau khi chốt đăng ký, phân bay/xe/phòng hoặc giải quyết hủy; có thể phải sửa nhiều bản. | Có mô hình quy trình và rủi ro không đồng bộ; **chưa đo** công sức/sai sót thực tế. |
| N3 | CBNV muốn biết yêu cầu sửa/hủy đã được tiếp nhận và xử lý ra sao để chủ động sắp xếp. | Khi kế hoạch cá nhân thay đổi; chưa rõ kênh nhận phản hồi và thời gian chờ. | Tài liệu có quy trình sửa/hủy; **chưa xác minh** mức độ khó khăn từ góc nhìn người dùng. |

**User Need Statement (N1):** CBNV tham gia một kỳ Team Building cần xác nhận tình trạng đăng ký và tra được thông tin di chuyển, lưu trú, lịch trình đáng tin cậy của chính mình để chủ động chuẩn bị và tránh phải phỏng đoán khi có thay đổi.

**User Problem Statement — phát biểu sơ bộ, sẽ sửa sau nghiên cứu:** CBNV tham gia kỳ Team Building nội bộ có thể gặp khó khăn khi xác định thông tin đăng ký và hành trình nào là thông tin hiện hành, nhất là trước ngày đi hoặc sau khi BTC điều chỉnh chuyến bay, xe hay phòng. Tài liệu dự án mô tả việc thông tin được tổng hợp và chia sẻ qua nhiều biểu mẫu, danh sách, kênh trao đổi; nếu các bản không được cập nhật nhất quán, CBNV có thể phải đối chiếu hoặc hỏi lại BTC để yên tâm chuẩn bị. Mức độ và nguyên nhân thực tế cần được phỏng vấn, quan sát kiểm chứng.

Không diễn đạt thành “CBNV cần app”: dù có ứng dụng, vấn đề vẫn tồn tại nếu BTC chưa kiểm tra và công bố thông tin đúng hoặc không thông báo thay đổi.

## 4. User Problem Statement Canvas (N1; thực hành 2)

| Thành phần | Nội dung sơ bộ và điều cần kiểm chứng |
|---|---|
| **User / Who** | CBNV tham gia kỳ Team Building, đặc biệt người có thông tin bay/xe/phòng thay đổi; chưa biết nhóm nào chịu ảnh hưởng nhiều nhất. |
| **Context / When, where** | Sau đăng ký, trước chuyến đi, khi BTC công bố hoặc thay đổi phân bổ; có thể tra cứu trên điện thoại khi di chuyển. |
| **Goal / Need** | Biết tình trạng đăng ký và thông tin hành trình đã được BTC xác nhận, đúng với cá nhân và kỳ đang tham gia. |
| **Pain / Problem** | Có thể khó xác định bản nào mới nhất, thiếu sự rõ ràng về trạng thái đã công bố; cần hỏi lại (giả thuyết). |
| **Alternatives hiện tại** | Xem email/nhóm chat, hỏi BTC hoặc trưởng nhóm, đối chiếu bảng/danh sách được chia sẻ (cần quan sát cách làm thực tế). |
| **Nhược điểm alternatives** | Có nguy cơ tin nhắn cũ hoặc nhiều bản mâu thuẫn; liên hệ thủ công có thể chậm (chưa xác minh). |
| **Emotional impact** | Giả thuyết: lo lắng, thiếu tự tin về giờ/địa điểm đi; hỏi trực tiếp để kiểm tra. Phỏng vấn để xác nhận, không áp cảm xúc cho mọi CBNV. |
| **Quantifiable impact** | Chưa có số liệu. Đề xuất đo số lần hỏi lại/kỳ, thời gian tìm đủ thông tin/người, số trường hợp nhận thông tin không nhất quán và thời gian BTC giải quyết. |
| **Evidence / Assumptions** | **Có trong tài liệu:** mô hình dùng nhiều danh sách/kênh và rủi ro thay đổi không đồng bộ. **Chưa biết:** CBNV gặp vấn đề bao nhiêu lần; nguyên nhân nằm ở kênh, công bố, trách nhiệm cập nhật hay yếu tố khác. |

**Key Insights & User Friction Points hiện mới là hướng điều tra, không phải kết quả nghiên cứu:** CBNV tìm thông tin từ nguồn nào; lúc nào họ tin là đã chốt; thay đổi được truyền đạt ra sao; ở bước nào phải hỏi lại; BTC mất công gì khi giải đáp. Nếu thông tin khó tra vì chưa được BTC xác nhận, cải tiến quy trình công bố có thể phù hợp hơn làm phần mềm mới.

## 5. User Problem → Operational Impact → Business Problem (thực hành 3)

**Chuỗi ưu tiên (chưa kiểm chứng):** CBNV không rõ thông tin nào hiện hành → có thể hỏi/đối chiếu nhiều lần → BTC có thể mất công tra cứu, trả lời và sửa nhiều danh sách → việc điều phối kỳ có nguy cơ kém nhất quán → mong muốn giảm thao tác lặp và tăng tỷ lệ thông tin chính xác, kịp thời.

**Business Problem sơ bộ:** Trong công tác tổ chức kỳ Team Building, việc quản lý và truyền đạt đăng ký, phân bổ và thay đổi qua nhiều danh sách/kênh **có thể** khiến BTC tốn thêm công kiểm tra, cập nhật và giải đáp, đồng thời khó bảo đảm mọi bên dùng cùng thông tin đã chốt. Đây là vấn đề vận hành **giả định**, không phải tuyên bố doanh nghiệp đã thất thoát doanh thu/chi phí.

| Vấn đề kinh doanh cần khảo sát (3–5 tình huống) | Hiện trạng từ tài liệu | Nguyên nhân khả dĩ — cần 5 Whys/phỏng vấn | Tác động dự kiến / dữ liệu cần thu |
|---|---|---|---|
| B1 — xác định danh sách hiện hành | Nhiều danh sách đăng ký, bay, xe, phòng. | Không rõ nguồn chuẩn hay quy tắc cập nhật? | Công đối chiếu, số bản sai khác; thu phiên bản file và thời gian đối chiếu. |
| B2 — đồng bộ thay đổi | BTC điều chỉnh sau khi chia sẻ danh sách. | Thiếu đầu mối cập nhật, thiếu quy trình thông báo, hay công cụ? | Số thay đổi chưa truyền đến đúng người; đối chiếu nhật ký thay đổi và tin nhắn. |
| B3 — xử lý câu hỏi lặp | CBNV có thể cần hỏi BTC để tra cứu. | Thông tin chưa công bố, khó tìm hay không tin nguồn? | Số câu hỏi theo chủ đề/người và phút xử lý; rà soát kênh hỗ trợ. |

**Root cause analysis:** với B2, hỏi liên tiếp “vì sao xe chưa khớp với giờ bay mới?” → “ai nhận thay đổi?” → “khi nào cập nhật danh sách xe?” → “ai xác nhận đã công bố?” → “quy trình bàn giao đang thiếu bước nào?” Đây là **chuỗi câu hỏi 5 Whys để điều tra**, không phải câu trả lời đã được chứng minh. Có thể dùng fishbone theo nhóm quy trình, con người, dữ liệu, công cụ, thời điểm. Không được kết luận “thiếu phần mềm” là nguyên nhân gốc chỉ vì hiện đang dùng bảng tính.

**Desired business outcomes và chỉ số (đề xuất, chưa có baseline/target chính thức):**

- Giảm **phút BTC xử lý một thay đổi hành trình**, đo từ lúc nhận yêu cầu đến khi cập nhật/xác nhận tới người liên quan (phút/yêu cầu).
- Giảm **số lần đối chiếu/sửa lại** một thay đổi bay–xe–phòng; đo số thao tác/ca và tỷ lệ trường hợp thông tin lệch giữa các danh sách (%).
- Tăng **tỷ lệ CBNV xác định đúng hành trình đã công bố** trong tác vụ thử (%); đồng thời theo dõi số câu hỏi phải gửi BTC trên mỗi 100 người tham gia.

Đo hiện trạng trước, chốt mục tiêu cùng BTC sau. Chỉ số người dùng (hiểu đúng hành trình) không thay thế chỉ số vận hành (công xử lý); thử nghiệm giao diện một mình không chứng minh tiết kiệm chi phí.

## 6. Lean UX Canvas — 8 ô (thực hành 4)

| Ô | Nội dung đề xuất |
|---|---|
| 1. Business Problem | B1/B2: BTC có thể tốn công đối chiếu và khó duy trì thông tin nhất quán khi thay đổi phân bổ. |
| 2. Business Outcomes | Giảm phút xử lý/thay đổi, số bản sai khác và số câu hỏi phải xử lý; xác định baseline rồi mới đặt ngưỡng. |
| 3. Users / customers | CBNV tham gia (người nhận thông tin); BTC (người điều phối). Bên đầu tư/phê duyệt là đơn vị tổ chức, chưa xác định cá nhân tài trợ. |
| 4. User Outcomes / benefits | CBNV biết đúng tình trạng đăng ký và hành trình đã công bố; BTC xác định được thay đổi nào đã cập nhật và ai cần được thông báo. |
| 5. Solution ideas | **Không mặc định làm app:** chuẩn hóa một đầu mối công bố và mẫu thông báo; quy trình xác nhận thay đổi; hoặc thử cổng web tra cứu hành trình theo từng kỳ cùng bước kiểm tra trước công bố. |
| 6. Hypotheses | Nếu BTC xác nhận một nguồn thông tin hiện hành và CBNV dễ nhận biết trạng thái công bố/thay đổi, CBNV sẽ tra cứu đúng với ít lượt hỏi lại hơn; BTC có thể giảm thời gian giải đáp. Cần so với cách làm hiện tại. |
| 7. Riskiest assumptions / what to learn | Người dùng thực sự khó biết bản nào đúng? Công việc hỏi lại có đáng kể? BTC có cập nhật nguồn chung kịp không? CBNV tin nguồn mới không? Cải tiến quy trình không phần mềm có đủ không? |
| 8. MVP / smallest experiment | Mẫu hành trình cá nhân và thông báo thay đổi được BTC kiểm tra thủ công trên dữ liệu ẩn danh cho **một tình huống/kỳ thí điểm**; có thể dùng bản web click được hoặc mẫu thông báo, chưa cần xây hệ thống phân bổ đầy đủ. |

## 7. Experiment Plan (thực hành 5)

**Giả thuyết rủi ro cao nhất:** trở ngại chủ yếu là không xác định được thông tin **đã chốt và mới nhất**, thay vì thông tin chưa sẵn sàng do BTC chưa hoàn tất phân bổ. Nếu giả thuyết sai, giải pháp tra cứu riêng sẽ không giải quyết vấn đề cốt lõi.

1. **Khám phá và baseline:** phỏng vấn/quan sát thử 5–8 CBNV và 2–3 thành viên BTC (cỡ mẫu *đề xuất*, không đại diện thống kê); xem một quy trình công bố và một thay đổi. Đếm số câu hỏi, thời gian tra cứu/giải đáp và trường hợp lệch dữ liệu nếu được tiếp cận. Hỏi vì sao người dùng không tin hoặc không hiểu thông tin.
2. **So sánh hai phương án tối thiểu:** A = một đầu mối thông báo chuẩn, xác nhận thủ công của BTC; B = nguyên mẫu tra cứu cá nhân có nhãn “chưa công bố/đã công bố” và lịch sử thay đổi. Cùng một kịch bản giả lập (đăng ký, đổi chuyến bay, cập nhật xe); cho CBNV tìm giờ/điểm tập trung, nguồn xác nhận và nêu việc sẽ làm. Không dùng dữ liệu cá nhân thật trong nguyên mẫu.
3. **Chỉ số và cách ghi:** tỷ lệ người chọn đúng thông tin đã công bố (%), thời gian hoàn thành (giây), số lần hỏi/nhầm (lượt), mức tin tưởng và lý do (phỏng vấn); BTC đo phút cập nhật và số vị trí phải sửa cho cùng thay đổi. Ghi riêng kết quả từng phương án; tránh suy ra hiệu quả vận hành từ nguyên mẫu chỉ thử CBNV.
4. **Ngưỡng ra quyết định thử nghiệm (đề xuất, cần nhóm/BTC duyệt trước khi chạy):** ít nhất 4/5 người thử xác định đúng lịch đã công bố và không phải nhờ hỗ trợ; phương án thử không tạo thêm bước cập nhật gây lệch thông tin cho BTC. Mẫu nhỏ chỉ dùng phát hiện trở ngại, **không** chứng minh tỷ lệ chung của doanh nghiệp.
5. **Sau thử nghiệm:** nếu A đủ tốt, ưu tiên chuẩn hóa quy trình thay vì làm hệ thống; nếu B hữu ích và BTC cập nhật được, thí điểm giới hạn một kỳ và đo chỉ số vận hành; nếu cả hai không đạt, quay lại nghiên cứu nguyên nhân, sửa User Problem Statement/Canvas và thử lại.

## 8. Business Requirements → System Request (bản nháp để quyết định đầu tư)

**Business requirements (kết quả cần đạt, không khóa giải pháp):** BR-01: BTC và CBNV phải xác định được phiên bản thông tin đã được xác nhận cho từng kỳ; BR-02: thay đổi đăng ký/phân bổ phải có người chịu trách nhiệm cập nhật và thông báo tới đối tượng liên quan; BR-03: chỉ công bố dữ liệu đã kiểm tra, bảo vệ thông tin cá nhân; BR-04: theo dõi được thời gian xử lý thay đổi, sai khác dữ liệu và câu hỏi lặp. Phương án thực hiện có thể là quy trình, công cụ sẵn có hoặc hệ thống mới.

| Mục System Request | Đề xuất để xem xét, **chưa phê duyệt** |
|---|---|
| 1. Project title | Thí điểm cổng quản lý kỳ Team Building nội bộ. |
| 2. Sponsor / requestor | Đơn vị tổ chức/BTC (vai trò dự kiến); **chưa có tên người tài trợ, yêu cầu xác nhận**. |
| 3. Business need / problem | Cần bảo đảm thông tin đăng ký/hành trình nhất quán và giảm công đối chiếu, cập nhật, giải đáp của BTC; mức độ vấn đề phải đo theo §5–7. |
| 4. Vision / goals | CBNV tra được thông tin của mình đã được BTC công bố; BTC theo dõi đăng ký, thay đổi và xác nhận kết quả; mục tiêu định lượng chốt sau baseline. |
| 5. Business benefits | Kỳ vọng ít sai khác dữ liệu, bớt câu hỏi lặp, vận hành minh bạch hơn; **chưa lượng hóa tiết kiệm tiền/doanh thu**. |
| 6. High-level requirements | Theo kỳ: ghi nhận đăng ký/tình trạng; BTC kiểm tra, cập nhật và công bố; CBNV chỉ tra cứu hành trình của mình; ghi nhận thay đổi và thông báo; BTC xem chỉ số vận hành. Phân bổ tự động bay/xe/phòng là hướng mở rộng khi đã xác minh nhu cầu, không phải điều kiện của thử nghiệm tối thiểu. |
| 7. Constraints / assumptions | Nội bộ, truy cập theo vai trò và kỳ; hạn chế lộ thông tin riêng tư; BTC cần có dữ liệu đầu vào được xác nhận. **Ngân sách, thời hạn, hạ tầng và số người dùng thực tế: chưa được sponsor cung cấp.** |
| 8. Feasibility | Kỹ thuật: cần đánh giá đồng bộ dữ liệu và phân quyền; kinh tế: đo baseline/công sức trước khi tính ROI; vận hành: BTC có nhận quy trình cập nhật không; lịch trình: chỉ ước lượng sau khi xác nhận phạm vi và nguồn lực. **Chưa đủ dữ liệu để kết luận khả thi.** |
| 9. Expected deliverables | Trước quyết định đầu tư: báo cáo khám phá vấn đề, baseline, canvas, kết quả thử nghiệm và đề xuất go/no-go; nếu duyệt thí điểm: nguyên mẫu/quy trình công bố, hướng dẫn BTC và báo cáo đánh giá. |
| 10. Risks | Dữ liệu nguồn sai/chậm cập nhật; lộ hành trình cá nhân; người dùng nhầm thông tin chưa công bố; kết quả thử nghiệm nhỏ bị diễn giải quá mức. Cần kiểm soát quyền, gắn trạng thái công bố, kiểm tra trước gửi. |
| 11. Approval / signature | **Chưa phê duyệt.** Người tài trợ: cần xác định; ngày/quyết định go–no-go: ghi sau khi hoàn tất nghiên cứu và đánh giá khả thi. |

## 9. Đầu ra và việc nhóm cần hoàn thành

- [ ] Thu thập biên bản phỏng vấn/quan sát có ngày, vai trò, số mẫu và dẫn chứng ẩn danh; phân biệt phát biểu người tham gia với suy luận của nhóm.
- [ ] Đo baseline của các chỉ số §5; xác nhận nguyên nhân theo 5 Whys thay vì mặc nhiên kết luận “thiếu hệ thống”.
- [ ] Cập nhật 2–3 nhu cầu, nhu cầu ưu tiên, User Problem Statement và canvas theo bằng chứng mới.
- [ ] Hoàn thiện Business Problem, chuỗi tác động vận hành và Business Outcomes có số đo/đơn vị.
- [ ] Chạy thử nghiệm §7, ghi cả kết quả không ủng hộ giả thuyết; so sánh phương án quy trình với phương án phần mềm.
- [ ] Trình sponsor duyệt phạm vi, mục tiêu, nguồn lực và System Request trước khi coi dự án được khởi động.

**Tiêu chí tự kiểm:** Nhu cầu không phải tính năng; Problem Statement có người dùng–bối cảnh–trở ngại–hệ quả và không cài sẵn giải pháp; mỗi khẳng định nêu nguồn hoặc đánh dấu giả định; vấn đề người dùng nối với vấn đề kinh doanh qua tác động vận hành; giả thuyết có thể bác bỏ; KPI có cách đo; thử nghiệm có tiêu chí điều chỉnh; System Request chưa được xem như phê duyệt khi thiếu sponsor/dữ liệu khả thi. Quy trình này có tính lặp: kết quả nghiên cứu có thể buộc nhóm quay lại sửa vấn đề ưu tiên.