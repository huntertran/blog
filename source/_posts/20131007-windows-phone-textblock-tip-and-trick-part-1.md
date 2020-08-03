---
title: '[Windows Phone] Textblock tip and trick – Part 1'
tags:
  - richtextbox
  - textblock
  - textbox
  - windows phone
id: '251'
categories:
  - - c
    - Windows Phone
date: 2013-10-07 11:04:10
---

Vậy là, bạn đã có một thời gian dài làm việc với Windows Phone

Hôm nay, tôi sẽ hướng dẫn bạn một số mẹo vặt khi sử dụng Textblock trong Windows Phone

![advanced text](https://farm8.staticflickr.com/7407/10135898285_7ea60ebd9a_o.png)
<!-- more -->
*   [1\. Multiple line trong cùng Textblock](#1-multiple-line-trong-cùng-textblock)
*   [2\. Canh đều 2 bên cho Textblock](#2-canh-đều-2-bên-cho-textblock)
    
    *   [2.1. Giải pháp](#21-giải-pháp)
*   [3\. Run Control](#3-run-control)

# 1\. Multiple line trong cùng Textblock

![](https://farm4.staticflickr.com/3782/10136087586_2967ef0062_o.png)

Đây là một textblock bình thường

Vấn đề được đặt ra: Làm thế nào để có thể hiển thị 2 dòng trong Textblock này?

![](https://farm8.staticflickr.com/7386/10136108785_5fe51d5aa7_o.png)

Problem Solved ![Party smile](https://cuoilennaocacban2.files.wordpress.com/2013/10/wlemoticon-partysmile1.png)

Vậy còn trong Code C# thì sao?

![](https://farm8.staticflickr.com/7316/10136204654_88cfbb6b67_o.png)

# 2\. Canh đều 2 bên cho Textblock

chờ chút đã, canh đều 2 bên thì có gì khó. Justify là xong

Đây là Right

![](https://farm3.staticflickr.com/2888/10136343715_2961551886_o.png)

Đây là Center

![](https://farm4.staticflickr.com/3699/10136477973_38ce651897_o.png)

Và đây là Justify

![](https://farm4.staticflickr.com/3829/10136441596_37cb7b47d7_o.png)

## 2.1. Giải pháp

Dùng RichTextBox như hình dưới

![](https://farm3.staticflickr.com/2883/10139054113_9a87a5c1fd_o.png)

Problem Solved

# 3\. Run Control

Trong các ví dụ trên, nhiều lần bạn gặp từ khóa “Run”. Nó là một control con nằm trong các control TextBlock và TextBox, RichTextBox.

Run Control cho phép bạn hiển thị các đoạn văn bản khác nhau trong cùng một control TextBlock hoặc TextBox. Mỗi Run Control sẽ mang các thuộc tính định dạng riêng.

Hết rồi, hẹn gặp lại các bạn ở phần 2 nhé