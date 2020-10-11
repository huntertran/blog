---
title: '[ASP.NET for Beginner] - Part 4 - CRUD và Data Validation'
tags: []
id: '1010'
categories:
  - - CSharp
    - ASP.NET
  - - Others
date: 2018-03-25 06:03:16
---

Vậy là bạn đã có một khái niệm cơ bản về MVC, cách kết nối tới database, lựa chọn cho mình một front end phù hợp, đã tới lúc bắt tay vào thực hiện 4 thao tác cơ bản nhất của bất kỳ ứng dụng web nào: CRUD

<!-- more -->

> Xem các bài viết trong series
> 
> * [Phần 1: Mô hình MVC](https://huntertran.com/2018/03/04/asp-net-for-beginner-part-1-mvc/)
> * [Phần 2: Connect Database và Model Binding](https://huntertran.com/2018/03/11/asp-net-for-beginner-part-2-connect-database-and-model-binding/)
> * [Phần 3: Front end framework nào](https://huntertran.com/2018/03/18/asp-net-for-beginner-part-3-front-end-framework-nao/)
> * [Phần 4: CRUD và Data Validation](https://huntertran.com/2018/03/25/aspnet-for-beginner-part-4-crud-va-data-validation/)

<!-- TOC -->

- [1. CRUD](#1-crud)
    - [1.1. DbContext](#11-dbcontext)
    - [1.2. Create](#12-create)
    - [1.3. Read](#13-read)
    - [1.4. Update](#14-update)
        - [1.4.1. The Simplest - 2 trip to database](#141-the-simplest---2-trip-to-database)
        - [1.4.2. A more complicated](#142-a-more-complicated)
        - [1.4.3. Track???](#143-track)
    - [1.5. Delete](#15-delete)
- [2. DbContext - Một cách code tốt hơn](#2-dbcontext---m%E1%BB%99t-c%C3%A1ch-code-t%E1%BB%91t-h%C6%A1n)
    - [2.1. Nếu CRUD failed?](#21-n%E1%BA%BFu-crud-failed)
    - [2.2. await hay không?](#22-await-hay-kh%C3%B4ng)
- [3. Model Validation](#3-model-validation)
    - [3.1. DataAnnotation](#31-dataannotation)
    - [3.2. Client side validation](#32-client-side-validation)

<!-- /TOC -->

# 1. CRUD
<a id="markdown-crud" name="crud"></a>

CRUD viết tắt cho 4 hành động liên quan tới database là `Create`, `Read`, `Update` và `Delete`

> Bài viết này giả định rằng bạn sử dụng Entity Framework, như đã nói ở [phần 2](https://huntertran.com/2018/03/11/asp-net-for-beginner-part-2-connect-database-and-model-binding/), và đã có sẵn code trong ví dụ Bạn có thể clone code tại Github ở [đây](https://github.com/huntertran/mvcbasic/releases/tag/0.2)

## 1.1. DbContext
<a id="markdown-dbcontext" name="dbcontext"></a>

Trong ví dụ `mvcbasic`, `MvcBasicDbContext` đã được tạo sẵn cho bạn, và được khai báo ở mỗi Controller cần thiết. Ta sẽ sử dụng class này

Trong class PhoneController đã được tạo sẵn trong ví dụ, bạn có thể thấy cả 4 phương thức này được viết sẵn.

## 1.2. Create
<a id="markdown-create" name="create"></a>

Để tạo 1 record trong database, đối với Entity Framework, chuyện rất đơn giản

```csharp
var phone = new Phone
{
    Name = "Samsung Galaxy A5 (2017)"
};
 
_context.Phones.Add(phone);
_context.SaveChanges();
```

Trong trường hợp bạn muốn thêm nhiều dòng cùng một lúc, thì Entity Framework hỗ trợ một phương thức khác

```csharp
var phones = new List<Phone>();
 
var phone = new Phone
{
    Name = "Phone 1"
};

phones.Add(phone);
 
phone = new Phone
{
    Name = "Phone 2"
};

phones.Add(phone);
 
_context.Phones.AddRange(phones);
_context.SaveChanges();
```

## 1.3. Read
<a id="markdown-read" name="read"></a>

Để lấy 1 dòng dữ liệu từ 1 bảng, bạn có thể dùng method `Find`

```csharp
var id = 1;
var phone = _context.Phones.Find(id);
```

Method `Find` sẽ tìm trong bảng Phone có khóa chính = id của bạn. Kết quả trả về null nếu khóa đó không tồn tại

Để lấy nhiều dòng dữ liệu thỏa một điều kiện nào đó, bạn có thể dùng `LINQ` để query

```csharp
var searchKey = "samsung";
var phones = _context.Phones.Where(x => x.Name.Contains(searchKey));
```

`x` đại diện cho 1 object Phone trong database

`x.Name.Contains(searchKey)` nghĩa là Name có chứa string `searchKey`

> Hầu như tất cả các query bạn quen thuộc khi viết câu truy vấn bằng SQL đều có thể viết được dưới dạng LINQ. Đây gọi là LINQ to Entities (Dùng Linq để query thông qua các entities trong Entity Framework)
> 
> Bạn có thể tìm các câu lệnh tương ứng trong Linq bằng từ khóa: "How to _**hành động bạn muốn làm**_ using linq"

Kết quả trả về của một truy vấn là kiểu dữ liệu `IQueryable`. Bạn có thể tiếp tục lọc, gom nhóm, filter lại, hoặc chuyển đổi thành một kiểu dữ liệu khác như List, Array, etc

Bạn có thể xem thêm về các câu lệnh Linq được support ở đây: [Supported and Unsupported LINQ Methods (LINQ to Entities) on docs.microsoft.com](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/ef/language-reference/supported-and-unsupported-linq-methods-linq-to-entities#type-methods)

## 1.4. Update
<a id="markdown-update" name="update"></a>

Không đơn giản như các lệnh khác, update dùng Entity Framework hơi phức tạp (hơi thôi)

### 1.4.1. The Simplest - 2 trip to database
<a id="markdown-the-simplest---2-trip-to-database" name="the-simplest---2-trip-to-database"></a>

Cách đơn giản nhất để update 1 record gồm 3 bước 1. Lấy record đó lên từ database - Truy cập database lần 1 2. Thay đổi 1 thông tin nào đó trong record 3. Update lại record đó trong database - Truy cập database lần 2

code của nó như sau

```csharp
// get the phone object from database
var phone = _context.Phones.Find(phoneId);
 
// change some info
phone.Name = "Test"
 
// update the change to database
_context.SaveChanges();
```

Như bạn thấy, cách này bắt buộc bạn phải lấy 1 dữ liệu từ database lên trước khi bạn có thể edit nó

### 1.4.2. A more complicated
<a id="markdown-a-more-complicated" name="a-more-complicated"></a>

Vậy nếu bạn biết trước tất cả các dữ liệu của object thì sao? Trong trường hợp này, query record đó từ database là không cần thiết

```csharp
// Create the object from your brain
var phone = new Phone
{
    Id = 1
};
 
// Attach it to DbContext, so the DbContext can "track" the object
// Gắn nó vào DbContext, để DbContext có thể "theo dõi" object của bạn
_context.Phones.Attach(phone);
 
// Do some change
phone.Name = "Test";
 
// Save the change
_context.SaveChanges();
```

### 1.4.3. Track???
<a id="markdown-track%3F%3F%3F" name="track%3F%3F%3F"></a>

Entity Framework có 1 cách rất hay (và hơi phức tạp) để có thể tối ưu hóa các phương thức truy xuất/cập nhật dữ liệu: Nó sẽ theo dõi các thay đổi của 1 object

Giả sử, object của bạn có 50 field. Bạn chỉ thay đổi 1 field trong đó, rồi gọi `_context.SaveChanges()`, EF sẽ biết được rằng chỉ có 1 field bị thay đổi, và nó sẽ cập nhật đúng 1 field duy nhất, tăng hiệu suất của ứng dụng.

Để làm được điều này, nó sẽ query object đó trước bằng khóa chính, và khi bạn gọi Attach, nó sẽ bắt đầu theo dõi object của bạn.

Khi bạn thay đổi 1 field, thì trạng thái của field đó từ `Unmodified` sẽ chuyển thành `Modified`

## 1.5. Delete
<a id="markdown-delete" name="delete"></a>

Tương tự như edit, khi muốn delete 1 object, bạn cũng cần "2 chuyến" tới database

```csharp
var phone = _context.Phones.Find(id);
 
_context.Phones.Remove(phone);
_context.SaveChanges();
```

# 2. DbContext - Một cách code tốt hơn
<a id="markdown-dbcontext---m%E1%BB%99t-c%C3%A1ch-code-t%E1%BB%91t-h%C6%A1n" name="dbcontext---m%E1%BB%99t-c%C3%A1ch-code-t%E1%BB%91t-h%C6%A1n"></a>

## 2.1. Nếu CRUD failed?
<a id="markdown-n%E1%BA%BFu-crud-failed%3F" name="n%E1%BA%BFu-crud-failed%3F"></a>

Sẽ có nhiều trường hợp, khi gọi các câu lệnh crud bằng entity framework, ko có dòng data nào được thêm vào hoặc sửa đổi. Vậy làm sao bạn biết khi nào thành công khi nào không?

```csharp
_context.SaveChanges();
```

May mắn là method trên trả về _**số lượng record có thay đổi**_

Vì vậy, bạn có thể kiểm tra rất dễ bằng cách

```csharp
// your code here to CRUD
var result = _context.SaveChanges();
```

bằng cách kiểm tra "result > 0", bạn có thể biết được câu lệnh save changes của mình có thành công hay ko

## 2.2. await hay không?
<a id="markdown-await-hay-kh%C3%B4ng%3F" name="await-hay-kh%C3%B4ng%3F"></a>

Trong code controller được sinh ra bởi asp.net, bạn sẽ thấy các câu lệnh có dùng `_context` đều có `async` đằng sau, đằng trước là `await`, và kiểu dữ liệu của method là `Task`

Hiểu một cách đơn giản, async - await là một cặp từ khóa giúp đơn giản hóa việc lập trình multi thread.

> Nếu bạn chưa nắm vững kỹ thuật async-await, thì mình khuyên bạn là nên... bỏ hẳn và chỉ sử dụng các method trong các phần code bên trên trong bài viết này

# 3. Model Validation
<a id="markdown-model-validation" name="model-validation"></a>

Chắc hẳn bạn đã từng nghe các ràng buộc như

```
Tên không được chứa quá 20 ký tự Số điện thoại phải có 10 số
```

Bạn có tự hỏi "Họ đã làm điều đó như thế nào?"

## 3.1. DataAnnotation
<a id="markdown-dataannotation" name="dataannotation"></a>

ASP.NET cho phép bạn ràng buộc dữ liệu thông qua các `DataAnnotation` được viết thêm trên đầu mỗi property

Lấy ví dụ với model `Phone`, mình muốn thêm 1 ràng buộc là tên không được quá 50 ký tự, và báo lỗi khi user nhập quá số lượng

```csharp
namespace mvcbasic.Models
{
    using System.ComponentModel.DataAnnotations;
 
    public class Phone
    {
        public int Id { get; set; }
 
        [StringLength(50, ErrorMessage = "Name cannot be more than 50 characters")]
        public string Name { get; set; }
    }
}
```

> Bạn có thể tìm hiểu sâu hơn về cách làm 1 câu error message chung cho tất cả các property cùng loại tại đây: [Error Message – chung mà riêng](https://huntertran.com/2018/01/14/asp-net-mvc-error-message-chung-ma-rieng/)

Để check một object có thỏa điều kiện của model ko, bạn có thể dùng `ModelState`. Ví dụ trong method `Create`

```csharp
// POST: Phone/Create
// To protect from overposting attacks, please enable the specific properties you want to bind to, for 
// more details see http://go.microsoft.com/fwlink/?LinkId=317598.
[HttpPost]
[ValidateAntiForgeryToken]
public async Task<IActionResult> Create([Bind("Id,Name")] Phone phone)
{
    // CHECK MODEL STATE HERE
    if (ModelState.IsValid)
    {
        _context.Add(phone);
        await _context.SaveChangesAsync();
 
        var phone2 = new Phone
        {
            Name = "Test"
        };
 
        var phones = new List<Phone>();
 
        _context.Phones.AddRange(phones);
 
        return RedirectToAction(nameof(Index));
    }
    return View(phone);
}
```

## 3.2. Client side validation
<a id="markdown-client-side-validation" name="client-side-validation"></a>

Client side validation cho phép user thấy các lỗi dữ liệu ngay khi họ nhập mà chưa cần gửi data lên server của bạn

Việc bạn cần làm là thêm các dòng sau vào code View của mình

```html
<!--dòng này có thể đã nằm trong file View/Shared/_Layout.cshtml của bạn rồi-->
<a href="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-2.2.0.min.js">https://ajax.aspnetcdn.com/ajax/jQuery/jquery-2.2.0.min.js</a>
 
<a href="https://ajax.aspnetcdn.com/ajax/jquery.validate/1.16.0/jquery.validate.min.js">https://ajax.aspnetcdn.com/ajax/jquery.validate/1.16.0/jquery.validate.min.js</a>
<a href="https://ajax.aspnetcdn.com/ajax/jquery.validation.unobtrusive/3.2.6/jquery.validate.unobtrusive.min.js">https://ajax.aspnetcdn.com/ajax/jquery.validation.unobtrusive/3.2.6/jquery.validate.unobtrusive.min.js</a>
```

và trong form, bạn thêm đoạn code sau để hiển thị thông báo lỗi (nếu có)

```html
<form asp-action="Create">
    <!--dòng này hiển thị một thông báo tổng hợp tất cả các lỗi-->
    <div class="text-danger"></div>
    <div class="form-group">
 
 
        <!--dòng này hiển thị thông báo lỗi cụ thể cho form-->
        <span class="text-danger"></span>
    </div>
    <div class="form-group">
 
    </div>
</form>
```

Lỗi hiển thị như sau

![bug](https://farm5.staticflickr.com/4783/41003265721_c53a2103d8_o.png)

> Bạn có thể xem toàn bộ các annotation ở đây: [Data Annotation on docs.microsoft.com](https://docs.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations?view=netcore-2.0)

Thế là xong. Các bạn đón chờ phần tiếp theo nhé