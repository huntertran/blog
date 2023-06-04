---
title: '[ASP.NET for Beginner] - Part 2 - Connect Database and Model Binding'
tags:
  - core
  - database
  - entity framework
  - model
id: '952'
categories:
  - - CSharp
    - ASP.NET
date: 2018-03-11 12:11:47
---

Ở phần trước bạn đã có một khái niệm cơ bản về mô hình MVC. Dựa vào đó, chúng ta sẽ tiếp tục tìm hiểu thêm về database những vấn đề liên quan nhé.

<!-- more -->

> Xem các bài viết trong series
> 
> * [Phần 1: Mô hình MVC](https://huntertran.ca/2018/03/04/asp-net-for-beginner-part-1-mvc/)
> * [Phần 2: Connect Database và Model Binding](https://huntertran.ca/2018/03/11/asp-net-for-beginner-part-2-connect-database-and-model-binding/)
> * [Phần 3: Front end framework nào](https://huntertran.ca/2018/03/18/asp-net-for-beginner-part-3-front-end-framework-nao/)
> * [Phần 4: CRUD và Data Validation](https://huntertran.ca/2018/03/25/aspnet-for-beginner-part-4-crud-va-data-validation/)

_**Table of Contents**_

<!-- TOC -->

- [1. Lựa chọn database](#1-l%E1%BB%B1a-ch%E1%BB%8Dn-database)
    - [1.1. SQL Server](#11-sql-server)
    - [1.2. The others](#12-the-others)
- [2. Entity Framework](#2-entity-framework)
- [3. Tạo Model và Database](#3-t%E1%BA%A1o-model-v%C3%A0-database)
    - [3.1. Tạo model Phone](#31-t%E1%BA%A1o-model-phone)
    - [3.2. Tạo Database Context](#32-t%E1%BA%A1o-database-context)
    - [3.3. Cài đặt Connection String](#33-c%C3%A0i-%C4%91%E1%BA%B7t-connection-string)
    - [3.4. Cài đặt kết nối](#34-c%C3%A0i-%C4%91%E1%BA%B7t-k%E1%BA%BFt-n%E1%BB%91i)
    - [3.5. Tạo Migration đầu tiên](#35-t%E1%BA%A1o-migration-%C4%91%E1%BA%A7u-ti%C3%AAn)
- [4. Model Binding](#4-model-binding)
    - [4.1. Tạo Controller](#41-t%E1%BA%A1o-controller)
    - [4.2. Các nuget cần thiết](#42-c%C3%A1c-nuget-c%E1%BA%A7n-thi%E1%BA%BFt)
    - [4.3. Scaffolding](#43-scaffolding)
- [5. Model Binding](#5-model-binding)

<!-- /TOC -->

Có thể hiểu database là trái tim của ứng dụng, còn asp.net là bộ não. Thiết kế một database cho đúng chuẩn thì đòi hỏi kha khá thời gian học + luyện tập thì nó mới lên trình được.

Một cách khác rất hay là bắt tay vào làm một project thực tế. Nếu làm theo phần trước, chắc bạn cũng đã có 1 sample project với tên mvcbasic nhỉ.

Nhìn chung, bạn sẽ có 1 project giống như sau: [MVC Basic 0.1 on Github](https://github.com/huntertran/mvcbasic/releases/tag/0.1)

# 1. Lựa chọn database
<a id="markdown-l%E1%BB%B1a-ch%E1%BB%8Dn-database" name="l%E1%BB%B1a-ch%E1%BB%8Dn-database"></a>

Có hơi bị nhiều hệ quản trị cơ sở dữ liệu đang đấu đá nhau trên thị trường. Ở đây mình sẽ nói sơ qua 1 số loại phổ biến

## 1.1. SQL Server
<a id="markdown-sql-server" name="sql-server"></a>

Cây nhà là vườn, miễn phí cho người dùng cá nhân, hiệu suất cao, mạnh mẽ, là hệ cơ sở dữ liệu có quan hệ. Sql Server đã chứng minh cho mọi dev thấy tính ổn định của nó.

## 1.2. The others
<a id="markdown-the-others" name="the-others"></a>

Nhìn chung, Microsoft có hỗ trợ kha khá các hệ cơ sở dữ liệu khác như MySQL, PostgreSQL, SQLite, nhưng nếu đã lựa chọn các hệ này, thì bạn sẽ phải tự mày mò kha khá các vấn đề mà đa phần đã được giải quyết khi dùng SQL Server

# 2. Entity Framework
<a id="markdown-entity-framework" name="entity-framework"></a>

ASP.NET có một điểm mạnh là Entity Framework (EF). Ở phiên bản core thì nó có thêm EF Core. EF hiểu nôm na là một bộ công cụ cho phép bạn kết nối tới database, truy vấn, thêm xóa sửa vân vân mà không cần phải có kiến thức về cách viết SQL.

Có lợi thì cũng phải có hại, EF theo đánh giá của nhiều người thì nó khá....chậm. Điều này đã và đang được cải thiện rất nhiều ở phiên bản mới đi kèm với ASP.NET Core là Entity Framework Core.

Bạn cần cài đặt

* [SQL Server Express](https://www.microsoft.com/en-us/sql-server/sql-server-editions-express)
* [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms) (optional)

Cài nuget package

Mở project mvcbasic bằng vscode

Lần lượt gõ các lệnh sau trong terminal

```s
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
```

Sau đó, mở file mvcbasic.csproj và thêm dòng sau

```xml
<ItemGroup>
  <DotNetCliToolReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet" Version="2.0.0" />
</ItemGroup>
```

tiếp tục gõ trong terminal

```s
dotnet restore
```

# 3. Tạo Model và Database
<a id="markdown-t%E1%BA%A1o-model-v%C3%A0-database" name="t%E1%BA%A1o-model-v%C3%A0-database"></a>

Có 2 cách để bắt đầu làm việc với database trong asp.net core là Code first và Database first.

Ngắn gọn thì Code first cho phép bạn viết code trước (tạo các model class), rồi các model bạn tạo sẽ được cập nhật lên database thông qua các `migration`. Database first thì là cách truyền thống từ xưa tới nay: Tạo database trước, và code của bạn có nghĩa vụ 'connect' tới database đó.

Bạn có thể tham khảo thêm ở đây: [Code first vs Database first](https://huntertran.ca/2017/01/06/asp-net-mvc-code-first-vs-database-first/)

## 3.1. Tạo model Phone
<a id="markdown-t%E1%BA%A1o-model-phone" name="t%E1%BA%A1o-model-phone"></a>

chuột phải vào folder Models > new file > Phone.cs

```cs
namespace mvcbasic.Models
{
    public class Phone
    {
        public int Id { get; set; }
        public string Name { get; set; }
    }
}
```

## 3.2. Tạo Database Context
<a id="markdown-t%E1%BA%A1o-database-context" name="t%E1%BA%A1o-database-context"></a>

Database Context có thể hiểu như một công cụ cho phép ứng dụng của bạn kết nối tới Database và thực hiện các tác vụ thêm xóa sửa.

Tạo 1 folder mới ở thư mục gốc với tên 'Data'

Chuột phải vào folder Data > new file > MvcBasicDbContext.cs

```cs
namespace mvcbasic.Data
{
    using Models;
    using Microsoft.EntityFrameworkCore;
 
    public class MvcBasicDbContext : DbContext
    {
        public MvcBasicDbContext(DbContextOptions<MvcBasicDbContext> options) : base(options)
        {
        }
 
        public DbSet<Phone> Phones { get; set; }
    }
}
```

## 3.3. Cài đặt Connection String
<a id="markdown-c%C3%A0i-%C4%91%E1%BA%B7t-connection-string" name="c%C3%A0i-%C4%91%E1%BA%B7t-connection-string"></a>

Để kết nối tới database, thì Entity Framework sẽ cần có các thông tin như username, password, tên database, server đang host cái database này. Tất cả thông số đó đều gộp chung lại thành 1 đoạn string, và giang hồ gọi nó là `connection string`

Mở file appsettings.json và thêm vào đoạn json sau

```json
"ConnectionStrings" : { "PhoneDbConnectionString": "Server=(localdb)\\\\mssqllocaldb;Database=PhoneDb;Trusted\_Connection=True;" }
```

> Đoạn connection string trên có ý nghĩa như sau Server: LocalDb (là một dạng database local có trên các phiên bản mới của SQL Server) Database: PhoneDb Connection tới database dùng Windows Authentication

Bạn có thể sẽ phải config lại đoạn connection string này cho đúng với môi trường làm việc của bạn

## 3.4. Cài đặt kết nối
<a id="markdown-c%C3%A0i-%C4%91%E1%BA%B7t-k%E1%BA%BFt-n%E1%BB%91i" name="c%C3%A0i-%C4%91%E1%BA%B7t-k%E1%BA%BFt-n%E1%BB%91i"></a>

Mở file Startup.cs, tìm method `ConfigureServices` và thêm vào dòng sau

```cs
services.AddDbContext<MvcBasicDbContext>(options => options.UseSqlServer(Configuration.GetConnectionString("PhoneDbConnectionString")));
```

và nhớ add thêm 2 dòng using

```cs
using Microsoft.EntityFrameworkCore;
using mvcbasic.Data;
```

## 3.5. Tạo Migration đầu tiên
<a id="markdown-t%E1%BA%A1o-migration-%C4%91%E1%BA%A7u-ti%C3%AAn" name="t%E1%BA%A1o-migration-%C4%91%E1%BA%A7u-ti%C3%AAn"></a>

Sau khi tất cả các thao tác chuẩn bị đã hoàn tất, đã tới lúc bạn tạo migration đầu tiên của mình

Trong terminal, gõ

```s
dotnet ef migrations add InitialCreate
```

VSCode sẽ tự động tạo ra một thư mục tên Migrations, và thêm cơ số file vào đấy

[new files](/images/flickr/4784/40748059781_d2b5740095_o.png)

Tiếp tục, gõ

```s
dotnet ef database update
```

thì những migration này sẽ được thực thi, và database sẽ được tạo ra

![database created](/images/flickr/4774/38937566770_e203e7c169_o.png)

> Để kiểm tra, bạn có thể dùng Microsoft SQL Server Management Studio với các thông số sau
> 
> * **Server Name**: (LocalDb)\\MSSQLLocalDB
> * **Authentication**: Windows Authentication
> 
> MSSQLLocalDB là tên instance của bạn, có thể khác nếu khi cài SQL Server bạn ko chọn như default

# 4. Model Binding
<a id="markdown-model-binding" name="model-binding"></a>

Sau khi hoàn tất các bước trên, cơ bản web app của bạn đã có thể kết nối tới database. Nhưng để thực hiện các hành động thêm xóa sửa, thì bạn cần phải có Controller nữa

> Bạn có thể tải project hoàn tất ở bước 3 tại [đây](https://github.com/huntertran/mvcbasic/releases/tag/0.2)

## 4.1. Tạo Controller
<a id="markdown-t%E1%BA%A1o-controller" name="t%E1%BA%A1o-controller"></a>

VSCode cũng hỗ trợ bạn trong việc tự động tạo ra controller mong muốn mà ko phải code nhiều (thực ra ko phải là VSCode hỗ trợ, mà một công cụ gọi là .NET Cli tools và vài nuget package cho phép bạn làm chuyện này, nhưng trước mắt cứ hiểu vậy đã)

Tên Controller, theo asp.net convention như mình đã nói ở phần 1, sẽ có dạng `[Tên]Controller`, trong trường hợp này sẽ là `PhoneController`.

> Một quy tắc đặt tên phổ biến là
> * Tên bảng -> số nhiều: Phones
> * Tên model -> số ít: Phone
> * Tên controller: PhoneController
> * Tên view: Create, Delete, Details, Edit và Index

## 4.2. Các nuget cần thiết
<a id="markdown-c%C3%A1c-nuget-c%E1%BA%A7n-thi%E1%BA%BFt" name="c%C3%A1c-nuget-c%E1%BA%A7n-thi%E1%BA%BFt"></a>

Để có thể tạo controller, bạn sẽ cần thêm một số tool nữa

Mở mvcbasic.csproj và thêm các dòng sau

```xml
...
<PackageReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Design" Version="2.0.2" />
...
<DotNetCliToolReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Tools" Version="2.0.2" />
...
```

Tổng quan, file csproj sẽ giống như sau

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
 
  <PropertyGroup>
    <TargetFramework>netcoreapp2.0</TargetFramework>
  </PropertyGroup>
 
  <ItemGroup>
    <PackageReference Include="Microsoft.AspNetCore.All" Version="2.0.5" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="2.0.1" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer.Design" Version="1.1.5" />
    <PackageReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Design" Version="2.0.2" />
  </ItemGroup>
 
  <ItemGroup>
    <DotNetCliToolReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet" Version="2.0.1" />
    <DotNetCliToolReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Tools" Version="2.0.2" />
  </ItemGroup>
 
</Project>
```

## 4.3. Scaffolding
<a id="markdown-scaffolding" name="scaffolding"></a>

Mở terminal, và gõ lệnh sau

```s
dotnet restore
dotnet build
 
dotnet aspnet-codegenerator controller -name PhoneController -m Phone -dc MvcBasicDbContext --relativeFolderPath Controllers --useDefaultLayout --referenceScriptLibraries
```

Nhìn vào câu lệnh trên, chắc bạn cũng sẽ đoán được nó làm gì: "Này dotnet, tạo cho tao 1 controller mới tên là `PhoneController`, dùng model là `Phone`, Data Context là `MvcBasicDbContext`, trong folder tên là `Controllers`, dùng default layout, à có scripts đi kèm nhá"

2 câu lệnh đầu tiên giúp bạn thực sự cài nuget, và build project một phát để đảm bảo ko có lỗi phát sinh, và clear các file tạm ko còn cần thiết

![create new controller](/images/flickr/4782/40705936652_1e3d6b551d_o.png)

gõ tiếp `dotnet run` để chạy thử app

![app with phone controller](/images/flickr/4779/25877724937_7bfed1c8d7_o.png)

bạn có thể vọc vạch các kiểu với các link mà asp.net core tạo sẵn cho bạn, create new, edit, delete, details gì đấy thì tùy

# 5. Model Binding
<a id="markdown-model-binding" name="model-binding"></a>

Mở file PhoneController ra, bạn sẽ thấy có sẵn code trong đấy rồi, tuy ko đẹp lắm, nhưng nhìn chung là nó chạy tốt

Hãy nhìn vào method Details

```cs
// GET: Phone/Details/5
public async Task<IActionResult> Details(int? id)
{
    if (id == null)
    {
        return NotFound();
    }
 
    var phone = await _context.Phones
                              .SingleOrDefaultAsync(m => m.Id == id);
    if (phone == null)
    {
        return NotFound();
    }
 
    return View(phone);
}
```

Method này nhận một tham số là nullable int có tên là id, khi bạn gọi tới url Phone/Details/5 (như dòng comment ở bên trên), thì số 5 đó sẽ được hiểu là Id. Đó chính là model binding

Tiếp tục, nhìn vào class Create có attribute `[HttpPost]`

```cs
// POST: Phone/Create
// To protect from overposting attacks, please enable the specific properties you want to bind to, for 
// more details see http://go.microsoft.com/fwlink/?LinkId=317598.
[HttpPost]
[ValidateAntiForgeryToken]
public async Task<IActionResult> Create([Bind("Id,Name")] Phone phone)
{
    if (ModelState.IsValid)
    {
        _context.Add(phone);
        await _context.SaveChangesAsync();
        return RedirectToAction(nameof(Index));
    }
    return View(phone);
}
```

Model binding còn vi diệu ở chỗ, nếu bạn dùng hẳn 1 class làm parameter, thì ASP.NET sẽ tự hiểu các property trong class đó, và gắn đúng từng giá trị một

Bạn có thể xóa `[Bind("Id,Name")]` đi và code vẫn chạy tốt, nhưng như Microsoft đã cảnh báo, để bảo vệ bạn khỏi chuyện orver posting attack, thì bạn phải chỉ định luôn là property nào sẽ được gắn

Method này tương ứng với Views > Phone > Create.cshtml

```html
<!--dòng 17-->
<input asp-for="Name" class="form-control" />
```

từ khóa `asp-for` thông báo rằng Name là property sẽ được truyền lên server, và server sẽ "gắn" nó vào model phone của method Create

> Tại sao lại ko có Id? Vì Id mặc định được coi như Key của bảng Phone, và key thì ko cần phải có khi tạo mới, vì database sẽ tự sinh ra nó

Tiếp tục, mở Views > Phone > Index.cshtml bạn sẽ thấy đoạn code sau

```cs
@foreach (var item in Model)
{
    <tr>
        <td>
            @Html.DisplayFor(modelItem => item.Name)
        </td>
        <td>
            <a asp-action="Edit" asp-route-id="@item.Id">Edit</a> |
            <a asp-action="Details" asp-route-id="@item.Id">Details</a> |
            <a asp-action="Delete" asp-route-id="@item.Id">Delete</a>
        </td>
    </tr>
}
```

> ô lạ chưa, có foreach trong html Ngôn ngữ này gọi là Razor, cho phép bạn thực thi một số đoạn code C# trong html, giúp cho việc render ra các tag html như mong muốn.

Razor thông minh tới mức nó tự hiểu chỗ nào là code html, và chỗ nào là code Razor, với các nguyên tắc vô cùng đơn giản

* Mỗi đoạn code razor đều bắt đầu bằng dấu `@`
* Ngay sau dấu `{` hoặc `(` thì ko cần `@`

Database và Model binding còn nhiều điều để nói. Tạm thời ta cứ hiểu vậy đã

Đón đọc phần 3 bạn nhé 😃