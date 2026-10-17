# 1. Giới thiệu & Bối cảnh dự án

## 1.1. Thông tin dự án

**Tên dự án:** Hệ thống quản lý Team Building tập trung (Team Building Portal)  
**Phạm vi:** Phân tích và thiết kế hệ thống quản lý toàn bộ quy trình tổ chức Team Building  
**Vai trò:** Business Analyst  
**Thời gian phân tích:** Tháng 9 - Tháng 10, 2026

## 1.2. Bối cảnh nghiệp vụ

### Tổ chức
Công ty có quy mô 100-200 nhân viên, hoạt động đa chi nhánh, tổ chức Team Building định kỳ hàng năm (thường tại các điểm du lịch như Phú Quốc, Đà Nẵng) với mục tiêu gắn kết đội ngũ và tri ân nhân viên.

### Tần suất & quy mô điển hình
- **Tần suất:** 1-2 lần/năm
- **Quy mô:** 100-150 người tham gia/kỳ
- **Thời lượng:** 3-4 ngày 2-3 đêm
- **Nguồn lực BTC:** 3-5 người, làm kiêm nhiệm

## 1.3. Lý do thực hiện dự án

### Động lực kinh doanh (Business Drivers)

1. **Tăng hiệu quả vận hành**
   - Giảm thời gian chuẩn bị từ 4-6 tuần xuống còn 2-3 tuần
   - Giảm 60% thời gian phân bổ thủ công (từ ~20 giờ → ~8 giờ)

2. **Cải thiện trải nghiệm nhân viên**
   - Tăng tỷ lệ hài lòng (khảo sát sau kỳ TB2025: chỉ 68% hài lòng về "thông tin minh bạch")
   - Giảm số lượng câu hỏi gửi BTC (trung bình 180 email/kỳ)

3. **Giảm thiểu rủi ro & chi phí sai sót**
   - Tránh tình trạng overbooking chuyến bay (đã xảy ra TB2025)
   - Giảm chi phí đặt dư xe (thường đặt +20% để đảm bảo)

4. **Tuân thủ & minh bạch**
   - Đáp ứng yêu cầu audit nội bộ về truy vết thay đổi
   - Công khai lịch trình, giảm thắc mắc

## 1.4. Phương pháp phân tích

### Các hoạt động đã thực hiện

| Hoạt động | Đối tượng | Thời gian | Kết quả |
|-----------|-----------|-----------|---------|
| **Phỏng vấn sâu** | 3 thành viên BTC từng tổ chức 2+ kỳ | 3 buổi × 90 phút | 12 pain points, 8 yêu cầu nghiệp vụ |
| **Quan sát quy trình** | Theo dõi BTC chuẩn bị kỳ TB2026 | 2 tuần | Bản đồ quy trình As-Is (BPMN) |
| **Khảo sát nhân viên** | 85 CBNV đã tham gia TB2025 | Online, 1 tuần | Tỷ lệ phản hồi 71% |
| **Phân tích tài liệu** | File Excel, email, checklist BTC | - | 15 file nguồn, 200+ email |
| **Workshop xác định yêu cầu** | BTC + 2 trưởng phòng + 1 đại diện CBNV | 1 buổi × 3 giờ | Danh sách 28 User Stories ưu tiên |

### Công cụ phân tích
- **Process Mapping:** BPMN (Business Process Model and Notation)
- **Requirements Elicitation:** User Story, Use Case
- **Prioritization:** MoSCoW (Must have, Should have, Could have, Won't have)
- **Data Modeling:** Entity Relationship Diagram (ERD - simplified)

## 1.5. Phạm vi phân tích (Scope)

### Trong phạm vi (In Scope)
✅ Quy trình từ mở đăng ký → kết thúc kỳ TB  
✅ 4 nhóm người dùng: BTC, Nhân viên, Trưởng team, Super Admin  
✅ 5 module chính: Đăng ký, Chuyến bay, Xe, Gala Dinner, My Journey  
✅ Chatbot hỗ trợ tra cứu thông tin  

### Ngoài phạm vi (Out of Scope - Phase 2)
❌ Tích hợp hệ thống HR (đồng bộ danh sách nhân viên tự động)  
❌ Thanh toán/Kế toán  
❌ Mobile app native (chỉ responsive web)  
❌ Quản lý ngân sách chi tiết  

## 1.6. Mục tiêu dự án (SMART)

| Mục tiêu | Chỉ số hiện tại | Mục tiêu | Thời hạn |
|----------|----------------|----------|----------|
| Giảm thời gian phân bổ | 20 giờ/kỳ | ≤ 8 giờ/kỳ | Q4 2026 |
| Tăng tỷ lệ hài lòng về thông tin | 68% | ≥ 85% | Đo sau kỳ đầu dùng hệ thống |
| Giảm số email hỏi BTC | 180 email/kỳ | ≤ 50 email/kỳ | Đo trong kỳ đầu |
| Độ chính xác phân bổ | 92% (8% cần điều chỉnh) | ≥ 98% | Q4 2026 |