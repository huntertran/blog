---
title: Machine Learning - 1.4 - Matrices and Vectors
tags:
  - matrice
  - matrix
  - vector
id: '1084'
categories:
  - - Machine Learning
date: 2018-10-01 07:47:01
---

Bài viết thứ 4 trong loạt bài tự học Machine Learning trên Coursera của giáo sư Andrew Ng. Trong bài viết này, ta sẽ nói về Matrix và Vector, cùng các phép toán của chúng.
<!-- more -->
Xem các bài viết khác tại [Machine Learning Course Structure](https://coding4food.net/machine-learning-course/)

*   [1\. Các ký hiệu](#1-các-ký-hiệu)
    *   [1.1. Matrix](#11-matrix)
    *   [1.2. Vector](#12-vector)
    *   [1.3. Ký hiệu](#13-ký-hiệu)
*   [2\. Phần mềm](#2-phần-mềm)
*   [3\. Các phép tính](#3-các-phép-tính)
    *   [3.1. Phép cộng và phép nhân matrix số thực](#31-phép-cộng-và-phép-nhân-matrix-số-thực)
    *   [3.2. Nhân matrix với vector](#32-nhân-matrix-với-vector)
    *   [3.3. Nhân 2 matrix với nhau](#33-nhân-2-matrix-với-nhau)
    *   [3.4. Các tính chất của phép nhân matrix](#34-các-tính-chất-của-phép-nhân-matrix)
    *   [3.5. Identity Matrix](#35-identity-matrix)
*   [4\. Inverse (nghịch đảo) và Transpose (chuyển vị)](#4-inverse-nghịch-đảo-và-transpose-chuyển-vị)
    *   [4.1. Inverse (nghịch đảo)](#41-inverse-nghịch-đảo)
    *   [4.2. Transpose (chuyển vị)](#42-transpose-chuyển-vị)

# 1\. Các ký hiệu

## 1.1. Matrix

Matrix là một mảng 2 chiều (có thể mở rộng ra n chiều).

$latex \\begin{bmatrix}a & b & c \\\\d & e & f \\\\g & h & i \\\\j & k & l \\end{bmatrix}$

Matrix bên trên có 4 dòng và 3 cột, ký hiệu là $latex R^{4x3}$.

## 1.2. Vector

Vector là một matrix chỉ có 1 cột và nhiều dòng.

$latex \\begin{bmatrix} w \\\\ x \\\\ y \\\\ z \\end{bmatrix}$

Vector trên là một matrix 4x1.

## 1.3. Ký hiệu

*   $latex A\_{ij}$ là phần tử ở dòng i và cột j của matrix.
*   Vector A với 'n' dòng sẽ là một Vector có n chiều.
*   $latex v\_{i}$ là phần tử ở dòng i của vector.

> Bình thường, vector và matrix sẽ dùng index bắt đầu từ 1. Trong đa số các ngôn ngữ lập trình, mảng thường bắt đầu từ phần tử 0.

*   Matrix thường được ký hiệu bằng chữ cái in hoa, vector thường được ký hiệu bằng chữ cái in thường.
*   `Scalar` nghĩa là một vật thể là một giá trị, không phải vector hay matrix.
*   $latex \\mathbb{R}$ được ký hiệu cho tập các số thực.
*   $latex \\mathbb{R}^n$ được ký hiệu cho tập các vector số thực n chiều.

# 2\. Phần mềm

Để thử nghiệm nhanh chóng các giả thuyết - thuật toán liên quan tới toán học trong Machine Learning, ta có thể dùng một phần mềm mang tên [Octave](https://www.gnu.org/software/octave/download.html) Bạn có thể chạy đoạn code dưới đây trong Octave hoặc Matlab \[code lang=matlab\] % The ; denotes we are going back to a new row. A = \[1, 2, 3; 4, 5, 6; 7, 8, 9; 10, 11, 12\] % Initialize a vector v = \[1;2;3\] % Get the dimension of the matrix A where m = rows and n = columns \[m,n\] = size(A) % You could also store it this way dim\_A = size(A) % Get the dimension of the vector v dim\_v = size(v) % Now let's index into the 2nd row 3rd column of matrix A A\_23 = A(2,3) \[/code\]

# 3\. Các phép tính

## 3.1. Phép cộng và phép nhân matrix số thực

Đối với phép cộng và nhân, chỉ cần đơn giản cộng và nhân với mỗi phần tử của matrix.

$latex \\begin{bmatrix} a & b \\\\ c & d \\\\ \\end{bmatrix} +\\begin{bmatrix} w & x \\\\ y & z \\\\ \\end{bmatrix} =\\begin{bmatrix} a+w & b+x \\\\ c+y & d+z \\\\ \\end{bmatrix}$

Tương tự đối với phép nhân và chia:

$latex \\begin{bmatrix} a & b \\\\ c & d \\\\ \\end{bmatrix} \* x =\\begin{bmatrix} a\*x & b\*x \\\\ c\*x & d\*x \\\\ \\end{bmatrix}$

$latex \\begin{bmatrix} a & b \\\\ c & d \\\\ \\end{bmatrix} / x =\\begin{bmatrix} a /x & b/x \\\\ c /x & d /x \\\\ \\end{bmatrix}$

## 3.2. Nhân matrix với vector

Để nhân một matrix với một vector, nhân mỗi phần tử rồi cộng kết quả:

$latex \\begin{bmatrix} a & b \\\\ c & d \\\\ e & f \\end{bmatrix} \*\\begin{bmatrix} x \\\\ y \\\\ \\end{bmatrix} =\\begin{bmatrix} a\*x + b\*y \\\\ c\*x + d\*y \\\\ e\*x + f\*y\\end{bmatrix}$

> Một matrix `m x n` nhân với một vector `n x 1` sẽ ra kết quả là một vector `m x 1`.

Kiến thức về matrix này có thể áp dụng vào hàm hypothesis của linear regression: Ta có bộ input các giá trị của x như sau: \[code lang=text\] x1 = 21 x2 = 30 x3 = 25 x4 = 22 \[/code\] hàm hypothesis:

$latex h\_{0} = -40 + 0.25x$

Để tính nhanh các giá trị dự đoán của y, ta có thể tạo ra matrix x và vector hypothesis, và tạo thành phép tính như sau:

$latex \\begin{bmatrix} 1 & 21 \\\\ 1 & 30 \\\\ 1 & 25 \\\\ 1 & 22 \\end{bmatrix} \* \\begin{bmatrix} -40 \\\\ 0.25 \\end{bmatrix}$

Phép tính này có thể dễ dàng tính toán bằng Octave \[code lang=matlab\] A = \[1,21;1,30;1,25;1,22\] B = \[-40;0.25\] mul\_AB = A \* B \[/code\] Kết quả: \[code lang=matlab\] A = 1 21 1 30 1 25 1 22 B = -40.00000 0.25000 mul\_AB = -34.750 -32.500 -33.750 -34.500 \[/code\]

## 3.3. Nhân 2 matrix với nhau

Tương tự như việc nhân 1 matrix với 1 vector, bạn chỉ cần tách phép nhân 2 matrix thành nhiều phép nhân matrix với vector.

$latex \\begin{bmatrix} a & b \\\\ c & d \\\\ e & f \\end{bmatrix} \*\\begin{bmatrix} w & x \\\\ y & z \\\\ \\end{bmatrix} =\\begin{bmatrix} a\*w + b\*y & a\*x + b\*z \\\\ c\*w + d\*y & c\*x + d\*z \\\\ e\*w + f\*y & e\*x + f\*z\\end{bmatrix}$

> Một matrix `m x n` khi nhân với một matrix `n x o` sẽ cho ra kết quả là một matrix `m x o`.

## 3.4. Các tính chất của phép nhân matrix

Phép nhân 2 số thực có một số tính chất không thể áp dụng với phép nhân 2 matrix. Gọi $latex A$ và $latex B$ là 2 matrix, ta có:

*   $latex A \\times B \\neq B \\times A$
*   $latex A \\times B \\times C = A \\times (B \\times C) = (A \\times B) \\times C$

## 3.5. Identity Matrix

Một matrix bất kỳ khi nhân với một Identity matrix phù hợp sẽ có kết quả là chính nó. Ký hiệu: $latex I$ hoặc $latex I\_{n \\times n}$ Ví dụ:

$latex I\_{1 \\times 1} = \\begin{bmatrix} 1 \\end{bmatrix}$

$latex I\_{2 \\times 2} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}$

$latex I\_{3 \\times 3} = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}$

> Lưu ý: $latex A \\times I = I \\times A$

# 4\. Inverse (nghịch đảo) và Transpose (chuyển vị)

## 4.1. Inverse (nghịch đảo)

> **Một ví dụ với số thực** 3 là một số thực. Ta có: $latex 3 \\times (3^{-1}) = 1$ Tổng quát: $latex a \\times (a^{-1}) = 1$

Ta có matrix A:

$latex A \\times A^{-1} = A^{-1} \\times A = I$

> Matrix gồm toàn các phần tử 0 không có nghịch đảo

## 4.2. Transpose (chuyển vị)

Gọi B là matrix chuyển vị của A, ta có:

$latex A = \\begin{bmatrix} a & b \\\\ c & d \\\\ e & f \\end{bmatrix}$

$latex A^T = \\begin{bmatrix} a & c & e \\\\ b & d & f \\end{bmatrix}$

Hay nói cách khác:

$latex A\_{ij} = A^T\_{ji}$