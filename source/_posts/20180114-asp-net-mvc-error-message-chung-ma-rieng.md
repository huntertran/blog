---
title: '[asp.net mvc] Error Message - chung mà riêng'
tags:
  - error message
  - resource
id: '935'
categories:
  - - CSharp
    - ASP.NET
date: 2018-01-14 05:00:42
---

Bạn có đang dùng Entity Framework với ASP.NET MVC, cùng với đó là client-validation?

Đối với mỗi \`\`\`DataAnnotation\`\` attribute, bạn lại có 1 câu thông báo lỗi khác nhau, và bạn nhét tất cả chúng vào Resource?

Có một số cách giúp bạn khắc phục một vài nhược điểm trên ;)

<!-- more -->

<!-- TOC -->

- [1. Generic Customized Error Message](#1-generic-customized-error-message)
- [2. Error Message Localization](#2-error-message-localization)
    - [2.1. Nếu bạn có Resharper](#21-n%E1%BA%BFu-b%E1%BA%A1n-c%C3%B3-resharper)
    - [2.2. Nếu bạn muốn dùng hàng miễn phí](#22-n%E1%BA%BFu-b%E1%BA%A1n-mu%E1%BB%91n-d%C3%B9ng-h%C3%A0ng-mi%E1%BB%85n-ph%C3%AD)

<!-- /TOC -->

# 1. Generic Customized Error Message
<a id="markdown-generic-customized-error-message" name="generic-customized-error-message"></a>

Generic tức là chung chung. Dùng chung 1 câu thông báo cho nhiều property cùng loại, chỉ thay đổi các yếu tố cần thiết

Ví dụ:
```
Tên phải chứa ít hơn 15 ký tự 
Địa chỉ phải chứa ít hơn 150 ký tự
```

Trong ví dụ trên, phần `tên`, `địa chỉ`, `15`, `150` là những tham số ta phải thay đổi cho câu thông báo. Vậy làm bằng cách nào?

Mò vào source code của từng loại DataAnnotation, chúng ta sẽ thấy 1 số điều thú vị

> Source code cho DataAnnotation [https://github.com/Microsoft/referencesource/tree/master/System.ComponentModel.DataAnnotations/DataAnnotations](https://github.com/Microsoft/referencesource/tree/master/System.ComponentModel.DataAnnotations/DataAnnotations)

Tất cả các Attribute đều override lại method FormatErrorMessage. Mò vào từng implementation của các attribute, ta sẽ biết thứ tự các biến tham số của error message.

| Attribute | Source code | Giải thích |
|-|-|-|
| StringLength | String.Format(CultureInfo.CurrentCulture,<br>              errorMessage,<br>              name,<br>              this.MaximumLength,<br>              this.MinimumLength);<br>return; | {0} = name,<br>{1} = MaximumLength,<br>{2} = MinimumLength |
| Compare | String.Format(CultureInfo.CurrentCulture,<br>              ErrorMessageString,<br>              name,<br>              OtherPropertyDisplayName ?? OtherProperty);<br>return; | {0} = name,<br>{1} = OtherPropertyDisplayName / OtherProperty |
| MinLength | string.Format(CultureInfo.CurrentCulture,<br>              ErrorMessageString,<br>              name,<br>              Length);<br>return; | {0} = name,<br>{1} = Length |

Như vậy, thay vì ta phải viết thẳng từng câu error message, ta chỉ cần dùng string.Format với thứ tự chính xác của các tham số

Ví dụ với trường hợp StringLength

```cs
[StringLength(70, ErrorMessage = "{0} phải chứa ít hơn {1} ký tự")]
public string Name { get; set; }
```

# 2. Error Message Localization
<a id="markdown-error-message-localization" name="error-message-localization"></a>

Thực ra thì chiêu sau đây không những giúp bạn localize string của Error Message, mà bất kỳ đoạn string nào bạn muốn

> Bạn phải tạo một file Resource trong project (.resx) để sử dụng
> 
> Thông tin thêm ở đây: [https://docs.microsoft.com/en-us/aspnet/core/fundamentals/localization](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/localization)

## 2.1. Nếu bạn có Resharper
<a id="markdown-n%E1%BA%BFu-b%E1%BA%A1n-c%C3%B3-resharper" name="n%E1%BA%BFu-b%E1%BA%A1n-c%C3%B3-resharper"></a>

Resharper là một sản phẩm hỗ trợ dev kha khá của JetBrains

Đặt con trỏ tại một string bất kỳ -> Resharper -> Refactor -> Move...

![resharper move to resource](https://farm5.staticflickr.com/4750/39647359142_98791bd35d_o.png)

Resharper tính phí bản quyền

## 2.2. Nếu bạn muốn dùng hàng miễn phí
<a id="markdown-n%E1%BA%BFu-b%E1%BA%A1n-mu%E1%BB%91n-d%C3%B9ng-h%C3%A0ng-mi%E1%BB%85n-ph%C3%AD" name="n%E1%BA%BFu-b%E1%BA%A1n-mu%E1%BB%91n-d%C3%B9ng-h%C3%A0ng-mi%E1%BB%85n-ph%C3%AD"></a>

Visual Studio có một extension rất hay là [RestXManager](https://github.com/tom-englert/ResXResourceManager). Chức năng của nó thì tương tự như Resharper, thậm chí còn nhỉnh hơn một tí
* Open source
* Active Development
* Hỗ trợ dịch text

Bạn có thể tìm và tải trực tiếp trong Visual Studio: `Tools &gt; Extensions and Updates &gt; Online &gt; search "ResXManager"`

![ResXManager](https://farm5.staticflickr.com/4616/38972346614_45410a6157_o.png)

hoặc

tại link sau: [https://marketplace.visualstudio.com/items?itemName=TomEnglert.ResXManager](https://marketplace.visualstudio.com/items?itemName=TomEnglert.ResXManager)

Sau đó, tương tự như Resharper, đặt con trỏ tại một string bất kỳ > Chuột phải > Move to Resource

![Move to Resource](https://farm5.staticflickr.com/4704/38783776745_f94606e40c_o.png)

Còn một số chiêu khác với những loại DataAnnotation khác nữa bạn nhé