---
title: '[Machine Learning] - 3.1 - Classification and Representation'
tags: []
id: '1148'
categories:
  - - Machine Learning
date: 2019-05-14 05:43:52
---

Tuần 3 trong course Machine Learning của giáo sư Andrew Ng trên Coursera.
<!-- more -->
*   [1\. Classification and Representation](#1-classification-and-representation)
    *   [1.1. Sigmoid Function or Logistic Function](#11-sigmoid-function-or-logistic-function)
    *   [1.2. Decision Boundary](#12-decision-boundary)
*   [2\. Ví dụ](#2-v%C3%AD-d%E1%BB%A5)

# **1\. Classification and Representation**

## **1.1. Sigmoid Function or Logistic Function**

Trong bài toán phân loại (classification), mặc dù ta có thể tiếp cận nó bằng các thuật toán linear regression đã biết bằng cách tạm thời quên đi giá trị của y chỉ có thể là 0 hoặc 1.Cách tiếp cận này có vẻ không được tốt cho lắm. Giá trị của $latex h\_0(x)$ phải nằm trong khoảng từ 0 tới 1.

Để giải quyết vấn đề này, ta sẽ biến đổi hàm hypotheses $latex h\_0(x)$ để thỏa điều kiện $latex 0<=h\_\\theta(x)<=1$.Ta sẽ _nhét_ $latex \\theta^Tx$ vào Logistic Function:

$latex h\_\\theta (x) = g ( \\theta^T x )$
$latex z = \\theta^T x$
$latex g(z) = \\dfrac{1}{1 + e^{-z}}$ 

biểu thức trên có biểu diễn đồ thị như sau:

![](https://i.imgur.com/9IHlEt9.png)

Function g(z) có thể biểu diễn bất kỳ số thực nào nằm trong khoảng từ 0 đến 1.$latex h\_\\theta(x)$ cho chúng ta xác suất kết quả = 1. Ví dụ như nếu $latex h\_\\theta(x) = 0.7$ có nghĩa là xác suất kết quả = 1 là 70%. Ngược lại, xác xuất kết quả = 0 là 30% (vì output chỉ có thể có 2 giá trị là 0 và 1).

$latex h\_\\theta(x) = P(y=1 | x ; \\theta) = 1 - P(y=0 | x ; \\theta)$
$latex P(y = 0 | x;\\theta) + P(y = 1 | x ; \\theta) = 1$ 

## **1.2. Decision Boundary**

Dựa vào Logistic function ở trên, ta có thể \`biến đổi\` hàm hypothesis của ta lại thành như sau:

 
 $latex h\_\\theta(x) \\geq 0.5 \\Rightarrow y = 1$
 $latex h\_\\theta(x) < 0.5 \\Rightarrow y = 0$ 

Function g(z) hoạt động như sau:

$latex g(z) \\geq 0.5$
when
$latex z \\geq 0$ 

Nhớ rằng:

$latex z=0, e^{0}=1 \\Rightarrow g(z)=1/2$
$latex z \\to \\infty, e^{-\\infty} \\to 0 \\Rightarrow g(z)=1$
$latex z \\to -\\infty, e^{\\infty}\\to \\infty \\Rightarrow g(z)=0$ 

Như vậy, ta có thể viết:

$latex h\_\\theta(x) = g(\\theta^T x) \\geq 0.5$
when
$latex \\theta^T x \\geq 0$ 

Từ những phát biểu trên, ta có thể viết

$latex \\theta^T x \\geq 0 \\Rightarrow y = 1$
$latex \\theta^T x < 0 \\Rightarrow y = 0$ 

**Decision Boundary** chính là đường phân chia vùng y = 0 và vùng y = 1, được tạo ra bởi hàm hypothesis của chúng ta

# **2\. Ví dụ**

Ta có ví dụ sau:

$latex \\theta = \\begin{bmatrix}5\\\\ -1\\\\ 0\\end{bmatrix}$
$latex y = 1 \\; if \\; 5 + (-1) x\_1 + 0 x\_2 \\geq 0$
$latex 5 - x\_1 \\geq 0$
$latex - x\_1 \\geq -5$
$latex x\_1 \\leq 5$ 

vậy đồ thị của chúng ta sẽ giống như sau

![](https://i.imgur.com/VNSdsHL.png)

Lưu ý rằng tùy vào hàm hypothesis và các tham số theta, hình dáng boudary line có thể thay đổi tương ứng