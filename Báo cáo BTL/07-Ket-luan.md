# CHƯƠNG 7. KẾT LUẬN

## 7.1. Tổng kết

Đề tài phân tích và thiết kế hệ thống quản lý du lịch/Team Building nội bộ theo hướng tập trung vào vòng đời thông tin: cấu hình kỳ, khai nhu cầu, điều phối tài nguyên, công bố, tra cứu và xử lý hủy. Cách tiếp cận không chỉ chuyển bảng tính lên web mà xác định ranh giới actor, quyền sở hữu dữ liệu và các điểm cần bảo vệ tính nhất quán.

Báo cáo xây dựng bảy nhóm ca sử dụng trọng tâm, mô tả tiền/hậu điều kiện, luồng chính/thay thế/ngoại lệ và hợp đồng thao tác. Mô hình lĩnh vực và CRC làm rõ trách nhiệm; SSD phân tích hệ thống như hộp đen; các biểu đồ lớp/trình tự thiết kế phân tách API, nghiệp vụ và lưu trữ. Ma trận CRUD và truy vết nối yêu cầu với dữ liệu và test case.

Thiết kế dữ liệu chọn 12 bảng nghiệp vụ thay vì đưa toàn bộ schema 27 bảng vào thân báo cáo. Đăng ký là trung tâm một người trong một kỳ; phân bay tách theo chiều, xe biểu diễn qua dòng nhu cầu chặng và phòng nằm trên đăng ký hiện hành. Mô hình hành trình tổng hợp tránh tạo bản sao dữ liệu dễ lệch nhau.

## 7.2. Kết quả ở mức phân tích và thiết kế

- Xác định phạm vi nội bộ, không nhầm với bán tour/thanh toán.
- Phân tách hiện trạng và quy trình mục tiêu, không dựng số liệu khảo sát.
- Mô hình hóa quy trình có preview/xác nhận và kiểm lại lúc ghi.
- Phân biệt ràng buộc DB với điều kiện service: role, cùng kỳ, sức chứa và thời gian.
- Thiết kế hành trình chỉ đọc theo user/phase, không trả dữ liệu thử trước công bố.
- Đề xuất kế hoạch kiểm thử chức năng, cạnh tranh và quyền truy cập với kết quả mong đợi cụ thể.

Đây là kết quả của **tài liệu phân tích/thiết kế**. Không khẳng định đạt mục tiêu hiệu năng, giảm thời gian tổ chức hay tất cả chức năng chạy đúng khi chưa có phép đo và test mới. Các module hiện thực đã được tham khảo qua source; cần bổ sung log/ảnh demo để kết luận ở mức vận hành.

## 7.3. Hạn chế

Khảo sát dựa tài liệu project, chưa có phỏng vấn trực tiếp. Một số quy tắc học thuật được tinh giản để giữ chiều sâu; ngoại lệ sản phẩm thực tế có thể rộng hơn. SQLite có giới hạn ghi đồng thời; heuristic không bảo đảm tối ưu toàn cục. Sơ đồ/wireframe là bản nháp và cần chỉnh hình thức khi ghép Word/PDF. Kết quả kiểm thử thực tế chưa được bổ sung vì giới hạn môi trường trong lần biên soạn.

## 7.4. Hướng phát triển

Ưu tiên hoàn thành thử nghiệm xuyên suốt và cạnh tranh; đo hiệu năng bằng tập dữ liệu/môi trường xác định; chuẩn hóa quy trình thay đổi và lưu lý do; bổ sung chính sách lưu/xóa dữ liệu cá nhân. Khi tải tăng, đánh giá DB server dựa trên đo đạc thay vì chuyển chỉ vì tên công nghệ. Có thể bổ sung tối ưu phân bổ bằng mô hình ràng buộc, tích hợp SSO, module Gala hoặc hỏi đáp, nhưng phải phân tích quyền và dữ liệu riêng cho các tính năng đó.

## 7.5. Bài học phương pháp

Phân tích trước thiết kế giúp tránh nhầm actor với bảng hay giao diện, và tránh dựa toàn bộ schema hiện có để quyết định phạm vi báo cáo. Sự thống nhất giữa UC, hợp đồng, lớp, dữ liệu và test quan trọng hơn số lượng sơ đồ. Một mô hình tốt phải giải thích được cả trường hợp thành công, thất bại và thay đổi cạnh tranh, không chỉ minh họa luồng thuận lợi.