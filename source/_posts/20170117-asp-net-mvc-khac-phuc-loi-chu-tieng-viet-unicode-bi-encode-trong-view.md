---
title: '[ASP.NET MVC] Khắc phục lỗi chữ tiếng việt Unicode bị encode trong View'
tags:
  - encode
  - lỗi
  - unicode
id: '684'
categories:
  - - CSharp
    - ASP.NET
date: 2017-01-17 03:14:03
---

![](https://farm1.staticflickr.com/420/31984906310_6b01d5c873_o.png)

Làm web mà có tiếng Việt thì khổ nhất là chữ tiếng Việt nó cứ bị encode thành mấy ký tự vô nghĩa

Điều này ảnh hưởng đến nhìu thứ, đặc biệt là SEO, lưu trữ data lên DB, vân vân và vân vân.

Vậy khắc phục làm sao?
<!-- more -->
# Nguồn gốc sâu xa

Lý do rất là củ chuối của nó là do trong tiếng Việt có một số ký tự trùng với các ký tự latin (trong cái bảng này nè: [http://www.akadia.com/services/iso8859.html](http://www.akadia.com/services/iso8859.html))

Để tránh bị nhầm lẫn giữa các ký tự latin này, rất nhìu ngôn ngữ lập trình tự động encode các ký tự này thành chuỗi mà máy có thể hiểu được

## Chuỗi đó là gì?

Dùng trang này để convert qua lại online, bạn sẽ thấy: [https://r12a.github.io/apps/conversion/](https://r12a.github.io/apps/conversion/)

ASP.NET convert chuỗi đó sang một dạng code gọi là "Unicode Decimal Code". Ví dụ: [http://www.codetable.net/decimal/224](http://www.codetable.net/decimal/224)

# Cách khắc phục

1.  Mở file Web.config ra
2.  Tìm tag `<system.web>`
3.  Thêm vào: `<globalization fileEncoding="utf-8" />`

Thành quả:

![](https://farm1.staticflickr.com/436/32241635761_2b342942b1_o.png)

Thế là xong :D

Bạn nào có cách khắc phục khác hay hơn thì nói cho mình biết với nhóe