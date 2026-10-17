# BÁO CÁO BÀI TẬP LỚN — PHÂN TÍCH THIẾT KẾ HỆ THỐNG

## Đề tài: Hệ thống quản lý du lịch và Team Building nội bộ

Bộ tài liệu này trình bày nội dung báo cáo theo bảy chương của **NoiDungBaoCaoBTL.pdf**, kết hợp phương pháp mô hình hóa trong **Báocáo.pdf**. Đối tượng nghiên cứu là hoạt động tổ chức chuyến du lịch nội bộ, không phải hệ thống bán tour thương mại. Trọng tâm là quản lý kỳ, đăng ký, hủy tham gia, phân chuyến bay, phân xe, xếp phòng và công bố hành trình. Chatbot và chọn ghế Gala không thuộc phạm vi phân tích chi tiết.

### Thứ tự ghép bản báo cáo

1. [Chương 1 — Đặt vấn đề](01-Dat-van-de.md)
2. [Chương 2 — Phân tích nghiệp vụ](02-Phan-tich-nghiep-vu.md)
3. [Chương 3 — Phân tích yêu cầu](03-Phan-tich-yeu-cau.md)
4. [Chương 4A — Kiến trúc và thiết kế ca sử dụng](04A-Kien-truc-va-thiet-ke-ca-su-dung.md)
5. [Chương 4B — Thiết kế cơ sở dữ liệu](04B-Thiet-ke-co-so-du-lieu.md)
6. [Chương 4C — Thiết kế giao diện](04C-Thiet-ke-giao-dien.md)
7. [Chương 5 — Thực hiện và triển khai](05-Thuc-hien-va-trien-khai.md)
8. [Chương 6 — Thử nghiệm và đánh giá](06-Thu-nghiem-va-danh-gia.md)
9. [Chương 7 — Kết luận](07-Ket-luan.md)
10. [Tài liệu tham khảo và đối chiếu mẫu](08-Tai-lieu-tham-khao-va-doi-chieu.md)

Chương 4 được chia ba file để thuận tiện chỉnh sửa, khi ghép báo cáo vẫn là một chương. Các hình Mermaid là **sơ đồ nháp**, không phải ảnh chụp hệ thống. Đánh số hình theo chương và giữ nội dung khi vẽ lại bằng Excalidraw/UML editor. Những flowchart dùng để phác Use Case, gói hoặc điều hướng được ghi rõ không phải ký pháp UML/IFML hoàn chỉnh.

Chương 3 tổ chức ba góc nhìn **chức năng–cấu trúc–hành vi** cho cả 7 UC: đặc tả chức năng; kịch bản, lớp phân tích và CRC; activity, state machine cần thiết và SSD. Chương 2 giữ mô hình lĩnh vực chung; Chương 4 giữ thiết kế kỹ thuật, không nhầm sequence API/service với SSD hộp đen.

### Căn cứ và độ tin cậy

- Hai PDF mẫu và tám PDF bài giảng đã được trích xuất văn bản và đối chiếu các phần liên quan. Báo cáo mẫu 168 trang dùng bảy nhóm Use Case, mô hình lớp, CRC, hành vi, CRUD, ánh xạ bảng, DAM và giao diện. Hướng dẫn 12 trang quy định bảy chương, Operation Contracts và SSD.
- Schema được tham khảo từ models và `ERD.MD` hiện hành, không lấy schema lịch sử làm thiết kế đang chạy.
- Khảo sát hiện trạng được xây dựng từ mô tả nhu cầu trong repository; không có biên bản phỏng vấn trực tiếp. Không khẳng định các số liệu tiết kiệm chi phí/thời gian đã được đo.
- Mô hình phân tích có thể tinh giản so với phần mềm. Lớp Repository/DAM trong thiết kế là **phương án phân tách trách nhiệm**, không khẳng định code hiện có đầy đủ các class tương ứng.
- Chương 6 là kế hoạch và tiêu chí kiểm thử chi tiết. Chưa có kết quả chạy ứng dụng mới trong lần lập báo cáo vì Docker engine không hoạt động và không có Python CLI. Không ghi kết quả Pass giả.
- Trang bìa, tên trường, giảng viên, sinh viên, MSSV và phân công cá nhân không được tự điền bằng thông tin của nhóm trong báo cáo mẫu.

### Quy ước thống nhất

`UC-01` quản lý kỳ; `UC-02` đăng ký; `UC-03` xử lý hủy; `UC-04` phân chuyến bay; `UC-05` phân xe; `UC-06` xếp phòng; `UC-07` công bố/tra cứu hành trình. Đăng nhập, danh mục người dùng và nhật ký là chức năng hỗ trợ, không mở thành các nhóm lớn khiến báo cáo lan rộng.

PK: khóa chính; FK: khóa ngoại; UQ: duy nhất; NN: không null. CBNV: cán bộ nhân viên; BTC: ban tổ chức; SSD: biểu đồ trình tự hệ thống; CRC: Class–Responsibility–Collaborator; DAM: quản lý truy cập dữ liệu.