# 4. Vai trò và Phân quyền

## 4.1. Các vai trò trong hệ thống

### Employee (Nhân viên)
**Số lượng:** ~100-1000 người/kỳ

**Nhu cầu:**
- Đăng ký tham gia Team Building một cách nhanh chóng
- Xem được toàn bộ hành trình của mình (bay, xe, khách sạn, Gala)
- Tra cứu thông tin lịch trình, quy định bất cứ lúc nào
- Nhận thông báo khi có thay đổi

**Quyền hạn:**
- Đăng ký/sửa đăng ký khi còn mở
- Xem **chỉ dữ liệu của mình** (My Journey)
- Hỏi chatbot về hành trình cá nhân

### Team Leader (Trưởng nhóm)
**Số lượng:** 8-12 người/kỳ

**Nhu cầu:**
- Tất cả nhu cầu của Employee
- Theo dõi tình trạng đăng ký của team mình
- Chọn chỗ ngồi Gala Dinner cho cả team
- Động viên thành viên đăng ký

**Quyền hạn:**
- Quyền của Employee
- Xem danh sách đăng ký của team mình
- Chọn ghế Gala cho team (theo lượt bốc thăm)

### Admin (Ban Tổ Chức - BTC)
**Số lượng:** 2-5 người

**Nhu cầu:**
- Quản lý toàn bộ kỳ Team Building
- Giảm thiểu thời gian phân bổ thủ công
- Có công cụ tự động hóa nhưng vẫn kiểm soát được
- Điều chỉnh ngoại lệ dễ dàng
- Theo dõi được ai thay đổi gì, khi nào

**Quyền hạn:**
- Tạo và cấu hình kỳ Team Building
- Quản lý chuyến bay, xe, khách sạn
- Chạy phân bổ tự động
- Điều chỉnh phân bổ thủ công
- Chuyển trạng thái kỳ (mở/đóng đăng ký, công bố thông tin)
- Gửi thông báo, email hàng loạt
- Export báo cáo

### Super Admin (Quản trị hệ thống)
**Số lượng:** 1-2 người

**Nhu cầu:**
- Tất cả quyền của Admin
- Quản lý tài khoản người dùng
- Cấu hình hệ thống
- Xem audit log đầy đủ

**Quyền hạn:**
- Quyền của Admin
- Quản lý user/role
- Xem toàn bộ audit log
- Cấu hình hệ thống

## 4.2. Ma trận phân quyền

| Chức năng | Employee | Team Leader | Admin | Super Admin |
|---|:---:|:---:|:---:|:---:|
| Đăng ký tham gia | ✅ | ✅ | ✅ | ✅ |
| Xem hành trình cá nhân | ✅ | ✅ | ✅ | ✅ |
| Xem danh sách team | ❌ | ✅ (team mình) | ✅ (tất cả) | ✅ |
| Chọn ghế Gala | ❌ | ✅ (team mình) | ✅ | ✅ |
| Tạo/cấu hình kỳ TB | ❌ | ❌ | ✅ | ✅ |
| Quản lý chuyến bay/xe | ❌ | ❌ | ✅ | ✅ |
| Phân bổ tự động | ❌ | ❌ | ✅ | ✅ |
| Điều chỉnh phân bổ | ❌ | ❌ | ✅ | ✅ |
| Gửi thông báo hàng loạt | ❌ | ❌ | ✅ | ✅ |
| Quản lý user/role | ❌ | ❌ | ❌ | ✅ |
| Xem audit log đầy đủ | ❌ | ❌ | ✅ (event) | ✅ (tất cả) |

## 4.3. Nguyên tắc bảo mật

### Isolation dữ liệu cá nhân
- Employee **chỉ** truy cập được dữ liệu của mình qua **mọi** endpoint
- Chatbot chỉ trả lời về hành trình của người hỏi (dựa vào JWT)
- API backend validate quyền, không tin frontend

### Audit trail đầy đủ
Mọi thay đổi quan trọng đều ghi log:
- **Ai** (actor_id)
- **Làm gì** (action, entity_type, entity_id)
- **Khi nào** (created_at)
- **Giá trị trước/sau** (before_data, after_data)
- **Lý do** (reason - bắt buộc với điều chỉnh thủ công)

### Công bố thông tin có kiểm soát
Hành trình chi tiết (chuyến bay, xe, phòng, ghế Gala) chỉ hiển thị khi BTC chuyển trạng thái sang **"Đã công bố"**.

Trước đó, Employee chỉ thấy: *"Đang chờ BTC công bố thông tin"*