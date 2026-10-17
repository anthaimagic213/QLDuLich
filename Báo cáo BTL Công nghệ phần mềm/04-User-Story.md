# 4. User Stories

## 4.1. Giới thiệu về User Story

User Story là cách mô tả yêu cầu chức năng từ góc nhìn người dùng cuối, theo format:

```
Là một <vai trò>
Tôi muốn <chức năng>
Để mà <lợi ích>
```

## 4.2. Phân nhóm User Stories theo Module

### Module 1: Đăng ký tham gia (Registration)

#### US-01: Đăng ký tham gia Team Building
**Là một** Nhân viên  
**Tôi muốn** điền form đăng ký tham gia kỳ Team Building  
**Để mà** BTC biết tôi có tham gia và có thể phân bổ chuyến bay, xe, phòng cho tôi

**Acceptance Criteria:**
- ✅ Form có nhiều bước: thông tin cá nhân → quy định → ca làm việc → nhu cầu xe → xác nhận
- ✅ Phải tích chọn "Đồng ý với quy định" mới được tiếp tục
- ✅ Lưu version quy định đã đồng ý (để audit)
- ✅ Gửi email xác nhận ngay sau khi đăng ký thành công
- ✅ Chỉ cho phép đăng ký khi kỳ TB ở trạng thái "Mở đăng ký"

---

#### US-02: Sửa thông tin đăng ký
**Là một** Nhân viên  
**Tôi muốn** sửa thông tin đăng ký (ca làm việc, điểm đón xe)  
**Để mà** cập nhật khi tôi có thay đổi kế hoạch

**Acceptance Criteria:**
- ✅ Chỉ cho phép sửa khi kỳ còn mở đăng ký
- ✅ Hiển thị thông tin đã đăng ký trước đó
- ✅ Gửi email thông báo thay đổi
- ✅ Ghi audit log

---

#### US-03: Hủy đăng ký
**Là một** Nhân viên  
**Tôi muốn** hủy đăng ký khi có việc đột xuất  
**Để mà** không chiếm slot của người khác

**Acceptance Criteria:**
- ✅ Chỉ cho phép hủy khi kỳ còn mở đăng ký
- ✅ Hiển thị cảnh báo "Bạn có chắc chắn muốn hủy?"
- ✅ Gửi email xác nhận hủy
- ✅ Cập nhật trạng thái đăng ký thành "Đã hủy"

---

### Module 2: Quản lý chuyến bay (Flight Management)

#### US-04: Theo dõi tình trạng đăng ký
**Là một** BTC  
**Tôi muốn** xem dashboard số lượng CBNV đã đăng ký theo từng team  
**Để mà** biết team nào còn nhiều người chưa đăng ký và nhắc nhở

**Acceptance Criteria:**
- ✅ Dashboard hiển thị: tổng đã đăng ký / tổng CBNV
- ✅ Phân tích theo team: Team A: 12/15, Team B: 8/12, ...
- ✅ Danh sách CBNV chưa đăng ký (có thể gửi email nhắc)
- ✅ Real-time update

---

#### US-05: Phân bổ chuyến bay tự động
**Là một** BTC  
**Tôi muốn** hệ thống tự động phân bổ CBNV vào các chuyến bay  
**Để mà** tiết kiệm thời gian thay vì phân thủ công (mất 2-3 ngày)

**Acceptance Criteria:**
- ✅ Thuật toán ưu tiên giữ team cùng chuyến bay
- ✅ Phân bổ theo ca làm việc (sáng/chiều)
- ✅ Không vượt quá số slot của mỗi chuyến
- ✅ Hiển thị preview trước khi xác nhận
- ✅ Cảnh báo khi team bị tách
- ✅ Thời gian xử lý ≤ 5 giây cho 1000 người

---

#### US-06: Điều chỉnh phân bổ thủ công
**Là một** BTC  
**Tôi muốn** chuyển một CBNV từ chuyến này sang chuyến khác  
**Để mà** xử lý các trường hợp ngoại lệ (ví dụ: CBNV yêu cầu đổi ca)

**Acceptance Criteria:**
- ✅ Kiểm tra slot còn trống trước khi chuyển
- ✅ Cảnh báo nếu chuyển làm team bị tách
- ✅ Bắt buộc nhập lý do khi điều chỉnh
- ✅ Ghi audit log đầy đủ
- ✅ Gửi email thông báo đến CBNV bị ảnh hưởng

---

### Module 3: Quản lý xe (Bus Management)

#### US-07: Phân xe tự động theo chuyến bay
**Là một** BTC  
**Tôi muốn** hệ thống tự động phân xe cho CBNV theo chuyến bay và điểm đón  
**Để mà** đảm bảo xe đón đúng người đúng giờ

**Acceptance Criteria:**
- ✅ Phân xe cho 4 chặng: đến sân bay (đi), rời sân bay (đến), đến resort, rời resort (về)
- ✅ Gom CBNV cùng chuyến bay và cùng điểm đón lên cùng xe
- ✅ Ưu tiên giữ team cùng xe
- ✅ Không vượt sức chứa xe
- ✅ Hiển thị danh sách từng xe: số xe, biển số, danh sách hành khách

---

#### US-08: Chỉ định Trưởng xe
**Là một** BTC  
**Tôi muốn** chỉ định một CBNV làm Trưởng xe cho mỗi chuyến xe  
**Để mà** có người điểm danh và hỗ trợ trong quá trình di chuyển

**Acceptance Criteria:**
- ✅ Chọn Trưởng xe từ danh sách CBNV trên xe đó
- ✅ Trưởng xe nhận email thông báo (có danh sách hành khách và SĐT tài xế)
- ✅ Hiển thị thông tin Trưởng xe trên My Journey của các CBNV cùng xe

---

### Module 4: Gala Dinner

#### US-09: Chọn chỗ ngồi Gala cho team
**Là một** Trưởng team  
**Tôi muốn** chọn chỗ ngồi Gala Dinner cho cả team mình  
**Để mà** team ngồi gần nhau và ở vị trí mong muốn

**Acceptance Criteria:**
- ✅ Hiển thị sơ đồ chỗ ngồi dạng 2D (bàn tròn, ghế xung quanh)
- ✅ Phân biệt màu: ghế trống / đã chọn / đang hold
- ✅ Chỉ cho phép chọn đủ số ghế bằng số thành viên team
- ✅ Hold ghế 120 giây (chống team khác chọn trùng)
- ✅ Xác nhận → lock ghế vĩnh viễn
- ✅ Không cho phép chọn khi chưa đến lượt team mình

---

#### US-10: Bốc thăm thứ tự chọn ghế
**Là một** BTC  
**Tôi muốn** hệ thống random thứ tự các team chọn ghế  
**Để mà** đảm bảo công bằng (tránh team nào cũng muốn chọn trước)

**Acceptance Criteria:**
- ✅ Random 1 lần duy nhất khi BTC click "Bốc thăm"
- ✅ Hiển thị kết quả: Team A → Team B → Team C → ...
- ✅ Gửi email thông báo thứ tự đến các Trưởng team
- ✅ Lưu seed random để audit

---

### Module 5: My Journey - Hành trình cá nhân

#### US-11: Xem toàn bộ hành trình của mình
**Là một** Nhân viên  
**Tôi muốn** xem toàn bộ hành trình của mình trên một màn hình  
**Để mà** biết chuyến bay nào, xe nào, phòng nào, ngồi đâu trong Gala mà không phải hỏi BTC

**Acceptance Criteria:**
- ✅ Hiển thị đầy đủ:
  - Thông tin cá nhân (họ tên, team)
  - Chuyến bay đi/về (mã chuyến, giờ, sân bay)
  - Xe đưa đón 4 chặng (mã xe, điểm đón, giờ tập trung, Trưởng xe, SĐT tài xế)
  - Phòng khách sạn (số phòng, tầng, người cùng phòng)
  - Chỗ ngồi Gala Dinner (bàn, ghế, người cùng bàn)
  - Lịch trình chi tiết 3 ngày
- ✅ Thiết kế mobile-first (dễ xem trên điện thoại tại sân bay)
- ✅ Chỉ hiển thị khi BTC đã công bố (trước đó hiển thị "Đang chờ BTC")
- ✅ Có nút Export PDF hành trình

---

#### US-12: Hỏi chatbot về hành trình
**Là một** Nhân viên  
**Tôi muốn** hỏi chatbot về lịch trình và hành trình của mình  
**Để mà** nhanh chóng có câu trả lời mà không cần tìm kiếm

**Acceptance Criteria:**
- ✅ Trả lời được câu hỏi về:
  - Quy định chung: "Có được mang người thân không?"
  - Lịch trình: "Gala Dinner lúc mấy giờ?"
  - Hành trình cá nhân: "Tôi bay chuyến nào?", "Xe tôi giờ mấy?"
- ✅ Chatbot chỉ trả lời về dữ liệu của chính người hỏi (không lộ dữ liệu người khác)
- ✅ Giao diện chat thân thiện
- ✅ Thời gian phản hồi ≤ 3 giây

---

### Module 6: Quản trị hệ thống

#### US-13: Chuyển trạng thái kỳ Team Building
**Là một** BTC  
**Tôi muốn** chuyển trạng thái kỳ TB qua các giai đoạn  
**Để mà** kiểm soát quy trình (mở/đóng đăng ký, công bố thông tin, ...)

**Acceptance Criteria:**
- ✅ Tuân thủ state machine:
  ```
  Draft → Mở đăng ký → Đóng đăng ký → Đang phân bổ 
        → Đã công bố → Đang diễn ra → Hoàn thành
  ```
- ✅ Kiểm tra điều kiện trước khi chuyển (ví dụ: không chuyển sang "Đang diễn ra" nếu Gala chưa xếp xong)
- ✅ Ghi audit log
- ✅ Gửi email thông báo đến CBNV khi chuyển sang "Đã công bố"

---

#### US-14: Xem audit log
**Là một** BTC  
**Tôi muốn** xem lịch sử thay đổi (ai sửa gì, khi nào)  
**Để mà** truy vết khi có vấn đề hoặc tranh chấp

**Acceptance Criteria:**
- ✅ Hiển thị: thời gian, người thực hiện, hành động, đối tượng, giá trị trước/sau
- ✅ Lọc theo: kỳ TB, loại hành động, thời gian, người thực hiện
- ✅ Export Excel
- ✅ Không cho phép xóa log

---

## 4.3. Phân loại theo độ ưu tiên (MoSCoW)

### Must Have (Bắt buộc - MVP)
- ✅ US-01: Đăng ký tham gia
- ✅ US-05: Phân bổ chuyến bay tự động
- ✅ US-07: Phân xe tự động
- ✅ US-09: Chọn chỗ ngồi Gala
- ✅ US-11: Xem My Journey
- ✅ US-13: Chuyển trạng thái kỳ

### Should Have (Nên có)
- 🔹 US-02: Sửa thông tin đăng ký
- 🔹 US-04: Dashboard theo dõi đăng ký
- 🔹 US-06: Điều chỉnh phân bổ thủ công
- 🔹 US-08: Chỉ định Trưởng xe
- 🔹 US-12: Chatbot
- 🔹 US-14: Xem audit log

### Could Have (Có thể có)
- 🟡 US-03: Hủy đăng ký
- 🟡 US-10: Bốc thăm thứ tự Gala
- 🟡 Email tự động nhắc nhở

### Won't Have (Phase 2)
- ❌ Tích hợp SSO
- ❌ Mobile app native
- ❌ Báo cáo BI nâng cao

---

## 4.4. Story Points ước lượng

| User Story | Độ phức tạp | Story Points | Ghi chú |
|---|---|---|---|
| US-01 | Trung bình | 5 | Form nhiều bước, validation |
| US-05 | Cao | 13 | Thuật toán phân bổ phức tạp |
| US-06 | Trung bình | 8 | Logic validation + audit |
| US-07 | Cao | 13 | Tương tự US-05 nhưng có 4 chặng |
| US-09 | Rất cao | 21 | Canvas 2D, lock mechanism, real-time |
| US-11 | Trung bình | 8 | Tổng hợp nhiều nguồn dữ liệu |
| US-12 | Cao | 13 | Tích hợp RAG, tool calling |
| US-14 | Thấp | 3 | CRUD đơn giản |

**Tổng Story Points (MVP)**: ~70 points

---

## 4.5. Kết luận

Đã phân tích **14 User Stories** chính, phân nhóm theo 6 module nghiệp vụ. Ưu tiên triển khai 6 user stories bắt buộc trong MVP, sau đó mở rộng dần theo phản hồi người dùng.