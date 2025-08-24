---
title: '[Visual Studio] XAML Element Inspector with Visual Studio 2015 [vi-vn]'
tags:
  - live visual tree
  - on the fly
  - property
  - Visual Studio
id: '493'
categories:
  - - uncategorized
date: 2015-10-07 07:02:29
---

Trong phiên bản mới nhất của Visual Studio (aka Visual Studio 2015), Microsoft đã giới thiệu 2 tính năng cực khủng gọi là "Live Visual Tree" và "Live Property Explorer". Sử dụng 2 tính năng này, bạn có thể dễ dàng xem và sửa code XAML khi app đang chạy \[insert hình há mỏ kinh ngạc\]
<!-- more -->

# 1. Live Visual Tree

Để sử dụng Live Visual Tree, mở bất kỳ project nào có code XAML. Nó có thể là App Windows 8, 8.1, Windows Universal App, hoặc Universal Windows Platform (UWP, aka App phát triển cho Windows 10)

Build và chạy thử app, sau đó quay lại Visual Studio, bạn sẽ thấy một cục toolbar nhỏ gọi là "Live Visual Tree". Nhấn zô nó để mở ra

![](https://farm1.staticflickr.com/543/20216853242_f1655e2c2e_o.png)

Nhấn vô nút hình cái ghim nhỏ nhỏ để dính nó zô đó, dễ xài hơn

![](http://cuoilennaocacban2.files.wordpress.com/2015/08/080215_1141_windowsxaml1.png)

Trong cửa sổ này, click vào biểu tượng hình tam giác trỏ trỏ vô cái hình chữ nhật nho nhỏ. Đó chính là Inspector, rất giống với Element Inspector của Google Chrome. Quay lại app đang chạy, bạn sẽ thấy con trỏ đi tới đâu, một cái khối hộp chữ nhật viền chấm đỏ bao xung quanh element bên dưới con trỏ.

![](http://cuoilennaocacban2.files.wordpress.com/2015/08/080215_1141_windowsxaml2.png)

Click một phát, và Live Visual Tree sẽ nhảy tới vị trí chính xác của element đó

![](https://farm1.staticflickr.com/528/19602618384_1423c50319_o.png)

Bạn cũng có thể click vào các elements khác trong Live Visual Tree, và cái khung chấm đỏ sẽ nhảy tới element trên app đang chạy của bạn. Bằng cách này, bạn có thể hiểu chính xác những element nào được vẽ trên app của bạn.

Bạn cũng có thể search một element bằng tên hoặc loại của nó

![](https://farm1.staticflickr.com/438/20038725589_1b8097c624_o.png)

# 2. Live Property Explorer

Với một element bất kỳ được chọn trong Live Visual Tree, nhìn wa bên phải của Visual Studio, bạn sẽ thấy "Live Property Explorer", click vô nó để mở ra, rùi click cái ghim để đó dính zô đó

![](https://farm1.staticflickr.com/425/20037363128_c89bbbe6d5_o.png)

Ủa mà sao có ít propery hơn bình thường nhỉ. Đừng lo, mở rộng cái group "Default" ra và bạn sẽ thấy mấy property còn lại"

Một điều hay của Live Property Explorer là bạn có thể thay đổi các giá trị trong các property, và xem sự thay đổi đó ngay lập tức trên app đang chạy của bạn.

Mình sẽ thử đổi Height thành 100, và xem chuyện gì sẽ xảy ra trong app

![](https://farm1.staticflickr.com/504/20199163156_3fc683e0c9_o.png)

Giờ tới cái app

![](https://farm1.staticflickr.com/555/20231217491_5d41f98c4f_o.png)

Quá kinh khủng phải ko? Bạn có thể thay đổi hầu như mọi thứ, ngoại trừ một số property bị khóa (màu xám xịt) trong Live Property Explorer

Quá đã. Thế là bây giờ bạn đã biết sử dụng Live Visual Tree để dò code XAML của bạn được render như thế nào trên app, và dùng Live Property Explorer để thay đổi giá trị của các Property, và xem sự thay đổi đó ngay lập tức, ngay trên app đang chạy mà không cần phải build lại.

Hẹn gặp lại bạn trong những bài post tiếp theo về những tính năng cực khủng của Visual Studio 2015 nhé