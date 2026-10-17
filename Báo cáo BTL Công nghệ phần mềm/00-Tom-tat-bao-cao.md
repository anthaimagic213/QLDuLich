# TÓM TẮT BÁO CÁO

## Thông tin chung

**Đề tài:** Hệ thống quản lý Team Building nội bộ (Team Building Portal)

**Vai trò phân tích:** Business Analyst

**Phạm vi:** Phân tích yêu cầu và thiết kế hệ thống quản lý toàn bộ quy trình tổ chức Team Building

---

## Bài toán nghiệp vụ

### Hiện trạng
- Quản lý bằng nhiều file Excel riêng lẻ, dữ liệu phân tán
- Phân bổ thủ công mất 2-3 ngày làm việc cho 100-200 người
- CBNV không biết hành trình của mình, phải hỏi BTC liên tục
- Dễ xảy ra sai sót: vượt slot, trùng phòng, team bị tách
- Không có lịch sử thay đổi, khó truy vết

### Mục tiêu
> **"Một cổng duy nhất cho toàn bộ hành trình Team Building"**

- **Tập trung hóa:** Một nguồn dữ liệu duy nhất
- **Tự động hóa:** Phân bổ tự động trong vài giây
- **Minh bạch:** CBNV tự tra cứu 24/7
- **Giảm sai sót:** Validation tự động
- **Truy vết:** Audit log đầy đủ

---

## Giải pháp đề xuất

### 5 Module chính

1. **Đăng ký tham gia**
   - Form nhiều bước với validation
   - Khai báo nhu cầu: ca làm việc, điểm đón xe
   - Email xác nhận tự động

2. **Quản lý chuyến bay**
   - Nhập thông tin chuyến bay và slot
   - Phân bổ tự động theo team và ca
   - Preview trước khi áp dụng
   - Điều chỉnh thủ công có kiểm soát

3. **Quản lý xe đưa đón**
   - 4 chặng độc lập: đi sân bay → sân bay đến → resort → sân bay về
   - Phân xe theo chuyến bay và điểm đón
   - Chỉ định Trưởng xe cho mỗi chuyến

4. **Gala Dinner**
   - Sơ đồ chỗ ngồi trực quan 2D
   - Bốc thăm thứ tự team chọn ghế
   - Cơ chế hold 120 giây chống tranh chấp

5. **My Journey - Dashboard cá nhân**
   - Hiển thị toàn bộ hành trình trên một màn hình
   - Mobile-first design
   - Chỉ hiển thị sau khi BTC công bố

---

## Người dùng hệ thống

| Vai trò | Số lượng | Quyền chính |
|---------|----------|-------------|
| **Nhân viên** | 100-1000/kỳ | Đăng ký, xem hành trình của mình |
| **Trưởng team** | 8-12/kỳ | + Xem team, chọn ghế Gala |
| **Ban Tổ Chức** | 3-5 | Quản lý kỳ, phân bổ tài nguyên |
| **Super Admin** | 1-2 | + Quản lý user, audit log |

---

## Phân tích yêu cầu

### 7 Use Cases chính

1. **UC-01:** Quản lý kỳ du lịch
2. **UC-02:** Đăng ký tham gia ⭐
3. **UC-03:** Xử lý hủy tham gia
4. **UC-04:** Phân bổ chuyến bay ⭐
5. **UC-05:** Phân bổ xe theo chặng ⭐
6. **UC-06:** Xếp phòng khách sạn
7. **UC-07:** Tra cứu hành trình ⭐

⭐ = Use case ưu tiên cao trong MVP

### 14 User Stories

Phân theo độ ưu tiên MoSCoW:
- **Must Have:** 6 stories (đăng ký, phân bay, phân xe, Gala, My Journey, trạng thái)
- **Should Have:** 6 stories (sửa đăng ký, dashboard, điều chỉnh, Trưởng xe, chatbot, audit)
- **Could Have:** 2 stories (hủy, bốc thăm)

**Tổng Story Points (MVP):** ~70 points

---

## Kế hoạch triển khai Agile/Scrum

### Timeline 12 tuần

**Sprint 0 (2 tuần):** Setup & Foundation

**Sprint 1-2 (4 tuần):** Core Features
- Đăng ký tham gia
- Quản lý chuyến bay
- Phân bổ tự động cơ bản

**Sprint 3-4 (4 tuần):** Advanced Features
- Quản lý xe 4 chặng
- My Journey dashboard
- Gala Dinner chọn ghế

**Sprint 5-6 (2 tuần):** Polish & Launch
- Testing toàn diện
- Tối ưu performance
- Deployment

### Scrum Team (5 người)

- 1 Product Owner (kiêm BA)
- 1 Scrum Master (kiêm Tech Lead)
- 2 Full-stack Developers
- 1 QA/Tester

### Sprint Planning

- **Sprint length:** 2 tuần
- **Velocity dự kiến:** 12-15 points/sprint
- **Ceremonies:**
  - Daily standup: 15 phút/ngày
  - Sprint planning: 2-3 giờ đầu sprint
  - Sprint review: 1 giờ cuối sprint
  - Retrospective: 45 phút sau review

---

## Giá trị mang lại

### Định lượng

| Chỉ số | Trước | Sau | Cải thiện |
|--------|-------|-----|-----------|
| Thời gian phân bổ | 2-3 ngày | Vài giây | **99%** ⬇️ |
| Email hỏi BTC | 180/kỳ | ~50/kỳ | **70%** ⬇️ |
| Sai sót phân bổ | 8% | <2% | **75%** ⬇️ |
| Độ hài lòng CBNV | 68% | >85% | **25%** ⬆️ |

### Định tính

✅ **BTC:** Tiết kiệm thời gian, giảm stress, có audit log
✅ **Nhân viên:** Tra cứu mọi lúc, không phải chờ, trải nghiệm tốt
✅ **Tổ chức:** Chuyên nghiệp hóa, có dữ liệu để cải tiến

---

## Công nghệ đề xuất (tham khảo)

- **Frontend:** React 19 + TypeScript + Tailwind CSS
- **Backend:** FastAPI (Python) hoặc Node.js/Express
- **Database:** PostgreSQL
- **Realtime:** WebSocket cho seat selection
- **Email:** SMTP (Mailpit cho dev)
- **Chatbot:** RAG với LangChain + OpenAI API

---

## Kết luận

Hệ thống **Team Building Portal** giải quyết triệt để bài toán tổ chức Team Building quy mô lớn thông qua:

1. ✅ **Tập trung hóa** dữ liệu
2. ✅ **Tự động hóa** quy trình
3. ✅ **Minh bạch** thông tin
4. ✅ **Truy vết** đầy đủ
5. ✅ **Trải nghiệm** tốt cho người dùng

Đề tài có **tính thực tiễn cao**, phù hợp triển khai trong doanh nghiệp thực tế, đồng thời thể hiện khả năng phân tích nghiệp vụ và thiết kế hệ thống của nhóm.

---

## Cấu trúc báo cáo đầy đủ

```
00-Gioi-thieu.md          → Giới thiệu tổng quan
00-Tom-tat-bao-cao.md     → File này - Tóm tắt executive
01-Ly-do-chon-de-tai.md   → Bối cảnh và lý do
02-Nguoi-dung-he-thong.md → Phân tích người dùng
03-Use-Case.md            → 7 Use Cases chi tiết
04-User-Story.md          → 14 User Stories
05-Phan-tich-yeu-cau.md   → Yêu cầu chức năng & phi chức năng
06-Ke-hoach-Agile-Scrum.md → Kế hoạch 12 tuần
07-Ket-luan.md            → Kết luận và hướng phát triển
README.md                 → Hướng dẫn sử dụng báo cáo
```

---

**Lưu ý cho việc làm slide:**

Báo cáo này được thiết kế để hỗ trợ slide 11-12 trang:

1. **Slide 1:** Trang bìa
2. **Slide 2:** Bối cảnh & vấn đề (từ file 01)
3. **Slide 3:** Người dùng hệ thống (từ file 02)
4. **Slide 4:** Giải pháp - 5 module (từ file 03, 04)
5. **Slide 5:** Use Case Diagram (từ file 03)
6. **Slide 6-7:** Use Cases quan trọng (UC-02, UC-04, UC-07)
7. **Slide 8:** User Stories MVP (từ file 04)
8. **Slide 9:** Yêu cầu hệ thống (từ file 05)
9. **Slide 10:** Kế hoạch Agile 12 tuần (từ file 06)
10. **Slide 11:** Giá trị mang lại (từ file 07)
11. **Slide 12:** Kết luận & Q&A

Mỗi file MD có cấu trúc rõ ràng với heading, table, bullet points để dễ dàng chuyển sang slide.