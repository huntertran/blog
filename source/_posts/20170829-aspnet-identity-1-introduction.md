---
title: '[ASP.NET Identity] - 1 - Introduction'
tags:
  - identity
id: '894'
categories:
  - - CSharp
    - ASP.NET
date: 2017-08-29 22:54:40
---

Một trong những thứ bí ẩn nhất khi làm web bằng ASP.NET là hệ thống ASP.NET Identity cũng do Microsoft phát triển. Với khá nhiều hardcode, kèm với nhiều yêu cầu phức tạp về users và roles, Identity phình to tới mức khó tin, và là một cục xương khó nhằn cho bất kỳ ai mới học ASP.NET
<!-- more -->
*   [1. Quá trình phát triển](#1-quá-trình-phát-triển)
    
    *   [1.1. Asp.net Membership](#11-aspnet-membership)
    *   [1.2. Asp.net Simple Membership](#12-aspnet-simple-membership)
    *   [1.3. ASP.NET Universal Providers](#13-aspnet-universal-providers)
    *   [1.4. Asp.net Identity](#14-aspnet-identity)
*   [2. Bắt đầu với ASP.NET Identity](#2-bắt-đầu-với-aspnet-identity)
*   [3. Break-down](#3-break-down)
    
    *   [3.1. Database](#31-database)
        
        *   [3.1.1. Kết nối tới database](#311-kết-nối-tới-database)
        *   [3.1.2. Code first](#312-code-first)
        *   [3.1.3. Cấu trúc](#313-cấu-trúc)
    *   [3.2. Kiến trúc và các khái niệm](#32-kiến-trúc-và-các-khái-niệm)
        
        *   [3.2.1. AspNetUsers](#321-aspnetusers)
        *   [3.2.2. AspNetUserLogins](#322-aspnetuserlogins)
        *   [3.2.3. AspNetUserClaims](#323-aspnetuserclaims)

# 1. Quá trình phát triển

## 1.1. Asp.net Membership

Hồi năm 2k hồi đó, có nhu cầu rõ rệt về websites phải có đăng nhập, đăng ký thành viên đồ các kiểu. MS thấy vậy nhảy vào và ASP.NET Membership ra đời

Version này cực kỳ hạn chế + DB được thiết kế cho SQL Server, và ko thể thay đổi + Tuy các provider được thiết kể để có thể thay đổi, nhưng mà hàng loạt hardcode + tư duy chắc chắn phải dùng SQL server của dev khiến việc thay đổi này vô cùng cực khổ + Ko xài được OWIN

## 1.2. Asp.net Simple Membership

Sang tới 2k10, lúc này WebMatrix đang thịnh, MS cũng cho ra liền một bản rút gọn / nâng cấp của Membership, nhưng tóm lại vẫn quá nhiều vấn đề

## 1.3. ASP.NET Universal Providers

Tới hồi Azure ra đời, MS vẫn chưa chịu từ bỏ nền tảng Membership, cho ra mắt phiên bản Universal Providers (đặt tên sang choảnh)

Vì xài chung nền tảng kiến trúc, nên các lỗi lầm từ trước đó vẫn còn y nguyên

## 1.4. Asp.net Identity

Sau quá nhiều feedback, asp.net team cho ra đời version này, khắc phục mấy cái hạn chế trên kia.

*   Có thể xài chung cho nhiều Framework (MVC, Forms, Web Pages, Web API, SingalR)
*   Dễ gắn thêm field vào user profile
*   Có thể gắn các Storage khác vô ngoài SQL Server (bớt đau khổ hơn tí)
*   Unit test được
*   Dùng claims (sẽ giải thích sau)
*   OWIN tốt
*   Support Azure Active Directory
*   Cài được bằng Nuget

Bắt đầu nhảy vô nhé

# 2. Bắt đầu với ASP.NET Identity

> Xem code ở đây: [ASP.NET Identity 2 clone on GitHub](https://github.com/cuoilennaocacban/ASP.NETIdentty2)

Để hiểu rõ hơn, bạn có thể tạo một Sample Project bằng ASP.NET, chọn Identity là Individual nhé File > New > Project...

![New Project](https://farm5.staticflickr.com/4408/36631193821_b2fea13a5c_o.png)

Ngay khi tạo xong, bạn có thể nhấn chạy luôn

![Run Project](https://farm5.staticflickr.com/4402/35961354023_95481c7d6a_o.png)

# 3. Break-down

Bây giờ mình sẽ tìm hiểu từng phần một của Identity nhé

## 3.1. Database

### 3.1.1. Kết nối tới database

Mặc định, Identity dùng connection string có tên "DefaultConnection" Mở `Models/IdentityModels`

\[code lang=csharp\] public class ApplicationDbContext : IdentityDbContext<ApplicationUser> { public ApplicationDbContext() : base("DefaultConnection", throwIfV1Schema: false) { }

public static ApplicationDbContext Create() { return new ApplicationDbContext(); } } \[/code\]

Mở Web.config, kiếm `DefaultConnection`, bạn sẽ thấy connection string của nó nối tới Database

\[code lang=xml\] <connectionStrings> <add name="DefaultConnection" connectionString="Data Source=(LocalDb)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\\aspnet-LearnIdentity2-20170824112720.mdf;Initial Catalog=aspnet-LearnIdentity2-20170824112720;Integrated Security=True" providerName="System.Data.SqlClient" /> </connectionStrings> \[/code\]

Như vậy, Identity, tùy theo framework bạn sử dụng, sẽ dùng LocalDb hoặc SQL Server Dùng SQL Server Management Studio connect tới db này, bạn sẽ thấy nó đang nằm chình ình trong đó

![Database trong LocalDb](https://farm5.staticflickr.com/4337/36631439311_5da8d15c1a_o.png)

Vậy bạn có tự hỏi làm sao mà mới chỉ chạy project thôi mà Identity đã tạo được database?

### 3.1.2. Code first

Để trả lời cho câu hỏi đó, từ EF4, MS đã giới thiệu một hướng tiếp cận hoàn toàn mới gọi là Code first, bên cạnh hướng tiếp cận truyền thống là Database First như xưa nay. Với hướng tiếp cận này, Dev chỉ cần tập trung vào code của mình, db sẽ do EF tạo ra ứng với code của dev

Một flow cơ bản là Dev viết các model và class -> Nhấn F5 -> EF tạo / map database -> Ứng dụng khởi chạy với datbase được tạo / map

### 3.1.3. Cấu trúc

Identity tạo ra 5 bảng trong DB, và mỗi bảng đều liên hệ với nhau

![Db Structure](https://farm5.staticflickr.com/4381/35961946823_1e233cd9ef_o.png)

Tất cả các trường Id đều dùng nvarchar(128), giá trị lưu trữ là code GUID

## 3.2. Kiến trúc và các khái niệm

### 3.2.1. AspNetUsers

**PasswordHash**

Identity ko lưu trữ trực tiếp password theo dạng plain text (đề phòng trường hợp Db của bạn bị hack, hacker cũng ko biết password) `ASP.NETIdentty2/src/Microsoft.AspNet.Identity.Core/Crypto.cs`

Identity Hash password của bạn dựa trên 1 chuỗi salt 128 bit. Nói chung về thuật toán mã hóa bạn cũng ko cần phải quan tâm :D

Trong Identity Core, thuật toán này có thay đổi, nên việc convert từ Identity 2 lên 3 sẽ cần configure lại đôi chút

**SecurityStamp**

Về cơ bản, SecurityStamp được dùng để xác thực một request nào đó. Giả sử như bạn đổi pass ở máy này, nhưng trên máy khác vẫn lưu cookie, thì ngay khi đổi pass xong, SecurityStamp thay đổi, cookie trên tất cả các máy khác sẽ mất hiệu lực

### 3.2.2. AspNetUserLogins

Bảng này chịu trách nhiệm cho việc login bằng account của các dịch vụ thứ 3 như Google, Facebook, Twitter,...

**LoginProvider**

Là tên của Service được dùng để login (ví dụ "Facebook", "Google")

**ProviderKey**

Là một key ko trùng lặp do service cung cấp cho bạn, key này gắn liền với tài khoản của bạn tại service đó

Cả 3 field này kết hợp tạo thành khóa chính. Tức là 1 user có thể đăng nhập bằng nhiều dịch vụ khác nhau

Bảng này cho phép Identity dùng OWIN

### 3.2.3. AspNetUserClaims

`claim` là một hành vi mô mà một chủ thể nào đó tuyên bố điều gì đó về chính nó hoặc về các chủ thể khác.

> Ví dụ: User A claim rằng A có quyền xem hình

**`Claim-base Security`** Identity hỗ trợ 2 kiểu Security là Role-base Security và Claim-base Security. Về role-base security sẽ nói trong đoạn tiếp theo của bài blog này

**Một ví dụ thực tiễn**

Claim-base Security có mặt xung quanh chúng ta. Một ví dụ thực tiễn là khi bạn đi máy bay. Khi đi, bạn phải mang theo CMND/Passport + vé máy bay:

1.  `Authentication`: Nhân viên kiểm soát sẽ kiểm tra khuôn mặt của bạn với CMND/Passport
2.  `Authorization`: Nhân viên kiểm tra vé của bạn xem có đúng là vé thiệt ko, ngồi ở hàng nào, ghế nào, sau cùng xuất ra cho bạn một tấm boarding passNhư vậy, tấm boarding pass này chứa khá nhiều thông tin: số chuyến bay, ghế ngồi, tên hành khách, và nhiều khi còn có thêm một dải băng từ màu đen ở mặt sau chứa mã số đã được mã hóa của tấm boarding pass đó nhằm chứng tỏ nó là một tấm boarding pass thiệt, ko phải đồ giả. Tấm boarding pass này chính là 1 tập hợp các `claim`, được xuất ra bởi một `issuer`. Khi bạn tới sân bay, trình các `claim` này ra, nhân viên sẽ đơn giản đối chiếu các claim này với database và cho bạn lên máy bay. Cũng cần lưu ý là tấm boarding pass này có thể được xuất bởi nhiều nguồn: trực tiếp tại quầy làm thủ tục, hay đại lý vé máy bay. Những nguồn này gọi là `issuer` Trong phần mềm, tập hợp các claim này gọi là `security token`. Mỗi security token được ký bởi một `issuer` đã tạo ra nó. Một ứng dụng có `claim-base security` yêu cầu user phải xác thực tài khoản của mình, và tùy vào các claim mà họ có để cấp các quyền cần thiết.

**Role-base Security**

Ngoài claim, Identity còn cung cấp cho bạn một Role-base Security nữa

Role thì dễ hiểu rồi. Một user có thể được thêm vào nhiều role, và mỗi role sẽ cho user đó một số quyền hạn nhất định

Trong bài viết tiếp theo, chúng ta sẽ cùng đi vào tìm hiểu về code của ASP.NET Identity nhé

> Xem code ở đây: [ASP.NET Identity 2 clone on GitHub](https://github.com/cuoilennaocacban/ASP.NETIdentty2)