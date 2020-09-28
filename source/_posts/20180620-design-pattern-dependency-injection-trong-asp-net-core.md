---
title: '[Design Pattern] - Dependency Injection trong ASP.NET Core'
tags:
  - ASP.NET
  - dependency injection
id: '1041'
categories:
  - - Design Pattern
date: 2018-06-20 08:30:55
---

Dependency Injection là một kỹ thuật vô cùng thông dụng để _nới lỏng_ các objects và class phụ thuộc vào chúng. Nghe khó hiểu quá phải ko các bạn?

Bài viết này sẽ mô tả kỹ thuật này, cho bạn một cái nhìn tổng quan (hy vọng là khách quan) về DI
<!-- more -->
*   [1. Vấn đề](#1-vấn-đề)
*   [2. Lợi ích](#2-lợi-ích)
*   [3. Back to code](#3-back-to-code)
    *   [3.1. Interface](#31-interface)
    *   [3.2. Implementation](#32-implementation)
*   [4. Register](#4-register)
    *   [4.1. Lifetime](#41-lifetime)
    *   [4.2. Contructor Injection](#42-contructor-injection)
    *   [4.3. Action Injection](#43-action-injection)
    *   [4.4. Service trong Service](#44-service-trong-service)

# 1. Vấn đề

Hãy tưởng tượng bạn muốn uống coca, nhà ko còn chai coca nào Bạn phải ra Circle K, đi lòng vòng trong cửa hàng để kiếm 1 chai coca, trả tiền, đi về

*   Bạn có thể quên ko trả tiền
*   Bạn có thể ko tìm thấy Circle K nào gần cả
*   Bạn có thể ko tìm thấy chai coca nào trong circle k cả
*   Bạn có thể lấy nhầm 1 chai xá xị chương dương thay vì coca

Với Dependency Injection, mọi việc sẽ khác đi

Bạn đưa tiền cho 1 thằng nhóc có nhiệm vụ chuyên đi mua nước ngọt cho khu xóm 5 phút sau, nó xuất hiện với chai coca của bạn

Một người khác trong cùng khu xóm cũng có nhu cần gần giống bạn, nhưng họ muốn uống pepsi

Thay vì cũng phải đi ra cửa hàng và tự mua pepsi và gặp các vấn đề như bạn gặp, họ cũng gọi thằng nhóc đó lại, và 5 phút sau, chai pepsi ướp lạnh ở trong tay họ. Thằng nhóc đó chính là 1 **_Service_**, và bạn phụ thuộc vô thằng nhóc đó để có nước ngọt uống

# 2. Lợi ích

Quay trở lại với ví dụ trên, lợi ích của bạn khi dùng **_Service_** mua nước ngọt của thằng nhóc là gì?

*   Bạn ko cần quan tâm thằng nhóc đó nó làm gì để có nước ngọt cho bạn
*   Bạn có thể yêu cầu nhiều loại nước ngọt khác nhau mà ko cần biết hình dạng hay chỗ bán

# 3. Back to code

Quay trở lại với code, bạn sẽ implement DI như thế nào?

## 3.1. Interface

```csharp
public interface IDrinkBuyer { void BuyDrink(string name); }
```

Khi thằng nhóc mua nước ngọt ở bên trên đã già, nó sẽ muốn truyền lại nhiệm vụ mua nước ngọt cho 1 thằng nhóc khác, và cứ thể. Mọi thằng nhóc mua nước ngọt trong xóm đều sẽ có 1 phương thức cơ bản là `BuyDrink` chấp nhận 1 param là tên của loại nước cần mua Bạn đóng vai trò là `WebApplication`, sẽ gọi phương thức này để có nước ngọt uống

## 3.2. Implementation

Người quản lý của mấy thằng nhóc mua nước ngọt này sẽ phân nhiệm vụ cho từng thằng nhóc 1

*   Nhóc A mua ở Circle K
*   Nhóc B mua ở Vinmart

Và họ sẽ implement như sau 
```csharp
public class CircleKDrinkBuyer: IDrinkBuyer 
{
  public void BuyDrink(string name) 
  {
    // Go to circle k 
    // Find the -name- drink 
    // Buy it and deliver 
  }
}

public class VinmartDrinkBuyer: IDrinkBuyer 
{
  public void BuyDrink(string name) 
  {
    // Go to Vinmart 
    // Find the -name- drink 
    // Buy it and deliver 
  }
}
```

Thế là xong Khi nhà bạn gần Vinmart, người quản lý sẽ cử thằng nhóc B - VinmartDrinkBuyer canh trước cổng nhà bạn. Bất kể khi nào bạn có nhu cầu mua nước ngọt, bạn sẽ gọi nó. Bạn đâu có biết là thằng nhóc B đó nó chỉ biết mua nước ngọt ở Vinmart thôi. Bạn chỉ quan tâm là bạn gọi nó, và bạn có nước ngọt uống

# 4. Register

Như vậy, khai báo như thế nào trong ứng dụng của bạn? khi tạo mới một ứng dụng asp.net core 2, đã có sẵn 1 số phương thức giúp bạn bắt đầu ngay và luôn ![method in startup.cs](https://farm2.staticflickr.com/1750/42864104992_c6bcdb3276_o.png) bằng cách thêm vào dòng code sau `services.AddScoped();` bạn đã khai báo cho tất cả các class có dùng phương thức `BuyDrink` sẽ mua nước ngọt ở CircleK

## 4.1. Lifetime

`AddScoped` dùng để chỉ định _thời gian sống_ của service này, có 3 loại:

*   Transient: mỗi lần gọi tới nó sẽ là 1 biến thể mới hoàn toàn. Cái này chỉ phù hợp cho các loại service siu nhẹ nhàng và ko có lưu trữ trạng thái
*   Scoped: Trong cùng 1 request, nó sẽ chỉ được tạo 1 lần duy nhất
*   Singleton: Nó sẽ được tạo lần đầu tiên khi được gọi, và sẽ sống quài cho tới khi app bạn chết

## 4.2. Contructor Injection

Sau khi đã register service của bạn với 1 lifetime phù hợp, việc tiếp theo chính là _tiêm - inject_ nó vào chỗ cần dùng (thường sẽ là controller) ASP.NET Core 2 hỗ trợ bạn inject service vào controller thông qua contructor của controller đó ![inject to controller](https://farm2.staticflickr.com/1753/42012713695_56fcb2b4a5_o.png)

## 4.3. Action Injection

Đôi khi bạn chỉ cần cái service này trong 1 action cụ thể nào đó của controller thôi, thì sẽ có cách hơi khác 

```csharp
public IActionResult About([FromServices] IDrinkBuyer drinkBuyer) 
{
  drinkBuyer.BuyDrink("coca");
  return View();
}
```

## 4.4. Service trong Service

Nested services, service con, vân vân và mây mây

Đôi khi bạn cần phải có 1 service con để service cha chạy được, thì inject như nào

Rất đơn giản, cũng dùng contructor injection thôi

Giả sử Service `DrinkBuyer` cần có service `Trasport` để chạy 

```csharp
public interface ITransport
{
  void Transport();
}
public class BikeTransport: ITransport
{
  public void Transport() 
  {
    // transport by bike 
  }
}

public class CarTransport: ITransport
{
  public void Transport()
  {
    // transport by car
  }
}
```

đầu tiên đăng ký nó trong `Startup.cs` `services.AddScoped();`

sau đó bạn inject nó vào `DrinkBuyer` như sau

```csharp
public class CircleKDrinkBuyer: IDrinkBuyer 
{
  private readonly ITransport _transport;
  
  public CircleKDrinkBuyer(ITransport transport) 
  {
      _transport = transport;
  }
  
  public void BuyDrink(string name) {
    // Go to circle k 
    // Find the -name- drink 
    // Buy it 
    // Deliver 
    _transport.Transport();
  }
}
```

thế nà xong :D
