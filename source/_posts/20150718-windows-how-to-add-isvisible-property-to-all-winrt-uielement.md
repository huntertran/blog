---
title: '[Windows] How to add IsVisible Property to all WinRT UIElement'
tags: []
id: '452'
categories:
  - - Others
date: 2015-07-18 23:56:05
---

Trong quá trình dev app sử dụng XAML và C#, chắc chắn bạn sẽ gặp trường hợp phải đặt thuộc tính Visibility, và thuộc tính này có 2 giá trị là Visible/Collapsed. Và để binding tới nó sử dụng bool, bạn phải sử dụng một converter. Vậy tại sao Microsoft không thiết kế nó sử dụng bool từ đầu nhỉ. Và có cách nào để khắc phục không?

Bài viết được biên tập lại từ: [http://www.rudyhuyn.com/blog/2015/03/26/how-to-add-isvisible-property-to-all-winrt-ui-elements/](http://www.rudyhuyn.com/blog/2015/03/26/how-to-add-isvisible-property-to-all-winrt-ui-elements/)
<!-- more -->
# Lịch sử

Thuộc tính Visibility kế thừa các giá trị của nó từ WPF, gồm có 3 giá trị:

*   Visible: Hiển thị control
*   Hidden: Không hiển thị control, nhưng giữ chỗ của control này trên giao diện (Giống như Opacity = 0, Visibility = Visible)
*   Collapsed: Không hiển thị control, và cũng không giữ chỗ của nó trên giao diện.

Qua đến Silverlight, sau này Windows RT trên Windows 8.1 và Windows Phone 8.1, thuộc tính hidden đã bị bỏ, nhưng do vẫn dùng chung nhân Windows NT nên Microsoft không chỉnh sửa giá trị nó thành bool mà vẫn giữ 2 giá trị cũ

# Cách khắc phục

Đây là một class nhỏ giúp bạn thêm một thuộc tính gọi là "IsVisible" vào UIElements và truyền cho nó giá trị true hoặc false

```csharp
public class Extension: DependencyObject
{
    public static readonly DependencyProperty IsVisibleProperty = DependencyProperty.RegisterAttached("IsVisible",
                                                                                                      typeof(bool),
                                                                                                      typeof(Extension),
                                                                                                      new PropertyMetadata(true, IsVisibleCallback));

    private static void IsVisibleCallback(DependencyObject d, DependencyPropertyChangedEventArgs e)
    {
        ((UIElement) d).Visibility = (bool) e.NewValue ? Visibility.Visible : Visibility.Collapsed;
    }

    public static void SetIsVisible(UIElement element, bool value)
    {
        element.SetValue(IsVisibleProperty, value);
    }

    public static bool GetIsVisible(UIElement element)
    {
        return (bool) element.GetValue(IsVisibleProperty);
    }
}
```


Vậy là xong, bạn có thể sử dụng nó ngay

```xml
<Page x:Class="IsVisibleSample.MainPage"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
      xmlns:ext="using:Huyn"
      mc:Ignorable="d">
    <Rectangle Height="100"
               Width="100"
               Fill="Red" 
               x:Name="Rectangle" 
               ext:Extension.IsVisible="false"/>
</Page>
```


Hoặc dùng Binding với nó

```xml
<CheckBox x:Name="MyCheckBox"
          IsChecked="True"
          Content="show rectangle"/>
<Rectangle Height="100"
           Width="100"
           Fill="Red"
           x:Name="Rectangle"
           ext:Extension.IsVisible="{Binding IsChecked,ElementName=MyCheckBox}"/>
```


Hoặc dùng nó như một Binding Source

```xml
<CheckBox IsChecked="{Binding (ext:Extension.IsVisible),ElementName=Rectangle}"
          IsEnabled="False"
          Content="rectangle is visible?"/>
```


Hoặc dùng nó trong code behind

```csharp
 var val = Extension.GetIsVisible(Rectangle);
 Extension.SetIsVisible(Rectangle,true);
 ```

Thế là xong