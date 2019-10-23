# **Project 2: Multi Agent**

#### Q1:

Hàm Reflex Agent xét đến các yếu tố:
    
* Khoảng cách manhattan đến con ma gần mình nhất (x)
* Khoảng cách mahattan đến thức an gần nhất (y)
* Số lượng thức ăn của trạng thái đó (z) 

Score sẽ xét đến các yếu tố sao cho con ma càng gần mình thì score càng thấp (nếu khoảng cách bằng 0 thì score cực thấp),
khoảng cách đến thức ăn càng gần thì điểm càng cao,  đồng thời số lượng thức ăn càng ít thì điểm càng cao.
Sau khi chọn tham số, score của ta sẽ là -(5/x + y + 100 * z)

#### Q2,3,4:

Đơn thuần là cài đặt theo các thuật toán đã học trên lớp.


#### Q5:

Thêm 1 giá trị là :

* khoảng cách mahatan từ pacman đến capsule gần nhất (t)

Công thức lúc này sẽ là -(5/x + y + 5/t + 100 * z)
