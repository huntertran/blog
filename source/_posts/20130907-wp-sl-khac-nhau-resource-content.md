---
title: 'Windows Phone – Silverlight: Khác nhau giữa “resource” và “content”'
tags:
  - content
  - file
  - project
  - resource
  - windows phone
id: '186'
categories:
  - - c
    - Windows Phone
date: 2013-09-07 04:59:02
---

Mọi thứ có trong project folder, ta đều phải lựa chọn: Resource hay Content? Bài viết này sẽ nói về sự khác biệt giữa 2 thể loại này, cũng như lợi/hại của từng loại
<!-- more -->
*   [1. Khác nhau](#1-khác-nhau)
*   [2. Truy xuất](#2-truy-xuất)
    
    *   [2.1. Hình ảnh thuộc tính Content](#21-hình-ảnh-thuộc-tính-content)
    *   [2.2. Hình ảnh thuộc tính Resource](#22-hình-ảnh-thuộc-tính-resource)
*   [3. Chọn cái nào](#3-chọn-cái-nào)

# 1. Khác nhau

khác biệt chính là Resource được kèm vào trong file dll, trong khi đó, Content lại trở thành một file riêng, đi kèm với file dll.

Bạn tự hỏi, vậy Isolated Storage là gì. Đừng nhầm lẫn, Isolated Storage lại là một khái niệm khác, một bộ nhớ độc lập được tạo ra khi bạn cài đặt ứng dụng

Hãy làm một bài test nhỏ. Tạo một project Silverlight (Windows Phone cho dễ :3 ), thêm vào vài cái hình. Rồi chọn resource cho một số hình, và content cho các hình còn lại. Build file XAP. Đổi tên file XAP thành ZIP, giải nén nó ra. Bạn sẽ thấy, những file có thuộc tính content thì nằm ngay bên ngoài. Những file Resource thì đã được nhúng kèm trong dll, nên chúng ta ko thấy nữa.

# 2. Truy xuất

Truy xuất tới các file resource và content khác nhau một tí

## 2.1. Hình ảnh thuộc tính Content

Content là một file nằm riêng biệt, nên truy xuất dễ dàng:

XAML:

\[code lang=xml\] <Image Stretch=”None” Source=”/images/yourImage.png”/> \[/code\]

C#:

\[code lang=csharp\] Uri uri = new Uri("/images/yourImage.png", UriKind.Relative); BitmapImage imgSource = new BitmapImage(uri); \[/code\]

## 2.2. Hình ảnh thuộc tính Resource

Resource, vì nằm trong một file dll, nên truy xuất nó khó khăn hơn nhiều

XAML:

\[code lang=xml\] <Image Source="/TestProjet;component/images/yourImage.png"/> \[/code\]

C#:

\[code lang=csharp\] Uri uri = new Uri("/TestProjet;component/images/yourImage.png", UriKind.Relative); this.Image.Source = new BitmapImage(uri); \[/code\]

# 3. Chọn cái nào

Hiểu rồi, giờ bạn sẽ chọn cái nào cho các file thêm vào project?

Một file Resource sẽ load nhanh hơn khi bạn truy xuất nó. Tuy nhiên, ứng dụng sẽ khởi động chậm hơn. Và ngược lại, một file Content sẽ load chậm hơn, bù lại, ứng dụng sẽ không phải load file này vào bộ nhớ trong lúc đang khởi động.

Nếu bạn cần truy xuất một file rất lớn, mà ứng dụng chưa cần ngay, hay chọn ngay Content. Ngược lại, nếu ứng dụng của bạn cần load file đó ngay khi chạy (ví dụ như Wallpaper chẳng hạn), thì lời khuyên là nên chọn Resource cho nó, vì đằng nào bạn cũng phải load nó lên.

Chọn Resource sẽ giảm thiểu hiện tượng ứng dụng load lên được mấy phần trăm giây thì bỗng nhiên Background Image "xuất hiện"