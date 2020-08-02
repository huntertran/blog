---
title: Misconception with async and await in C#
tags: []
id: '1128'
categories:
  - - Others
---

## 1\. Giới thiệu

Asynchronous programming, đúng như tên gọi của nó, chỉ mang tính chất 'Bất đồng bộ' mà thôi. Trước kia, trong cùng một method, các function được gọi và thực thi lần lượt theo thứ tự trong code thì với async, nó có thể thực thi các function bất đồng bộ với nhau, không nhất thiết phải theo thứ tự được ghi trong code.

Hãy tưởng tượng cả ứng dụng của bạn là một quán cafe, thì một method chính là 1 khách uống cafe.

*   Synchronous programming sẽ là bạn order 1 ly cafe, trả tiền, rồi đứng tại chỗ chờ nhân viên pha chế để lấy luôn.

*   Asynchronous programming sẽ giống như việc bạn vào order một ly Cappuccino , trả tiền, xong ra ghế ngồi đọc báo chờ nhân viên mang ra cho bạn vậy.

## 2\. Các lầm tưởng

### 2.1. Nó không phải là multi-threading

Async không phải là muti-threading như nhiều người lầm tưởng. Trong một số loại ứng dụng (như UWP, hay WPF), các async methods sẽ được chạy ở một thread khác so với UI thread, nhưng nó vẫn ko phải là multi-thread.

### 2.2. Nó không chạy song song

Trên cùng một thread, các tasks sẽ không chạy song song với nhau, mà nó chỉ tuần tự thực hiện. Giống như cái ví dụ mua cafe ở trên, bạn không thể nào vừa order cafe vừa ngồi ghế đọc báo được.

## 3\. Chỉ có 1 số function mới nên dùng async/await

Microsoft có một danh sách các API có hỗ trợ async/await như sau

**Application Area**

**.NET type with async methods**

**Windows Runtime type with async methods**

Web access

[HttpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpclient)

[SyndicationClient](https://docs.microsoft.com/en-us/uwp/api/windows.web.syndication.syndicationclient)

Working with files

[StreamWriter](https://docs.microsoft.com/en-us/dotnet/api/system.io.streamwriter)  
[StreamReader](https://docs.microsoft.com/en-us/dotnet/api/system.io.streamreader)  
[XmlReader](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xmlreader)

[StorageFile](https://docs.microsoft.com/en-us/uwp/api/windows.storage.storagefile)

Working with Images

[MediaCapture](https://docs.microsoft.com/en-us/uwp/api/windows.media.capture.mediacapture)  
[BitmapEncoder](https://docs.microsoft.com/en-us/uwp/api/windows.graphics.imaging.bitmapencoder)  
[BitmapDecoder](https://docs.microsoft.com/en-us/uwp/api/windows.graphics.imaging.bitmapdecoder)

WCF Programming

[Synchronous and Asynchronous operations](https://docs.microsoft.com/en-us/dotnet/framework/wcf/synchronous-and-asynchronous-operations)

Nhìn chung, các function mà đẩy việc xử lý ra khỏi ứng dụng và xử lý nó trên một thành phần khác (hệ điều hành, resource web, SQL Server, vân vân và mây mây) đều hưởng lợi về responsiveness khi dùng async và await

## 4\. Một ví dụ