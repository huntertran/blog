---
title: '[ASPNET Core 2] – Middleware'
tags: []
id: '1032'
categories:
  - - CSharp
    - ASP.NET
date: 2018-06-12 00:18:39
---

For English version: [\[ASPNET Core 2\] – Middleware](https://tuanmsp.wordpress.com/2018/06/08/aspnet-core-2-middleware/)

Đôi khi bạn có một yêu cầu éo le: Viết Hello world bằng ASP.NET

Dễ ẹt, `dotnet new mvc`, rồi sửa `Views/Home/Index.cshtml` cho nó trả về 1 dòng

\[code lang=html\] <p>hello world</p> \[/code\]

Thế là xong, phải ko? Có cách khác :D
<!-- more -->
*   [1. Middleware là giề](#1-middleware-là-giề)
*   [2. Các loại middleware](#2-các-loại-middleware)
*   [3. Default middleware](#3-default-middleware)
*   [4. Viết một middleware](#4-viết-một-middleware)
    *   [4.1. Dùng delegate](#41-dùng-delegate)
    *   [4.2. Xài class riêng](#42-xài-class-riêng)
    *   [ghi chú khi xài Dependency Injection](#ghi-chú-khi-xài-dependency-injection)

# 1. Middleware là giề

Tưởng tượng rằng ứng dụng asp.net của bạn là 1 đường ống nước. Data chính là nước. Nước ở đầu ống (request) thì bẩn như kênh nhiêu lộc. Bạn mong muốn rằng nước ở cuối ống (response) phải sạch như nước khoáng Lavie. Chắc phải có lọc gì đó ở giữa ống nhể? Middleware chính là loại lọc đó. Nó gắn vào ứng dụng để xử lý requests và responses ![middleware](https://farm2.staticflickr.com/1751/27794903017_13f284ce64_o.png)

> middleware có thể quyết định là nó có tiếp tục truyền cái request nó đã xử lý cho 1 middleware tiếp theo hay ko. Trong trường hợp nó ngắt luôn ko truyền, thì ta gọi đó là \[code lang=text\] short-circuit \[/code\]

# 2. Các loại middleware

Có 3 loại middleware, phân loại bằng cách bạn implement nó như nào

Loại

Có thể short-circuit

Dùng để

Use

Có

Short-circuit một request  
Logic để tạo response

Run

Không

Kết thúc pipeline

Map  
MapWhen

Không

Phân nhánh pipeline dựa trên request path  
MapWhen phân nhánh dựa trên điều kiện  
Hỗ trợ Nesting (multi-level branching)

> ## So sánh với đồ cổ ASP.NET MVC5
> 
> ASP.NET MVC5
> 
> ASP.NET Core 2
> 
> Khái niệm
> 
> HTTP Handlers  
> HTTP Modules
> 
> middleware
> 
> Lựa chọn?
> 
> HTTP Handlers => Dựa trên filename extension  
> HTTP Modules => Móc vào life cycle bằng cách dùng events
> 
> Định nghĩa theo 1 thứ tự đặc biệt và các từ khóa  
> Run => kết thúc pipeline  
> Use => short-circuit và xử lý logic  
> Map => phân nhánh dựa trên path
> 
> Dễ xài ko?
> 
> Đòi hỏi hiểu sâu về ASP.NET life-cycle  
> Khó xài vì nhiều modules có thể móc vào cùng 1 event
> 
> Yêu cầu 1 thứ tự nhất định  
> Chỉ có 1 dòng pipeline, dễ hiểu/xài/debug

# 3. Default middleware

Khi mới tạo 1 project asp.net core mới, .net cli sẽ thêm vào 1 số middleware cho bạn

1.  Exception Handler: handle exception từ các middleware ở dưới
2.  Static Files: trả về files trong wwwroots
3.  Mvc: Hướng request tới các action trong controller

source code nè \[code lang=csharp\] public static void Configure(IApplicationBuilder app, IHostingEnvironment env) { if (env.IsDevelopment()) { app.UseDeveloperExceptionPage(); } else { app.UseExceptionHandler("/Error/500"); } app.UseStaticFiles(); app.UseAuthentication(); app.UseSession(); if (!env.IsDevelopment()) { app.UseMiddleware<ErrorHandlingMiddleware>(); } app.UseMvc(routes => { routes.MapRoute( name: "default", template: "{controller=Home}/{action=Index}/{id?}"); }); } \[/code\] [Đây](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-2.1&tabs=aspnetcore2x#built-in-middleware) danh sách các built-in middlewares

# 4. Viết một middleware

## 4.1. Dùng delegate

thêm code vào `Startup.cs`, method `Configure` \[code lang=csharp\] app.Use((context, next) => { var cultureQuery = context.Request.Query\["culture"\]; if (!string.IsNullOrWhiteSpace(cultureQuery)) { var culture = new CultureInfo(cultureQuery); CultureInfo.CurrentCulture = culture; CultureInfo.CurrentUICulture = culture; } // Call the next delegate/middleware in the pipeline return next(); }); \[/code\]

## 4.2. Xài class riêng

phức tạp hơn, nhưng bù lại linh hoạt hơn đầu tiên, code cho middleware \[code lang=csharp\] public class RequestCultureMiddleware { private readonly RequestDelegate \_next; public RequestCultureMiddleware(RequestDelegate next) { \_next =next; } public Task InvokeAsync(HttpContext context) { var cultureQuery = context.Request.Query\["culture"\]; if (!string.IsNullOrWhiteSpace(cultureQuery)) { var culture = new CultureInfo(cultureQuery); CultureInfo.CurrentCulture = culture; CultureInfo.CurrentUICulture = culture; } // Call the next delegate/middleware in the pipeline return this.\_next(context); } } \[/code\] sau đó, code cho extension để xài được middleware đó trong method `Configure` \[code lang=csharp\] // Expose through IApplicationBuilder public static class RequestCultureMiddlewareExtensions { public static IApplicationBuilder UseRequestCulture(this IApplicationBuilder builder) { return builder.UseMiddleware<RequestCultureMiddleware>(); } } \[/code\] cuối cùng, xài trong `Configure` method \[code lang=csharp\] // Use in Startup.cs => Configure method public void Configure(IApplicationBuilder app) { app.UseRequestCulture(); app.Run(async (context) => { await context.Response.WriteAsync($"Hello{CultureInfo.CurrentCulture.DisplayName}"); }); } \[/code\]

## ghi chú khi xài Dependency Injection

> `Scoped lifetime service` phải được inject vào Invoke hoặc InvokeAsync method Inject cái `scoped lifetime service` thông qua constructor sẽ ép cái service đó thành singleton

có 3 loại lifetime cho một service trong asp.net, là `transient`, `scoped` và `singleton`

*   **Transient** lifetime services được tạo ra mỗi lần nó được gọi. Loại này phù hợp cho các service lightweight, stateless.
    
*   **Scoped** lifetime services được tạo cho mỗi request.
    
*   **Singleton** lifetime services được tạo cho lần requested đầu tiên (hoặc khi ConfigureServices khởi chạy nếu bạn có tạo 1 instance của service trong đó) rồi các request sau đó sẽ xài lại instance này.