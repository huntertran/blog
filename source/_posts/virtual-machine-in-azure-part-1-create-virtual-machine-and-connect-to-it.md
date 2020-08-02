---
title: 'Virtual Machine in Azure Part 1: Create virtual machine and connect to it'
tags:
  - azure
  - virtual machine
id: '372'
categories:
  - - Azure
date: 2014-12-03 12:30:51
---

Chào các bạn, vậy là azure đã cho đăng ký chính thức ở Việt Nam. Và 1 dịch vụ rất hay của Azure đó là máy ảo. Bạn được phép tạo một cái máy ảo như máy thật, chạy Windows Server 2012 hoặc 2014, thậm chí là tạo một cái máy ảo chạy thử Windows 10 Technical Preview cũng vẫn được.
<!-- more -->
# Tạo máy ảo

Đăng nhập vào portal của azure, tạo Storage Account. Bước này có thể làm tự động, nhưng tạo tay sẽ cho phép bạn đặt cho nó một cái tên ý nghĩa: [https://manage.windowsazure.com](https://manage.windowsazure.com "https://manage.windowsazure.com") Tiếp theo, tạo một Virtual Machine từ Gallery ![](https://farm8.staticflickr.com/7490/15316844594_6ea298d7d3_o.png) Ở đây, bạn có thể chọn từ rất nhiều Image, có cả các image có sẵn Visual Studio 2013, và có cả Windows 10 Enterprise Technical Preview ![](https://farm8.staticflickr.com/7555/15938450692_9b8b964e62_o.png) Đặt một cái tên mang tính gợi nhớ cho bạn. Ví dụ như Windows81VM hay gì đó đại loại vậy Chọn cấu hình cho máy bạn. Nếu bạn chọn những Image có cài sẵn nhiều thứ, thì nên chọn cấu hình cao cao một chút. Lưu ý là cấu hình càng cao thì càng tốn tiền Tạo username và password cho bạn. Phải nhớ username và password này ![](https://farm8.staticflickr.com/7487/15938466492_dfc0b4d6f0_o.png) Availability tức là VM của bạn sẽ được backup ở một số nơi khác ngoài nơi bạn tạo chính. Tất nhiên là sẽ tốn phí ![](https://farm8.staticflickr.com/7554/15751845320_971cdc5574_o.png) Xong hết rồi thì bấm Create. Chờ nó phân vùng, tạo máy ảo, đăng ký, khởi động, blah blah blah rất là lâu.

# Đăng nhập

Tạo xong thì phải đăng nhập. Và bạn sẽ đăng nhập bằng Remote Desktop của Windows Sau khi máy ảo đã khởi động xong, bạn nhấn vào nút connect để tải về một file .RDP. Nút connect chỉ xuất hiện ở dashboard của Virtual Machine mà bạn tạo ![](https://farm9.staticflickr.com/8668/15319517683_95abc6ee6a_o.png) Double click file này để chạy, bạn sẽ thấy một khung đăng nhập. Bây giờ tới phần éo le Select “Other Account”. Ở ô username, bạn nhập theo cú pháp “hostname\\username”. Hostname lấy trong phần dashboard của virtual machine trong Azure. Password bạn nhập đúng password lúc tạo máy ảo ![](https://farm9.staticflickr.com/8646/15938501022_5b036859a4_o.png) Bạn sẽ gặp phải một vài cảnh báo về chứng chỉ. Cứ việc cho phép nó. Đến bây giờ bạn đã có thể đăng nhập vào máy ảo.