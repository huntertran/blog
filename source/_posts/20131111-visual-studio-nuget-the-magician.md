---
title: '[Visual Studio] NUGET the Magician'
tags:
  - nuget
  - windows phone
id: '259'
categories:
  - - C#
  - - c
    - Windows Phone
date: 2013-11-11 09:20:58
---

Khi sử dụng Visual Studio để lập trình, chắc hẳn sẽ có lúc bạn cần thêm các thư viện từ bên ngoài. Cách cũ là lên Google search (Bing search), rồi tìm thư viện, tải về và add thủ công vào Project. Từ bây giờ, bạn không cần phải làm như thế nữa. ![nuget](https://farm1.staticflickr.com/819/40232598394_27c397f3e4_o.png) Nuget là một công cụ giúp bạn thêm các thư viện ngoài vào Project của mình. Sử dụng Nuget rất đơn giản và dễ dàng
<!-- more -->
*   [1\. Chuẩn bị](#1-chuẩn-bị)
*   [2\. Cập nhật Nuget Package](#2-cập-nhật-nuget-package)
*   [3\. Sử dụng](#3-sử-dụng)
    *   [3.1. Cài đặt 1 gói Nuget](#31-cài-đặt-1-gói-nuget)
*   [4\. Giới thiệu một số gói Nuget hay](#4-giới-thiệu-một-số-gói-nuget-hay)

# 1\. Chuẩn bị

Đổi DNS của bạn thành Google DNS Không hiểu vì lý do gì mà khi để DNS mặc định, mình không thể truy cập Nuget ![](https://farm6.staticflickr.com/5509/10797602224_31099726fb_o.png) ![](https://farm3.staticflickr.com/2875/10797506925_685b5619ac_o.png) ![](https://farm3.staticflickr.com/2890/10797641014_1c326253d2_o.png)

# 2\. Cập nhật Nuget Package

Mở Visual Studio lên, chọn Tool > Extension and Update Chọn Mục Update và update tất cả mọi thứ mà bạn có thể. Nếu bạn chưa update lần nào thì rất có thể bạn sẽ có mục Nuget Package trong các gói update ![](https://farm8.staticflickr.com/7415/10797728624_43f2fd7efb_o.png)

# 3\. Sử dụng

Mở một Project bất kỳ, ở đây mình sẽ chọn Windows Phone, Project mẫu là RSS Reader Bật Solution Explorer, nhấn chuột phải vào References > Manage Nuget Package ![](https://farm6.staticflickr.com/5539/10799289075_a237ff0703_o.png) Chọn mục Online ![](https://farm6.staticflickr.com/5525/10799278546_20f8a4db7f_o.png) Từ đây, bạn có thể thấy rất nhiều package hay ho cho ứng dụng của bạn Nếu ứng dụng của bạn dùng Json, bạn có thể cài đặt Json.NET Ở cột bên phải là các thông tin liên quan tới gói Nuget đang được chọn. Nhiều gói Nuget có cả thông tin về cách sử dụng. Bạn có thể lên [https://www.nuget.org](https://www.nuget.org "https://www.nuget.org") để tìm hiểu thêm hoặc tìm kiếm các gói nuget phù hợp nhanh hơn

## 3.1. Cài đặt 1 gói Nuget

Gõ cái bạn muốn tìm vào ô Search ![](https://farm3.staticflickr.com/2855/10799595293_319514afd3_o.png) Chọn gói Nuget thích hợp ở bên trái, nhấn Install ![](https://farm3.staticflickr.com/2818/10799522506_b6433bafaa_o.png) Chờ nó cài đặt một tí. Bạn sẽ luôn có gói Nuget mới nhất phù hợp với project của bạn. Nếu Project của bạn không phù hợp, Nuget Package Manager sẽ tự động gỡ nó ra khỏi Project ![](https://farm8.staticflickr.com/7386/10799395825_24406f0f1f_o.png) Vậy là xong, bạn đã có thể bắt đầu sử dụng ngay gói Nuget đó

# 4\. Giới thiệu một số gói Nuget hay

*   **Json.NET**: Dùng để thao tác với dữ liệu Json
*   **HtmlAgilityPack**: Dùng để thao tác với dữ liệu HTML