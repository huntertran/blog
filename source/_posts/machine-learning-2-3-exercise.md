---
title: Machine Learning - 2.3 - Exercise
tags: []
id: '1104'
categories:
  - - Machine Learning
date: 2018-10-18 05:58:06
---

Bài viết này đưa ra bài giải và chi tiết cách giải của mỗi bài tập trong tuần 2 của khóa học Machine Learning của giáo sư Andrew Ng.

Xem các bài viết khác tại [Machine Learning Course Structure](https://coding4food.net/machine-learning-course/).
<!-- more -->
*   [1\. Cài đặt Octave](#1-cài-đặt-octave)
*   [2\. Warmup](#2-warmup)
*   [3\. Cost Function J](#3-cost-function-j)
*   [4\. Gradient Descent](#4-gradient-descent)
*   [5\. Normal Equation](#5-normal-equation)

# 1\. Cài đặt Octave

Còn gì dễ hơn: [Download Octave](https://www.gnu.org/software/octave/download.html)

Chọn phiên bản 64-bit nha: octave-4.4.1-w64-installer.exe (~ 238 MB)

# 2\. Warmup

Yêu cầu: Trả về 5x5 identity matrix

```
A = eye(5);
```

# 3\. Cost Function J

Công thức:

$latex J(\\theta) = \\frac{1}{2m}\\sum\\limits\_{i=1}^m(h\_0(x^{(i)})-y^{(i)})^2$

Vectorize:

Ta có:

$latex h\_0(x^{(i)}) =\\theta\_0X\_0 + \\theta\_1X\_1+...+\\theta\_nX\_n$

Nếu coi $latex \\theta$ là vector $latex n\\times1$, X là matrix $latex m\\times n$, thì phép tính trên còn đơn giản như sau:

$latex h\_0(x^{(i)})=\\begin{bmatrix}x\_0^{(1)} & x\_1^{(1)} \\\\x\_0^{(2)} & x\_1^{(2)} \\\\ ... & ... \\\\ x\_0^{(m)} & x\_1^{(m)} \\end{bmatrix}\\times\\begin{bmatrix}\\theta\_0 \\\\ \\theta\_1 \\\\ ... \\\\ \\theta\_m \\end{bmatrix}=X\\times\\theta$

Vậy cost function biến đổi lại thành:

$latex J(\\theta) = \\frac{1}{2m}\\sum\\limits\_{i=1}^m(X\\times\\theta-y)^2$

Code:

```
J = (1/(2*m))*sum((X*theta - y).^2)
```

# 4\. Gradient Descent

Thuật toán Gradient Descent có 2 bước:

1.  Tính bộ giá trị $latex \\theta$
2.  Thay vào cost function để kiểm tra hội tụ

Để cho đơn giản, ta sẽ giả định rằng chỉ có 2 feature là $latex x\_0 = 1$ và $latex x\_1$ (n = 2)

Công thức:

$latex \\theta\_j = \\theta\_j - \\alpha \\frac{1}{m} \\sum\\limits\_{i=1}^{m} (h\_\\theta(x^{(i)}) - y^{(i)}) \\cdot x\_j^{(i)}$

Ta tách công thức trên thành 2 phần:

$latex \\theta\_j = \\theta\_j - gradient$

với

$latex gradient = \\alpha \\frac{1}{m} \\sum\\limits\_{i=1}^{m} (h\_\\theta(x^{(i)}) - y^{(i)}) \\cdot x\_j^{(i)}$

với:

*   X = $latex \\begin{bmatrix}x\_0^{(1)} & x\_1^{(1)} \\\\x\_0^{(2)} & x\_1^{(2)} \\\\ ... & ... \\\\ x\_0^{(m)} & x\_1^{(m)} \\end{bmatrix}$
*   $latex \\theta = \\begin{bmatrix}\\theta\_0 \\\\ \\theta\_1 \\end{bmatrix}$
*   y = $latex \\begin{bmatrix}y\_1 \\\\ y\_2 \\\\ ... \\\\ y\_m \\end{bmatrix}$

Tương tự như cost function, ta có:

$latex (X\\times\\theta - y)=\\begin{bmatrix} \\theta\_0x\_0^{(1)}+\\theta\_1x\_1^{(1)}-y\_1 \\\\ \\theta\_0x\_0^{(2)}+\\theta\_1x\_1^{(2)}-y\_2 \\\\ ... \\\\ \\theta\_0x\_0^{(m)}+\\theta\_1x\_1^{(m)}-y\_m \\end{bmatrix}=\\begin{bmatrix} a\_1 \\\\ a\_2 \\\\ ... \\\\ a\_m \\end{bmatrix}= a$

với a là vector m x 1

**Nhân với $latex x\_j^{(i)}$ và tính tổng**

Đối với mỗi tham số của vector a, ta nhân nó với x tương ứng, rồi cộng tất cả các kết quả lại.

Để vừa nhân, vừa tính tổng và trả về một vector chứa kết quả là các giá trị của gradient, ta sẽ phải biến đổi matrix X một chút.

$latex X^T = \\begin{bmatrix}x\_0^{(1)} & x\_0^{(2)} & ... & x\_0^{(m)}\\\\ x\_1^{(1)} & x\_1^{(2)} & ... & x\_1^{(m)}\\end{bmatrix}$

Khi nhân matrix này với vector a, ta sẽ có kết quả như mong muốn.

$latex X^T\\times a = \\begin{bmatrix}x\_0^{(1)} & x\_0^{(2)} & ... & x\_0^{(m)}\\\\ x\_1^{(1)} & x\_1^{(2)} & ... & x\_1^{(m)}\\end{bmatrix} \\times \\begin{bmatrix} a\_1 \\\\ a\_2 \\\\ ... \\\\ a\_m \\end{bmatrix}=\\begin{bmatrix} a\_1x\_0^{(1)} + a\_2x\_0^{(2)} + ... + a\_mx\_0^{(m)} \\\\ a\_1x\_1^{(1)} + a\_2x\_1^{(2)} + ... + a\_mx\_1^{(m)} \\end{bmatrix}$

Code:

```
file gradientDescent.m

function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters
gradient = (alpha/m) * X' * (X*theta - y);
theta = theta - gradient;

% Save the cost J in every iteration
J_history(iter) = computeCost(X, y, theta);
end
end
```

> Code này có thể dùng chung cho gradient descent với nhiều feature

# 5\. Normal Equation

Cái này thì khá dễ, nên mình không giải thích mà sẽ đưa code luôn nhé

```
file normalEqn.m

function [theta] = normalEqn(X, y)
%NORMALEQN Computes the closed-form solution to linear regression
%   NORMALEQN(X,y) computes the closed-form solution to linear
%   regression using the normal equations.

theta = zeros(size(X, 2), 1);

theta = pinv(X'*X)*X'*y;
end
```

Bắt đầu tuần 3 nào :D