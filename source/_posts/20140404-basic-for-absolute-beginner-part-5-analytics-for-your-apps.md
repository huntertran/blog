---
title: '[Basic for Absolute Beginner] – [Part 5] – Analytics for your apps'
tags:
  - analytics
  - windows phone
  - windows store
id: '311'
categories:
  - - C#
  - - c
    - Windows Phone
    - Windows Store App
date: 2014-04-04 10:28:33
---

Phân tích hành vi người dùng là một điều hết sức cần thiết và quan trọng trong việc cải thiện chất lượng ứng dụng của bạn.

Và lần này, ta sẽ dựa và công cụ phân tích và theo dõi người dùng kinh khủng nhất thế giới: Google Analytics

![](https://farm8.staticflickr.com/7322/13573942035_b413d8924a_o.png)

Đúng rồi, Windows Phone và Windows 8, sử dụng dịch vụ Analytics của “đối thủ”. Nghe lạ chưa :3
<!-- more -->
*   [Trên Project](#trên-project)
    
    *   [Cài SDK](#cài-sdk)
    *   [Khai báo thông tin](#khai-báo-thông-tin)
*   [Trên Google Analytics](#trên-google-analytics)
*   [Thiết lập theo dõi](#thiết-lập-theo-dõi)
    
    *   [Coding](#coding)
*   [Xem Analytics](#xem-analytics)

# Trên Project

## Cài SDK

Mở project của bạn lên, vào Tools > NuGet Package Manager > Package Manager Console

![](http://farm8.staticflickr.com/7070/13574117965_55d85b93db_o.png)

Một ô nho nhỏ xinh xinh hiện ra, gõ dòng lệnh sau

\[code lang=bash\] Install-Package GoogleAnalyticsSDK \[/code\]

![](http://farm3.staticflickr.com/2835/13574223523_c343351607_o.png)

Chờ một chút cho nó chạy

## Khai báo thông tin

Sau khi chạy xong, Project của bạn sẽ có thêm một số thứ mới

File analytics.xml

File này chứa các thông số cần thiết để Google Analytics theo dõi ứng dụng của bạn.

Trong file này có các dòng comment vô cùng đầy đủ, bạn có thể Comment out nó và tự điền các thông số mong muốn

![](http://farm8.staticflickr.com/7185/13574595064_28071ab5ae_o.png)

File analytics.xsd

Là file compiled của file trên, bạn không cần quan tâm tới file này

# Trên Google Analytics

vào link này: [Google Analytics Account](http://google.com/analytics)

Nhấn nút Đăng nhập

![](http://farm8.staticflickr.com/7316/13574390013_fc95019363_o.png)

Chọn tab Quản trị

![](http://farm8.staticflickr.com/7026/13574407623_8c32c154eb_o.png)

Tạo thuộc tính mới

![](http://farm4.staticflickr.com/3781/13574432883_7b8b91df2f_o.png)

Chọn các thông số phù hợp. Lưu ý, ở mục “Bạn muốn theo dõi điều gì”, chọn Ứng dụng di động nhé

![](http://farm4.staticflickr.com/3819/13574765814_c96d25bb44_o.png)

Sau đó, bạn sẽ có 1 ID theo dõi dạng UA-#######-##, copy chuỗi này và paste vào bên trong file analytics.xml trong project của bạn

# Thiết lập theo dõi

Về cơ bản, bạn có thể theo dõi rất nhiều thứ, bao gồm:

*   Màn hình ứng dụng: màn hình nào người dùng sử dụng nhiều
*   Event: Nút nào được click nhiều, sự kiện nào xảy ra nhiều
*   Exception: Lỗi nào bị bắt nhiều nhất
*   Transaction: Thanh toán, mua đồ, In-app Purchase
*   Social: Chia sẻ trong mạng xã hội
*   Timing: thời gian mà ứng dụng chạy một task nào đó

Và tất nhiên, bạn sẽ có các con số sau đây:

*   Số lượng người dùng
*   Người dùng mới cài đặt trong ngày
*   Người dùng đang sử dụng app hiện tại (Realtime)
*   Mức độ trung thành
*   Tỷ lệ thoát ứng dụng
*   Phiên bản ứng dụng (cái này phải cài đặt trong file XML)

## Coding

Trong sự kiện `RootFrame_NavigationFailed`, thêm đoạn code sau

\[code lang=csharp\] GoogleAnalytics.EasyTracker.GetTracker().SendException(e.Exception.Message, false);

\[/code\]

Đoạn code này có nhiệm vụ theo dõi các Exception khi lỗi chuyển trang

Trong sự kiện `Application_UnhandledException`, thêm đoạn code sau:

\[code lang=csharp\] GoogleAnalytics.EasyTracker.GetTracker().SendException(e.ExceptionObject.Message, false);

\[/code\]

Đoạn code này có nhiệm vụ theo dõi các Exception cho tất cả các lỗi khác

Trong method `InitializePhoneApplication()`, khai báo một Event Handler:

\[code lang=csharp\] // Track Navigation RootFrame.Navigated += RootFrame\_Navigated; \[/code\]

Trong Event Handler, thêm đoạn code sau:

\[code lang=csharp\] if (e.Content != null) { GoogleAnalytics.EasyTracker.GetTracker().SendView(e.Content.ToString()); } \[/code\]

# Xem Analytics

Xem kết quả Analytics khá thú vị ở chỗ nó cho phép bạn xem rất nhiều thông tin, mà cái hay nhất có lẽ là số người dùng hiện tại đang sử dụng app

![](http://farm4.staticflickr.com/3726/13575637933_a49df7e626_o.png)

Bạn có thể khám phá thêm trong trang Google Analytics của mình.

Lưu ý là ứng dụng nhiều người dùng, sử dụng mạng thì mới xem được Analytics nhé.