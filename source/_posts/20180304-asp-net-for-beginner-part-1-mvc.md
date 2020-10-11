---
title: '[ASP.NET for Beginner] - Part 1 - MVC'
tags:
  - beginner
  - mvc
id: '949'
categories:
  - - CSharp
    - ASP.NET
date: 2018-03-04 07:41:16
---

MVC, mờ vờ cờ, model-view-controller, ai ai cũng đã nghe qua, nhưng bạn mới bắt đầu học nó, thì làm sao cho đúng?

Bài viết này đưa ra một số khái niệm cơ bản, và cách áp dụng chúng trong code thực tế.

<!-- more -->

> Xem các bài viết trong series
> 
> * [Phần 1: Mô hình MVC](https://huntertran.com/2018/03/04/asp-net-for-beginner-part-1-mvc/)
> * [Phần 2: Connect Database và Model Binding](https://huntertran.com/2018/03/11/asp-net-for-beginner-part-2-connect-database-and-model-binding/)
> * [Phần 3: Front end framework nào](https://huntertran.com/2018/03/18/asp-net-for-beginner-part-3-front-end-framework-nao/)
> * [Phần 4: CRUD và Data Validation](https://huntertran.com/2018/03/25/aspnet-for-beginner-part-4-crud-va-data-validation/)

<!-- TOC -->

- [1. MVC là gì?](#1-mvc-l%C3%A0-g%C3%AC)
    - [1.1. Model](#11-model)
    - [1.2. View](#12-view)
    - [1.3. Controller](#13-controller)
- [2. Một ví dụ đơn giản](#2-m%E1%BB%99t-v%C3%AD-d%E1%BB%A5-%C4%91%C6%A1n-gi%E1%BA%A3n)
    - [2.1. Bài toán](#21-b%C3%A0i-to%C3%A1n)
    - [2.2. Phân tích](#22-ph%C3%A2n-t%C3%ADch)
    - [2.3. Triển khai](#23-tri%E1%BB%83n-khai)
        - [2.3.1. Tính năng xem danh sách](#231-t%C3%ADnh-n%C4%83ng-xem-danh-s%C3%A1ch)
        - [2.3.2. Tính năng thêm](#232-t%C3%ADnh-n%C4%83ng-th%C3%AAm)
- [3. Tự tạo project](#3-t%E1%BB%B1-t%E1%BA%A1o-project)
    - [3.1. Phần mềm cần thiết](#31-ph%E1%BA%A7n-m%E1%BB%81m-c%E1%BA%A7n-thi%E1%BA%BFt)
    - [3.2. Triển](#32-tri%E1%BB%83n)
    - [3.3. ASP.NET Convention](#33-aspnet-convention)

<!-- /TOC -->

# 1. MVC là gì?
<a id="markdown-mvc-l%C3%A0-g%C3%AC%3F" name="mvc-l%C3%A0-g%C3%AC%3F"></a>

MVC là một kiến trúc phần mềm dùng để phát triển kha khá ứng dụng bạn đang dùng trên thị trường. Mô hình MVC bóc tách 3 tầng của ứng dụng thành 3 thành phần khác nhau, giúp việc phát triển dễ dàng hơn.

MVC là viết tắt của Model-View-Controller

> 3 thành phần này phải đi kèm với nhau, nhưng đối với người mới học, sẽ rất khó để hình dung ra chúng liên kết như thế nào. Học bất kỳ thành phần nào trước đều khó khăn khi không hiểu 2 thành phần kia. Vì vậy mình khuyên các bạn chỉ cần hình dung mỗi thành phần ra trong đầu, chứ đừng bắt tay ngay vào việc tìm hiểu liên kết giữa chúng.

## 1.1. Model
<a id="markdown-model" name="model"></a>

Model là cách mà bạn thể hiện data trong code của mình. Giả sử trong cơ sở dữ liệu của bạn có table Users, mỗi user đều có tên tuổi địa chỉ, thì model của bạn sẽ là

```cs
// A basic model
public class User
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Address { get; set; }
}
```

## 1.2. View
<a id="markdown-view" name="view"></a>

View chỉ đóng 1 vai trò duy nhất: Render ra giao diện cho người dùng. Textbox (ô để điền text), dropdown list (chọn giá trị từ 1 danh sách), checkbox (ô chọn có/không) là những thứ thường thấy trên View.

Ví dụ, để hiển thị 1 user ra màn hình, thì code asp.net như sau

```html
@model User
<div>
    @Model.Name
    @Model.Age
    @Model.Address
</div>
```

## 1.3. Controller
<a id="markdown-controller" name="controller"></a>

Controller là thứ quyết định View nào sẽ được hiển thị khi user nhập một URL. Nó cũng sẽ là thứ nhận data từ user khi họ điền một form, click một nút, vân vân và vân vân

# 2. Một ví dụ đơn giản
<a id="markdown-m%E1%BB%99t-v%C3%AD-d%E1%BB%A5-%C4%91%C6%A1n-gi%E1%BA%A3n" name="m%E1%BB%99t-v%C3%AD-d%E1%BB%A5-%C4%91%C6%A1n-gi%E1%BA%A3n"></a>

Vì ví dụ này được đưa ra để bạn hiểu mô hình MVC, nên bạn ko cần phải làm theo. Chỉ cần đọc tiếp thôi

## 2.1. Bài toán
<a id="markdown-b%C3%A0i-to%C3%A1n" name="b%C3%A0i-to%C3%A1n"></a>

Thế giới di động cần 1 cái website có thể hiện thị danh sách các điện thoại, thêm/xóa/sửa một điện thoại nào đó (bỏ qua tất cả các yêu cầu về bảo mật, đăng nhập, giao diện)

## 2.2. Phân tích
<a id="markdown-ph%C3%A2n-t%C3%ADch" name="ph%C3%A2n-t%C3%ADch"></a>

Đọc vào thấy ngay, ta cần một model cho điện thoại, 4 view cho 4 cái tính năng là `xem danh sách`, `thêm`, `xóa`, `sửa`. Vì cả 4 view này đều thao tác trên cái model `điện thoại`, nên ta chỉ cần 1 controller mà thôi

## 2.3. Triển khai
<a id="markdown-tri%E1%BB%83n-khai" name="tri%E1%BB%83n-khai"></a>

### 2.3.1. Tính năng xem danh sách
<a id="markdown-t%C3%ADnh-n%C4%83ng-xem-danh-s%C3%A1ch" name="t%C3%ADnh-n%C4%83ng-xem-danh-s%C3%A1ch"></a>

**Model**

```cs
public class MobilePhone
{
    // To identify which phones
    // Dùng để xác định cái điện thoại nào
    public int Id { get; set; }
 
    public string Name { get; set; }
}
```

**Controller**

```cs
public class MobilePhoneController
{
    public void List()
    {
        // Get all phones from database
        var allPhones = database.MobilePhones;
 
        // Return the View that render a list of phones
        return View(allPhones)
    }
}
```

**View**

```html
@model List<MobilePhone>
<div>
    <table>
        <!--Table headers-->
        <th>
            <td>Id</td>
            <td>Name</td>
        </th>
        <!--Table body-->
        <tbody>
            @foreach(var phone in Model)
            {
                <tr>
                    <td>@phone.Id</td>
                    <td>@phone.Name</td>
                </tr>
            }
        </tbody>
    </table>
</div>
```

ASP.NET tự động hiểu class `MobilePhoneController` sẽ có đường dẫn là `/MobilePhone`

Khi người dùng trỏ tới URL sau:

```s
yourdomain/MobilePhone/List
```

thì bằng một cách thần kỳ nào đó, asp.net đã gọi method `List` trong controller này, và chạy những đoạn code trong đó, trả về một cái bảng danh sách các điện thoại hiển thị lên cho người dùng

### 2.3.2. Tính năng thêm
<a id="markdown-t%C3%ADnh-n%C4%83ng-th%C3%AAm" name="t%C3%ADnh-n%C4%83ng-th%C3%AAm"></a>

Dùng lại model cũ, ta chỉ cần thêm code cho View và Controller

**Controller**

```cs
public class MobilePhoneController
{
    public void List()
    {
        // Get all phones from database
        // Lấy tất cả điện thoại từ database
        var allPhones = database.MobilePhones;
 
        // Return the View that render a list of phones
        // Trả về view chứa thông tin tất cả điện thoại
        return View(allPhones)
    }
 
    // Render the Add form
    // Hiển thị cái form Add
    public void Add()
    {
        return View();
    }
 
    // Recieved the new phone input by user
    // Nhận data được nhập vào từ người dùng
    [HttpPost]
    public void Add(MobilePhone newPhone)
    {
        var existedPhone = database.MobilePhones.Find(newPhone.Id)
 
        if(existedPhone != null)
        {
            // Phone is existed, return the Add View
            // Điện thoại với Id này đã tồn tại, trả về cái view Add
            return View(newPhone);
        }
 
        // Add new data to database
        database.MobilePhones.Add(newPhone);
 
        // Save the changes
        database.SaveChanges();
    }
}
```

> Tại sao lại có 2 method Add? Ở method đầu tiên, ASP.NET sẽ trả về cái form rỗng cho người dùng tự nhập vào giá trị. Method thứ 2 có chứa parameter là newPhone. Method có trách nhiệm nhận thông tin được post lên từ phía người dùng. ASP.NET đủ thông minh để có thể tự hiểu nó là object kiểu MobilePhone, và nó gọi là `Model Binding`. Ta sẽ tìm hiểu về chủ đề này sau.

**View**

```html
thêm file Add.cshtml
```

Đối với ASP.NET Core

```html
@model MobilePhone
 
<form asp-action="Add" asp-controller="MobilePhone">
    <label>Id</label>
    <input asp-for="Id"/>
    <label>Name</label>
    <input asp-for="Name"/>
</form>
```

Đối với ASP.NET MVC cũ

```html
@model MobilePhone
 
@using(Html.BeginForm("Add","MobilePhone",Method.Post))
{
    <label>Id</label>
    @Html.TextBoxFor(x => x.Id)
    <label>Name</label>
    @Html.TextBoxFor(x => x.Name)
}
```

# 3. Tự tạo project
<a id="markdown-t%E1%BB%B1-t%E1%BA%A1o-project" name="t%E1%BB%B1-t%E1%BA%A1o-project"></a>

Từ khúc này trở đi, bạn sẽ cần phải làm theo từng bước một

ASP.NET có kha khá phiên bản, `MVC1`, `MVC2`, `MVC3`, `MVC4`, và gần đây nhất là `MVC5` và `MVC Core`. Từ version 5 trở xuống là cách phát triển cũ, chỉ chạy được trên môi trường Windows, từ phiên bản `MVC Core` trở lên là cách phát triển mới, có thể chạy được trên `Linux`, `Windows` hoặc `MacOS`. Nếu đang học, thì mình khuyến khích nên học luôn từ `MVC Core` trở lên luôn cho nó hot

## 3.1. Phần mềm cần thiết
<a id="markdown-ph%E1%BA%A7n-m%E1%BB%81m-c%E1%BA%A7n-thi%E1%BA%BFt" name="ph%E1%BA%A7n-m%E1%BB%81m-c%E1%BA%A7n-thi%E1%BA%BFt"></a>

* [.NET Core SDK 2.0](https://www.microsoft.com/net/core) trở lên
* [Visual Studio Code](https://code.visualstudio.com/)
* VS Code [C# extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.csharp)

## 3.2. Triển
<a id="markdown-tri%E1%BB%83n" name="tri%E1%BB%83n"></a>

Mở VSCode lên, nhấn Ctrl + \` để hiện Terminal, hoặc làm như hình

![show termial](https://farm5.staticflickr.com/4710/39714628535_591c6163e7_o.png)

dùng các lệnh `cd` để trỏ tới thư mục mong muốn tạo project của bạn

hoặc

![open in vscode](https://farm5.staticflickr.com/4712/39898696364_c24a372543_o.png)

gõ

```s
dotnet new mvc
```

Bấm F5 > Chọn .NET Core

Nếu bạn được hỏi "Required assets to build and debug are missing from blah blah blah", thì bấm Yes nhé

![yes to build](https://farm5.staticflickr.com/4800/38800136200_57afdcf698_o.png)

Vậy là bạn đã tạo project MVC đầu tiên của mình, dùng ASP.NET Core rồi nhé. Bạn có thể mở class HomeController để hiểu rõ hơn về mô hình MVC mình vừa nói ở trên.

## 3.3. ASP.NET Convention
<a id="markdown-asp.net-convention" name="asp.net-convention"></a>

ở trên mình có nhắc tới MobilePhoneController, thì đường dẫn của nó sẽ là /MobilePhone, hay ở project bạn mới tạo, HomeController sẽ có đường dẫn là /Home .ASP.NET tự hiểu controller của bạn, và sẽ có đường dẫn tương ứng.

Mặc định, các method `Index` trong controller của bạn sẽ là method được gọi khi URL ko có bất kỳ cái gì đằng sau. Ví dụ như HomeController ở trên, nếu bạn chỉ nhập https://localhost:5000/Home/ thì method `Index` sẽ được gọi, View `Index.cshtml` sẽ được hiển thị.

Như vậy, bạn đã hiểu khá đủ về mô hình MVC, ở [phần tiếp theo](https://huntertran.com/2018/03/11/asp-net-for-beginer-part-2-connect-database-and-model-binding/) mình sẽ tiếp tục nói về kết nối database và những thứ bạn có thể làm với Model cho đúng _chuẩn_ nhé