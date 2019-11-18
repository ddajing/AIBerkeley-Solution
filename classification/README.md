# Classification
## Câu 1:
Cách làm dựa trên thuật toán được đưa ra ở bài giảng trên website. Ta sẽ thực hiện việc cập nhật weight vector dựa trên thuật toán đã cho qua một số epoch nhằm tối ưu độ chính xác của mô hình trên tập train.

Score: 4/4, PASSED

## Câu 2:
Sau khi thực hiện trích chọn ra 100 features quan trọng nhất. Kết quả nhận được giống với miêu tả a trọng đầu bài. Đồng thời ta cũng nhận thấy rằng các features quan trọng nhất của weigted vector của từng label có hình dáng khá giống với label đó.

Score: 1/1, PASSED

## Câu 3:
Duyệt qua tất cả các giá trị C co trong C grid, sau đó thực hiện việc tối ưu mô hình dựa trên thuật toán đã cho và chọn ra giá trị C có accuracy là lớn nhất, weigted vector cũng là giá trị weigted vector tương ứng mà ta đạt được khi duyệt qua giá trị C này.

Score 6/6, PASSED

## Câu 4:
Ta sẽ thêm features mới cho dữ liệu dựa trên sô thành phần bit 0 liên thông. Ta có thể thực hiện việc này dựa trên thuật toán Deapth First Search. Duyệt qua tất cả các pixel của dữ liệu đầu vào, với mỗi pixed chưa được thăm, ta sẽ tăng biến đếm lên 1 và thăm tất cả các pixel thuộc cũng thành phần liên thông với nó. cnt là số thành phần liên thông, features mới sẽ được dựa trên giá trị của cnt, ta có thêm 3 binary features tương ứng với các giá trị cnt > 1, cnt > 3, cnt > 5.

Score: 6/6, PASSED

## Câu 5:
Thực hiện cài đặt hoàn toàn giống với thuật toán đã cho ở đề bài.

Score: 4/4, PASSED

## Câu 6:
Các feature được thêm vào:
* ```nearest_ghost```: Khoảng cách gần nhất tính theo Manhattan giữa Pacman và con các Ghost trong trạng thái sau đó.
* ```ghost_count```: Đếm số con Ghost có khoảng cách Manhattan với Pacman nhỏ hơn 3 trong trạng thái sau đó.
* ```nearest_food```: Khoảng cách gần nhất tính theo Manhattan giữa Pacman và thức ăn trong trạng thái sau đó.
* ```scared_ghost```: Số con Ghost đang ở trạng thái Scared
* ```stop_now```: Pacman có đang đừng yên trong trạng thái sau đó hay không?

Score: 4/4, PASSED
