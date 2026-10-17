# 2. Phân tích bài toán nghiệp vụ

## 2.1. Quy trình tổ chức Team Building hiện tại

### Thực trạng

Khi một doanh nghiệp có quy mô 100+ nhân viên tổ chức chuyến Team Building, Ban Tổ Chức (BTC) thường phải đối mặt với quy trình phức tạp và phân tán:

1. **Thu thập thông tin đăng ký**
   - CBNV điền form Google Forms hoặc Excel riêng lẻ
   - BTC nhận về nhiều file Excel từ các phòng ban khác nhau
   - Khó kiểm soát thời hạn đăng ký và theo dõi ai chưa đăng ký

2. **Quản lý thông tin phân tán**
   - File Excel quản lý danh sách đăng ký
   - File Excel khác quản lý chuyến bay và slot
   - File Excel thứ ba quản lý phân xe
   - File Excel thứ tư quản lý phòng khách sạn
   - File PowerPoint hoặc Word quản lý sơ đồ bàn Gala Dinner
   - Không có nguồn dữ liệu chung (Single Source of Truth)

3. **Phân bổ thủ công tốn thời gian**
   - BTC phải tự tay phân CBNV vào các chuyến bay (cố gắng giữ team cùng bay)
   - Phân xe đưa đón theo từng chặng (sân bay → khách sạn → điểm tham quan → Gala)
   - Phân phòng khách sạn (2-3 người/phòng)
   - Sắp xếp chỗ ngồi Gala Dinner (cố gắng cùng team ngồi cùng bàn)
   - **Mất 2-3 ngày làm việc** cho BTC với kỳ 100 người

4. **Dễ xảy ra sai sót**
   - Vượt quá số slot chuyến bay
   - Xe quá tải hoặc để trống
   - Trùng phòng, trùng chỗ ngồi
   - Team bị tách rời trên các chuyến bay/xe khác nhau
   - Thay đổi một chỗ → phải cập nhật nhiều file

5. **Thiếu minh bạch với CBNV**
   - CBNV không biết mình đi chuyến bay nào, xe nào, ở phòng nào
   - Phải liên tục hỏi BTC qua Zalo/email
   - BTC phải trả lời lặp đi lặp lại cùng câu hỏi
   - Thông tin công bố muộn (1-2 ngày trước sự kiện)

6. **Không có lịch sử thay đổi**
   - Không biết ai đã sửa, sửa gì, khi nào
   - Khó truy vết khi có sự cố
   - Không có bằng chứng khi có tranh chấp

## 2.2. Hệ quả của thực trạng

### Đối với Ban Tổ Chức
- ⚠️ Tốn 2-3 ngày làm việc cho việc phân bổ thủ công
- ⚠️ Áp lực cao, dễ sai sót
- ⚠️ Phải xử lý hàng chục cuộc gọi/tin nhắn hỏi thông tin
- ⚠️ Khó điều chỉnh khi có thay đổi (ví dụ: 1 người hủy → phải xếp lại xe, phòng)

### Đối với Nhân viên
- 😟 Không biết lịch trình của mình
- 😟 Lo lắng về thông tin chuyến bay, giờ tập trung
- 😟 Phải chủ động hỏi BTC nhiều lần
- 😟 Nhận thông tin muộn, không chủ động chuẩn bị

### Đối với Lãnh đạo
- 📊 Không có báo cáo tổng quan
- 📊 Không theo dõi được tiến độ đăng ký
- 📊 Khó đánh giá hiệu quả tổ chức

## 2.3. Yêu cầu giải pháp

### Mục tiêu cốt lõi
> **"Một cổng duy nhất cho toàn bộ hành trình Team Building"**

### Yêu cầu từ góc nhìn nghiệp vụ

1. **Tập trung hóa dữ liệu**
   - Một hệ thống duy nhất quản lý toàn bộ thông tin
   - Thay đổi một chỗ → cập nhật mọi nơi
   - Loại bỏ việc đồng bộ dữ liệu giữa nhiều file Excel

2. **Tự động hóa phân bổ**
   - Hệ thống tự động phân chuyến bay theo team/ca
   - Tự động phân xe theo chuyến bay + địa điểm đón
   - Giảm thời gian phân bổ từ 2-3 ngày → **vài phút**

3. **Tăng tính minh bạch**
   - CBNV xem được toàn bộ hành trình của mình: chuyến bay → xe → phòng → Gala → lịch trình
   - Cập nhật real-time khi có thay đổi
   - Chatbot trả lời tự động các câu hỏi thường gặp

4. **Giảm thiểu sai sót**
   - Kiểm tra tự động: vượt slot, quá tải, xung đột
   - Cảnh báo khi team bị tách
   - Khóa chỗ ngồi Gala để tránh tranh chấp

5. **Truy vết và kiểm soát**
   - Ghi lại mọi thay đổi: ai, khi nào, làm gì, tại sao
   - Hỗ trợ điều tra khi có sự cố
   - Đảm bảo tuân thủ quy trình

6. **Dễ dàng sử dụng**
   - Giao diện thân thiện, mobile-first (CBNV tra cứu tại sân bay)
   - Quy trình đăng ký đơn giản, rõ ràng
   - Dashboard trực quan cho BTC

## 2.4. Phạm vi triển khai (MVP)

### Trong phạm vi
✅ 5 module chính: Đăng ký → Chuyến bay → Xe → Gala Dinner → My Journey  
✅ Phân bổ tự động chuyến bay và xe  
✅ Chatbot RAG trả lời câu hỏi  
✅ Audit log đầy đủ  
✅ Responsive cho cả mobile và desktop  

### Ngoài phạm vi (Phase 2)
❌ Phân phòng tự động nâng cao (MVP chỉ import Excel)  
❌ Tích hợp SSO thật (MVP dùng JWT)  
❌ Thông báo qua Microsoft Teams  
❌ Báo cáo BI phức tạp  
❌ Mobile app native  

## 2.5. Quy mô mục tiêu

- **Số lượng CBNV**: ≤ 1.000 người/kỳ
- **Số kỳ quản lý đồng thời**: 2-3 kỳ (kỳ hiện tại + kỳ sắp tới)
- **Thời gian phân bổ tự động**: ≤ 5 giây
- **Số người dùng đồng thời**: ~100 (peak khi công bố thông tin)

## 2.6. Lợi ích kỳ vọng

### Định lượng
- ⏱️ Giảm **80-90%** thời gian phân bổ (từ 2-3 ngày → vài phút)
- 📞 Giảm **70%** số cuộc hỏi/gọi từ CBNV đến BTC
- ❌ Giảm **90%** sai sót phân bổ (vượt slot, quá tải, trùng lặp)
- 📊 Tăng **100%** tính minh bạch (CBNV biết hành trình của mình)

### Định tính
- ✨ Nâng cao trải nghiệm nhân viên
- 🎯 BTC tập trung vào công việc chiến lược thay vì thủ công
- 🔒 Tăng tính chuyên nghiệp và minh bạch trong tổ chức sự kiện
- 📈 Có dữ liệu để cải tiến các kỳ sau