---
title: Machine Learning - 2.1 - Multiple Features
tags: []
id: '1087'
categories:
  - - Machine Learning
date: 2018-10-03 05:48:42
---

Tuần 2 trong course Machine Learning của giáo sư Andrew Ng trên Coursera. Trong phần này, bạn sẽ thấy linear regression được mở rộng thành `multiple input features`, và những best practices để thực hiện linear regression.
<!-- more -->
Xem các bài viết khác tại [Machine Learning Course Structure](https://coding4food.net/machine-learning-course/)

*   [1\. Mutiple Features](#1-mutiple-features)
    *   [1.1. Ký hiệu](#11-ký-hiệu)
    *   [1.2. Hypothesis](#12-hypothesis)
    *   [1.3. Trick](#13-trick)
*   [2\. Gradient Descent cho Multiple Variables](#2-gradient-descent-cho-multiple-variables)
*   [3\. Gradient Descent in Practice](#3-gradient-descent-in-practice)
    *   [3.1. Feature Scaling và Mean Normalization](#31-feature-scaling-và-mean-normalization)
    *   [3.2. Learning Rate](#32-learning-rate)
*   [4\. Features và Polynomial Regression](#4-features-và-polynomial-regression)

# 1\. Multiple Features

Linear Regression với `multiple features` còn được biết đến với cái tên `multivariate linear regression`.

## 1.1. Ký hiệu

*   $latex x^{(i)}\_j$ = giá trị của feature `j` trong training example thứ `i`.
*   $latex x^{(i)}$ = input (feature) thứ `i` của training example.
*   m = số training example
*   n = số features

## 1.2. Hypothesis

Như vậy, hàm hypothesis của chúng ta được viết lại như sau:

$latex h\_0(x) = \\theta\_0x\_0 + \\theta\_1x\_1 + ... + \\theta\_nx\_n$

với $latex x\_0 = 1$.

## 1.3. Trick

Áp dụng các kiến thức về phép nhân matrix đã học ở bài trước, ta có như sau

$latex h\_0(x) = \\begin{bmatrix} \\theta\_0 & \\theta\_1 & ... & \\theta\_n \\end{bmatrix} \\begin{bmatrix} x\_0 \\\\ x\_1 \\\\ ... \\\\ x\_n \\end{bmatrix} = \\theta^Tx$

Trên đây là công thức của hàm hypothesis được rút gọn thành phép nhân matrix với vector.

# 2\. Gradient Descent cho Multiple Variables

Công thức cho thuật toán Gradient Descent thì y hệt như cũ. Ta chỉ lặp lại nó cho `n` features mà thôi. Lặp lại cho tới khi hội tụ:

$latex \\theta\_0 := \\theta\_0 - \\alpha \\frac{1}{m} \\sum\\limits\_{i=1}^{m} (h\_\\theta(x^{(i)}) - y^{(i)}) \\cdot x\_0^{(i)} \\\\ \\theta\_1 := \\theta\_1 - \\alpha \\frac{1}{m} \\sum\\limits\_{i=1}^{m} (h\_\\theta(x^{(i)}) - y^{(i)}) \\cdot x\_1^{(i)} \\\\ \\theta\_2 := \\theta\_2 - \\alpha \\frac{1}{m} \\sum\\limits\_{i=1}^{m} (h\_\\theta(x^{(i)}) - y^{(i)}) \\cdot x\_2^{(i)} \\\\ ...$

hoặc diễn giải theo một cách khác:

$latex \\theta\_j := \\theta\_j - \\alpha \\frac{1}{m} \\sum\\limits\_{i=1}^{m} (h\_\\theta(x^{(i)}) - y^{(i)}) \\cdot x\_j^{(i)}$

với j:= 0...n

> Đối với $latex \\theta\_0$, $latex x^i\_0 = 1$

# 3\. Gradient Descent in Practice

## 3.1. Feature Scaling và Mean Normalization

Khi các features có giá trị giao động trong các khoảng cách xa nhau, thì thuật toán Gradient Descent thường tốn nhiều thơi gian để tìm ra kết quả. Ví dụ ta có 2 feature là `diện tích nhà` và `số phòng ngủ`: \[code lang=text\] 200 < Diện tích nhà < 2000 1 < Số phòng ngủ < 5 \[/code\] Nếu vẽ đồ thị cho hàm hypothesis dự đoán giá nhà, bạn sẽ thấy nó là một dạng đồ thị hình cái tô với đáy rất nhọn, nhưng dẹp. Điều này làm cho mỗi step của gradient descent trải dài về bề ngang, nhưng không đi nhanh về điểm hội tụ, làm tổng thời gian chạy thuật toán gradient descent tăng lên. ![plot](https://i.imgur.com/DA49vil.png) _hình ảnh chỉ mang tính chất minh họa ;)_ Ta có thể tăng tốc gradient descent bằng cách `biến đổi` các giá trị của feature cho nó nằm trong một khoảng gần giống nhau. Lý do là $latex \\theta$ sẽ di chuyển nhanh hơn trong vùng bé hơn và ngược lại, chậm hơn trong vùng lớn hơn. Nhìn chung, ta sẽ biến đổi sao cho:

$latex -1 \\leq x\_{(i)} \\leq 1$

hoặc

$latex -0.5 \\leq x\_{(i)} \\leq 0.5$

Trên đây chỉ là ví dụ, mục tiêu là làm cho vùng giá trị của các feature càng gần nhau càng tốt. 2 kỹ thuật để làm chuyện này là `Feature Scaling` và `Mean Normalization`.

> Feature Scaling là chia input với khoảng giá trị (max - min). Mean Normalization là input - giá trị trung bình của input.

$latex x\_i := \\frac{x\_i - \\mu\_i}{\\delta\_i}$

với:

*   $latex \\mu\_i$: trung bình của feature i
*   $latex \\delta\_i$: Max - min hoặc độ lệch chuẩn

> Max - min sẽ cho ra kết quả rất khác với độ lệch chuẩn.

## 3.2. Learning Rate

Để xác định tham số $latex \\alpha$, ta có thể áp dụng 1 số kỹ thuật:

*   Vẽ đồ thị với trục x = số bước lặp của gradient descent, trục y = giá trị của $latex J(\\theta)$. Nếu $latex J(\\theta)$ tăng, thì bạn phải giảm giá trị $latex \\alpha$ xuống và làm lại từ đầu.
*   Automatic convergence test: Xác định điểm hội tụ khi giá trị $latex J(\\theta)$ không vượt quá E trong một lần lặp, với E là một giá trị rất nhỏ nào đó. Tuy nhiên trong thực tế, thường rất khó xác định giá trị E này.

Người ta đã chứng minh được rằng, nếu learning rate $latex \\alpha$ đủ nhỏ, thì giá trị $latex J(\\theta)$ sẽ giảm sau mỗi lần lặp. Túm lại: \* Nếu $latex \\alpha$ quá nhỏ: gradient descent chạy lâu. \* Nếu $latex \\alpha$ quá lớn: $latex J(\\theta)$ có thể sẽ không giảm sau mỗi lần lặp -> không hội tụ.

# 4\. Features và Polynomial Regression

Ta có thể cải thiện features và dạng của hàm hypothesis bằng nhiều cách. Một trong số những cách đó là **kết hợp** các feature lại với nhau. Ví dụ như khi ta có 2 feature là `dài` và `rộng`, ta có thể kết hợp chúng thành `diện tích = dài * rộng`. Ngoài ra, không phải lúc nào ta cũng có thể sử dụng được hàm hypothesis là một đường thẳng, nhất là khi nó không "vừa" với bộ data. Lúc này, có thể biến đổi nó một chút, hoặc bẻ cong nó bằng cách nâng lũy thừa, hoặc lấy căn của các features (hoặc bất cứ dạng nào khác đều được). Ví dụ:

$latex h\_{\\theta}(x) = \\theta\_0 + \\theta\_1x\_1$

Ta có thể thêm 1 feature mới bằng cách lũy thừa x lên:

$latex h\_{\\theta}(x) = \\theta\_0 + \\theta\_1x\_1 + \\theta\_2x\_1^2$

hoặc lấy căn của nó:

$latex h\_{\\theta}(x) = \\theta\_0 + \\theta\_1x\_1 + \\theta\_2\\sqrt{x\_1}$

> Một điều quan trọng là khi bạn biến đổi các feature như thế này, vùng giá trị của nó sẽ trở nên cách biệt so với feature gốc. Lúc này, bạn sẽ phải áp dụng những cách tối ưu như `Feature Scaling` và `Mean Normalization` đã nói ở trên để tối ưu thuật toán Gradient Descent.