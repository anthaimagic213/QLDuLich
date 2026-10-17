# 8. Biểu đồ Use Case

## 8.1. Tổng quan

Hệ thống Team Building Portal có 4 actors chính và 15 use cases được nhóm theo 5 module nghiệp vụ.

## 8.2. Actors (Tác nhân)

| Actor | Mô tả | Role trong hệ thống |
|---|---|---|
| **Nhân viên** | Cán bộ nhân viên công ty | `employee` |
| **Trưởng team** | Người dẫn dắt một team | `team_leader` |
| **Ban Tổ Chức (BTC)** | Người quản lý kỳ Team Building | `admin` |
| **Super Admin** | Quản trị viên hệ thống | `super_admin` |

## 8.3. Danh sách Use Cases

### Module 1: Quản lý đăng ký

| UC ID | Tên Use Case | Actor | Mô tả |
|---|---|---|---|
| UC-01 | Đăng ký tham gia Team Building | Nhân viên | Điền form đăng ký nhiều bước, xác nhận quy định, chọn ca làm việc, đăng ký nhu cầu xe |
| UC-02 | Sửa thông tin đăng ký | Nhân viên | Chỉnh sửa đăng ký khi kỳ còn mở |
| UC-03 | Hủy đăng ký | Nhân viên | Hủy tham gia khi có việc đột xuất |
| UC-04 | Theo dõi tình trạng đăng ký | BTC | Xem dashboard số lượng đã đăng ký theo team/phòng ban |
| UC-05 | Gửi email nhắc nhở | BTC | Gửi email nhắc CBNV chưa đăng ký |

### Module 2: Quản lý chuyến bay

| UC ID | Tên Use Case | Actor | Mô tả |
|---|---|---|---|
| UC-06 | Nhập thông tin chuyến bay | BTC | Thêm/sửa chuyến bay, slot, giờ khởi hành |
| UC-07 | Phân bổ chuyến bay tự động | BTC | Chạy thuật toán phân bổ theo team/ca, xem preview, confirm |
| UC-08 | Điều chỉnh chuyến bay thủ công | BTC | Chuyển CBNV sang chuyến khác khi có ngoại lệ |
| UC-09 | Xem audit log chuyến bay | BTC | Tra cứu lịch sử thay đổi |

### Module 3: Quản lý xe đưa đón

| UC ID | Tên Use Case | Actor | Mô tả |
|---|---|---|---|
| UC-10 | Cấu hình xe theo chặng | BTC | Tạo xe cho 4 chặng (đi sân bay, rời sân bay, đến resort, về sân bay) |
| UC-11 | Phân xe tự động | BTC | Phân xe theo chuyến bay + team + điểm đón |
| UC-12 | Chỉ định Trưởng xe | BTC | Gán người chịu trách nhiệm điều phối mỗi xe |

### Module 4: Quản lý Gala Dinner

| UC ID | Tên Use Case | Actor | Mô tả |
|---|---|---|---|
| UC-13 | Thiết kế sơ đồ chỗ ngồi | BTC | Kéo thả bàn, ghế trên canvas |
| UC-14 | Chọn chỗ ngồi cho team | Trưởng team | Chọn ghế theo thứ tự bốc thăm, có cơ chế hold 2 phút chống tranh chấp |

### Module 5: Tra cứu hành trình cá nhân

| UC ID | Tên Use Case | Actor | Mô tả |
|---|---|---|---|
| UC-15 | Xem My Journey | Nhân viên | Xem toàn bộ hành trình: chuyến bay, xe, phòng, lịch trình, Gala |
| UC-16 | Hỏi chatbot | Nhân viên | Hỏi về quy định, lịch trình, hành trình của mình |

### Module 6: Quản lý hệ thống

| UC ID | Tên Use Case | Actor | Mô tả |
|---|---|---|---|
| UC-17 | Quản lý tài khoản | Super Admin | CRUD users, phân quyền |
| UC-18 | Quản lý phòng ban & team | Super Admin | CRUD departments, teams |
| UC-19 | Chuyển trạng thái kỳ TB | BTC | Chuyển qua các giai đoạn: mở đăng ký → đóng → phân bổ → công bố |

## 8.4. Biểu đồ Use Case chính

```
┌─────────────────────────────────────────────────────────────────────┐
│                   HỆ THỐNG TEAM BUILDING PORTAL                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐                                                  │
│  │   Nhân viên  │──────► (UC-01) Đăng ký tham gia                  │
│  └──────────────┘        (UC-02) Sửa đăng ký                        │
│         │                (UC-03) Hủy đăng ký                        │
│         │                (UC-15) Xem My Journey ◄─── include ───    │
│         │                (UC-16) Hỏi chatbot                        │
│         │                                                           │
│         │                                                           │
│  ┌──────────────┐                                                  │
│  │ Trưởng team  │──────► (UC-14) Chọn chỗ ngồi Gala                │
│  └──────────────┘        (kế thừa quyền Nhân viên)                 │
│         │                                                           │
│         │                                                           │
│  ┌──────────────┐                                                  │
│  │     BTC      │──────► (UC-04) Theo dõi đăng ký                  │
│  └──────────────┘        (UC-05) Gửi email nhắc                    │
│         │                (UC-06) Nhập chuyến bay                    │
│         │                (UC-07) Phân bổ bay tự động ◄─── extend ──│
│         │                (UC-08) Điều chỉnh thủ công                │
│         │                (UC-09) Xem audit log                      │
│         │                (UC-10) Cấu hình xe                        │
│         │                (UC-11) Phân xe tự động                    │
│         │                (UC-12) Chỉ định Trưởng xe                 │
│         │                (UC-13) Thiết kế sơ đồ Gala                │
│         │                (UC-19) Chuyển trạng thái kỳ               │
│         │                                                           │
│         │                                                           │
│  ┌──────────────┐                                                  │
│  │ Super Admin  │──────► (UC-17) Quản lý tài khoản                 │
│  └──────────────┘        (UC-18) Quản lý phòng ban & team          │
│                          (kế thừa quyền BTC)                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 8.5. Mối quan hệ giữa các Use Case

### Include (bao gồm)
- **UC-15 (Xem My Journey) include UC-16 (Hỏi chatbot)**: Khi xem hành trình, CBNV có thể click vào chatbot để hỏi chi tiết

### Extend (mở rộng)
- **UC-08 (Điều chỉnh thủ công) extend UC-07 (Phân bổ tự động)**: Sau khi phân bổ tự động, BTC có thể điều chỉnh các trường hợp ngoại lệ
- **UC-09 (Xem audit log) extend UC-08**: Mỗi lần điều chỉnh thủ công đều tự động ghi log

### Generalization (kế thừa)
- **Trưởng team** kế thừa tất cả quyền của **Nhân viên** + thêm quyền chọn ghế Gala cho team
- **Super Admin** kế thừa tất cả quyền của **BTC** + thêm quyền quản trị hệ thống

## 8.6. Điều kiện tiên quyết (Preconditions)

| Use Case | Điều kiện tiên quyết |
|---|---|
| UC-01, UC-02, UC-03 | Kỳ TB ở trạng thái `registration_open` |
| UC-07, UC-11 | Đã có đủ dữ liệu: CBNV đã đăng ký, chuyến bay/xe đã tạo |
| UC-14 | Kỳ TB ở trạng thái `information_published`, team đã được bốc thăm thứ tự |
| UC-15 | Kỳ TB ở trạng thái `information_published` trở lên |
| UC-19 | Dữ liệu đủ điều kiện chuyển (ví dụ không chuyển sang `event_started` khi Gala chưa xếp xong) |

## 8.7. Luồng chính của Use Case quan trọng

### UC-01: Đăng ký tham gia Team Building

**Actor**: Nhân viên

**Luồng chính**:
1. Nhân viên đăng nhập hệ thống
2. Hệ thống hiển thị thông tin kỳ TB đang mở đăng ký
3. Nhân viên click "Đăng ký tham gia"
4. Hệ thống hiển thị form đăng ký nhiều bước:
   - Bước 1: Xác nhận thông tin cá nhân (họ tên, email, phòng ban, team)
   - Bước 2: Chọn ca làm việc (ảnh hưởng đến chuyến bay)
   - Bước 3: Đăng ký nhu cầu xe đưa đón cho 4 chặng (có/không, điểm đón)
   - Bước 4: Xác nhận quy định (checkbox, lưu terms_version)
   - Bước 5: Xem lại và xác nhận
5. Nhân viên điền đầy đủ và nhấn "Gửi đăng ký"
6. Hệ thống validate dữ liệu
7. Hệ thống lưu đăng ký vào database
8. Hệ thống gửi email xác nhận
9. Hệ thống hiển thị màn hình "Đăng ký thành công"

**Luồng thay thế**:
- 6a. Dữ liệu không hợp lệ → hiển thị lỗi, quay lại bước tương ứng
- 6b. Kỳ TB đã đóng đăng ký → hiển thị thông báo, không cho đăng ký

### UC-07: Phân bổ chuyến bay tự động

**Actor**: BTC

**Luồng chính**:
1. BTC vào màn hình "Quản lý chuyến bay"
2. BTC chọn chiều bay (đi/về)
3. BTC click "Phân bổ tự động"
4. Hệ thống hỏi xác nhận: "Chạy thử (dry-run) hay phân bổ thật?"
5. BTC chọn "Chạy thử"
6. Hệ thống chạy thuật toán phân bổ:
   - Gom CBNV theo team
   - Xếp vào các chuyến bay theo ca, giảm thiểu team bị tách
   - Tính toán flag cảnh báo (team tách, slot vượt, ...)
7. Hệ thống hiển thị preview: danh sách CBNV đã phân, slot còn lại, cảnh báo
8. BTC xem preview, hài lòng
9. BTC click "Xác nhận phân bổ"
10. Hệ thống ghi dữ liệu phân bổ vào `flight_assignments`
11. Hệ thống ghi audit log
12. Hệ thống hiển thị "Phân bổ thành công"

**Luồng thay thế**:
- 8a. BTC không hài lòng → điều chỉnh thủ công (UC-08) hoặc cấu hình lại chuyến bay
- 10a. Dữ liệu thay đổi trong khi chạy thử → hiển thị cảnh báo, yêu cầu chạy lại

### UC-15: Xem My Journey

**Actor**: Nhân viên

**Luồng chính**:
1. Nhân viên đăng nhập
2. Nhân viên click menu "My Journey"
3. Hệ thống kiểm tra trạng thái kỳ TB
4. Kỳ TB đã ở trạng thái `information_published`
5. Hệ thống lấy dữ liệu hành trình của CBNV này:
   - Thông tin cá nhân & team
   - Chuyến bay đi + về (giờ, sân bay, mã đặt chỗ)
   - Xe đưa đón 4 chặng (mã xe, điểm đón, giờ tập trung)
   - Phòng khách sạn (tên phòng, tầng, người cùng phòng)
   - Chỗ ngồi Gala Dinner (bàn, ghế)
   - Lịch trình chi tiết 3 ngày
6. Hệ thống hiển thị dashboard hành trình, mobile-friendly
7. CBNV xem thông tin, có thể click vào chatbot để hỏi thêm (UC-16)

**Luồng thay thế**:
- 4a. Kỳ TB chưa công bố → hiển thị "Đang chờ BTC công bố thông tin"
- 5a. CBNV chưa đăng ký → hiển thị "Bạn chưa đăng ký tham gia"

## 8.8. Tóm tắt phân tích Use Case

- **Tổng số Use Case**: 19
- **Use Case phức tạp nhất**: UC-07 (Phân bổ chuyến bay tự động) - cần thuật toán, validation, preview, audit
- **Use Case quan trọng nhất**: UC-15 (Xem My Journey) - mục tiêu chính của hệ thống là "single source of truth"
- **Use Case có tương tác nhiều nhất**: UC-08 (Điều chỉnh thủ công) - liên quan đến audit log, email thông báo, validation slot

---

*Biểu đồ Use Case chi tiết có thể vẽ bằng công cụ như draw.io, PlantUML, hoặc Lucidchart để trình bày trong slide.*