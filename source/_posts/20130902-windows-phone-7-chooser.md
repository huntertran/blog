---
title: Windows Phone 7 Chooser
tags:
  - chooser
  - windows phone
id: '160'
categories:
  - - CSharp
    - Windows Phone
date: 2013-09-02 12:13:41
---

Windows Phone có nhiều tài nguyên để bạn tận dụng, carmera này, danh bạ này, hình ảnh này, blah blah blah. Làm sao để sử dụng những tài nguyên này trong ứng dụng Windows Phone của bạn?
<!-- more -->
Có một cách: Windows Phone Chooser API. Nó sẽ giúp cho bạn truy cập các tài nguyên này một cách đơn giản và hiệu quả

Đây là danh sách các chooser của WP

*   CameraCaptureTask – kích hoạt camera để chụp hình, trả về hình (tất nhiên)
*   EmailAddressChooserTask – kích hoạt 'Contacts', trả về địa chỉ email của contact đã chọn
*   PhoneNumberChooserTask – như trên, nhưng trả về số điện thoại
*   PhotoChooserTask – kích hoạt Photo, trả về hình đã chọn
*   SaveEmailAddressTask - Kích hoạt ‘Contact’ và cho phép bạn gắn địa chỉ email vào một contact nào đó. Trả về giá trị xác định có thành công hay ko.
*   SavePhoneNumberTask – Như trên, nhưng mà cho phép bạn gắn số điện thoại :3

Xài làm sao?

Tùy vào từng Task sẽ có từng cách xài riêng, bạn tự google nhé. Hiện tại chưa kịp viết :3 Sẽ edit bài này sau