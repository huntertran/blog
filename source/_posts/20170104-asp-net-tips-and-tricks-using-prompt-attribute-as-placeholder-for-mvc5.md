---
title: '[ASP.NET Tips and Tricks] Using Prompt Attribute as Placeholder for MVC5'
tags:
  - htmlhelper
  - placeholder
  - prompt
id: '657'
categories:
  - - CSharp
    - ASP.NET
  - - Others
date: 2017-01-04 08:30:57
---

Khi bạn làm một cái form trong ASP.NET MVC5, chắc bạn sẽ dùng HtmlHelpers chứ nhỉ.

Vậy làm thế nào để hiển thị placeholder, sử dụng thuộc tính prompt?

![31716564800_af2c594490_o](https://cuoilennaocacban2.files.wordpress.com/2017/01/31716564800_af2c594490_o.png)

<!-- more -->

# Chuẩn bị trong ViewModel (hoặc Model)

Các properties trong ViewModel sẽ có default get set như sau

```csharp
public int DistrictId { get; set; }
```

Bạn sẽ phải thêm các DisplayAttribute cho Property này như sau

```csharp
[Display(Name = "Quận huyện", Prompt = "Gõ để chọn từ danh sách")]
public int DistrictId { get; set; }
```

DisplayAttribute có chức năng dựng ra các thuộc tính HTML cần thiết để hiển thị ra web khi bạn dùng HtmlHelpers để tạo các tag input

Thuộc tính Name sẽ được dùng cho label của input, thuộc tính Prompt sẽ được dùng cho placeholder của input

# Code cho C#

Placeholder không phải là một HtmlHelper có sẵn, nên bạn phải tự tạo ra nó

```csharp
public static class Extensions
{
    public static MvcHtmlString DisplayPlaceHolderFor<TModel, TValue>(
                                                                      this HtmlHelper html,
                                                                      Expression<Func<TModel, TValue>> expression)
    {
        var result = ModelMetadata.FromLambdaExpression(expression, html.ViewData).Watermark;
        return new MvcHtmlString(result);
    }
}
```

Expression sẽ là câu truy vấn bạn truyền vô cho cái extension này

# Code cho Razor

```csharp
//Hiển thị label
@Html.LabelFor(x => x.DistrictId)
//Hiển thị Textbox và Placeholder
@Html.TextBoxFor(x => x. DistrictId,
                 new {@class = "form-control",
                 placeholder = Html.DisplayPlaceHolderFor(x => x.DistrictId)})

```

Thế là xong :D