---
title: Machine Learning - 1.3 - Parameter Learning
tags:
  - gradient descent
  - hypothesis
id: '1080'
categories:
  - - Machine Learning
date: 2018-09-27 05:17:23
---

Bài thứ 3 trong chuỗi bài viết tự học Machine Learning. Ở 2 bài trước, chúng ta đã có hàm hypothesis và cách để biết hàm đó có phù hợp với bộ training example của chúng ta hay ko. Bây giờ chúng ta sẽ tìm cách tìm ra các tham số cho hàm hypothesis.
<!-- more -->
Xem các bài viết khác tại [Machine Learning Course Structure](https://coding4food.net/machine-learning-course/)

*   [1\. Gradient Descent](#1-gradient-descent)
    *   [1.1. Biểu diễn đồ thị](#11-biểu-diễn-đồ-thị)
    *   [1.2. Mô tả thuật toán](#12-mô-tả-thuật-toán)
    *   [1.3. Xây dựng](#13-xây-dựng)
*   [2\. Gradient Descent cho Linear Regression](#2-gradient-descent-cho-linear-regression)

# 1\. Gradient Descent

Ở 2 bài trước, chúng ta đã có hàm hypothesis và cách để biết hàm đó có phù hợp với bộ training example của chúng ta hay ko. Bây giờ chúng ta sẽ tìm cách tìm ra các tham số cho hàm hypothesis, và đó là nhiệm vụ của `Gradient Descent`. Để đơn giản, trong phần này, ta sẽ xét các hàm hypothesis có 2 tham số là $latex \\theta\_{0}$ và $latex \\theta\_{1}$. Đối với các trường hợp có nhiều hơn 2 tham số, cách thực hiện là tương tự.

## 1.1. Biểu diễn đồ thị

Gọi $latex J(\\theta\_{0},\\theta\_{1})$ là kết quả của cost function. Ta biểu diễn các tham số lên một đồ thị có 3 trục x, y và z như sau:

*   $latex \\theta\_{0}$ là trục x.
*   $latex \\theta\_{1}$ là trục y.
*   $latex J(\\theta\_{0},\\theta\_{1})$ là trục z.

![gradient descent graph](https://farm2.staticflickr.com/1899/44863403391_91a4cf87aa_o.png) Các mũi tên đỏ chỉ những điểm thấp nhất của đồ thị này, đó là các điểm mà ta tìm kiếm (nhằm mục đích tối thiểu giá trị của cost function).

## 1.2. Mô tả thuật toán

Chọn 1 điểm bất kỳ, sau đó di chuyển từng bước nhỏ về vùng trũng nhất của đồ thị. Cách làm là lấy đạo hàm của cost function. Đối với một hàm số, đạo hàm của nó chính là đường tiếp tuyến của nó. Độ dốc của đường tiếp tuyến tại một điểm chính là giá trị của hàm đạo hàm tại điểm đó. Độ dốc này cho ta biết hướng đi để chọn điểm tiếp theo. Độ dài của mỗi step được xác định bởi tham số $latex \\alpha$, gọi là `learning rate`. Điểm ban đầu được chọn khác nhau sẽ cho ra các kết quả rất khác nhau. Hình bên trên có 2 điểm ban đầu khác nhau, và sẽ cho ra 2 điểm thấp nhất là 2 mũi tên đỏ. Như vậy, thuật toán Gradient Descent sẽ là: lặp lại cho tới khi hội tụ: $latex \\theta\_{j} := \\theta\_{j} - \\alpha \\frac{\\partial}{\\partial\\theta\_{j}}J(\\theta\_{0},\\theta\_{1})$ với: $latex j=0,1,2,...,m$, đại diện cho index Với mỗi lần lặp, cả $latex \\theta\_{0}$ và $latex \\theta\_{1}$ phải được tính đồng thời.

## 1.3. Xây dựng

Để cho đơn giản, ta sẽ dùng hàm số chỉ có 1 biến $latex \\theta\_{1}$ và từng bước xây dựng công thức cho `Gradient Descent`. Vậy công thức của ta còn: Lặp lại cho tới khi hội tụ: $latex \\theta\_{1} := \\theta\_{1} - \\alpha \\frac{\\partial}{\\partial\\theta\_{1}}J(\\theta\_{1})$ với

*   $latex \\alpha$ là learning rate
*   $latex \\frac{\\partial}{\\partial\\theta\_{1}}J(\\theta\_{1})$ là độ dốc của đường tiếp tuyến (slope) tại $latex \\theta\_{1}$

![plot](https://i.imgur.com/G01t68o.png) Nhìn vào đồ thị trên, khi slope nằm bên trái của điểm hội tụ, thì giá trị $latex \\theta\_{1}$ tăng, và ngược lại khi nó nằm bên phải của điểm hội tụ.

> Tham số $latex \\alpha$ nên được điều chỉnh hợp lý sao cho thuật toán gradient descent hội tụ trong 1 khoảng thời gian phù hợp. Khi $latex \\alpha$ quá nhỏ, thời gian tìm đến điểm hội tụ sẽ lâu. Khi quá lớn, thuật toán rất có thể sẽ không tìm thấy điểm hội tụ.

Với một tham số $latex \\alpha$ hợp lý, càng về gần điểm hội tụ, độ dốc của tiếp tuyến sẽ càng nhỏ, do đó, thuật toán gradient descent sẽ có bước đi nhỏ hơn, và sẽ bằng 0 khi tới điểm hội tụ. Trong trường hợp điểm xuất phát chính là điểm hội tụ, thì thuật toán gradient descent sẽ cho ra $latex \\theta\_{1}$ không đổi với $latex \\alpha$ bất kỳ, vì đạo hàm của nó là 0.

# 2\. Gradient Descent cho Linear Regression

Khi áp dụng thuật toán Gradient Descent vào hàm số Hypothesis của ta trong các bài viết trước, ta có thể tìm được 2 tham số $latex \\theta\_{0}$ và $latex \\theta\_{1}$: Lặp lại cho tới khi hội tụ: $latex \\theta\_0 := \\theta\_0 - \\alpha \\frac{1}{m} \\sum\\limits\_{i=1}^{m}(h\_\\theta(x\_{i}) - y\_{i})$ $latex \\theta\_1 := \\theta\_1 - \\alpha \\frac{1}{m} \\sum\\limits\_{i=1}^{m}\\left((h\_\\theta(x\_{i}) - y\_{i}) x\_{i}\\right)$ với:

*   m là tổng số training example.
*   $latex \\theta\_0$ tham số sẽ thay đổi đồng thời với $latex theta\_1$ và $latex x\_{i}$.
*   $latex y\_{i}$ là các giá trị được cho bởi bộ training example.

Như vậy, số 2 dưới mẫu trong công thức của bài kỳ trước đã bị triệt tiêu vì đạo hàm

> Gradient Descent trong bài toán này thường được gọi là `Batch Gradient Descent`, vì nó tính tổng của tất cả các giá trị Hàm hypothesis của bài toán Linear Regression có hình dạng như một cái tô, và chỉ có 1 điểm hội tụ duy nhất.