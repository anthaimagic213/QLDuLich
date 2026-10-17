# 3. Phân tích chức năng hệ thống

## 3.1. Tổng quan 5 module chính

Hệ thống được thiết kế theo 5 module nghiệp vụ chính, tương ứng với các giai đoạn tổ chức Team Building:

```
Đăng ký → Phân bổ chuyến bay → Phân xe → Sắp xếp Gala → Tra cứu hành trình
```

## 3.2. Module 1: Đăng ký tham gia

### Mục đích
Thu thập thông tin tham gia của CBNV một cách có tổ chức, đảm bảo nhân viên hiểu rõ quy định và cung cấp đầy đủ thông tin cần thiết.

### Chức năng chính

| Chức năng | Mô tả | Đầu ra |
|---|---|---|
| **Form nhiều bước** | Thu thập thông tin theo từng bước: xác nhận quy định → chọn ca làm việc → nhu cầu xe theo chặng → thông tin bổ sung | Hồ sơ đăng ký hoàn chỉnh |
| **Xác nhận quy định** | CBNV phải đọc và đồng ý với quy định (lưu version quy định để audit) | Bằng chứng đồng ý pháp lý |
| **Chọn ca làm việc** | Chọn ca khi đi và về (ảnh hưởng đến chuyến bay phù hợp) | Ràng buộc thời gian |
| **Đăng ký nhu cầu xe** | Chọn điểm đón/trả theo từng chặng (4 chặng: Đi sân bay, Đến khách sạn, Đến sân bay về, Từ sân bay về) | Input cho phân xe |
| **Email xác nhận** | Tự động gửi email xác nhận ngay sau khi đăng ký thành công | Thông báo & lưu vết |

### Quy trình nghiệp vụ

```
1. Nhân viên đăng nhập → Hệ thống kiểm tra kỳ TB đang mở đăng ký
2. Hiển thị form đăng ký nhiều bước
3. Bước 1: Đọc quy định → Tích chọn đồng ý (bắt buộc)
4. Bước 2: Chọn ca làm việc (sáng/chiều) cho ngày đi và về
5. Bước 3: Chọn điểm đón/trả xe cho 4 chặng
6. Bước 4: Ghi chú bổ sung (không bắt buộc)
7. Xác nhận → Lưu database → Gửi email tự động
```

### Validation quan trọng
- Chỉ cho phép đăng ký khi `event.status = registration_open`
- Một CBNV chỉ đăng ký được 1 lần cho 1 kỳ
- Cho phép sửa đăng ký khi kỳ còn mở

---

## 3.3. Module 2: Quản lý chuyến bay & phân bổ

### Mục đích
Tự động phân bổ CBNV vào các chuyến bay phù hợp theo team và ca, giảm thiểu thao tác thủ công và sai sót.

### Chức năng chính

| Chức năng | Mô tả | Người dùng |
|---|---|---|
| **Import chuyến bay** | Nhập thông tin chuyến bay từ Excel: mã chuyến, giờ bay, số slot, giá vé | BTC |
| **Phân bổ tự động** | Thuật toán phân bổ CBNV vào chuyến bay dựa trên: team (ưu tiên giữ team cùng chuyến), ca làm việc, slot còn trống | BTC |
| **Preview trước khi áp dụng** | Xem trước kết quả phân bổ: số người/chuyến, team bị tách, slot còn lại | BTC |
| **Điều chỉnh thủ công** | Chuyển CBNV sang chuyến khác (có kiểm tra slot, cảnh báo tách team) | BTC |
| **Audit log** | Ghi lại mọi thay đổi: ai, khi nào, từ chuyến nào sang chuyến nào, lý do | Hệ thống |

### Thuật toán phân bổ (Greedy với trọng số)

**Input:**
- Danh sách CBNV đã đăng ký (team, ca làm việc)
- Danh sách chuyến bay (giờ bay, slot)

**Logic:**
1. Nhóm CBNV theo team
2. Với mỗi team, tìm chuyến bay phù hợp nhất:
   - Giờ bay phù hợp với ca làm việc
   - Đủ slot cho cả team
3. Nếu team quá lớn, tách thành nhóm nhỏ hơn
4. Ưu tiên: Giữ team cùng chuyến > Phù hợp giờ bay > Tối ưu số slot

**Output:**
- Danh sách phân bổ: CBNV → Chuyến bay
- Cảnh báo: Team bị tách, slot vượt mức (nếu có)

### Ràng buộc nghiệp vụ
- Không được vượt slot của chuyến bay
- Cảnh báo khi team bị tách ra nhiều chuyến
- Mọi thay đổi sau khi công bố phải ghi lý do

---

## 3.4. Module 3: Quản lý xe đưa đón

### Mục đích
Phân bổ xe phù hợp theo chặng hành trình và chuyến bay, đảm bảo đưa đón đúng người đúng giờ.

### Đặc điểm nghiệp vụ
Xe đưa đón có **4 chặng riêng biệt**:

| Chặng | Mô tả | Thời gian phụ thuộc |
|---|---|---|
| 1. Đến sân bay (đi) | Xe đón CBNV từ điểm tập trung đến sân bay | Giờ bay đi |
| 2. Đến khách sạn | Xe đón từ sân bay điểm đến về khách sạn | Giờ bay đến |
| 3. Đến sân bay (về) | Xe đưa từ khách sạn ra sân bay về | Giờ bay về |
| 4. Từ sân bay về nhà | Xe đưa từ sân bay về điểm trả | Giờ bay hạ cánh |

### Chức năng chính

| Chức năng | Mô tả |
|---|---|
| **Cấu hình xe theo chặng** | Mỗi chặng có danh sách xe riêng: mã xe, biển số, sức chứa, điểm đón/trả |
| **Phân xe tự động** | Dựa trên: chuyến bay đã phân, điểm đón đã chọn, sức chứa xe |
| **Liên kết với chuyến bay** | Xe chặng 1 liên kết với chuyến bay đi, xe chặng 3 liên kết với chuyến bay về |
| **Chỉ định Trưởng xe** | BTC chỉ định một CBNV làm Trưởng xe (điểm danh, hỗ trợ) |
| **Thông tin tài xế** | Lưu tên và SĐT tài xế cho mỗi xe |

### Ví dụ phân xe chặng 1

```
Chuyến bay VN101 (8:00) → 30 CBNV
  ├─ Điểm đón A (Hà Đông): 12 người → Xe 01 (16 chỗ)
  ├─ Điểm đón B (Cầu Giấy): 10 người → Xe 02 (16 chỗ)
  └─ Điểm đón C (Long Biên): 8 người → Xe 03 (16 chỗ)

Giờ tập trung: 6:00 (trước 2 tiếng)
```

---

## 3.5. Module 4: Gala Dinner - Chọn ghế

### Mục đích
Cho phép Team chọn ghế ngồi Gala Dinner một cách công bằng, tránh tranh chấp chỗ ngồi.

### Đặc điểm nghiệp vụ

**Cơ chế bốc thăm thứ tự:**
- Hệ thống random thứ tự các Team
- Team được chọn trước có lợi thế chọn vị trí đẹp
- Đảm bảo công bằng qua cơ chế ngẫu nhiên

### Chức năng chính

| Chức năng | Mô tả | Kỹ thuật |
|---|---|---|
| **Sơ đồ ghế trực quan** | Hiển thị layout bàn ghế dạng 2D, màu sắc phân biệt trạng thái | Canvas/SVG |
| **Bốc thăm thứ tự team** | Random thứ tự team chọn ghế (1 lần duy nhất) | Random seed |
| **Chọn ghế theo lượt** | Team chọn theo thứ tự, mỗi lần chọn cho cả team | Queue system |
| **Hold ghế tạm thời** | Khi đang chọn, ghế bị "hold" 120 giây, tránh 2 team chọn cùng lúc | Lock timeout |
| **Xác nhận ghế** | Sau khi chọn xong, xác nhận → ghế bị đánh dấu đã chọn vĩnh viễn | Database transaction |

### Quy trình chọn ghế

```
1. BTC bốc thăm thứ tự team → Công bố thứ tự
2. Team thứ 1 vào hệ thống → Xem sơ đồ ghế
3. Chọn bàn/ghế cho team (click trên sơ đồ)
4. Hệ thống hold ghế 120 giây
5. Team xác nhận → Ghế bị khóa
6. Team thứ 2 lặp lại bước 2-5 (thấy ghế team 1 đã bị khóa)
7. Tiếp tục cho đến hết
```

### Xử lý tranh chấp (Race condition)

**Vấn đề:** 2 team cùng chọn 1 ghế trong cùng 1 giây

**Giải pháp:**
- Database transaction với lock
- Kiểm tra ghế còn trống TRƯỚC khi ghi
- Team chọn sau nhận thông báo "Ghế đã có người chọn"

---

## 3.6. Module 5: My Journey - Tra cứu hành trình

### Mục đích
Cung cấp cho CBNV cái nhìn tổng quan, đầy đủ về toàn bộ hành trình Team Building của mình trên một màn hình duy nhất.

### Thông tin hiển thị

| Nhóm thông tin | Chi tiết |
|---|---|
| **Thông tin cá nhân** | Họ tên, team, điểm đón/trả đã chọn |
| **Chuyến bay** | 2 chiều: mã chuyến, giờ bay, sân bay, cổng |
| **Xe đưa đón** | 4 chặng: mã xe, điểm đón/trả, giờ tập trung, Trưởng xe, SĐT tài xế |
| **Khách sạn** | Tên khách sạn, địa chỉ, số phòng, loại phòng, người ở cùng |
| **Gala Dinner** | Bàn số mấy, ghế số mấy, danh sách người cùng bàn |
| **Lịch trình** | Timeline 3 ngày: sáng/chiều/tối mỗi ngày làm gì |
| **Thông báo** | Các thông báo từ BTC (thay đổi, nhắc việc) |

### Nguyên tắc hiển thị

**Theo trạng thái kỳ TB:**

| Trạng thái kỳ | CBNV thấy gì |
|---|---|
| `registration_open` | Chỉ thấy thông tin đăng ký của mình |
| `registration_closed` | Thông báo "BTC đang xử lý, vui lòng chờ" |
| `allocation_processing` | Thông báo "BTC đang xử lý, vui lòng chờ" |
| `information_published` | Thấy TOÀN BỘ thông tin hành trình |
| `event_started` | Thấy toàn bộ + có thể tải PDF |

**Quy tắc bảo mật:**
- CBNV chỉ thấy dữ liệu của chính mình
- Không thấy dữ liệu người khác (kể cả cùng team)
- Team leader thấy thêm danh sách team mình

### Thiết kế giao diện

**Mobile-first:**
- Màn hình chính được thiết kế cho điện thoại
- Use case: CBNV tra cứu tại sân bay, trên xe
- Layout: Cards xếp dọc, dễ scroll

**Tính năng bổ sung:**
- Export PDF hành trình cá nhân
- Thêm vào lịch (Calendar)
- Chia sẻ thông tin (email, SMS)

---

## 3.7. Chức năng bổ sung: Chatbot Tibi

### Mục đích
Trả lời tự động các câu hỏi thường gặp về lịch trình, quy định và hành trình cá nhân, giảm tải cho BTC.

### Phạm vi trả lời

| Loại câu hỏi | Ví dụ | Nguồn dữ liệu |
|---|---|---|
| **Quy định chung** | "Có được mang theo người thân không?" | Knowledge base |
| **Lịch trình** | "Gala Dinner diễn ra lúc mấy giờ?" | Lịch trình công khai |
| **Hành trình cá nhân** | "Tôi bay chuyến nào?" | Database (chỉ của người hỏi) |
| **Hướng dẫn** | "Làm sao để đổi điểm đón xe?" | FAQ |

### Công nghệ: RAG (Retrieval Augmented Generation)

**Quy trình:**
```
1. User hỏi câu hỏi
2. Hệ thống tìm kiếm tài liệu liên quan (Vector search)
3. Nếu câu hỏi về cá nhân → Gọi tool lấy dữ liệu của chính user
4. LLM tổng hợp câu trả lời từ tài liệu + dữ liệu
5. Trả về câu trả lời tự nhiên
```

### Bảo mật dữ liệu cá nhân

**Nguyên tắc quan trọng:**
- Chatbot KHÔNG BAO GIỜ trả lời về dữ liệu người khác
- Tool lấy dữ liệu cá nhân chỉ nhận `user_id` từ JWT (không cho user tự nhập)
- Không dùng text-to-SQL (tránh SQL injection lấy dữ liệu người khác)

**Ví dụ:**
```
❌ Sai: "Anh Trung bay chuyến nào?"
   → Từ chối: "Tôi chỉ cung cấp thông tin hành trình của bạn"

✅ Đúng: "Tôi bay chuyến nào?"
   → Trả lời: "Bạn bay chuyến VN101 lúc 8:00 ngày 15/12"
```