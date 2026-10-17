# 5. Luồng nghiệp vụ chính

## 5.1. Vòng đời một kỳ Team Building

```
Nháp → Mở đăng ký → Đóng đăng ký → Đang xử lý phân bổ
      → Đã công bố → Đang diễn ra → Hoàn thành
```

### Các trạng thái

| Trạng thái | Mô tả | Hành động được phép |
|---|---|---|
| **Nháp** | BTC đang chuẩn bị | BTC cấu hình thông tin cơ bản |
| **Mở đăng ký** | CBNV có thể đăng ký | CBNV: đăng ký, sửa, hủy<br>BTC: theo dõi dashboard |
| **Đóng đăng ký** | Hết hạn đăng ký | BTC nhập chuyến bay, slot |
| **Đang xử lý phân bổ** | BTC phân bổ tài nguyên | BTC: phân chuyến bay, xe, phòng, Gala |
| **Đã công bố** | CBNV xem được hành trình | CBNV: xem My Journey, chọn ghế Gala<br>BTC: điều chỉnh, gửi thông báo |
| **Đang diễn ra** | Sự kiện đang diễn ra | Chỉ xem, không sửa |
| **Hoàn thành** | Kết thúc | Export báo cáo, lưu trữ |

## 5.2. Quy trình đăng ký của CBNV

```
┌─────────────────┐
│ 1. Đăng nhập    │
└────────┬────────┘
         ↓
┌─────────────────────────────┐
│ 2. Xem thông tin kỳ TB      │
│    (ngày, địa điểm, lịch    │
│     trình, quy định)        │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ 3. Chọn tham gia / Không    │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ 4. Xác nhận đọc quy định    │
│    (lưu version)            │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ 5. Chọn ca làm việc         │
│    (sáng/chiều - nếu có)    │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ 6. Đăng ký nhu cầu xe       │
│    theo từng chặng          │
│    (sân bay → khách sạn,    │
│     khách sạn → điểm tham   │
│     quan, v.v.)             │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ 7. Ghi chú bổ sung (nếu có) │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ 8. Xác nhận và gửi          │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ 9. Nhận email xác nhận      │
└─────────────────────────────┘
```

**Lưu ý:**
- CBNV có thể sửa đổi đăng ký khi kỳ còn ở trạng thái "Mở đăng ký"
- Sau khi đóng đăng ký, chỉ xem được thông tin đã đăng ký

## 5.3. Quy trình phân bổ tài nguyên của BTC

### Bước 1: Phân bổ chuyến bay

```
┌────────────────────────────┐
│ 1. Nhập danh sách chuyến   │
│    bay và số ghế (slot)    │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 2. Chạy phân bổ tự động    │
│    (theo team, ca)         │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 3. Xem preview kết quả     │
│    - Đã xếp bao nhiêu      │
│    - Slot còn lại          │
│    - Team bị tách (warning)│
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 4. Điều chỉnh thủ công     │
│    (nếu cần)               │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 5. Xác nhận và lưu         │
└────────────────────────────┘
```

### Bước 2: Phân bổ xe đưa đón

```
┌────────────────────────────┐
│ 1. Cấu hình xe theo chặng  │
│    (mã xe, biển số, sức    │
│     chứa, điểm đón/trả)    │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 2. Phân xe tự động         │
│    (theo chuyến bay + team)│
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 3. Chỉ định Trưởng xe      │
│    (tên, SĐT)              │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 4. Điều chỉnh (nếu cần)    │
└────────────────────────────┘
```

### Bước 3: Phân bổ phòng khách sạn

```
┌────────────────────────────┐
│ 1. Import danh sách phòng  │
│    (Excel)                 │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 2. Phân phòng cho CBNV     │
│    (thủ công hoặc theo quy │
│     tắc)                   │
└────────────────────────────┘
```

### Bước 4: Sắp xếp Gala Dinner

```
┌────────────────────────────┐
│ 1. Tạo sơ đồ bàn ghế       │
│    (số bàn, ghế/bàn)       │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 2. Random thứ tự team      │
│    chọn ghế                │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 3. Team Leader chọn ghế    │
│    cho team mình theo lượt │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 4. Hệ thống lock ghế đã    │
│    chọn (chống tranh chấp) │
└────────────────────────────┘
```

### Bước 5: Công bố thông tin

```
┌────────────────────────────┐
│ 1. Kiểm tra đầy đủ dữ liệu │
│    (bay, xe, phòng, Gala)  │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 2. Chuyển trạng thái sang  │
│    "Đã công bố"            │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ 3. Gửi email thông báo     │
│    đến toàn bộ CBNV        │
└────────────────────────────┘
```

## 5.4. Quy trình chọn ghế Gala Dinner

### Cơ chế chống tranh chấp ghế

```
Team Leader chọn ghế
         ↓
┌────────────────────────────┐
│ Hệ thống HOLD ghế          │
│ (khóa tạm 120 giây)        │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ Team Leader xác nhận       │
│ chọn ghế                   │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ Hệ thống ghi nhận và       │
│ LOCK vĩnh viễn             │
└────────────────────────────┘
```

**Nếu không xác nhận trong 120 giây:**
- Hệ thống tự động giải phóng HOLD
- Team Leader khác có thể chọn ghế đó

## 5.5. Tra cứu hành trình (My Journey)

```
┌────────────────────────────┐
│ CBNV đăng nhập             │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ Xem My Journey Dashboard   │
│ - Thông tin cá nhân/Team   │
│ - Chuyến bay đi/về         │
│ - Các chặng xe             │
│ - Phòng khách sạn          │
│ - Bàn/ghế Gala             │
│ - Lịch trình 3 ngày        │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ Hỏi Chatbot (nếu cần)     │
│ - Quy định                 │
│ - Lịch trình chi tiết      │
│ - Hành trình của mình      │
└────────────────────────────┘
```

## 5.6. Điều chỉnh sau khi công bố

```
┌────────────────────────────┐
│ BTC phát hiện cần điều     │
│ chỉnh (CBNV đổi ca, hủy    │
│ tham gia, thay chuyến bay) │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ Điều chỉnh trên hệ thống   │
│ (ghi lý do)                │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ Hệ thống ghi Audit Log     │
│ (ai, khi nào, đổi gì)      │
└────────┬───────────────────┘
         ↓
┌────────────────────────────┐
│ Gửi email thông báo thay   │
│ đổi đến CBNV liên quan     │
└────────────────────────────┘
```

**Nguyên tắc:**
- Mọi thay đổi sau khi công bố phải có lý do rõ ràng
- Hệ thống tự động validate (không vượt slot, không trùng lặp)
- CBNV nhận thông báo ngay khi có thay đổi liên quan đến mình