---
title: '[Windows Phone] Input Scope'
tags:
  - input
  - input scope
  - scope
  - textbox
  - windows phone
id: '220'
categories:
  - - c
    - Windows Phone
date: 2013-09-18 01:51:24
---

Trong Windows Phone, bạn có một tính năng rất hay gọi là “Input Scope” Nếu đã dùng thử Android, bạn sẽ thấy nó cố gắng nhồi nhét thật nhiều thứ vào bàn phím ảo, dẫn tới việc bạn dễ bị bấm nhầm từ không mong muốn.
<!-- more -->
Windows Phone giải quyết việc thiếu không gian này bằng các Input Scope, chỉ hiển thị các ký tự cần thiết khi nhập một cái gì đó lên màn hình. ![keyboard](http://farm8.staticflickr.com/7433/9796093016_baa65fbbae_o.jpg)  Giả sử, bạn muốn nhập một địa chỉ email. Các nút “@” và “.” sẽ hiển thị lên bàn phím ảo Tương tự, bạn muốn nhập một số điện thoại, bàn phím sẽ chuyển về dạng bàn phím số. Để thiết lập Input Scope cho một input control (TextBox), rất đơn giản. ![inputcontrol](http://farm8.staticflickr.com/7437/9796016076_d007a63394_o.png) Chọn cho mình một InputScope phù hợp, và ứng dụng của bạn sẽ được người dùng đánh giá cao, vì tiết kiệm cho họ một khoảng thời gian nho nhỏ. Có nhiều Input Scope không thay đổi bàn phím ảo, nhưng có một số tính năng tiện dụng:

*   PersonalFullName: Tự động đổi sang ký tự in hoa cho chữ cái đầu tiên của mỗi từ
*   Password: nhập password
*   DateMonthName: Tên của tháng
*   Digits: Số, có thập phân
*   Email các loại: hiển thị thêm ký tự @