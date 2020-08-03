---
title: '[ASP.NET CORE] – My road trip to ASP.NET core – Getting Started'
tags:
  - core
id: '604'
categories:
  - - c
    - ASP.NET
date: 2016-07-06 05:11:44
---

Bài viết theo quan điểm cá nhân, các bạn vui lòng đừng ném đá u đầu chết.

Microsoft is cool again

Ngày 27 tháng 6 năm 2016, MS ra mắt một loạt 3 sản phẩm cực khủng, hứa hẹn sẽ thay đổi cán cân quyền lực, lập lại bản đồ Server, và nó là .NET core, ASP.NET core, và Entity Framework Core. Tất cả đều mang số hiệu 1.0

Vậy bạn tự hỏi, chúng nó là gì?
<!-- more -->
# Giới thiệu

Xưa kia, khi muốn làm web, bạn có vô vàn lựa chọn:

*   Nhanh, đơn giản, miễn phí: PHP, cài thêm PHP my assmin vô, cùng Apache Tomcat hay XAMPP gì gì đấy
*   Bảo mật thì Java Server Page, bao chậm luôn
*   Một số lựa chọn mới nổi như Node.js, vân vân
*   Lựa chọn cuối cùng, vẫn là ASP.NET, vì nó đòi:
    
    *   Chạy trên Windows Server
    *   Code bằng .NET (C#)
    *   Ít host nào hỗ trợ (vì server tốn phí bản quyền)
    *   Hỗ trợ ít cơ sơ dữ liệu (SQL Server chả hạn)

Với ASP.NET Core, bạn vẫn có các ưu điểm như code bằng C#, debug dễ dàng, IDE khủng, và các nhược điểm bị loại bỏ (chạy được trên Mac, Win, Linux, Docker, free to use, open source, blah blah blah)

# Tài liệu

Xưa kia, muốn học ASP.NET, bạn có khá nhiều lựa chọn, mỗi cái đều có nhược điểm. Cái thì quá ít thông tin, cái thì tốn phí, cái thì sơ sài, và đa phần tản mát trong dân gian.

Giờ đây, mọi tài liệu điều quy về 1 chỗ:

*   Tài liệu chung cho tất cả sản phẩm: [https://docs.microsoft.com/en-us/](https://docs.microsoft.com/en-us/)
*   Tài liệu cho ASP.NET: [https://docs.asp.net/en/latest/](https://docs.asp.net/en/latest/)

# Cho dev ko xài Windows

ASP.NET core có thể code được bằng nhiều thứ khác nhau như Sublime, Visual Studio Code hoặc trình soạn thảo khoái trá của bạn.

# Hello world

Bật visual studio > New Project > Chọn ASP.NET Core Web Application (.NET Core)

![](https://farm8.staticflickr.com/7352/28088746726_3720e218f0_o.png)

Sau khi nhấn OK, chọn Empty > Bỏ chọn Host in the cloud (hiện giờ thì cứ test local các kiểu đi đã) > OK

![](https://farm8.staticflickr.com/7379/28122930625_bc23f52a5b_o.png)

Sau khi nhấn OK, Visual Studio sẽ bắt đầu tạo project. Project tạo xong, nó sẽ bắt đầu restore các NuGet Package.

Điểm hay ở ASP.NET Core là nó ko còn dựa trên 1 library nhất định như các phiên bản ASP.NET cũ nữa, mà hoàn toàn dựa trên Nuget Package.

![](https://farm8.staticflickr.com/7431/28088835376_acf5813b9c_o.png)

Sau cùng, nhấn nút để chạy thử và xem thành quả

![](https://farm8.staticflickr.com/7336/27843235500_3a0cfbc3af_o.png)

![](https://farm8.staticflickr.com/7574/28045741121_29641faf2f_o.png)

# Publish lên Azure

Nhấn chuột phải vô Web Application > Publish

![](https://farm8.staticflickr.com/7442/27508633903_a7451490d9_o.png)

Chọn Publish target là Azure

![](https://farm8.staticflickr.com/7328/28123967115_9334fb7a48_o.png)

Nếu bạn muốn có riêng một Resource Group nào đó, thì tạo mới 1 cái

![](https://farm8.staticflickr.com/7389/28089848636_3a27dcdc72_o.png)

Nhớ chọn các thông số cần thiết

![](https://farm8.staticflickr.com/7350/27509151714_dcde6a8641_o.png)

App Service Plan thì free được rồi

![](https://farm8.staticflickr.com/7342/28021061142_26fe033b23_o.png)

Ra được cái màn hình này thì cứ nhấn publish thôi

![](https://farm8.staticflickr.com/7379/28021077182_9ced5d2930_o.png)

Chiêm ngưỡng thành quả

![](https://farm8.staticflickr.com/7321/27509194014_95f55d6dbd_o.png)