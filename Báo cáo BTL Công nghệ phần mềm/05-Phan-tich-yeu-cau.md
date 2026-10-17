# 5. PHÂN TÍCH YÊU CẦU HỆ THỐNG

## 5.1. Bài toán nghiệp vụ cốt lõi

### Thực trạng quản lý Team Building

Khi tổ chức chuyến Team Building cho 100-200 nhân viên, BTC phải đối mặt với:

**Vấn đề 1: Dữ liệu phân tán**
- Đăng ký qua Google Forms → Export Excel
- Quản lý chuyến bay trên file Excel riêng
- Phân xe trên file Excel khác
- Phòng khách sạn trên file Word/Excel
- Gala Dinner trên PowerPoint

**Vấn đề 2: Phân bổ thủ công tốn thời gian**
- Phân chuyến bay: 1-2 ngày (cố gắng giữ team cùng chuyến)
- Phân xe 4 chặng: 1 ngày
- Sắp xếp Gala: 0.5 ngày
- **Tổng: 2-3 ngày làm việc**

**Vấn đề 3: Dễ sai sót**
- Vượt slot chuyến bay
- Xe quá tải hoặc để trống
- Team bị tách rời
- Thay đổi một chỗ → phải cập nhật nhiều file

**Vấn đề 4: Thiếu minh bạch**
- CBNV không biết mình bay chuyến nào, xe nào
- Phải liên tục hỏi BTC
- Thông tin công bố muộn (1-2 ngày trước sự kiện)

### Giải pháp đề xuất

> **"Một cổng thông tin duy nhất cho toàn bộ hành trình Team Building"**

**Nguyên tắc thiết kế:**
1. **Tập trung hóa** – Single Source of Truth
2. **Tự động hóa** – Giảm công việc thủ công
3. **Minh bạch** – CBNV tự tra cứu 24/7
4. **Truy vết** – Audit log đầy đủ

---

## 5.2. Yêu cầu chức năng (Functional Requirements)

### FR-01: Quản lý kỳ Team Building

| ID | Yêu cầu | Mức độ |
|----|---------|--------|
| FR-01.1 | Tạo kỳ mới với thông tin cơ bản (tên, điểm đến, ngày, deadline đăng ký) | Must |
| FR-01.2 | Cấu hình ca bay (sáng/chiều) và chặng xe (4 chặng) | Must |
| FR-01.3 | Quản lý trạng thái kỳ: Draft → Mở đăng ký → Đóng → Phân bổ → Công bố → Diễn ra → Hoàn thành | Must |
| FR-01.4 | Import quy định từ file và lưu version | Should |

### FR-02: Đăng ký tham gia

| ID | Yêu cầu | Mức độ |
|----|---------|--------|
| FR-02.1 | Form đăng ký nhiều bước: thông tin → quy định → ca → nhu cầu xe → xác nhận | Must |
| FR-02.2 | Xác nhận đồng ý quy định (lưu version đã đồng ý) | Must |
| FR-02.3 | Chọn ca làm việc (ảnh hưởng đến chuyến bay phù hợp) | Must |
| FR-02.4 | Đăng ký nhu cầu xe cho 4 chặng (có/không, điểm đón) | Must |
| FR-02.5 | Gửi email xác nhận tự động | Must |
| FR-02.6 | Cho phép sửa đăng ký khi kỳ còn mở | Should |
| FR-02.7 | Yêu cầu hủy tham gia (cần BTC duyệt) | Could |

### FR-03: Phân bổ chuyến bay

| ID | Yêu cầu | Mức độ |
|----|---------|--------|
| FR-03.1 | Nhập thông tin chuyến bay: mã, ca, giờ, slot | Must |
| FR-03.2 | Phân bổ tự động theo thuật toán: giữ team, đáp ứng ca, không vượt slot | Must |
| FR-03.3 | Preview kết quả trước khi apply (dry-run) | Must |
| FR-03.4 | Cảnh báo: team bị tách, slot vượt mức | Must |
| FR-03.5 | Điều chỉnh thủ công (chuyển CBNV sang chuyến khác) | Should |
| FR-03.6 | Bắt buộc nhập lý do khi điều chỉnh thủ công | Should |

### FR-04: Phân bổ xe đưa đón

| ID | Yêu cầu | Mức độ |
|----|---------|--------|
| FR-04.1 | Cấu hình xe cho 4 chặng: mã xe, biển số, sức chứa, điểm đón | Must |
| FR-04.2 | Phân xe tự động theo: chuyến bay, điểm đón, team | Must |
| FR-04.3 | Chỉ định Trưởng xe (từ danh sách hành khách trên xe) | Should |
| FR-04.4 | Lưu thông tin tài xế (tên, SĐT) | Should |

### FR-05: Quản lý Gala Dinner

| ID | Yêu cầu | Mức độ |
|----|---------|--------|
| FR-05.1 | Thiết kế sơ đồ chỗ ngồi (bàn tròn, số ghế/bàn) | Must |
| FR-05.2 | Random thứ tự team chọn ghế (bốc thăm) | Must |
| FR-05.3 | Trưởng team chọn ghế cho cả team theo lượt | Must |
| FR-05.4 | Hold ghế tạm thời 120 giây (chống tranh chấp) | Must |
| FR-05.5 | Hiển thị sơ đồ real-time (ghế trống/đã chọn/đang hold) | Must |

### FR-06: My Journey - Hành trình cá nhân

| ID | Yêu cầu | Mức độ |
|----|---------|--------|
| FR-06.1 | Hiển thị toàn bộ hành trình: chuyến bay, xe 4 chặng, phòng, Gala, lịch trình | Must |
| FR-06.2 | Mobile-first design (xem dễ trên điện thoại) | Must |
| FR-06.3 | Chỉ hiển thị khi BTC công bố (trước đó: "Đang chờ BTC") | Must |
| FR-06.4 | Export PDF hành trình cá nhân | Could |

### FR-07: Chatbot hỗ trợ (RAG)

| ID | Yêu cầu | Mức độ |
|----|---------|--------|
| FR-07.1 | Trả lời câu hỏi về quy định, lịch trình chung | Should |
| FR-07.2 | Trả lời về hành trình cá nhân (chỉ của người hỏi) | Should |
| FR-07.3 | Không bao giờ trả lời về dữ liệu người khác | Must |
| FR-07.4 | Thời gian phản hồi ≤ 3 giây | Should |

---

## 5.3. Yêu cầu phi chức năng (Non-Functional Requirements)

### NFR-01: Hiệu năng

| ID | Yêu cầu | Giá trị mục tiêu |
|----|---------|------------------|
| NFR-01.1 | Hỗ trợ đồng thời | 100 users |
| NFR-01.2 | Thời gian phân bổ tự động | ≤ 5 giây (1000 người) |
| NFR-01.3 | Thời gian load My Journey | ≤ 2 giây |
| NFR-01.4 | Chatbot response time | ≤ 3 giây |

### NFR-02: Bảo mật & Phân quyền

| ID | Yêu cầu |
|----|---------|
| NFR-02.1 | CBNV chỉ xem được dữ liệu của mình (data isolation) |
| NFR-02.2 | Phân quyền rõ ràng: Employee / Team Leader / Admin / Super Admin |
| NFR-02.3 | Mọi thay đổi quan trọng đều ghi audit log |
| NFR-02.4 | Audit log không được phép xóa |

### NFR-03: Tính khả dụng

| ID | Yêu cầu |
|----|---------|
| NFR-03.1 | Uptime ≥ 99% trong thời gian đăng ký và sự kiện |
| NFR-03.2 | Responsive trên mobile (iPhone, Android) |
| NFR-03.3 | Hỗ trợ các trình duyệt: Chrome, Safari, Edge |

### NFR-04: Khả năng mở rộng

| ID | Yêu cầu |
|----|---------|
| NFR-04.1 | Không hard-code: số ca, số chặng xe, team đều là cấu hình |
| NFR-04.2 | Hỗ trợ nhiều kỳ TB song song |
| NFR-04.3 | Dễ dàng thay đổi quy định, lịch trình mà không cần sửa code |

### NFR-05: Trải nghiệm người dùng

| ID | Yêu cầu |
|----|---------|
| NFR-05.1 | Giao diện tiếng Việt |
| NFR-05.2 | Định dạng ngày giờ Việt Nam (dd/MM/yyyy HH:mm) |
| NFR-05.3 | Thông báo lỗi rõ ràng, hướng dẫn sửa |
| NFR-05.4 | Email template chuyên nghiệp |

---

## 5.4. Ràng buộc nghiệp vụ (Business Rules)

### BR-01: Quy tắc đăng ký

| ID | Quy tắc |
|----|---------|
| BR-01.1 | Một CBNV chỉ đăng ký được 1 lần cho 1 kỳ |
| BR-01.2 | Chỉ đăng ký được khi kỳ ở trạng thái "Mở đăng ký" |
| BR-01.3 | Phải đồng ý quy định mới được gửi đăng ký |

### BR-02: Quy tắc phân bổ chuyến bay

| ID | Quy tắc |
|----|---------|
| BR-02.1 | Không vượt quá slot của chuyến bay |
| BR-02.2 | Ưu tiên giữ team cùng chuyến bay |
| BR-02.3 | Cảnh báo khi team bị tách ra nhiều chuyến |
| BR-02.4 | Một CBNV chỉ có tối đa 1 chuyến mỗi chiều (đi/về) |

### BR-03: Quy tắc phân xe

| ID | Quy tắc |
|----|---------|
| BR-03.1 | Chỉ phân xe cho CBNV có nhu cầu |
| BR-03.2 | Không vượt sức chứa xe |
| BR-03.3 | Giờ xe phải phù hợp với giờ bay (chặng liên quan đến sân bay) |
| BR-03.4 | Gom theo điểm đón và chuyến bay |

### BR-04: Quy tắc Gala Dinner

| ID | Quy tắc |
|----|---------|
| BR-04.1 | Mỗi team chỉ chọn được số ghế = số thành viên team |
| BR-04.2 | Không cho phép 2 team chọn cùng ghế |
| BR-04.3 | Ghế đang hold không cho team khác chọn |
| BR-04.4 | Hold hết hạn sau 120 giây nếu không xác nhận |

### BR-05: Quy tắc công bố thông tin

| ID | Quy tắc |
|----|---------|
| BR-05.1 | Chỉ công bố khi đã phân bổ đầy đủ: bay, xe, phòng |
| BR-05.2 | CBNV chỉ thấy hành trình khi BTC chuyển sang "Đã công bố" |
| BR-05.3 | Mọi thay đổi sau công bố phải có lý do và ghi log |

---

## 5.5. Tóm tắt phân tích yêu cầu

### Thống kê

- **Yêu cầu chức năng**: 28 yêu cầu (7 nhóm)
- **Yêu cầu phi chức năng**: 15 yêu cầu (5 nhóm)
- **Ràng buộc nghiệp vụ**: 18 quy tắc (5 nhóm)

### Độ ưu tiên

- **Must Have (Bắt buộc)**: 60%
- **Should Have (Nên có)**: 30%
- **Could Have (Có thể có)**: 10%

### Phạm vi MVP

Tập trung vào 5 module cốt lõi:
1. ✅ Đăng ký tham gia
2. ✅ Phân bổ chuyến bay
3. ✅ Phân bổ xe
4. ✅ Gala Dinner
5. ✅ My Journey