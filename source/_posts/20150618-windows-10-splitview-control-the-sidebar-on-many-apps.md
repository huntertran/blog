---
title: '[Windows 10] SplitView Control (the sidebar on many apps)'
tags: []
id: '440'
categories:
  - - c
    - Windows 10
date: 2015-06-18 05:37:30
---

Ngôn ngữ thiết kế của Windows 10 đang được làm mới lại, trong đó có một thanh công cụ nằm bên hông của mỗi app.

Làm thế nào để bắt chước cách thiết kế này?
<!-- more -->
# SplitView Control

Microsoft đã xây dựng riêng một control cho việc đó và gọi nó là SplitView Control

Cơ bản, nó sẽ có 2 phần: Pane và Content

Phần Pane sẽ là nơi đặt các Menu, danh mục này nọ, phần Content sẽ thể hiện nội dung chính của ứng dụng.

![](http://lh4.ggpht.com/-UgAGBBcqi6I/VS7jhHAJx_I/AAAAAAAAQTY/N1TzXUut-dE/SplitView_thumb.gif?imgmax=800)

Có nhiều kiểu thiết kế cho SplitView này tùy theo bạn chọn. Ở đây mình sẽ hướng dẫn cơ bản

Tạo một Project mới sử dụng Universal Application Platform (UAP) từ Visual Studio

Trong MainPage, paste dòng sau vào

![](https://farm1.staticflickr.com/529/18912097922_259833232b_o.png)

Trong cấu trúc trên, bạn có thể thấy Pane là một thuộc tính của SplitView. Hãy coi Pane như một control mẹ và thêm các control khác vào bên trong nó

CompactPaneLength là chiều rộng của SplitView khi người dùng thu gọn nó lại

DisplayMode là cách thức hiển thị của SplitView. Có 4 kiểu:

*   CompactInline: Khi thu gọn sẽ quay về hình dạng 1 thanh dài bên hông màn hình, khi mở bung ra sẽ đẩy phần Content sang một bên
*   CompactOvelay: Khi thu gọn sẽ quay về hình dạng 1 thanh dài bên hông màn hình, khi mở bung ra sẽ ĐÈ LÊN phàn Content
*   Inline: Giống CompactInline, như khi thu gọn sẽ biết mất khỏi màn hình
*   Overlay: Giống Overlay, nhưng khi thu gọn sẽ biết mất khỏi màn hình

# Cấu trúc

Cấu trúc của SplitView bao gồm Pane và Content. Trong Pane sẽ có Hamburger Button và list các tính năng khác. Theo cấu trúc sau đây:

![](https://farm1.staticflickr.com/551/18295463384_027ca53bd8_o.png)

Code của cái trên rất đơn giản:

> <SplitView> <SplitView.Pane> <Grid> <Grid.RowDefinitions> <RowDefinition Height="Auto" /> <RowDefinition Height="\*"/> </Grid.RowDefinitions> <Button Grid.Row="0"/> <ListView Grid.Row="1"/> </Grid> </SplitView.Pane> <Grid/> </SplitView>

# Hamburger Button

Hamburger Button thực ra cũng không khó. Windows 10 có hẳn một font dành riêng cho các biểu tượng:

Để tạo một button có hình Hamburger, paste dòng code sau:

<Button x:Name="HamburgerButton" **FontFamily="Segoe MDL2** Assets" **Content=""/>**

Mục Content sẽ là đoạn code trong bảng mã sau: [http://modernicons.io/segoe-mdl2/cheatsheet/](http://modernicons.io/segoe-mdl2/cheatsheet/)

Để đóng mở Pane của cái SplitView, bạn set thuộc tính "IsPaneOpen = true" hoặc "IsPaneOpen = false" trong event click của button nhé.

Thế là xong. Chúc bạn thành công