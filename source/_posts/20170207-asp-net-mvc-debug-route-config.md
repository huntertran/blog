---
title: '[ASP.NET MVC] Debug Route Config'
tags:
  - route
id: '692'
categories:
  - - CSharp
    - ASP.NET
date: 2017-02-07 05:23:32
---

Route Map là một cái bảng. Khi bạn chạy một ứng dụng ASP.NET, cái bảng này sẽ được đem ra để so sánh với URL mà bạn gõ trên địa chỉ trình duyệt

Vì nó duyệt theo kiểu bảng như vậy nên rất khó để debug nó. Vỏ dừa dày có con dao nhọn. Vẫn có cách để trị nó nhóe

<!-- more -->

# 1. Cài nuget package

Trước tiên bạn phải cài một package có tên là routedebugger

![](/images/flickr/469/31947372973_69489bcb72_o.png)

Sau đó, thêm một dòng config trong Web.config

<add key="RouteDebugger:Enabled" value="true" />

![](/images/flickr/595/31947453593_6bbc0ddf77_o.png)

# 2. Debug cái route

Sau khi hoàn tất 2 bước trên, nhấn Debug, kéo xuống dưới cùng của website và bạn sẽ thấy bảng phân tích route

![](/images/flickr/586/31947500953_e3538ee6b5_o.png)

Bảng này sẽ cho bạn thấy route của bạn gõ trên thanh địa chỉ nó bị dinh vô cái config nào

Vậy là bạn đã debug được rồi nhóe