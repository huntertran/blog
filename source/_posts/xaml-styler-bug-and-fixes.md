---
title: XAML Styler – Bug and fixes
tags:
  - extension
  - Visual Studio
id: '367'
categories:
  - - c
    - Windows Phone
date: 2014-11-16 21:07:16
---

Dành cho bạn nào chưa biết, XAML Styler là một extension nho nhỏ dành cho Visual Studio, dùng để format lại file thiết kế giao diện xaml cho đẹp. XAML Styler được phát triển thêm dựa trên Beautiful Xaml extension, và sau này được đưa lên Visual Studio Gallery.
<!-- more -->
# The Good

XAML Styler cho Visual 2010 và 2012 phiên bản stable có thể download tại đây [http://xamlstyler.codeplex.com/](http://xamlstyler.codeplex.com/)

# The Bad

Phiên bản bên trên chỉ dành cho 2012 trở xuống thôi nha. Nếu bạn đang dùng Visual Studio 2013 và vẫn muốn XAML Styler, thì đây là câu trả lời cho bạn Thư mục chính của Project: [https://github.com/nicovermeir/xamlstyler](https://github.com/nicovermeir/xamlstyler) Tải extension đã build ở đây: [https://visualstudiogallery.msdn.microsoft.com/3de2a3c6-def5-42c4-924d-cc13a29ff5b7](https://visualstudiogallery.msdn.microsoft.com/3de2a3c6-def5-42c4-924d-cc13a29ff5b7)

## It's have a bug, annoying bug

XAML Styler dành cho 2013 có một bug rất khó chịu, đó là nó sẽ thêm nhiều dòng trống vào code XAML của bạn. Cách khắc phục?

# The Ugly

2012 so với 2013 về mặt cấu trúc cũng không khác nhau xa lắm. Đã có một người download toàn bộ XAML Styler của 2012 xuống và build lại cho phù hợp với Visual Studio 2013 [http://www.spikie.be/blog/post/2013/11/13/.aspx](http://www.spikie.be/blog/post/2013/11/13/.aspx) Tuy nhiên vô đây bạn sẽ hơi bị bối rối một chút. Để tiện cho việc download, mình đã up lại lên box.com [https://app.box.com/s/5qi6fj9sqb88412tsgf5](https://app.box.com/s/5qi6fj9sqb88412tsgf5) Lưu ý là phiên bản này không có version control, tức là nó sẽ không tự động cập nhật khi có version mới.

# How to use

Sau khi tải về, các bạn khởi động lại Visual Studio để Extension có hiệu lực Mở một file XAML bất kỳ, nhấn chuột phải, chọn Beautiful XAML ![](https://farm8.staticflickr.com/7569/15805843611_61f1d5ce4f_o.png) Trước khi format ![](https://farm6.staticflickr.com/5612/15188291573_8707455bf8_o.png) Sau khi format ![](https://farm6.staticflickr.com/5616/15805857981_77e68fecc3_o.png)

## Chỉnh các properties

Vào Tools > Option ![](https://farm6.staticflickr.com/5615/15807753295_85a73c7f39_o.png) Chọn XAML Styler nằm dưới cùng và tùy chỉnh như ý muốn ![](https://farm6.staticflickr.com/5604/15187797314_d356dce01e_o.png)