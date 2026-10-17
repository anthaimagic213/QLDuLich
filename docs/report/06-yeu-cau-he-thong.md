 # 6. Yêu cầu hệ thống
 
 ## 6.1. Yêu cầu chức năng chính
 
 ### Quản lý đăng ký
 - Cho phép CBNV đăng ký tham gia kỳ Team Building
 - Form đăng ký nhiều bước: thông tin cá nhân, xác nhận quy định, chọn ca, nhu cầu xe
 - Gửi email xác nhận tự động sau khi đăng ký
 - Cho phép sửa/hủy đăng ký khi kỳ còn mở
 - Theo dõi tỷ lệ đăng ký theo team/phòng ban
 
 ### Quản lý phân bổ tài nguyên
 - **Phân bổ chuyến bay tự động**: thuật toán xếp CBNV vào chuyến bay theo team và ca làm việc
 - **Phân bổ xe tự động**: phân xe theo 4 chặng (đi sân bay, đón sân bay, đi khách sạn cuối, về sân bay)
 - **Phân phòng khách sạn**: quản lý phòng đơn/đôi, giới tính, yêu cầu đặc biệt
 - Điều chỉnh thủ công với kiểm tra ràng buộc (slot, sức chứa)
 - Cảnh báo khi vượt sức chứa hoặc tách team
 
 ### Quản lý Gala Dinner
 - Thiết kế sơ đồ chỗ ngồi trực quan
 - Random thứ tự team chọn ghế (công bằng)
 - Cơ chế hold ghế tạm (120 giây) chống tranh chấp
 - Trưởng team chọn ghế cho cả team mình
 
 ### My Journey - Dashboard cá nhân
 - Hiển thị toàn bộ hành trình: chuyến bay đi/về, xe 4 chặng, phòng khách sạn, bàn/ghế Gala
 - Lịch trình chi tiết 3 ngày
 - Thông tin team và liên hệ
 - Thiết kế mobile-first (xem tại sân bay)
 
 ### Chatbot hỗ trợ (RAG)
 - Trả lời câu hỏi về lịch trình, quy định Team Building
 - Tra cứu hành trình của chính người hỏi
 - Bảo mật: không cho phép hỏi về thông tin người khác
 
 ## 6.2. Yêu cầu phi chức năng
 
 ### Tính linh hoạt
 - **Không hard-code**: số ca, chặng xe, sức chứa, team đều là dữ liệu cấu hình
 - Hỗ trợ nhiều kỳ Team Building song song
 - Dễ dàng thay đổi quy định, lịch trình mà không cần sửa code
 
 ### Bảo mật & phân quyền
 - Phân quyền rõ ràng: CBNV / Trưởng team / BTC / Super Admin
 - CBNV chỉ xem được dữ liệu của chính mình
 - Mọi thay đổi quan trọng đều có audit log
 - Hỗ trợ tích hợp SSO trong tương lai
 
 ### Tính minh bạch & truy vết
 - **Audit log đầy đủ**: ghi lại ai thay đổi gì, khi nào, lý do gì
 - Lưu giá trị trước/sau mỗi thay đổi (JSON)
 - Theo dõi lịch sử email gửi đi
 - Dashboard thống kê cho BTC
 
 ### Hiệu năng
 - Quy mô: hỗ trợ tối đa 1,000 CBNV/kỳ
 - Phân bổ tự động hoàn thành trong 5 giây
 - Responsive tốt trên mobile
 
 ### Trải nghiệm người dùng
 - Giao diện tiếng Việt
 - Định dạng ngày giờ Việt Nam (dd/MM/yyyy HH:mm)
 - Thông báo rõ ràng khi có lỗi
 - Email nhắc nhở tự động cho CBNV chưa đăng ký
 
 ## 6.3. Ràng buộc nghiệp vụ
 
 ### Vòng đời kỳ Team Building
 - Tuân thủ trạng thái: Draft → Mở đăng ký → Đóng đăng ký → Phân bổ → Công bố → Bắt đầu → Hoàn thành
 - Không cho phép thao tác sai thời điểm (ví dụ: đăng ký khi đã đóng)
 - Yêu cầu lý do khi quay lại bước trước
 
 ### Phân bổ
 - Ưu tiên giữ nguyên team trên cùng chuyến bay
 - Cảnh báo khi team bị tách
 - Không vượt quá slot/sức chứa
 - Phân xe phải khớp với chuyến bay đã phân
 
 ### Gala Dinner
 - Mỗi team chỉ chọn được số ghế bằng số thành viên
 - Không cho phép 2 team chọn cùng ghế (seat lock)
 - Kỳ không thể chuyển sang "Bắt đầu" nếu chưa xếp xong ghế
 
 ## 6.4. Tích hợp & mở rộng
 
 ### Hiện tại (MVP)
 - Gửi email qua SMTP (Mailpit cho demo)
 - Export danh sách Excel
 - Import chuyến bay, phòng từ Excel
 
 ### Tương lai (Phase 2)
 - Tích hợp SSO thực tế (LDAP, Azure AD)
 - Thông báo qua Microsoft Teams
 - Báo cáo BI nâng cao
 - Tối ưu thuật toán phân bổ (ILP/OR-Tools)
 - Mobile app native