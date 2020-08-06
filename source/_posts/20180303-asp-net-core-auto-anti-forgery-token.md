---
title: '[ASP.NET Core] Auto Anti-forgery Token'
tags:
  - attack
  - cross-site
  - forgery
  - forgery token
  - request
id: '946'
categories:
  - - CSharp
    - ASP.NET
date: 2018-03-03 04:09:06
---

Có một cách giúp bạn tự động áp dụng `ValidateAntiForgeryToken` vào tất cả các Post Action trong controller của mình
<!-- more -->
Chắc bạn đã từng nghe qua [Cross-site Request Forgery (CSRF) attacks](https://en.wikipedia.org/wiki/Cross-site_request_forgery). Hiểu một cách đơn giản là Server thực thi một request giả mạo xuất phát từ hacker, nhưng với chứng thực xịn của 1 user nào đó. Điều này rất dễ thực hiện. Giả sử bạn truy cập 1 forum nào đó, trong đó có chứa đoạn javascript giả mạo 1 request tới ngân hàng của bạn, yêu cầu chuyển tiền. Nếu bạn vẫn đang đăng nhập vào tài khoản ebanking của mình, và ngân hàng ko áp dụng bất kỳ phương pháp bảo vệ nào, thì như một cái búng tay, tiền của bạn đã chuyển vào túi hacker.

ASP.NET đã implement sẵn cho bạn cách để chống lại phương thức tấn công này, và họ gọi nó là _`Anti-forgery Token`_

# Default protection with ASP.NET Core 2

Với ASP.NET Core 2, mỗi khi bạn dùng `form` tag, asp.net sẽ tự động chèn anti-forgery token cho bạn

> Với điều kiện: `form` tag có attribute `method="post"` VÀ \* attribute `action` không có data: `action=""` HOẶC \* attribute `action` không có

Tiếp tục, bạn phải thêm attribute `[ValidateAntiForgeryToken]` và action nhận data post lên

\[code lang=csharp\] \[HttpPost\] \[ValidateAntiForgeryToken\] public async Task<IActionResult> RemoveLogin(RemoveLoginViewModel account) { // Do something here } \[/code\]

# Auto protection with ASP.NET Core 2

Ở cách trên, với mỗi Action nhận Post request, bạn đều phải thêm \[ValidationAntiForgeryToken\] thủ công

Asp.net Core giới thiệu 1 class mới, giúp bạn tự động hóa quá trình này

## Nếu bạn muốn tự động cho từng Controller

\[code lang=csharp\] \[Authorize\] \[AutoValidateAntiforgeryToken\] public class ManageController : Controller { // Your code here } \[/code\]

## Nếu bạn muốn áp dụng cho toàn bộ app

\[code lang=csharp\] public class Startup { public void ConfigureServices(IServiceCollection services) { services.AddMvc(options => { options.Filters.Add(new AutoValidateAntiforgeryTokenAttribute()); }); } } \[/code\]

Vậy là xong