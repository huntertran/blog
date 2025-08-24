---
title: '[UWP] Create image assets for your apps'
tags:
  - app
  - assets
  - automatically
  - generate
  - images
  - logo
  - maker
  - store
  - uwp
  - windows 10
id: '515'
categories:
  - - CSharp
    - Windows 10
date: 2015-10-26 01:01:01
---

Windows 10 apps (aka Universal Windows App) yêu cầu rất nhiều kích thước hình ảnh khác nhau trong project của nó (hiện tại là 39 kích thước khác nhau). Làm thế nào để tạo ra các hình ảnh này? Mở Photoshop hay GIMP lên để crop, resize, save, rồi lập lại 39 lần hẻ? Hôm nay, bạn đã có thể làm nó dễ dàng chỉ với 1 (vài) click. Thậm chí tạo ra kích thước custom được luôn.

<!-- more -->

# 1. The App

Có một ứng dụng mang tên "Universal Logo Maker for Windows" trên Windows Store. Nó có thể tạo ra tất cả hình ảnh bạn cần, đặc biệt là cho Windows 10 package.

Link: [https://www.microsoft.com/store/apps/9nblggh5zchk](https://www.microsoft.com/store/apps/9nblggh5zchk)

Nhìn vô biết xài liền, nhưng mà dù sao cũng hướng dẫn bạn một tí nhóe.

# 2. Using it

![](/images/flickr/1528/25014426576_2bb0afed82_o.png)

Nhìn hình trên là biết xài ngay phải hem. Bạn cũng có thể nghịch với các slider, nút này nọ để hiểu rõ hơn về app nhóe

# 3. Add custom size and scale

Nhấn cái nút dấu + nhỏ nhỏ

![](/images/flickr/5627/22493108391_1a6c030571_o.png)

Trong trang này, bạn có thể thêm các size mới của riêng mình

![](/images/flickr/1536/25014463126_d77238d3c3_o.png)

Platform name is the name of your custom collection. By this way, you can create many platforms that match your need, and choose to generate images for these custom platform or not.

Platform name là tên của danh sách những cái kích thước khác nhau của bạn. Bằng cách này, bạn có thể tạo bao nhiêu platforms cũng được. Nên đặt tên khác nhau cho dễ nhớ.

Cái text box bự bự bên dưới là chỗ bạn nhập các thông số kích thước.

Giải thích cú pháp:

Mỗi thông số cách nhau bởi dấu ":". Đầu tiên là tên, rồi rộng, rồi cao. Dễ ẹt mà.

Khi bạn đang gõ, nếu đúng, nó sẽ preview trước cho bạn xem cái kích thước sẽ được add vào platform đó

Làm xong rồi thì nhấn Add, cái kích thước đó sẽ nằm trong platform, và platform mới sẽ được thêm vào danh sách các platform.

Cái hay ho nhứt là, dần dần, danh sách các platform do bạn tạo ra sẽ được đồng bộ hóa giữa tất cả thiết bị mà bạn login bằng cùng tài khoản Microsoft Account. Kiểu như trên công ty tạo ra xài xong, về nhà mở máy lên là đã có sẵn để xài tiếp.

# 4. Settings

Trong setting, có cũng nhìu tùy chọn. Chọn chỗ lưu, về app này, feedback, blah blah blah. Cái hay nhất là "Update Database"

![](/images/flickr/1590/24922870222_cf003efd5f_o.png)

Bình thường, app sẽ update database tự động. Nhưng vì lý do nào đó (kiểu như bạn đang xài dữ liệu 3g, hay PC đang connect tới mạng chập chờn chả hạn), bạn có thể check update bằng tay. Cái này chỉ update cái danh sách platform default, không phải cái custom do bạn tự tạo, nên hok sao âu.

# 5. Rate for me, please, and feedback

Cuối cùng, nếu bạn thấy app này hữu ích, rate cho nó nhá. Nếu bạn gặp lỗi hay vấn đề gì, có thể gửi email cho mềnh tại [cuoilennaocacban@hotmail.com](mailto:cuoilennaocacban@hotmail.com)

Hẹn gặp lại các bạn ở những bài blog khác.