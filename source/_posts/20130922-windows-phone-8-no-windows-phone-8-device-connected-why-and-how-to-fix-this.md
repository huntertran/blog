---
title: >-
  [Windows Phone 8] No Windows Phone 8 Device connected – Why and How to fix
  this?
tags:
  - deploy
  - no device
  - windows phone
id: '223'
categories:
  - - c
    - Windows Phone
date: 2013-09-22 00:35:38
---

Nhiều tính năng của Windows Phone đòi hỏi ta phải có 1 cái máy thiệt để test (NFC, Pinch Zoom). Hoặc là sau cùng, ta cũng cần 1 cái máy thiệt để xem ứng dụng hoạt động như thế nào.

Cắm điện thoại vào cổng USB, chọn Device trong Visual Studio. Nhấn chạy. Nhưng:

![bug](http://www.f5debug.net/image.axd?picture=image_620.png)
<!-- more -->
*   [1\. Nguyên nhân](#1-nguyên-nhân)
*   [2\. Triệu chứng](#2-triệu-chứng)
*   [3\. Khắc phục](#3-khắc-phục)

Rõ ràng đã kết nối. Check lại trong Device Manager nào:

![lumia](http://farm4.staticflickr.com/3711/9867408893_b658aee6fb_o.png)

Bình thường. Vậy nguyên nhân do đâu?

# 1\. Nguyên nhân

1.  **Không đúng ngày giờ:** Ngày giờ trên điện thoại của bạn khác xa so với ngày giờ trên máy tính
2.  **Chưa bật các kết nối:** Thường xảy ra với máy chưa dev unlock. Khi Unlock, điện thoại phải bật các kết nối có sẵn (Wifi / 3G hoặc cả hai) để nó yêu cầu unlock từ phía Microsoft. Nếu không bật các kết nối này, nó sẽ không kết nối được và tất nhiên là không unlock được.
3.  **Sử dụng Windows 8 trên các laptop hoặc Desktop hơi cổ:** Các thể loại Laptop này dùng Intel Chipset 6 Series, hiện tại đang gặp vấn đề về tương thích với Windows 8 trở lên. Các chipset này điều khiển các kết nối USB. Máy hay bị lỗi nhất là các máy có cả cổng USB 3.0 Native và USB 2.0 cũ
4.  **Hư cáp USB:** Cáp USB nếu bị đứt một thành phần nào đó bên trong thì thường dẫn tới kết nối im re không có hiện tượng gì xảy ra. Còn không, có thể cáp bị nhiễu tín hiệu

# 2\. Triệu chứng

Mọi thứ đều bình thường. Bạn có thể thấy thư mục hình ảnh, nhạc, video trong điện thoại. Có thể đồng bộ hóa, copy thêm vào, nhưng tuyệt nhiên không thể deploy một file XAP lên được

# 3\. Khắc phục

1.  Cài đặt lại đúng ngày giờ cho trùng với trên máy tính. Máy tính bạn nên bật chức năng tự động cập nhật thời gian để có thời gian chính xác
2.  Mở các kết nối
3.  Disable/Enable các driver bị lỗi của Intel Chipset 6. Nó sẽ hoạt động bình thường trở lại.

Sau khi thực hiện các bước trên. Bạn tiếp tục vào Device Manager, uninstall các driver liên quan tới điện thoại của mình (Portable Devices và Unversal Serial Bus devices). Mục đích của bước này là xóa các Registry Key bị lỗi. Nếu không, máy bạn sẽ không bao giờ Deploy được, cho dù có thử như thế nào đi nữa, vì nó sẽ không ghi đè các Registry Key

1.  Tiếp tục chuyển sang một cổng USB 2.0 (phòng ngừa tình trạng tính năng Legacy trên USB 3.0 không hoạt động)
2.  Cắm điện thoại vào và chờ nó cài đặt driver
3.  Thử lại vận may của bạn

Tôi đã thử, và thành công. Còn bạn?