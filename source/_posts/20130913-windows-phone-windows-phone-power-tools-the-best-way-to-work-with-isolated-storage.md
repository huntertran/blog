---
title: >-
  [Windows Phone] Windows Phone Power Tools – the best way to work with Isolated
  Storage
tags:
  - isolated storage
  - power tools
  - windows phone
id: '200'
categories:
  - - CSharp
    - Windows Phone
date: 2013-09-13 23:02:24
---

Isolated Storage là một vùng nhớ trên Windows Phone, đúng như tên gọi của nó, đã bị Isolated (Cô lập). Cô lập tức là ứng dụng khác không thể truy cập vào nó, và bạn cũng không thể truy cập vào ứng dụng khác (trừ phi bạn có quyền root, chỉ dành cho Lumia 710 cooked room)

Vậy trong lúc phát triển app, làm sao để truy cập vùng nhớ này trực quan, sinh động và dễ dàng?
<!-- more -->
Có một cách, và theo mình, cách này là hay nhất, vô cùng trực quan, sinh động và thao tác dễ dàng. Bạn không cần phải gõ bất kỳ dòng lệnh nào để chạy nó so với Isolated Storage Explorer Tool

*   [1. Cài đặt](#1-cài-đặt)
*   [2. Sử dụng](#2-sử-dụng)
    
    *   [2.1. Install | Update](#21-install--update)
    *   [2.2. Dev Apps](#22-dev-apps)
    *   [2.3. Guild](#23-guild)
    *   [2.4. Name](#24-name)
    *   [2.5. Isolated Storage](#25-isolated-storage)
    *   [2.6. Nút Get](#26-nút-get)
    *   [2.7. Nút Put File](#27-nút-put-file)
    *   [2.8. Nút Put Directory](#28-nút-put-directory)
    *   [2.9. Nút Delete](#29-nút-delete)
    *   [2.10. Profile (Beta)](#210-profile-beta)
    *   [2.11. Giải pháp](#211-giải-pháp)
*   [3. Kết luận](#3-kết-luận)

# 1. Cài đặt

Tải và cài tại: [Windows Phone Power Tools on CodePlex](http://wptools.codeplex.com/)

# 2. Sử dụng

Mở một project Windows Phone bất kỳ, Run with Emulator (hoặc Device)

[![14-09-2013 10-47-34 AM](http://cuoilennaocacban2.files.wordpress.com/2013/09/14-09-2013-10-47-34-am.png "14-09-2013 10-47-34 AM")](http://www.flickr.com/photos/28322228@N04/9739566696/)

Bạn phải chờ cho ứng dụng bắt đầu chạy trên Emulator hoặc device, sau đó quay lại Power Tools Nhấn Connect, nhớ chọn đúng thiết bị bạn đang build project

[![14-09-2013 11-04-20 AM](http://cuoilennaocacban2.files.wordpress.com/2013/09/14-09-2013-11-04-20-am.png "14-09-2013 11-04-20 AM")](http://www.flickr.com/photos/28322228@N04/9737431929/)

Thế là xong

## 2.1. Install | Update

Phần này cho phép bạn cài đặt một app mới hoặc cập nhật một app sẵn có trên thiết bị. Tất cả mọi thứ bạn cần là Emulator đang chạy (hoặc thiết bị đang được kết nối), file XAP của ứng dụng. Đối với Windows Phone 7, bạn cần có Zune. Bạn chỉ được cài đặt các app chưa được ký bởi store (App ký rồi sẽ ko cài được). Và bạn chỉ được cập nhật các app đang develop

## 2.2. Dev Apps

[![14-09-2013 11-07-46 AM](http://cuoilennaocacban2.files.wordpress.com/2013/09/14-09-2013-11-07-46-am.png "14-09-2013 11-07-46 AM")](http://www.flickr.com/photos/28322228@N04/9739591682/)

Mục này cho phép bạn tùy chỉnh nhiều thứ về ứng dụng đang được develop trên thiết bị.

## 2.3. Guild

Guild là mã số của ứng dụng của bạn. Mỗi ứng dụng có một số Guild riêng. Và số này sẽ bị ghi đè khi upload và verified trên store

## 2.4. Name

Tên của ứng dụng của bạn. Bạn có thể chỉnh sửa nó để dễ nhìn hơn khi sử dụng Power Tools để dev nhiều app cùng lúc

[![14-09-2013 11-10-52 AM](http://cuoilennaocacban2.files.wordpress.com/2013/09/14-09-2013-11-10-52-am.png "14-09-2013 11-10-52 AM")](http://www.flickr.com/photos/28322228@N04/9739602720/)

[![14-09-2013 11-11-42 AM](http://cuoilennaocacban2.files.wordpress.com/2013/09/14-09-2013-11-11-42-am.png "14-09-2013 11-11-42 AM")](http://www.flickr.com/photos/28322228@N04/9737458719/)

Nhấn Enter sau khi đổi tên, Ứng dụng của bạn đã có tên mới.

Bạn phải connect lại một lần nữa tới thiết bị để hiển thị thay đổi này trong Isolated Storage. Nhấn vào nút `Connect to a device` bên trên cùng của Power Tools và chọn Connect lại

## 2.5. Isolated Storage

[![14-09-2013 11-14-05 AM](http://cuoilennaocacban2.files.wordpress.com/2013/09/14-09-2013-11-14-05-am.png "14-09-2013 11-14-05 AM")](http://www.flickr.com/photos/28322228@N04/9739619928/)

Thành phần chính của Power Tools

> Nếu bạn vẫn thấy ứng dụng của mình là dãy số Guild sau khi đổi tên ở mục Dev Apps, hãy nhấn `connect to a device` ở trên thanh tiêu đề, kết nối lại với emulator hoặc device, bạn sẽ thấy tên ứng dụng thay đổi đúng như mong muốn

Đây chính là Isolated Storage của ứng dụng bạn đang chạy trên máy. Isolated Storage này phản ánh chính xác mọi thứ bạn đang có trên bộ nhớ thật, theo một cấu trúc thư mục. Nhấn vào một file hoặc folder bất kỳ, thông tin của nó sẽ hiện ra

[![14-09-2013 11-15-59 AM](http://cuoilennaocacban2.files.wordpress.com/2013/09/14-09-2013-11-15-59-am.png "14-09-2013 11-15-59 AM")](http://www.flickr.com/photos/28322228@N04/9739643620/)

## 2.6. Nút Get

nút get cho phép bạn lấy file bạn đang chọn, và lưu nó trên máy tính. Bạn cũng có thể double click một file để mở nó trực tiếp, nhưng đó chỉ là một bản copy của file bạn đang chọn trong Isolated Storage, mọi thao tác chỉnh sửa đối với file này sẽ không được lưu lại trong Isolated Storage

## 2.7. Nút Put File

nút này cho phép bạn "đặt" một file vào trong Isolated Storage. Chính xác hơn là copy một file từ máy tính vào Isolated Storage. Tùy chọn Overwrite Existing sẽ ghi đè file trùng tên

## 2.8. Nút Put Directory

như nút put file, nhưng thực hiện cho cả một thư mục

## 2.9. Nút Delete

Xóa một file ra khỏi Isolated Storage. Bạn không thể phục hồi nó. Hãy cân nhắc trước khi xóa. Lưu một bản sao của chúng trên máy tính

## 2.10. Profile (Beta)

công cụ này, theo nhà phát triển, sẽ giúp bạn đánh giá ứng dụng của mình. Theo thử nghiệm của tôi, nó hoạt động ko được tốt lắm.

*   Đòi quyền quản trị –> đã cấp quyền quản trị
*   Yêu cầu khởi động lại Power Tools –> đã làm

Trong quá trình thử nghiệm, Power Tool bị lỗi và ko thể khởi động lại được. Khi cài lại, không có thiết bị nào trong danh sách để kết nối.

## 2.11. Giải pháp

Gỡ bỏ > Cài đặt lại > Tắt Emulator / Ngắt kết nối thiết bị > Chạy lại Emulator / Kết nối lại

# 3. Kết luận

Power Tools, theo tôi là công cụ tốt nhất để thao tác với Isolated Storage, nhưng công cụ Profile của nó có một số lỗi khó chịu. Ngoài lỗi này ra, tất cả đều tuyệt vời