---
title: '[Windows Store] When the property window in Visual Studio not responding'
tags:
  - Visual Studio
  - windows phone
id: '346'
categories:
  - - c
    - Windows Phone
    - Windows Store App
date: 2014-10-09 22:39:52
---

Khi làm việc với Visual Studio 2012, VS2013 trở lên, nhất là với việc thiết kế giao diện bằng ngôn ngữ XAML, bạn rất có thể sẽ bắt gặp một điều bất tiện: Sau một thời gian hoạt động ổn định, bạn không thể click, chỉnh sửa, tăng giảm bất cứ thứ gì trong cửa sổ property. Vậy là bạn phải chỉnh sửa trực tiếp trong code, khá bất tiện và mất thời gian.

Làm thế nào để sửa được lỗi này?
<!-- more -->
# OLD WAY: Restart your Visual Studio

Phải rồi, câu nói nổi tiếng của Apple Supporter: "Have you tried turn it off and on again?" Tắt đi bật lại Visual Studio chắc chắn sẽ giải quyết vấn đề cho bạn. Nhưng tiếp tục đọc tiếp bài blog này nhé

# NEW WAY: Run a piece of code

Đoạn code sau sẽ cho phép bạn kill designer task bên trong Visual Studio. Chạy đoạn code này xong, vào Visual Studio, bấm đường link "Click here to reload Designer", thế là xong.

Mở notepad, copy paste đoạn code sau:

taskkill /f /im XDesProc.exe

Lưu lại với đuôi .bat

Vậy là xong. Mỗi lần bị lỗi không thể edit trong khung property của Visual Studio, bạn chỉ cần double click file này là xong.

# More details: What does Microsoft say?

Các kỹ sư của Microsoft đã biết đến sự tồn tại của lỗi này. Và họ đã "wánh" nó là Won-fix in this version. Tức là trừ phi có phiên bản Visual Studio mới hơn, lỗi này sẽ không được sửa trong phiên bản 2012, 2013.