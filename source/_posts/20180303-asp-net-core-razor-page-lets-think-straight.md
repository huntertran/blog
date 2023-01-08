---
title: '[ASP.NET Core] - Razor Page - Let''s think straight'
tags:
  - page
  - razor
id: '1020'
categories:
  - - CSharp
    - ASP.NET
date: 2018-03-03 05:00:24
---

Khi bạn cần tạo thật nhanh một cái website có các page cần thiết mà không cần phải quan tâm tới các vấn đề phức tạp như mô hình, bảo mật, mở rộng, thì Razor Page chính là câu trả lời
<!-- more -->
*   [1. Yêu cầu](#1-yêu-cầu)
*   [2. Mô hình phát triển](#2-mô-hình-phát-triển)
*   [3. Các vấn đề của MVC](#3-các-vấn-đề-của-mvc)
    
    *   [3.1. Fat Controller](#31-fat-controller)
    *   [3.2. Chia cấp](#32-chia-cấp)
    *   [3.3. Duplicate](#33-duplicate)
*   [4. Razor Page Coding conventions](#4-razor-page-coding-conventions)
*   [5. The future is now?](#5-the-future-is-now)

# 1. Yêu cầu

*   [.NET Core 2.0 trở lên](https://www.microsoft.com/net/download)
*   [Visual Studio Code](https://code.visualstudio.com/)
*   Đọc sơ qua về [Razor Page](https://docs.microsoft.com/en-us/aspnet/core/mvc/razor-pages/?tabs=visual-studio)

# 2. Mô hình phát triển

Nếu bạn đã là một chiến binh ASP.NET lâu năm, thì chắc hẳn bạn sẽ quen thuộc với mô hình MVC, viết tắt cho Model-View-Controller. Ở Razor Page, bạn sẽ làm quen với một mô hình hoàn toàn mới và vô cùng đơn giản (đơn giản tới mức ko có gì để học luôn)

**Mô hình MVC**

![mvc pattern](https://farm1.staticflickr.com/794/39482986360_fe3ba6ff76_o.png)

> Nếu bạn muốn làm quen với mô hình MVC, có thể đọc bài viết [\[ASP.NET for Beginner\] – Part 1 – MVC](https://huntertran.ca/2018/03/04/asp-net-for-beginner-part-1-mvc/)

**'Mô hình' Razor Page**

![razor page pattern](https://farm1.staticflickr.com/822/40395935845_bdb4073f2f_o.png)

# 3. Các vấn đề của MVC

## 3.1. Fat Controller

Giả sử bạn có một controller xử lý các tác vụ liên quan tới giao dịch chuyển tiền giữa các tài khoản, tạm gọi là `TransactionController`

Có 4 thao tác cơ bản đối với 1 dòng dữ liệu: Create-Read-Update-Delete, tới đây thì ok không vấn đề gì

Pặc, bạn muốn xử lý thêm việc nạp thẻ điện thoại, chi trả hóa đơn điện, nước, internet => thêm các phương thức như `NapTheCao`, `TraTienDien`, `TraTienNuoc`, `TraTienInternet`. 2 tuần sau, bạn lại muốn thêm vài tính năng khác, tất cả đều liên quan tới transaction.

Càng về sau, `TransactionController` càng dài, và nó đã chính thức được gọi tên là Fat Controller.

## 3.2. Chia cấp

Mô hình MVC cho bạn một folder tên `Controllers` để chứa tất cả các controller của bạn. Điều này sd4 tương ứng với 1 cấp địa chỉ trên URL

Với ví dụ transaction phía trên, URL của bạn sẽ có dạng: `domain/transaction/create`

Nếu bạn muốn 1 cấp sâu hơn, ví dụ như `domain/transaction/phones/create` thì sao? Bạn phải hoặc customize lại route, hoặc tạo một `Area` tên `Transaction`, và tách các function liên quan với nhau thành từng controller khác nhau.

## 3.3. Duplicate

Đối với một form bất kỳ, trong mô hình mvc luôn phải có 2 action tương ứng với 2 hành động là Get và post, và người ta thường đặt tên 2 action này giống nhau cho dễ phân biệt với các tính năng khác trong cùng một controller. Điều này đôi khi gây ra những bất tiện nhất định, và bạn bắt buộc phải khai báo attribute `[HttpGet]` và `[HttpPost]`

# 4. Razor Page Coding conventions

Tương tự như MVC, Razor Page cũng có một số coding conventions

Conventions

MVC

RAZOR PAGES

Default View

Index.cshtml

Index.cshtml

return default view

return View();

return Page();

Http Verbs

\[HttpGet\]  
\[HttpPost\]

OnGet();  
OnPost();

Bind dữ liệu

ViewModel

\[BindProperty\]

Generate Link

Url.Action(...)

Url.Page(...)

multiple action for form submit

Not built-in

asp-page-handler=“TestHandler”  
OnTestHandler()

# 5. The future is now?

Razor Page, theo đánh giá của mình, chỉ phù hợp với các project vừa và nhỏ, với các view đơn giản về mật logic.

Tại phiên bản .NET CORE 2.0, Razor Page vẫn chưa hỗ trợ một số tính năng mà MVC đang có như sau

*   IActionFilter
*   Output Cache
*   IgnoreAntiforgeryToken attribute (bạn có thể tham khảo thêm tại [github issue này](https://github.com/aspnet/Mvc/issues/7012) để biết cách tắt **toàn bộ**)