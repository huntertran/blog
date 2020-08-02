---
title: '[ASPNET] Editor for với List và thêm mới item dùng AJAX'
tags:
  - ajax
  - editorfor
  - editorformany
  - list
id: '878'
categories:
  - - c
    - ASP.NET
date: 2017-04-25 03:32:39
---

Tưởng tượng bạn có list các item trong ViewModel Nếu bạn muốn cho phép user thêm mới 1 item, hoặc edit bất kỳ item nào trong list thì làm sao? Đọc xong bài này, bạn sẽ biết cách làm nhóe
<!-- more -->
*   [EditorFor Control](#editorfor-control)
*   [Class](#class)
    *   [C# code](#c-code)
    *   [JavaScript Code](#javascript-code)
*   [Cách xài](#cách-xài)
    *   [Chuẩn bị model](#chuẩn-bị-model)
    *   [Razor code](#razor-code)
*   [Kết quả](#kết-quả)
*   [Cách hoạt động](#cách-hoạt-động)
    *   [Các bước](#các-bước)
    *   [Tại sao lại cần Index](#tại-sao-lại-cần-index)

# EditorFor Control

Trong [bài kỳ trước](https://coding4food.net/2017/04/20/asp-net-mo-rong-editorfor/), bạn đã biết cách xài EditorFor và EditorForModel control. Một điểm hạn chế của 2 thằng này là chúng không tạo ra input cho các class tùy biến của bạn Còn 1 list các item thì lại càng không có. Hiển thị một list thì dễ, một vòng lặp for (hoặc foreach) là xong Nhưng một "Editor" cho cả một list thì ko được support, nên bạn phải tự tạo thôi Từ một bài viết thú vị từ Matt Lunn [ở đây](https://www.mattlunn.me.uk/blog/2014/08/how-to-dynamically-via-ajax-add-new-items-to-a-bound-list-model-in-asp-mvc-net/), chúng ta sẽ thay đổi một tí cho dễ xài và phù hợp với yêu cầu hơn nhóe

# Class

## C# code

\[code lang=csharp\] namespace Yournamespace.Utilities { using System; using System.Collections.Generic; using System.Linq; using System.Linq.Expressions; using System.Text; using System.Web.Mvc; using System.Web.Mvc.Html; public static class HtmlHelperExtensions { /// <summary> /// Generate appropriate control for a list of data /// </summary> /// <typeparam name="TModel">The Model contain the list</typeparam> /// <typeparam name="TValue">The Model of list of items</typeparam> /// <param name="html"></param> /// <param name="propertyExpression">Which property</param> /// <param name="indexResolverExpression">Select the property to be the index</param> /// <param name="isIncludeNewItem">Set to true to include a default new item</param> /// <param name="includeIndexField">Set to true to include Index in values sent to server</param> /// <returns>HTML codes of editorfor a list of items</returns> public static MvcHtmlString EditorForMany<TModel, TValue>( this HtmlHelper<TModel> html, Expression<Func<TModel, IEnumerable<TValue>>> propertyExpression, Expression<Func<TValue, string>> indexResolverExpression = null, bool isIncludeNewItem = false, bool includeIndexField = true) where TModel : class where TValue : new() { var items = propertyExpression.Compile()(html.ViewData.Model); var htmlBuilder = new StringBuilder(); var htmlFieldName = ExpressionHelper.GetExpressionText(propertyExpression); var htmlFieldNameWithPrefix = html.ViewData.TemplateInfo.GetFullHtmlFieldName(htmlFieldName); var indexResolver = GetIndexResolver(indexResolverExpression); items = AddDefaultNewItem(isIncludeNewItem, items); foreach (var item in items) { var dummy = new { Item = item }; var guid = indexResolver(item); var memberExp = Expression.MakeMemberAccess( Expression.Constant(dummy), dummy.GetType().GetProperty("Item")); var singleItemExp = Expression.Lambda<Func<TModel, TValue>>(memberExp, propertyExpression.Parameters); guid = string.IsNullOrEmpty(guid) ? Guid.NewGuid().ToString() : html.AttributeEncode(guid); BuildHtmlString(html, indexResolverExpression, includeIndexField, htmlBuilder, htmlFieldName, htmlFieldNameWithPrefix, guid, singleItemExp); } return new MvcHtmlString(htmlBuilder.ToString()); } private static void BuildHtmlString<TModel, TValue>( HtmlHelper<TModel> html, Expression<Func<TValue, string>> indexResolverExpression, bool includeIndexField, StringBuilder htmlBuilder, string htmlFieldName, string htmlFieldNameWithPrefix, string guid, Expression<Func<TModel, TValue>> singleItemExp) where TModel : class where TValue : new() { htmlBuilder.Append(@"<div>"); if (includeIndexField) { htmlBuilder.Append(\_EditorForManyIndexField(htmlFieldNameWithPrefix, guid, indexResolverExpression)); } htmlBuilder.Append(html.EditorFor(singleItemExp, null, $"{htmlFieldName}\[{guid}\]")); htmlBuilder.Append(@"</div>"); } private static IEnumerable<TValue> AddDefaultNewItem<TValue>(bool isIncludeNewItem, IEnumerable<TValue> items) where TValue : new() { if (isIncludeNewItem) { items = items.Concat(new\[\] { new TValue() }); } return items; } private static Func<TValue, string> GetIndexResolver<TValue>(Expression<Func<TValue, string>> indexResolverExpression) where TValue : new() { Func<TValue, string> indexResolver; if (indexResolverExpression == null) { indexResolver = x => null; } else { indexResolver = indexResolverExpression.Compile(); } return indexResolver; } public static MvcHtmlString EditorForManyIndexField<TModel>( this HtmlHelper<TModel> html, Expression<Func<TModel, string>> indexResolverExpression = null) { var htmlPrefix = html.ViewData.TemplateInfo.HtmlFieldPrefix; var first = htmlPrefix.LastIndexOf('\['); var last = htmlPrefix.IndexOf('\]', first + 1); if (first == -1 || last == -1) { throw new InvalidOperationException("EditorForManyIndexField called when not in a EditorForMany context"); } var htmlFieldNameWithPrefix = htmlPrefix.Substring(0, first); var guid = htmlPrefix.Substring(first + 1, last - first - 1); return \_EditorForManyIndexField(htmlFieldNameWithPrefix, guid, indexResolverExpression); } private static MvcHtmlString \_EditorForManyIndexField<TModel>( string htmlFieldNameWithPrefix, string guid, Expression<Func<TModel, string>> indexResolverExpression) { var htmlBuilder = new StringBuilder(); htmlBuilder.AppendFormat( @"<input type=""hidden"" name=""{0}.Index"" value=""{1}"" />", htmlFieldNameWithPrefix, guid); if (indexResolverExpression != null) { htmlBuilder.AppendFormat( @"<input type=""hidden"" name=""{0}\[{1}\].{2}"" value=""{1}"" />", htmlFieldNameWithPrefix, guid, ExpressionHelper.GetExpressionText(indexResolverExpression)); } return new MvcHtmlString(htmlBuilder.ToString()); } } } \[/code\]

## JavaScript Code

Đoạn code dưới dây dùng JQuery, nhưng bạn có thể convert nó sang JavaScript thuần cũng vẫn được nhóe \[code lang=javascript\] function GenerateGuid() { function s4() { return Math.floor((1 + Math.random()) \* 0x10000) .toString(16) .substring(1); } return s4() + s4() + "-" + s4() + "-" + s4() + "-" + s4() + "-" + s4() + s4() + s4(); } function AssignAddMoreButton() { $(".add-more-button").click(function (event) { event.preventDefault(); debugger; var id = "#" + $(this).data("class"); var clone = $(id).children().last().clone(); var guid = clone.children().first().val(); var regex = new RegExp(guid, "g"); var newHtml = clone.html(function (i, oldHtml) { return oldHtml.replace(regex, GenerateGuid()); }); $(id).append(newHtml); }); } \[/code\]

# Cách xài

## Chuẩn bị model

Cái model mà bạn muốn dùng với cái control EditorForMany này, bạn phải thêm một property là Index vô nữa Ví dụ, nếu tui có một cái class tên là Model luôn \[code lang=csharp\] public class Model { // Your normal, already existed properties // set to false if you don't want to generate a HTML input tag // for it when using with editorfor control \[ScaffoldColumn(false)\] public string Index { get; set; } } \[/code\]

## Razor code

\[code lang=csharp\] @using(Html.BeginForm("ActionName","ControllerName",FormMethod.Post, new {@class="CssClassName"})) { // the last parameter "true" is to generate a default item @Html.EditorForMany(x => x.Model, x => x.Index, true) } // include the javascript code file above AssignAddMoreButton(); \[/code\] Nếu bạn muốn đặt toàn bộ code javascript vào một file .js, nhớ gọi function AssignAddMoreButton sau khi "document ready" nhóe

# Kết quả

Kết quả nó sẽ giống vầy (có thêm style của bootstrap nữa nha) ![demo image](https://farm5.staticflickr.com/4169/34124808091_f4c2130fd2_o.png)

# Cách hoạt động

HtmlHelperExtensions chính là chỗ mà điều kỳ diệu xảy ra. Keyword Extensions sẽ "đăng ký" nó thành một extension của HtmlHelper

## Các bước

Về cơ bản, nó sẽ làm những bước sau

1.  Lấy danh sách Items
2.  Lấy Index property (nếu bạn có khai báo index)
3.  Generate một item default mới (nếu bạn kêu nó làm thế)
4.  Dựng code HTML

\[code lang=html\] <div class="form-group"> // List of your html input tag generated by editorfor and extended templates </div> \[/code\]

## Tại sao lại cần Index

Có 2 cách để send một list data tới controller

*   dùng một mảng có đánh số
    *   xóa 1 item sẽ làm lộn xộn cả list, controller chỉ nhận mảng liên tục
    *   thêm mới 1 item thì cần phải biết index cuối cùng là bao nhiêu

\[code lang=html\] <input type="text" name="YourList\[0\].Data"/> <input type="text" name="YourList\[1\].Data"/> \[/code\]

*   dùng mảng có index dạng string
    *   yêu cầu thêm một tag input ẩn để chứa index
    *   dễ thêm, xóa, sửa item

\[code lang=html\] <input type="hidden" name="YourList.Index" value="radomGuid1"/> <input type="text" name="YourList\[randomGuid1\].Data"/> <input type="hidden" name="YourList.Index" value="anotherGuid2"/> <input type="text" name="YourList\[anotherGuid2\].Data"/> \[/code\] Như bạn cũng thấy, giá trị của hidden input tag có thể là bất cứ gì, miễn là giá trị trong ngoặc vuông giống với nó. Bước 1 bước xa hơn, đoạn code javascript bên trên sẽ tạo ra index dạng GUID, cho nên bạn sẽ không phải lo về vấn đề trùng lặp index. Tuy nhiên, nó ko phải là GUID thiệt, vì để generate GUID thiệt sẽ hơi phức tạp, và làm cho app nặng lên, giống như xài tên lửa đi giết ruồi, cho nên để cho đơn giản, đoạn code đó chỉ sinh ra "fake" GUID, nhưng theo cách code thì khó mà trùng được Theo bạn, bạn có cách nào cải tiến đoạn code bên trên không?