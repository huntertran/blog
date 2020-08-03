---
title: '[Machine Learning] - 3.2 - Logistic Regression Model'
tags: []
id: '1157'
categories:
  - - Others
date: 2019-06-14 23:14:11
---

Bài thứ 2 trong tuần 3 của khóa học Machine Learning của giáo sư Andrew Ng
<!-- more -->
*   [1\. Cost Function for Logistic Regression](#1-cost-function-for-logistic-regression)
    *   [1.1. Công thức](#11-c%C3%B4ng-th%E1%BB%A9c)
    *   [1.2. Đồ thị](#12-%C4%91%E1%BB%93-th%E1%BB%8B)
    *   [1.3. Kết luận](#13-k%E1%BA%BFt-lu%E1%BA%ADn)
*   [2\. Đơn giản hóa Cost Function và áp dụng Gradient Descent](#2-%C4%91%C6%A1n-gi%E1%BA%A3n-h%C3%B3a-cost-function-v%C3%A0-%C3%A1p-d%E1%BB%A5ng-gradient-descent)
    *   [2.1. Biến đổi](#21-bi%E1%BA%BFn-%C4%91%E1%BB%95i)
    *   [2.2. Gradient Descent](#22-gradient-descent)
*   [3\. Advanced Optimization](#3-advanced-optimization)

# **1\. Cost Function for Logistic Regression**

Đối với linear regression, ta có thể dùng cost function như sau

$latex \\frac{1}{2m}\\sum\_{i=1}^m(h\_\\theta(x^{(i)})-y^{(i)})^2$

Tuy nhiên, nếu áp dụng cùng công thức này với Logistic Regression, ta sẽ có 1 đồ thị vô cùng "gập ghềnh", với rất nhiều điểm local optimal. Điều này trở thành một trở ngại vô cùng lớn với thuật toán gradient descent.

## 1.1. Công thức

Nói cách khác, nó sẽ không phải là một "convex function"

Thay vào đó, cost function cho Logistic Regression sẽ giống như sau

$latex  J(\\theta) = \\dfrac{1}{m} \\sum\_{i=1}^m \\mathrm{Cost}(h\_\\theta(x^{(i)}),y^{(i)})$
$latex   \\mathrm{Cost}(h\_\\theta(x),y) = -\\log(h\_\\theta(x)) \\quad \\quad \\quad \\text{if y = 1}$
$latex   \\mathrm{Cost}(h\_\\theta(x),y) = -\\log(1-h\_\\theta(x)) \\quad \\quad \\text{if y = 0}$

## 1.2. Đồ thị

Khi y = 1, ta có đồ thị sau cho $J(\\theta)$ và $h\_\\theta(x)$:

![if y = 1 plot](https://i.imgur.com/w6Ia2IS.png)

Tương tự, ta có đồ thị sau khi y = 0, ta có đồ thị sau

![if y = 0 plot](https://i.imgur.com/g9c2Fmn.png)

## Kết luận

Dựa vào đồ thị, ta có thể rút ra kết luận sau

$latex \\mathrm{Cost}(h\_\\theta(x),y) = 0 \\text{ if } h\_\\theta(x) = y$
$latex \\mathrm{Cost}(h\_\\theta(x),y) \\rightarrow \\infty \\text{ if } y = 0 \\; \\mathrm{and} \\; h\_\\theta(x) \\rightarrow 1$
$latex \\mathrm{Cost}(h\_\\theta(x),y) \\rightarrow \\infty \\text{ if } y = 1 \\; \\mathrm{and} \\; h\_\\theta(x) \\rightarrow 0$

Như vậy, khi cost = 0, thì hàm hypothesis = y (cho cả trường hợp y = 0 hoặc y = 1)

Ngược lại

*   nếu y = 0, và hypothesis tiến dần tới 1, thì cost sẽ tiến dần tới vô cực
*   nếu y = 1, và hypothesis tiến dần tới 0, thì cost sẽ tiến dần tới vô cực

# 2\. Đơn giản hóa Cost Function và áp dụng Gradient Descent

## 2.1. Biến đổi

Với biểu thức ở trên, chỉ cần biến đổi một chút, ta có thể thu gọn nó vào thành 1 biểu thức như sau:

$latex \\mathrm{Cost}(h\_\\theta(x),y) = - y \\; \\log(h\_\\theta(x)) - (1 - y) \\log(1 - h\_\\theta(x))$

y chỉ có 2 giá trị hoặc = 1 hoặc = 0. Lần lượt thay 2 giá trị này vào biểu thức trên, ta sẽ thấy 1 trong 2 biểu thức con bị triệt tiêu.

Với data của bộ training sets, ta có thể viết đầy đủ biểu thức của cost function như sau:

$latex J(\\theta) = -\\frac{1}{m} \\sum\_{i=1}^{m}\[y^{(i)}log(h\_\\theta(x^{(i)})) + (1-y^{(i)})log(1-h\_\\theta(x^{(i)}))\]$

Sau đó, ta có thể "vector hóa" biểu thức này

$latex h = g(X\\theta) \\ J(\\theta) = \\frac{1}{m} \\cdot \\left(-y^{T}\\log(h)-(1-y)^{T}\\log(1-h)\\right)$

## 2.2. Gradient Descent

Nhắc lại một chút, dạng tổng quát của Gradient Descent như sao:

$latex Repeat \\; \\lbrace \\ \\; \\theta\_j := \\theta\_j - \\alpha \\dfrac{\\partial}{\\partial \\theta\_j}J(\\theta) \\ \\rbrace$

Dùng đạo hàm, ta có thể tính được:

$latex Repeat \\; \\lbrace \\ \\; \\theta\_j := \\theta\_j - \\frac{\\alpha}{m} \\sum\_{i=1}^m (h\_\\theta(x^{(i)}) - y^{(i)}) x\_j^{(i)} \\ \\rbrace$

áp bộ giá trị của training set vào, và chuyển thành toán tuyến tính (vectorise), ta có phép tính sau

$latex \\theta:=\\theta-\\frac{\\alpha}{m}X^T(g(X\\theta)-\\vec{y})$

# 3\. Advanced Optimization

Bên cạnh thuật toán Gradient Descent dùng để tính toán giá trị tối ưu của $latex \\theta$, chúng ta còn có nhiều thuật toán phức tạp hơn, nhưng cũng nhanh hơn nhiều:

*   Conjugate gradient
*   BFGS
*   l-BFGS

Các thuật toán này đều đã được xây dựng và tối ưu hóa trong các thư viện số học của nhiều ngôn ngữ lập trình.

Đầu tiên, chúng ta sẽ cần công thức để tính toán 2 biểu thức

$latex J(\\theta) \\ \\dfrac{\\partial}{\\partial \\theta\_j}J(\\theta)$

Tùy thuộc vào ngôn ngữ lập trình sẽ có các cú pháp khác nhau. Đối với Matlab, ta có thể viết 1 function duy nhất trả về cả 2 giá trị trên:

function \[jVal, gradient\] = costFunction(theta)
  jVal = \[...code to compute J(theta)...\];
  gradient = \[...code to compute derivative of J(theta)...\];
end

Sau đó, ta dùng function `optimset()` để tạo ra 1 object chứa các option cân thiết. Dùng object này đưa vào function `fminunc()` của Octave. Kết quả tính toán sẽ là 1 vector chứa các giá trị tối ưu của $latex \\theta$

options = optimset('GradObj', 'on', 'MaxIter', 100);
initialTheta = zeros(2,1);
   \[optTheta, functionVal, exitFlag\] = fminunc(@costFunction, initialTheta, options);