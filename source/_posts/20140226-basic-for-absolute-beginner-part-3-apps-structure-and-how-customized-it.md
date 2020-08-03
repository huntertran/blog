---
title: >-
  [Basic for Absolute Beginner] – [Part 3] – App’s Structure and how customized
  it
tags:
  - app
  - beginner
  - structure
  - windows phone
id: '303'
categories:
  - - C#
  - - c
    - Windows Phone
date: 2014-02-26 09:19:49
---

![](http://farm4.staticflickr.com/3740/12789845873_f26035990e_o.png") Chào các bạn,

Sau đợt nghỉ lễ dài, hôm nay mình giới thiệu phần 3 của loạt bài viết \[Basic for Absolute Beginner\]

Phần 1 nói về các control cơ bản là Grid và StackPanel: [\[Windows Phone–Silverlight\] Layout with XAML–Basic for Absolute Beginner – Part 1](http://cuoilennaocacban2.wordpress.com/2013/11/22/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner/)

Phần 2 nói về thiết kế giao diện với XAML: [\[Windows Phone – Silverlight\] Layout with XAML – Basic for Absolute Beginner – Part 2](http://cuoilennaocacban2.wordpress.com/2014/01/21/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner-part-2/)

Tại sao tôi lại nói 2 phần này trước cả App's Structure. Các control là điều cơ bản nhất, cho dù sau này Structure một project có thể sẽ thay đổi, nhưng bạn sẽ tìm ra cách hiểu chúng nhanh thôi. Khi mới tạo một project Windows Phone, Visual Studio đã mở sẵn cho bạn file Mainpage.xaml để bạn chỉnh sửa.

Bây giờ, làm một cú lội ngược dòng, bạn sẽ học về cấu trúc một ứng dụng trong Windows Phone nhé
<!-- more -->
*   [**1\. Cách thức ứng dụng hoạt động trên thiết bị**](#1-cách-thức-ứng-dụng-hoạt-động-trên-thiết-bị)
*   [**2\. Cấu trúc của ứng dụng**](#2-cấu-trúc-của-ứng-dụng)
    
    *   [**2.1 Các thành phần**](#21-các-thành-phần)
        
        *   [**2.1.1 Giao diện chính**](#211-giao-diện-chính)
        *   [**2.1.2 Properties**](#212-properties)
        *   [**2.1.3 References**](#213-references)
        *   [**2.1.4 Assets**](#214-assets)
        *   [**2.1.5 Resource**](#215-resource)
        *   [**2.1.6 App.xaml và App.xaml.cs**](#216-appxaml-và-appxamlcs)
        *   [**2.1.7 LocalizedString.cs**](#217-localizedstringcs)
        *   [**2.1.8 MainPage.xaml và MainPage.xaml.cs**](#218-mainpagexaml-và-mainpagexamlcs)

# **1\. Cách thức ứng dụng hoạt động trên thiết bị**

Khi cài ứng dụng lên thiết bị, bạn sẽ có một mô hình như sau:

Áp dụng cho Windows Phone 7 và Windows Phone 8. Hứa hẹn sẽ có thay đổi lớn trong Windows Phone 8.1 ![](http://farm4.staticflickr.com/3834/12789771723_b7d84196a3_o.png)

Các mũi tên màu vàng biểu thị cho khả năng truy xuất

Nhìn hình trên, bạn sẽ thấy Ứng dụng của bạn chỉ được phép truy cập vào Isolated Storage của chính nó mà thôi (Cái tên Isolated tức là "Cô lập")

Ngoài ra, nếu muốn truy cập vào thẻ nhớ, ứng dụng của bạn bắt buộc phải thông qua API của hệ điều hành. Hiện tại thì Windows Phone chỉ mới cho phép đọc ghi các file media (nhạc, hình, video) lên thẻ nhớ mà thôi.

# **2\. Cấu trúc của ứng dụng**

Mở Visual Studio 2013 lên, bạn sẽ thấy giao diện như sau:

![](http://farm6.staticflickr.com/5497/12791385094_05d22bf96d_o.png")

Bấm chọn New Project, chọn Windows Phone > Windows Phone App

![](http://farm8.staticflickr.com/7351/12790972835_528e1f2515_o.png")

Một số loại Project khác bạn sẽ có cơ hội thực tập với nó sau

Ở bên dưới, có 2 tùy chọn khá vui

![](http://farm4.staticflickr.com/3810/12791424864_1cb8e8fe4a_o.png")

*   Create directory for Solution: Solution của bạn sẽ được đặt trong một folder "mẹ", và Project sẽ được đặt trong folder "con"

Nói thêm một chút về các thể loại Project của Visual Studio: Khi tạo mới, bạn sẽ tạo một Solution (đuôi file .sln). Và toàn bộ Project của bạn sẽ nằm trong Solution đó. Một Solution có thể chứa nhiều Project.

Vậy tại sao bạn lại cần nhiều Project trong 1 Solution? Vì mỗi Project sẽ tạo ra một module khác nhau của hệ thống. Có thể Project chính của bạn là một ứng dụng nghe nhạc, và Project phụ sẽ là một module cho phép cập nhật ngầm, tự động thông tin bài nhạc, hình album vân vân

*   Add to source control: Source Control là một thuật ngữ cho một loại công cụ giúp bạn quản lý code của mình được hiệu quả. Microsoft có một công cụ Source Control là Team Foundation Server. Các bài viết sau sẽ nói về nó nhé

Nhấn Ok để tạo Project

![](http://farm3.staticflickr.com/2812/12792547075_8aaa4aa9d4_o.png")

Trên đây là giao diện sau khi tạo (của bạn có thể không giống lắm)

## **2.1 Các thành phần**

### **2.1.1 Giao diện chính**

![](http://farm3.staticflickr.com/2842/12792570385_36061d5837_o.png")

Đây là designer, hiển thị trực quan những gì bạn code trong file XAML

![](http://farm8.staticflickr.com/7427/12793026714_6bcf6ec07b_o.png")

XAML, code định nghĩa giao diện của bạn. Cột bên phải là thanh cuộn cải tiến có từ Visual 2012

![](http://farm4.staticflickr.com/3673/12792616615_8cea25525e_o.png")

3 nút này có chức năng thay đổi cách bố cục. Nhấn thử và bạn sẽ biết

![](http://farm8.staticflickr.com/7301/12792644865_d7f85b1efd_o.png")

Còn đây là Solution Explorer, chứa cấu trúc tập tin trong Project của bạn

### **2.1.2 Properties**

Mở Properties ra, bạn sẽ thấy có 3 file

![](http://farm8.staticflickr.com/7292/12793106684_21d1a2cd0f_o.png")

Đối với người mới bắt đầu, bạn chỉ cần quan tâm tới "WMAppManifest.xml" là được. Double click vào nó để mở ra

Mục Application UI định nghĩa cho tên gọi, các Icon của ứng dụng

![](http://farm4.staticflickr.com/3783/12792710505_cd2f45bfd7_o.png")

Mục Capabilities định nghĩa những tài nguyên mà ứng dụng sử dụng như Camera, thư viện nhạc, hình, video, các loại cảm biến, mạng Internet, etc.

![](http://farm4.staticflickr.com/3810/12793179894_6ec2e78465_o.png")

Ứng dụng của bạn cần sử dụng cái gì thì tick chọn cái đó. Đừng tick dư

Requirement là những tài nguyên mà ứng dụng bạn "đòi" để có thể chạy được, ví dụ như NFC, Gyroscope

![](http://farm4.staticflickr.com/3681/12792917443_60e514fc62_o.png")

Tại sao vậy? Vì không hẳn tất cả các máy Windows Phone đều như nhau. Có máy có camera trước, có máy không có, blah blah blah. Nếu ứng dụng của bạn nhất thiết phải đòi có những tài nguyên đó, bạn hãy tick vào các ô này. Trên Windows Phone Store, tất cả các máy có cấu hình không đáp ứng được đòi hỏi của bạn sẽ không thể tải được.

Và cái cuối cùng dành cho việc đóng gói và hỗ trợ đa ngôn ngữ. Hiện thời bạn chưa cần quan tâm tới nó

![](http://farm8.staticflickr.com/7379/12792874415_005fd92688_o.png")

### **2.1.3 References**

References là thư mục chứa các thư viện mà ứng dụng của bạn sẽ sử dụng

![](http://farm6.staticflickr.com/5528/12792993413_7876c769c3_o.png")

Đa phần các thư viện này có thể cài đặt bằng NuGet

Tham khảo bài viết sau: [\[Visual Studio\] NUGET the Magician](http://cuoilennaocacban2.wordpress.com/2013/11/11/visual-studio-nuget-the-magician/)

Double click vào một thư viện sẽ cho bạn xem toàn bộ các class và method có trong thư viện đó (máy bạn nào yếu không nên bấm vào, treo máy đấy)

Tính năng này được gọi là Object Explorer, đã có từ lâu rồi

![](http://farm8.staticflickr.com/7422/12793098413_e19c21cbe5_o.png")

### **2.1.4 Assets**

Thư mục Assets chứa các tập tin hình ảnh, icon, âm thanh, video mà ứng dụng bạn sẽ sử dụng. Thực ra bạn không bị bắt buộc phải để cá tập tin đó vào thư mục này, nhưng cứ làm vậy cho nó có hệ thống

Nhấn chuột phải vào một tập tin nào đó và nhấn Property, bạn sẽ thấy thuộc tính của tập tin này. Thuộc tính quan trọng nhất là Build Action và Copy to output folder

![](http://farm4.staticflickr.com/3818/12793481294_7d345a6ec2_o.png")

Tham khảo bài viết sau để hiểu rõ về chúng: [\[Windows Phone – Silverlight\] - Khác nhau giữa "resource" và "content"](http://cuoilennaocacban2.wordpress.com/2013/09/07/wp-sl-khac-nhau-resource-content/)

Để thêm một tập tin nào đó vào thư mục này, chỉ đơn giản là nhấn phải > Add > Existing Item…

### **2.1.5 Resource**

Thư mục Resource chứa file Resource của ứng dụng.

File Resource thường được dùng để lưu các thông số, thuộc tính vân vân của ứng dụng. Tuy nhiên công dụng lớn nhất của nó là dùng để chuyển đổi ứng dụng của bạn thành ứng dụng đa ngôn ngữ. Ta sẽ nói về nó sau

### **2.1.6 App.xaml và App.xaml.cs**

Đối với mỗi một file XAML sẽ có một file XAML.CS đi kèm.

File XAML định nghĩa giao diện, còn CS sẽ định nghĩa cách thức hoạt động

File App.xaml và App.xaml.cs sẽ định nghĩa việc khởi tạo ứng dụng của bạn, khi mở lên như thế nào, đóng ứng dụng thì như thế nào, vân vân.

Bạn sẽ cần tới nó trong một số trường hợp sau này. Bạn có thể mở nó lên để xem thử

### **2.1.7 LocalizedString.cs**

File này cho phép ứng dụng hỗ trợ đa ngôn ngữ. Code trong file này do Visual Studio tự sinh ra, bạn không cần phải chỉnh sửa nó

### **2.1.8 MainPage.xaml và MainPage.xaml.cs**

Cuối cùng, đây là trang giao diện đầu tiên của ứng dụng. File MainPage.xaml sẽ được mở sẵn sau khi tạo mới ứng dụng

Như vậy, bạn đã hiểu rõ các thành phần cấu tạo nên một ứng dụng Windows Phone, áp dụng bài viết số 1 và số 2, hãy bắt tay vào thiết kế ngay cho bạn một ứng dụng Windows Phone hữu ích nào đó nhé