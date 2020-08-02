---
title: Upgrade your apps to Windows 8.1 – Tips and tricks
tags:
  - retarget
  - upgrade
  - Visual Studio
  - windows 8.1
id: '351'
categories:
  - - C++
  - - c
    - Windows Store App
date: 2014-10-20 01:09:29
---

Vậy là Windows 8.1 ra mắt cũng đã lâu. Đối với các ứng dụng viết mới thì target mặc định của nó đã là Windows 8.1. Vậy đối với các ứng dụng cũ kỹ thì sao? Microsoft cung cấp cho bạn một giải pháp, tuy chưa hoàn hảo, nhưng rất hữu ích. Bạn chỉ cần bấm và click.
<!-- more -->
# Retarget

Để retarget ứng dụng từ windows 8 lên 8.1, rất đơn giản, chọn chuột phải vào Project, nhấn Retarget to Windows 8.1 ![](https://farm6.staticflickr.com/5597/14959569523_93a2eea021_o.png) Một bảng nhỏ hiện ra, nói rằng bạn nên backup blah blah blah. Nếu bạn đang dùng version control như TFS, cách backup tốt nhất là check in trước khi retarget Nhấn OK để Visual Studio tiến hành Retarget ![](https://farm6.staticflickr.com/5615/15556047406_d430b4f604_o.png) Khi bạn thấy cái bảng này là thành công….một nửa ![](https://farm6.staticflickr.com/5604/15577095301_919a00e1f7_o.png)

# Fix errors and Warning

Như hình trên bạn cũng thấy, có nhiều Errors và Warning xuất hiện. Yên tâm, khi build thử project, bạn sẽ thấy còn nhiều errors hơn nữa

## Các errors về References

Như hình trên, ứng dụng cũ dùng Microsoft Advertising SDK for Windows 8 (XAML) version 6.1. Bạn đã Upgrade lên 8.1, thì phải dùng SDK phiên bản mới hơn. Right click Reference trong Project Folder, chọn Add Reference… ![](https://farm4.staticflickr.com/3942/14959045524_c16f0ccea0_o.png) Bỏ chọn các dòng bị mờ, và chọn dòng sáng rõ tương ứng. Như hình dưới đây. Xong rồi thì nhấn OK ![](https://farm4.staticflickr.com/3938/15393674778_6d1b670903_o.png)

## Reinstall Nuget Package

Có một số Nuget Package chưa chịu target sang Windows 8.1. Mình sẽ target nó lại bằng cách…Reinstall Mở Tool > Nuget Package Manager > Package Manager Console ![](https://farm4.staticflickr.com/3951/15556131206_828262a120_o.png) Có tùy chọn cho phép bạn Reinstall tất cả mọi nuget package, nhưng mà làm vậy thì hơi lâu. Bạn chỉ nên update một số package bị ảnh hưởng thôi. Tên Package bị ảnh hưởng nằm trong dòng thông báo lỗi Gõ dòng lệnh sau vào. Đoạn cuối cùng là tên package ![](https://farm4.staticflickr.com/3934/15580689642_679c2c614e_o.png) Package Manager Console sẽ chạy, nhìn rất chuyên nghiệp :3 Chú ý: khi reinstall Google Analytics SDK, bạn sẽ thấy file bị conflict. Gõ N vô để nó bỏ qua không overwrite cái file này. ![](https://farm4.staticflickr.com/3942/14959702053_fc3fe49d21_o.png) Tiếp tục làm tương tự cho các package khác. Lần này, bạn chỉ cần gõ phím mũi tên để paste lại lệnh gần nhất. Edit cái tên package là xong

## Fix warning về Resource

Bạn nào làm app Multiple language sẽ gặp warning này. Lý do là method GetValue đã bị obsoleted, bạn cần phải nâng cấp một tí ![](https://farm4.staticflickr.com/3939/15394661740_97dc995ef1_o.png) Rất đơn giản. Thêm một dòng "ResourceContext.GetForCurrentView() làm tham số thứ 2 là xong ![](https://farm6.staticflickr.com/5604/15577621901_91cf4673b5_o.png) Đổi thành cái này ![](https://farm6.staticflickr.com/5611/15394171128_99a5fc56b2_o.png)

## Fix lỗi querry for Windows Size directly

Ở windows 8.1, windows size đã có thể lấy trực tiếp ra ngoài. Vì vậy, dòng này trong Layout Aware Page bị lỗi thời. ![](https://farm6.staticflickr.com/5607/15394693500_050c985474_o.png) Sửa bằng cách ta sẽ sửa method DetermineVisualState Chuột phải DetermineVisualState > Go to Definition Sửa lại như sau `protected virtual string DetermineVisualState() { string visualState = "FullScreenLandscape"; var windowWidth = Window.Current.Bounds.Width; var windowHeight = Window.Current.Bounds.Height; if( windowWidth <= 500 ) { visualState = "Snapped" + "_Detail"; } else if( windowWidth <= 1366 ) { if( windowWidth < windowHeight ) { visualState = "FullScreenPortrait" + "_Detail"; } else { visualState = "FilledOrNarrow"; } } return visualState; }` Sau đó, thay thế method này với method cũ. Lưu ý method này không có tham số Vậy là xong. Build lại, bạn sẽ thấy không còn lỗi nào :yay: