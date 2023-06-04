---
title: '[ASP.NET] Mở rộng EditorFor'
tags:
  - custom
  - editorfor
  - extend
  - mở rộng
id: '874'
categories:
  - - CSharp
    - ASP.NET
  - - Others
date: 2017-04-20 00:26:01
---

Chắc là bạn đã quá quen với **_EditorFor_** control, nhưng nó chỉ render khi gặp những kiểu dữ liệu được hỗ trợ thôi. Bạn sẽ làm gì nếu muốn mở rộng EditorFor để render những kiểu dữ liệu của riêng bạn?
<!-- more -->
Mục lục

*   [1. Sử dụng EditorFor và EditorForModel](#1-sử-dụng-editorfor-và-editorformodel)
    
    *   [Model (hoặc ViewModel)](#model-hoặc-viewmodel)
    *   [View](#view)
*   [2. Mở rộng EditorFor](#2-mở-rộng-editorfor)
    
    *   [2.1 Tạo EditorTemplates](#21-tạo-editortemplates)

Có thể nói EditorFor và EditorForModel là những control hữu ích nhất khi mà nó có thể render cái bụp toàn bộ thẻ input cần thiết dựa trên một model của bạn.

# 1. Sử dụng EditorFor và EditorForModel

Tại sao chả thấy ai nói gì về Editor: Từ hồi MVC2, Editor control đi kèm với phiên bản đầu tiên của MVC có thể được thay thế bởi EditorFor. Từ "For" ám chỉ đây là một _strongly typed html helper_, tức là bạn có thể chọn tên property từ model mà không sợ sai

## Model (hoặc ViewModel)

Để render 1 cái form, bạn cần phải biết data nó nhận vô là gì. Để hiển thị những data này, bạn cần phải tạo một class với các Properties

Model

```csharp
public class Lesson
{
    // ScaffoldColumn mark that EditorFor should render it or not
    [ScaffoldColumn(false)]
    public int Id { get; set; }
 
    // To display as label
    [Display(Name = "Lesson Name")]
    public string Name { get; set; }
 
    [Display(Name = "CD Number")]
    public int CDNumber { get; set; }
 
    [Display(Name = "CD Track")]
    public int CDTrack { get; set; }
}
```

ViewModel

```csharp
public class LessonViewModel
{
    public Lesson LessonItem { get; set; }
}
```

## View

* EditorFor control phải nằm bên trong form tag
* Razor support bạn render cái form tag đó tự động luôn

```csharp
@model LessonViewModel
 
@using(Html.BeginForm("ActionName","ControllerName", FormMethod.Post,new {@class = "myformclass"}))
{
    @Html.EditorFor(x => x.LessonItem)
}
```

Nếu bạn không có ViewModel, nhưng muốn render trực tiếp từ Lesson model

```csharp
@model Lesson
 
@using(Html.BeginForm("ActionName","ControllerName", FormMethod.Post,new {@class = "myformclass"}))
{
    @Html.EditorForModel()
}
```

# 2. Mở rộng EditorFor

Tạo một class mới để giữ data

```csharp
public class TextBoxWithCheck
{
    [Display(Name = "Fancy Text")]
    public string MyText { get; set;}
 
    public bool IsTrue { get; set; }
}
```

Thêm cái class mới này vô Lesson model

```csharp
public TextBoxWithCheck FancyBox { get; set; }
```

Rồi giờ nếu bạn muốn một cái textbox có kèm checkbox giống vầy

![textbox with checkbox](/images/flickr/2897/33308184454_8240d60dd1_o.png)

Rõ ràng là chả có cái default control nào có thể làm được trò này, mà EditorFor cũng không biết chọn cái gì để render cái property "FancyBox" của kiểu "TextBoxWithCheck".

Vì thế, bạn sẽ **_dạy_** nó cách render nhóe.

## 2.1 Tạo EditorTemplates

*   Tạo folder "EditorTemplates" trong Views > Shared

![folder structure](/images/flickr/2855/34151179025_3e849d7d2c_o.png)

*   Thêm View mới vào folder đó, đặt tên là "TextBoxWithCheck.cshtml" (phải trùng tên với cái custom class)

```html
@model TextBoxWithCheck
 
@Html.LabelFor(x => x.MyText)
<div class="input-group">
    @Html.TextAreaFor(x => x.Answer, new {@class="form-control"})
    <span class="input-group-addon">
        @Html.CheckBoxFor(x => x.IsTrue)
    </span>
</div>
```

Thế là xong. Giờ EditorFor đã biết render tất cả instance của TextBoxWithCheck.

Cũng dễ mà phải không?