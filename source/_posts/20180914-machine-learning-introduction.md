---
title: Machine Learning - 1.1 - Introduction
tags: []
id: '1057'
categories:
  - - Machine Learning
date: 2018-09-14 11:22:30
---

Bài viết mở đầu cho chuỗi tự học Machine Learning. Các khái niệm cơ bản sẽ được giới thiệu trong bài viết này.
<!-- more -->
Xem các bài viết khác tại [Machine Learning Course Structure](https://coding4food.net/machine-learning-course/)

*   [1. Machine learning là gì](#1-machine-learning-là-gì)
*   [2. Phân loại](#2-phân-loại)
    *   [2.1. Supervised Learning](#21-supervised-learning)
        *   [2.1.1. Regression](#211-regression)
        *   [2.1.2. Classification](#212-classification)
    *   [2.2. Unsupervised Learning](#22-unsupervised-learning)

# 1. Machine learning là gì

Có 2 định nghĩa về machine learning:

> The field of study that gives computers the ability to learn without being explicitly programmed.
> 
> _Arthur Samuel_

Định nghĩa thứ 2:

> A computer program is said to learn from experience **E** with respect to some class of tasks **T** and performance measure **P**, if its performance at tasks in **T**, as measured by **P**, improves with experience **E**.
> 
> _Tom Mitchell_

Đọc thì có vẻ dài dòng, nhưng đưa nó vào một ví dụ là dễ hiểu ngay:

**Chơi cờ**

*   **E**(xperience): kinh nghiệm chơi cờ (càng chơi càng giỏi).
*   **T**(ask): nhiệm vụ là chơi cờ.
*   **P**(robability): Khả năng mà máy tính sẽ thắng trong ván tiếp theo.

# 2. Phân loại

Mọi chương trình Machine learning đều có thể chia thành 2 loại:

1.  Supervised Learning
2.  Unsupervised Learning

## 2.1. Supervised Learning

Trong loại này, ta biết trước dữ liệu đầu vào và kết quả. Hãy tưởng tượng nó như một dạng biểu đồ.

Dựa vào biểu đồ này, ta có thể dự đoán mối quan hệ giữa input và output. Khi đó, khi đưa một input bất kỳ, ta có thể tính ra được output.

Supervised learning được chia làm 2 loại là **regression** và **classification**.

### 2.1.1. Regression

Dựa vào mối liên hệ giữa input và output, ta dự đoán được kết quả

![bieu do](https://farm2.staticflickr.com/1856/42867061930_e41c2f94c0_o.png)

### 2.1.2. Classification

Dựa vào đặc điểm của input, ta đặt được nó vào một loại cụ thể

![classification](https://farm2.staticflickr.com/1879/43958802164_a713ef73dc_o.png)

## 2.2. Unsupervised Learning

Trong "thể loại" machine learning này, ta hoàn toàn ko biết trước được kết quả sẽ như thế nào.

Ví dụ:

1.  Trong 1 triệu bức ảnh, tìm cách nhóm các bức ảnh có cùng 1 chủ đề lại với nhau (nhà cửa, xe cộ, con người).
2.  Tìm và lọc ra tiếng người nói chuyện và tiếng nhạc trong 1 buổi tiệc ồn ào với nhiều loại âm thanh ([Cocktail Party Algorithm](https://en.wikipedia.org/wiki/Cocktail_party_effect)).

Trên đây là những khái niệm mở đầu cho Machine Learning, càng về những bài viết sau, bạn sẽ càng phải tự mình nghiên cứu và đào sâu vào các khái niệm phức tạp và thú vị hơn.

Hẹn gặp lại ở các bài viết sau nhé!