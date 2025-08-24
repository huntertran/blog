---
title: '[ASP.NET Core 2.0] Custom Tag Helper'
tags:
  - .net core
  - input
  - label
  - tag helper
id: '928'
categories:
  - - CSharp
    - ASP.NET
date: 2018-01-12 11:27:40
---

ASP.NET Core giới thiệu một cách vô cùng tự nhiên để xây dựng các thẻ `input`, `label` và một số thẻ khác với từ khóa `asp-for`, chúng được gọi là _`tag helper`_

Bạn cũng có thể tạo ra các `tag helper` của riêng mình để render ra các tag mong muốn

<!-- more -->

<!-- TOC -->

- [1. Một số tag helper](#1-m%E1%BB%99t-s%E1%BB%91-tag-helper)
- [2. Vấn đề với label tag helper](#2-v%E1%BA%A5n-%C4%91%E1%BB%81-v%E1%BB%9Bi-label-tag-helper)
- [3. Customize Label tag helper](#3-customize-label-tag-helper)
    - [3.1. Code](#31-code)
    - [3.2. Khai báo](#32-khai-b%C3%A1o)
- [4. Sử dụng](#4-s%E1%BB%AD-d%E1%BB%A5ng)

<!-- /TOC -->

# 1. Một số tag helper
<a id="markdown-m%E1%BB%99t-s%E1%BB%91-tag-helper" name="m%E1%BB%99t-s%E1%BB%91-tag-helper"></a>

ASP.NET MVC5

ASP.NET Core

| ASP.NET MVC5 | ASP.NET Core |
|-|-|
| `@Html.TextBoxFor()` | `<input asp-for=""/>` |
| `@Html.DropDownListFor()` | `<select asp-for="" asp-items=""/>` |
| `@Html.LabelFor()` | `<label asp-for=""></label>` |
| `@Html.ValidationMessageFor()` | `<anytag asp-validation-for=""></anytag>` |

# 2. Vấn đề với label tag helper
<a id="markdown-v%E1%BA%A5n-%C4%91%E1%BB%81-v%E1%BB%9Bi-label-tag-helper" name="v%E1%BA%A5n-%C4%91%E1%BB%81-v%E1%BB%9Bi-label-tag-helper"></a>

`label` là cái tag mà bạn sẽ customize hơi nhiều trong ứng dụng asp.net core của mình. Lý do là vì bạn muốn nó có thêm một dấu `*` màu đỏ đối với các input yêu cầu bắt buộc, bạn cũng muốn nó có thêm `(500 ký tự)` khi ô input chỉ cho phép nhập 500 ký tự.

Tất nhiên, tất cả những cái đó đều có thể thêm vào dễ dàng bằng cách ... add tay

ASP.NET MVC, và sau này là ASP.NET CORE, cho phép bạn xây dựng `model` với các `DataAnnotation` nhằm khai báo cho cơ sở dữ liệu biết các giới hạn hoặc định nghĩa của một column trên database, đồng thời giúp bạn validate input field của nó ở client-side code

```cs
[Required]
[Display(Name = "User name")]
[StringLenght(15)]
public string Username { get; set; }
```

Tuy nhiên, khi tạo input field cho property `username` này, bạn vẫn phải tự tạo tay các dấu `*` và dòng chữ `tối đa 15 ký tự` kia

```html
<label asp-for="Username"></label>
<input asp-for="Username"/>
<span asp-validation-for="Username"></span>
```

đoạn code trên sẽ generate ra các dòng html sau

```html
<label for="Username">User name</label>
....các dòng khác...
```

# 3. Customize Label tag helper
<a id="markdown-customize-label-tag-helper" name="customize-label-tag-helper"></a>

Chúng ta sẽ tạo ra một custom tag helper với tên là `requiredlabel`

## 3.1. Code
<a id="markdown-code" name="code"></a>

```cs
namespace YourNamespace.Extensions.TagHelpers
{
    using System;
    using System.IO;
    using System.Text.Encodings.Web;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.TagHelpers;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
    using Microsoft.AspNetCore.Razor.TagHelpers;
 
    // Source code for label tag helper: Mvc/src/Microsoft.AspNetCore.Mvc.TagHelpers/LabelTagHelper.cs
    // https://github.com/aspnet/Mvc/blob/dev/src/Microsoft.AspNetCore.Mvc.TagHelpers/LabelTagHelper.cs
 
    [HtmlTargetElement("requiredlabel", Attributes = ForAttributeName)]
    public class RequiredLabelTagHelper : TagHelper
    {
        private const string ForAttributeName = "asp-for";
 
        // Will be used as highlight-class in html
        public string HighlightClass { get; set; }
 
        /// <summary>
        /// Creates a new <see cref="LabelTagHelper"/>.
        /// </summary>
        /// <param name="generator">The <see cref="IHtmlGenerator"/>.</param>
        public RequiredLabelTagHelper(IHtmlGenerator generator)
        {
            Generator = generator;
        }
 
        /// <inheritdoc />
        public override int Order => -1000;
 
        [HtmlAttributeNotBound]
        [ViewContext]
        public ViewContext ViewContext { get; set; }
 
        protected IHtmlGenerator Generator { get; }
 
        /// <summary>
        /// An expression to be evaluated against the current model.
        /// </summary>
        [HtmlAttributeName(ForAttributeName)]
        public ModelExpression For { get; set; }
 
        /// <inheritdoc />
        /// <remarks>Does nothing if <see cref="For"/> is <c>null</c>.</remarks>
        public override void Process(TagHelperContext context, TagHelperOutput output)
        {
            if (context == null)
            {
                throw new ArgumentNullException(nameof(context));
            }
 
            if (output == null)
            {
                throw new ArgumentNullException(nameof(output));
            }
 
            var requiredMarkTagBuilder = new TagBuilder("span");
            requiredMarkTagBuilder.AddCssClass(HighlightClass);
            requiredMarkTagBuilder.InnerHtml.Append(" *");
 
            var tagBuilder = Generator.GenerateLabel(
                ViewContext,
                For.ModelExplorer,
                For.Name,
                labelText: null,
                htmlAttributes: null);
 
            if (For.ModelExplorer.Metadata.IsRequired)
            {
                using (var writer = new StringWriter())
                {
                    requiredMarkTagBuilder.WriteTo(writer, HtmlEncoder.Default);
                    tagBuilder.InnerHtml.AppendHtml(writer.ToString());
                }
            }
 
            output.TagName = tagBuilder.TagName;
            output.MergeAttributes(tagBuilder);
            output.Content.SetHtmlContent(tagBuilder.InnerHtml);
        }
    }
}
```

## 3.2. Khai báo
<a id="markdown-khai-b%C3%A1o" name="khai-b%C3%A1o"></a>

Mở `View/_ViewImports.cshtml`

```cs
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
 
@* Thêm dòng sau *@
@addTagHelper *, YourNamespace.Extensions
```

> Đoạn code này giúp tag helper của bạn có thể hoạt động trong các view razor. Với tên namespace khác, bạn cần phải thay đổi đoạn code đó tương ứng
> 
> Xem thêm tại: [https://docs.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/intro](https://docs.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/intro) mục _Managing Tag Helper scope_

# 4. Sử dụng
<a id="markdown-s%E1%BB%AD-d%E1%BB%A5ng" name="s%E1%BB%AD-d%E1%BB%A5ng"></a>

Vô cùng đơn giản

```html
<requiredlabel asp-for="Username" highlight-class="red bold"></requiredlabel>
```

sẽ render ra đoạn code html sau

```html
<label for="Username">User name<span class="red bold"> *</span></label>
```