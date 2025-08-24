---
title: C# string performance – Tips and Tricks
tags:
  - performance
id: '613'
categories:
  - - CSharp
date: 2016-07-11 00:38:34
---

Sau nhiều năm phát triển, C# trở thành một managed code vô cùng phổ biến và dễ sử dụng. Ai ai cũng có thể học C#, và điều này làm nảy sinh ra nhiều thói quen tai hại ảnh hưởng tới hiệu suất của chương trình viết bằng C#. Chỉ cần search một phát, sẽ ra hàng tá kết quả khác nhau, với các lời khuyên khác nhau, đi kèm với các đoạn code bench mark khác nhau, vô cùng rối ren khiến ta bối rối.

<!-- more -->

*   [Tại sao vậy?](#tại-sao-vậy)
*   [Các vấn đề](#các-vấn-đề)
    *   [Sai lầm 1: Cộng chuỗi](#sai-lầm-1-cộng-chuỗi)
    *   [Sai lầm 2: check null – so sánh chuỗi rỗng](#sai-lầm-2-check-null--so-sánh-chuỗi-rỗng)
*   [Kết luận](#kết-luận)

# 1. Tại sao vậy?

Rất đơn giản, là do các đoạn code bench mark này, mặc dù sử dụng cùng ngôn ngữ là C#, nhưng lại chạy trên các phiên bản .NET Framework khác nhau. Không cần đoán cũng biết rằng phiên bản càng về sau, compiler hoạt động càng hiệu quả, code bạn viết ra có hiệu suất càng cao. Thậm chí nó còn thông minh tới mức phát hiện ra các thói quen code xấu xí mà tự compile ra đoạn code hiệu quả nhất dùm bạn.

Tuy nhiên, nói chung lại thì có một số vấn đề "trường tồn cùng thời gian" mà bạn có thể sẽ bắt gặp khi code một ứng dụng C#

Bài viết này tập trung chủ yếu vào C# 6.0 đang được sử dụng cho các ứng dụng UWP của Windows 10

Project tham khảo có trong bài viết: [https://github.com/huntertran/00-Multi-Utilities/tree/master/09%20-%20Test%20Peformance/TestPerformance](https://github.com/huntertran/00-Multi-Utilities/tree/master/09%20-%20Test%20Peformance/TestPerformance)

# 2. Các vấn đề

String là một biến phức tạp của C#. Nếu như trong SQL, bạn khai báo varchar, nvarchar kèm theo một độ dài nhất định, thì trong C#, string có thể có độ dài cực lớn. Do đó, compiler sẽ rất là vất vả khi xử lý các biến string này.

## 2.1. Sai lầm 1: Cộng chuỗi

```
string msg = "Hello, ";
msg += "Tuan Tran";
msg += ". Today is ";
msg += System.DateTime.Now.ToString();
```

Đoạn code trên quá bình thường, bình thường như cân đường hộp sữa. Tuy nhiên, đây sẽ là những gì mà compiler nhìn thấy

```
string msg = "Hello, ";

string tmp1 = new String( msg + "Tuan Tran" );

string msg = tmp1; // "Hello " is garbage.

string tmp2 = new String( msg + ". Today is " );

msg = tmp2; // "Hello Tuan Tran" is garbage.

string tmp3 = new String( msg + DateTime.Now.ToString( ) );

msg = tmp3; // "Hello Tuan Tran. Today is " is garbage.
```

### 2.1.1. Giải quyết: string.Concat, StringBuilder và string.Format

Về tổng quan, `StringBuilder` luôn là cái chạy nhay nhất.

```
StringBuilder s = new StringBuilder();
s.Append("Tuan Tran"); s.Append(" Today is ");
blah blah blah
```

Tuy nhiên, đối với C# 6.0 như đã đề cập bên trên, compiler của nó đủ thông minh để compile ra một đoạn native code hiệu quả nhất.

Như vậy, nói tóm lại, bạn có thể sử dụng `string.Concat` để cộng các chuỗi đơn giản, `StringBuilder` để xây dựng các chuỗi bự hơn, và `string.Format` khi bạn muốn cộng các chuỗi từ các kiểu dữ liệu khác, hoặc muốn format nó theo một kiểu nào đó.

## 2.2. Sai lầm 2: check null – so sánh chuỗi rỗng

Quá đơn giản phải Không?

```
string s = "";

if(s == null || s == "")
{
    //do something here; 
}
```

Có một cách khác hiện đại hơn

```
string s = "";

if(string.IsNullOrEmpty(s))
{
    //do something here;
}
```

Và nếu bạn muốn so sánh 2 chuỗi với nhau, hãy sử dụng string.Equal

## 2.3. Kết luận

Hãy bỏ thời gian tìm hiểu các method được viết sẵn cho `string`, và sử dụng chúng trong các tình huống phù hợp. Microsof đã viết sẵn cho bạn, và họ cũng đã tối ưu hiệu suất cho các method đó, tại sao lại Không xài chúng chứ.

Sau đây mà tài liệu MSDN về string:

[https://docs.microsoft.com/en-us/dotnet/api/system.string?view=netcore-2.2](https://docs.microsoft.com/en-us/dotnet/api/system.string?view=netcore-2.2)