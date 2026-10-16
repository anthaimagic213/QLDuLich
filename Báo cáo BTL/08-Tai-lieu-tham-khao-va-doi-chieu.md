# TÀI LIỆU THAM KHẢO VÀ ĐỐI CHIẾU MẪU

## 1. Nguồn học phần và báo cáo mẫu

1. `D:/QLDuLich/NoiDungBaoCaoBTL.pdf`, **Nội dung báo cáo bài tập lớn môn học Phân tích thiết kế hệ thống**, 12 trang. Chương 1: đặt vấn đề; Chương 2: nghiệp vụ (optional); Chương 3: yêu cầu, Operation Contracts, SSD; Chương 4: kiến trúc/kỹ thuật/cấu trúc và hành vi UC/giao diện; Chương 5: thực hiện/triển khai; Chương 6: thử nghiệm/đánh giá; Chương 7: kết luận.
2. `D:/QLDuLich/Báocáo.pdf`, **Thiết kế hệ thống quản lý đào tạo**, nhóm Sa tị, Đại học Bách khoa Hà Nội, tháng 6/2026, 168 trang. Tham khảo phương pháp, không sao chép thông tin nhóm/tác giả vào trang bìa đề tài mới.
3. `D:/QLDuLich/l02-Enviroment Modeling - Feasibility.pdf`: mô hình môi trường và tính khả thi.
4. `D:/QLDuLich/l03- Buisiness - Requirement Modeling.pdf`: nghiệp vụ và yêu cầu.
5. `D:/QLDuLich/l04-FunctionalModeling.pdf`: mô hình chức năng/ca sử dụng.
6. `D:/QLDuLich/l05-StructuralModeling.pdf`: mô hình cấu trúc, lớp và trách nhiệm.
7. `D:/QLDuLich/l06- Behavioral_Modeling.pdf`: mô hình hành vi và tương tác.
8. `D:/QLDuLich/l07- Architecture Design.pdf`: thiết kế kiến trúc.
9. `D:/QLDuLich/l08- Class Method Design.pdf`: thiết kế lớp/phương thức, gắn kết và phụ thuộc.
10. `D:/QLDuLich/l10- Database design.pdf`: thiết kế dữ liệu, chuẩn hóa và ánh xạ mô hình.

Tên tác giả/năm xuất bản slide không được tự bổ sung nếu metadata/tài liệu chưa xác nhận. Khi nộp, có thể chuyển danh sách sang chuẩn trích dẫn khoa yêu cầu.

## 2. Đối chiếu cấu trúc báo cáo

| Nội dung nguồn | Trang mẫu/hướng dẫn | Vị trí trong báo cáo mới |
|---|---|---|
| Ngữ cảnh, mục tiêu, phạm vi, stakeholder | Hướng dẫn tr.1–2; mẫu tr.6–9 | Chương 1 |
| Cơ cấu, quy trình, lớp lĩnh vực | Hướng dẫn tr.2 | Chương 2 |
| Use Case và đặc tả | Mẫu tr.10–22; hướng dẫn tr.3–7 | Chương 3 |
| Lớp lĩnh vực và CRC | Mẫu tr.23–63 | Chương 2 và thiết kế Chương 4A |
| Hành vi/tương tác | Mẫu tr.64–81 | State Chương 2; SSD Chương 3; sequence Chương 4A |
| CRUD | Mẫu tr.82–83 | Chương 3 |
| Làm giàu mô hình | Mẫu tr.84–88 | Chương 4A |
| Ánh xạ bảng, chuẩn hóa, DAM | Mẫu tr.89–101 | Chương 4A/4B |
| Kiến trúc | Mẫu tr.102–103 | Chương 4A, Chương 5 |
| Giao diện, điều hướng và prototype | Mẫu tr.104–168 | Chương 4C |
| Thực hiện/triển khai/đánh giá/kết luận | Hướng dẫn tr.10–12 | Chương 5–7 |

Hai mẫu có cách chia chương khác nhau; báo cáo này ưu tiên bảy chương trong **hướng dẫn nội dung**, còn mẫu dài cung cấp độ sâu mô hình. Không sao chép sai sót về tên UC hoặc cách đánh số lặp trong mẫu.

## 3. Nguồn hiện thực project

- `D:/QLDuLich/README.md`, `D:/QLDuLich/docs/product-overview.md`, `D:/QLDuLich/docs/01-requirements.md`: bối cảnh và yêu cầu. Một số mô tả là thiết kế lịch sử, cần đối chiếu code.
- `D:/QLDuLich/ERD.MD`, `D:/QLDuLich/backend/app/models/`: schema hiện hành.
- `D:/QLDuLich/backend/app/services/event_service.py`: transitions và khóa cấu hình; lý do chuyển tùy chọn hiện hành.
- `D:/QLDuLich/backend/app/api/v1/`, `D:/QLDuLich/backend/app/services/`: phân quyền và xử lý UC.
- `D:/QLDuLich/backend/app/core/database.py`: SQLite PRAGMA/transaction.
- `D:/QLDuLich/docker-compose.yml`, `D:/QLDuLich/.env.example`: môi trường và secret bắt buộc.
- `D:/QLDuLich/frontend/package.json`, `D:/QLDuLich/backend/pyproject.toml`: stack/lệnh kiểm tra.
- `D:/QLDuLich/docs/05-allocation-algorithm.md`, `D:/QLDuLich/docs/12-test-cases.md`: thiết kế/test tham khảo, không lấy số test cũ làm kết quả lần chạy mới.

## 4. Ghi chú về cách đọc PDF

Văn bản của hai PDF và tám slide được trích xuất bằng PDF.js trong thư mục tạm bên ngoài source. Mẫu 168 trang có nhiều sơ đồ dạng ảnh/vector: trích text không bảo toàn mọi đường nối và bố cục đồ họa. Nội dung chữ/đề mục đã được đối chiếu, nhưng sơ đồ trong báo cáo mới được tự dựng theo nghiệp vụ và models, không tuyên bố sao chép chính xác từng hình mẫu. Các bản text tạm không cần đưa vào báo cáo nộp.

## 5. Danh mục việc biên tập cuối

Đưa tên trường/nhóm thật vào bìa; tạo mục lục tự động; ghép ba file Chương 4; render các khối Mermaid thành hình; chỉnh nhãn hình/giãn trang; bổ sung ảnh demo và log kiểm thử thật; kiểm tra trích dẫn; không đưa dữ liệu nhạy cảm. Nội dung các chương đã được viết, phần chưa có là bằng chứng thực thi và thông tin hành chính không được tự bịa.