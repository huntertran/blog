---
title: >-
  Virtual Machine in Azure Part 2: Configure to login with Microsoft Account &
  make it FTP Server
tags:
  - azure
  - file
  - ftp
  - virtual machine
id: '376'
categories:
  - - Azure
date: 2014-12-29 04:00:00
---

Chào các bạn, ở phần trước, các bạn đã biết cách tạo một Virtual Machine trên Azure. Phần này mình sẽ hướng dẫn cho các bạn cách thiết lập nó để đăng nhập bằng chính Microsoft Account của bạn, và biến nó thành một máy chủ FTP nhé.
<!-- more -->
# Login with MS Account

Tạo một user mới, dùng Microsoft Account làm username (ví dụ như [blahblahblah@hotmail.com](mailto:blahblahblah@hotmail.com) chả hạn) ![](https://farm8.staticflickr.com/7480/16133514591_b1627eeae8_o.png) ![](https://farm8.staticflickr.com/7553/16135418725_c4193f946f_o.png) Sau khi tạo xong, mở Computer Management, chọn mục Local Users and Groups trong System Tools. User mới tạo sẽ xuất hiện trong mục này với một cái tên bị cắt ngắn. Bạn mở Property của User này lên, chuyển sang thẻ Member of, thêm người này vào nhóm Remote Desktop Users. ![](https://farm8.staticflickr.com/7473/16134669652_56a4064c9b_o.png) ![](https://farm8.staticflickr.com/7494/16109629516_1bbd681b2b_o.png) Trong Control Panel, mở System and Security, chọt Allow Remote Access, bỏ chọn tùy chọn “Allow connections only … with Network Level Authentication”. ![](https://farm8.staticflickr.com/7550/16134669472_0ca0f6cf48_o.png) Bước cuối cùng là mở file .RDP lên bằng notepad, thay đổi dòng “**prompt for credentials:i:1**” thành “**enablecredsspsupport:i:0**” Vậy là xong. Sau khi đăng nhập lần đầu tiên, bạn có thể undo 2 bước cuối cùng.

# FTP Server

## Cài đặt trên Azure Portal

Bước đầu tiên, bạn phải tạo một port 21 trong phần quản lý của Azure Click chọn Add trong phần Endpoint của Virtual Machine của bạn ![](https://farm8.staticflickr.com/7555/15949429589_b3ec1b188f_o.png) Chọn Add a stand alone endpoint và nhấn next ![](https://farm8.staticflickr.com/7544/16133612571_e8534a1023_o.png) Chọn FTP, các thông số sẽ tự điền vô cho bạn (:yay:) ![](https://farm8.staticflickr.com/7520/15949443029_fc25fc17d1_o.png) Chờ nó hoàn tất ![](https://farm8.staticflickr.com/7568/15949450879_d152283f57_o.png)

## Cài đặt trên Virtual Machine

### Cài FileZilla Server

Trên VM, bạn tải FileZilla Server về: [https://filezilla-project.org/download.php?type=server](https://filezilla-project.org/download.php?type=server) Khi cài đặt, chấp nhận tất cả các tùy chọn mặc định của nó Mở FileZilla Server lên, chọn Edit > Users ![](https://farm8.staticflickr.com/7558/15948351778_1d23368c73_o.png) Thêm một User mới với tên tùy chọn. Đây là tên bạn sẽ dùng để đăng nhập vào FTP Server của mình sau này ![](https://farm8.staticflickr.com/7509/15948353428_0c2804bfc0_o.png) ![](https://farm9.staticflickr.com/8655/16110010396_2ff5e90b5b_o.png) Thêm password cho tài khoản này. Nếu không thì Man-in-the-middle sẽ truy cập được và server của bạn và tiến hành phá hoại ![](https://farm8.staticflickr.com/7547/16135806475_92b2f1c975_o.png) Tiếp theo, chọn Shared Folders và thêm vào Folder mà bạn sẽ kết nối để download hoặc upload dữ liệu ![](https://farm9.staticflickr.com/8579/16134067331_1317d1baa7_o.png) Lưu ý rằng có các tùy chọn cho phép các quyền khác nhau đối với folder, và các quyền này đi theo tài khoản mà bạn đã tạo và đã chọn trong FileZilla Server Lưu ý 2: Không được chọn Folder gốc (C:/ D:/ E:/), luôn luôn chọn Folder dưới mức gốc 1 level Tiếp tục, mở FileZilla Server Settings, chọn Passive Mode ![](https://farm8.staticflickr.com/7553/16110037406_9a3392ff54_o.png) Chọn "Use custom Port Range, và điền một số port cho cả 2 bên (vì bạn sẽ ko muốn tạo ra cả trăm port trên Azure Portal đâu) Tiếp tục chọn Retrieve external IP Address from ![](https://farm8.staticflickr.com/7529/16110190066_890fb9766c_o.png)

### Thiếp lập Firewall

Mở Windows Firewall lên và cho phép FileZilla Server Chọn Allow an app through Windows Filewall ![](https://farm8.staticflickr.com/7517/15950078947_c6588c56ac_o.png) Nếu bạn không tìm thấy FileZilla Server trong danh sách, thì duyệt tới file thực thi .exe của nó ![](https://farm8.staticflickr.com/7495/16135094662_38e4a8b7ab_o.png) Sau cùng nó phải giống như vầy ![](https://farm9.staticflickr.com/8675/15516120053_03bd077f97_o.png) Tiếp theo, ở Control Panel > Windows Firewall, chọn Advanced Settings ![](https://farm9.staticflickr.com/8644/16133948991_6f9fb96a8d_o.png) Chọn Inbound Rules, và thêm cái custom Port của bạn hồi nãy mới thiếp lập trong FileZilla Server ![](https://farm8.staticflickr.com/7570/15513526614_76337d6844_o.png) ![](https://farm9.staticflickr.com/8638/16110072306_90f3ffacf3_o.png) ![](https://farm8.staticflickr.com/7462/16135112792_25b507d9d3_o.png) Thiết lập cổng cho cái Inbound Rule này ![](https://farm8.staticflickr.com/7485/15513532304_2608708f49_o.png)

##  Cài đặt trên Local Machine

### Cài đặt FileZilla Client

Tải FileZilla Client tại: [https://filezilla-project.org/download.php?type=client](https://filezilla-project.org/download.php?type=client) Khi khởi chạy, điền dải IP trong Public IP trên Azure của bạn ![](https://farm8.staticflickr.com/7569/16135891365_c631a0fc94_o.png) Điền các thông tin vào các ô tương ứng và nhấn quick connect ![](https://farm9.staticflickr.com/8657/16134040481_9840ea9497_o.png) Danh sách các Folder bạn đã Share sẽ hiện ra :3 ![](https://farm9.staticflickr.com/8667/15949873649_5254d44ec9_o.png)

## Thử nghiệm tốc độ của FTP Server mới tạo

Tốc độ mạng của Azure ![](http://www.speedtest.net/result/4018401482.png) Download ![](https://farm8.staticflickr.com/7556/15948706180_d594463823_o.png) Mạng công ty bị QoS chặn download tốc độ cao file lớn (haiza) Upload ![](https://farm8.staticflickr.com/7470/15949950969_fbd629132e_o.png) Mạng công ty bị QoS chặn upload tốc độ cao file lớn (haiza)