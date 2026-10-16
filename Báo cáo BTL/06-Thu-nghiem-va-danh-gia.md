# CHƯƠNG 6. THỬ NGHIỆM VÀ ĐÁNH GIÁ

## 6.1. Mục tiêu và phạm vi

Kiểm thử xác nhận các ca sử dụng trọng tâm, sự nhất quán giữa các module và quyền truy cập. Ưu tiên lỗi làm sai dữ liệu: trùng đăng ký, vượt chỗ, sai kỳ/chặng/chiều, hủy không giải phóng đúng và lộ hành trình người khác. Kiểm thử không chỉ là mở các màn hình không báo lỗi.

Chương này cung cấp **kế hoạch, dữ liệu và kết quả mong đợi**. Trong lần biên soạn, Docker daemon không hoạt động và không có Python CLI nên chưa chạy lại backend/frontend hoàn chỉnh. Không ghi Pass hoặc số test thành công dựa trên tài liệu cũ. Kết quả thực tế được ghi là **chưa thực thi** cho các ca dưới đây.

## 6.2. Chiến lược kiểm thử

1. Unit test cho allocator và rule độc lập, dùng dữ liệu tổng hợp và không gọi mạng.
2. Integration test cho service/API/DB: transaction, FK, unique, role/ownership.
3. End-to-end bằng tài khoản test: đăng ký → phân bổ → công bố → xem → hủy.
4. Kiểm UI responsive, loading/error, số liệu sau invalidation.
5. Kiểm cạnh tranh: hai request cùng chỗ cuối, double submit/approve.
6. Kiểm hiệu năng với dữ liệu và môi trường đo được; báo cáo median/p95 hoặc ít nhất min/avg/max của số lần chạy xác định.

## 6.3. Dữ liệu thử nghiệm

Bộ dữ liệu tổng hợp đề xuất có hai kỳ K1/K2, người tham gia P1/P2/P3, người không tham gia P4, người thiếu giới tính P5. K1 có một chuyến đi F1 khả dụng 2 slot, chuyến về F2, chặng L1 và L2; B1 thuộc L1 có 2 chỗ, B2 thuộc L2; Hotel H1 thuộc K1 và H2 thuộc K2; R1 male, R2 female, R3 any. Dùng dữ liệu khác giới/khác kỳ để chủ động kiểm lỗi, không chỉ dùng trường hợp hợp lệ.

Mỗi test cần reset fixture hoặc tạo kỳ riêng để tránh phụ thuộc thứ tự; kiểm số bản ghi trước/sau. Không dùng dữ liệu cá nhân thật. Các mã trên là đề xuất dữ liệu test, không phải ID chắc chắn có trong seed hiện hành.

## 6.4. Kịch bản thử nghiệm chi tiết

Trong bảng, trạng thái mặc định của **tất cả TC là Chưa thực thi**. Kết quả mong đợi là tiêu chí thiết kế; khi hiện thực khác, ghi Fail hoặc khác biệt phạm vi, không chỉnh lại kỳ vọng sau khi xem kết quả để làm đẹp báo cáo.

| Mã | Tiền điều kiện và bước thử | Kết quả mong đợi |
|---|---|---|
| TC-01 | BTC tạo K1, ngày về trước ngày đi | Từ chối; không có kỳ dở dang. |
| TC-02 | K1 draft; BTC chuyển thẳng published | Từ chối transition; trạng thái/audit không thể hiện thành công giả. |
| TC-03 | K1 mở; P1 khai đủ, chấp thuận quy định và gửi | Đúng một đăng ký; nhu cầu và consent cùng lưu. |
| TC-04 | P1 gửi hai request tạo đồng thời | Không có hai bản `(event,user)`; lỗi/response nhất quán. |
| TC-05 | K1 đóng khi P1 đang nhập; gửi mới thông thường | Từ chối do trạng thái; không lưu một phần. Ngoại lệ đăng ký lại được test riêng nếu dùng. |
| TC-06 | P1 chọn shift/pickup thuộc K2 | Từ chối dữ liệu khác kỳ. |
| TC-07 | P1 sửa nhu cầu từ cần xe sang tự đi khi giai đoạn cho phép | Dữ liệu nhu cầu đúng; không giữ bus trái nhu cầu. |
| TC-08 | P1 đã phân bổ, gửi hủy cần duyệt | Tạo pending; bay/xe/phòng giữ nguyên. |
| TC-09 | P1 gửi pending thứ hai | Không tạo hai pending; giữ lịch sử. |
| TC-10 | BTC duyệt hủy P1 đang có bay/xe/phòng | Registration cancelled; liên kết tài nguyên giải phóng; quyết định/audit nhất quán. |
| TC-11 | BTC từ chối yêu cầu hoặc duyệt lại yêu cầu đã xử lý | Từ chối giữ chỗ hiện tại; duyệt lặp không giải phóng/ghi sai lần nữa. |
| TC-12 | BTC preview phân bay trên nguồn hợp lệ | Có phương án/flags; bản phân bổ chính thức trước/sau không đổi. |
| TC-13 | F1 chỉ 2 slot, có 3 người cần đi | Không xếp 3 vào F1; có người chưa xếp/flag. |
| TC-14 | Gán đăng ký chiều đi vào chuyến về | Từ chối; FK ghép/service không cho sai chiều. |
| TC-15 | P1 có gán manual; chạy auto không force | Manual giữ theo chính sách; auto không ghi đè âm thầm. |
| TC-16 | Preview xong, thêm gán chiếm slot rồi commit cũ | Kiểm lại và báo xung đột/preview lại; không vượt slot. |
| TC-17 | Gán B2 thuộc L2 cho nhu cầu L1 | Từ chối sai chặng. |
| TC-18 | B1 có 2 chỗ, hai request giành chỗ cuối | Tổng người ≤2, một yêu cầu bị từ chối nếu cần. |
| TC-19 | Chặng sân bay: giờ xe không phù hợp chuyến người | Phát hiện theo rule thời gian, không công bố như hợp lệ. |
| TC-20 | Người không cần xe được gán B1 | Từ chối hoặc yêu cầu thay nhu cầu hợp lệ trước; không vi phạm CHECK. |
| TC-21 | R1 capacity 2 đã đủ; chuyển thêm người | Từ chối; phòng cũ của người đó giữ nguyên. |
| TC-22 | Người nữ vào phòng policy male | Từ chối policy. |
| TC-23 | P5 thiếu giới tính vào phòng chỉ male/female | Từ chối; hiển thị cần bổ sung/room any hợp lệ. |
| TC-24 | Gán phòng thuộc H2/K2 cho đăng ký K1 | Từ chối khác kỳ. |
| TC-25 | CBNV đọc hành trình lúc đang phân bổ | Không trả phân bổ thử; trạng thái chờ công bố. |
| TC-26 | BTC công bố khi có lỗi cứng trong checklist | Chặn chuyển trạng thái; báo lỗi xử lý được. |
| TC-27 | Sau công bố, P1 mở journey/me | Chỉ hành trình P1, thông tin từ nguồn hiện hành. |
| TC-28 | P1 gọi journey/{P2} hoặc sửa ID request | Chặn quyền; không lộ dữ liệu P2. |
| TC-29 | BTC chuyển P1 từ F1 sang chuyến khác hợp lệ | Audit có actor/time/trước-sau phù hợp; dashboard/hành trình tải lại đúng. |
| TC-30 | Cố gán ID tài nguyên không tồn tại | Từ chối, không có liên kết mồ côi. |
| TC-31 | Preview không xếp đủ, đọc danh sách cảnh báo | Tên/đối tượng và nguyên nhân đủ để BTC xử lý theo quyền. |
| TC-32 | Restart hệ thống sau ghi dữ liệu; không reset volume | Dữ liệu và quan hệ giữ; không seed đè ngoài ý muốn. |

## 6.5. Kịch bản xuyên suốt

**Kịch bản 1 — Chuyến đi bình thường:** BTC tạo kỳ và mở đăng ký; P1 gửi; BTC đóng và chuyển phân bổ; preview/xác nhận bay đi/về, xe các chặng có nhu cầu, phòng; kiểm checklist và công bố; P1 xem hành trình. Bằng chứng gồm ảnh các bước quan trọng, response API và truy vấn xác nhận số bản ghi; không cần chụp mọi thao tác CRUD.

**Kịch bản 2 — Hủy sau công bố:** P1 có tài nguyên và gửi yêu cầu; kiểm chỗ chưa mất khi pending; BTC duyệt; kiểm đồng thời registration/cancellation/bay/xe/phòng/audit. Dashboard và hành trình sau refresh phải phản ánh hủy. Đây là phép thử nhất quán xuyên module.

**Kịch bản 3 — Thay đổi cạnh tranh:** preview tạo khi còn một slot; request khác chiếm slot trước commit; commit cũ phải kiểm lại. Bằng chứng phải ghi thứ tự request và trạng thái cuối, không chỉ lỗi một màn hình.

## 6.6. Cách chạy và thu kết quả

Sau khi triển khai thành công theo Chương 5:

```powershell
Set-Location 'D:/QLDuLich'
docker compose exec backend pytest -q
Set-Location 'D:/QLDuLich/frontend'
npm.cmd ci
npm.cmd run lint
npm.cmd run build
npm.cmd run check:render
```

Các lệnh frontend yêu cầu Node/npm tương thích với package lock và đủ dependencies. Lưu log exit code, ngày, commit, môi trường và dữ liệu. Unit test pass không thay kiểm UI và chịu tải. Không thực hiện `down -v` giữa các bước cùng kịch bản nếu cần giữ dữ liệu/audit.

### Biểu mẫu kết quả thực tế

| Hạng mục | Trạng thái tại lúc lập báo cáo |
|---|---|
| Trích xuất và đọc văn bản PDF | Đã thực hiện; có text của mẫu và bài giảng. |
| Đối chiếu models/router/compose | Đã thực hiện đọc source các phần liên quan. |
| Chạy lại test backend | Chưa thực hiện: Docker daemon không chạy, Python CLI không có. |
| Chạy lại build/render frontend | Chưa dùng như bằng chứng chức năng trong lần lập báo cáo. |
| Kiểm thử thao tác người dùng | Chưa thực thi. |
| Đo hiệu năng/quy mô | Chưa thực thi. |

## 6.7. Đánh giá thiết kế và hạn chế

Ở mức thiết kế, giải pháp có nguồn dữ liệu theo kỳ, ràng buộc unique/FK, preview và kiểm ghi, quyền sở hữu và audit. Những cơ chế đó xử lý trực tiếp vấn đề phân tán/thiếu truy vết, nhưng hiệu quả định lượng phải được chứng minh bằng thử nghiệm. SQLite phù hợp demo song có giới hạn ghi đồng thời. Thuật toán heuristic có thể để người chưa xếp khi tài nguyên không phù hợp; BTC vẫn cần điều chỉnh.

Phạm vi bỏ chatbot/Gala giúp tập trung nhưng không phải mô tả toàn bộ product. Một số lớp DAM và wireframe là thiết kế đề xuất; không coi ảnh phác là giao diện đã chạy. Kết quả cuối cùng phải tách **đánh giá thiết kế**, **bằng chứng đọc code** và **kết quả thử nghiệm thực tế**.