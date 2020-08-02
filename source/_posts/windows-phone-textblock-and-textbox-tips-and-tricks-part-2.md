---
title: '[Windows Phone] - TextBlock Tips and Tricks – Part 2 – TextBox too'
tags:
  - textblock
  - textbox
  - tip
  - tips
  - trick
  - tricks
id: '253'
categories:
  - - c
    - Windows Phone
date: 2013-10-12 23:58:57
---

Ở phần trước, bạn đã có một số tips and tricks khá thú vị phải ko?

> Link phần trước: [\[Windows Phone\] - Textblock Tips and Tricks - Part 1](https://wp.me/p1V2Tb-43)

![](https://farm8.staticflickr.com/7407/10135898285_7ea60ebd9a_o.png) Trong phần này, bạn sẽ còn có nhiều điều thú vị hơn nữa
<!-- more -->
*   [1\. Text quá dài và vấn đề bị mất chữ](#1-text-quá-dài-và-vấn-đề-bị-mất-chữ)
    *   [1.1. Nguyên nhân](#11-nguyên-nhân)
    *   [1.2. Khắc phục](#12-khắc-phục)
*   [2\. Selectable TextBlock](#2-selectable-textblock)

# 1\. Text quá dài và vấn đề bị mất chữ

![](https://farm3.staticflickr.com/2834/10238287965_30e435db37_o.png) Chữ bị mất một cách vô cùng kỳ quái phải không?

## 1.1. Nguyên nhân

Tất cả các control trong Windows Phone đều có 1 giới hạn kích thước mặc định: 2000 pixel 2000 pixel lớn tới mức nào? màn hình laptop tiêu chuẩn là 1366 x 768. So sánh với 2000 x 2000. Vậy là hơn gấp đôi nhưng đối với một số máy Windows Phone có độ phân giải Full HD (1900 x 1080), thì chỉ cần nhân đôi chiều rộng của máy ra là ta sẽ có 1 kích thước tối đa sao? Không phải vậy. Kích thước 2k chỉ áp dụng cho app Windows Phone 7

## 1.2. Khắc phục

Cách khắc phục rất đơn giản. Chia text của bạn ra nhiều phần, và gắn chúng vào các textblock khác nhau. Bao các textblock này trong ScrollViewer. Xong!

# 2\. Selectable TextBlock

Textblock, dĩ nhiên là không select được rồi. Vậy ta sẽ chỉnh một chút cho TextBox giống với TextBlock, để lợi dụng tính “Selectable” của nó add code sau vào resource \[code lang=xml\] <Style x:Key="TextBoxStyle1" TargetType="TextBox"> <Setter Property="Background" Value="{StaticResource PhoneBackgroundBrush}" /> <Setter Property="Foreground" Value="{StaticResource PhoneForegroundBrush}" /> <Setter Property="BorderBrush" Value="{StaticResource PhoneBackgroundBrush}" /> <Setter Property="SelectionBackground" Value="{StaticResource PhoneAccentBrush}" /> <Setter Property="SelectionForeground" Value="{StaticResource PhoneTextBoxSelectionForegroundBrush}" /> <Setter Property="Template"> <Setter.Value> <ControlTemplate TargetType="TextBox"> <Grid Background="Transparent"> <VisualStateManager.VisualStateGroups> <VisualStateGroup x:Name="CommonStates"> <VisualState x:Name="ReadOnly"> <Storyboard> <ObjectAnimationUsingKeyFrames Storyboard.TargetName="EnabledBorder" Storyboard.TargetProperty="Visibility"> <DiscreteObjectKeyFrame KeyTime="0"> <DiscreteObjectKeyFrame.Value> <Visibility>Collapsed</Visibility> </DiscreteObjectKeyFrame.Value> </DiscreteObjectKeyFrame> </ObjectAnimationUsingKeyFrames> <ObjectAnimationUsingKeyFrames Storyboard.TargetName="DisabledOrReadonlyBorder" Storyboard.TargetProperty="Visibility"> <DiscreteObjectKeyFrame KeyTime="0"> <DiscreteObjectKeyFrame.Value> <Visibility>Visible</Visibility> </DiscreteObjectKeyFrame.Value> </DiscreteObjectKeyFrame> </ObjectAnimationUsingKeyFrames> <ObjectAnimationUsingKeyFrames Storyboard.TargetName="DisabledOrReadonlyBorder" Storyboard.TargetProperty="Background"> <DiscreteObjectKeyFrame KeyTime="0" Value="{StaticResource PhoneBackgroundBrush}" /> </ObjectAnimationUsingKeyFrames> <ObjectAnimationUsingKeyFrames Storyboard.TargetName="DisabledOrReadonlyBorder" Storyboard.TargetProperty="BorderBrush"> <DiscreteObjectKeyFrame KeyTime="0" Value="{StaticResource PhoneBackgroundBrush}" /> </ObjectAnimationUsingKeyFrames> <ObjectAnimationUsingKeyFrames Storyboard.TargetName="DisabledOrReadonlyContent" Storyboard.TargetProperty="Foreground"> <DiscreteObjectKeyFrame KeyTime="0" Value="{StaticResource PhoneForegroundBrush}" /> </ObjectAnimationUsingKeyFrames> </Storyboard> </VisualState> </VisualStateGroup> </VisualStateManager.VisualStateGroups> <Border x:Name="EnabledBorder" Margin="{StaticResource PhoneTouchTargetOverhang}" Background="{TemplateBinding Background}" BorderBrush="{TemplateBinding BorderBrush}" BorderThickness="{TemplateBinding BorderThickness}"> <ContentControl x:Name="ContentElement" Margin="{StaticResource PhoneTextBoxInnerMargin}" HorizontalContentAlignment="Stretch" VerticalContentAlignment="Stretch" BorderThickness="0" Padding="{TemplateBinding Padding}" /> </Border> <Border x:Name="DisabledOrReadonlyBorder" Margin="{StaticResource PhoneTouchTargetOverhang}" Background="Transparent" BorderBrush="{StaticResource PhoneDisabledBrush}" BorderThickness="{TemplateBinding BorderThickness}" Visibility="Collapsed"> <TextBox x:Name="DisabledOrReadonlyContent" Background="Transparent" FontFamily="{TemplateBinding FontFamily}" FontSize="{TemplateBinding FontSize}" FontStyle="{TemplateBinding FontStyle}" FontWeight="{TemplateBinding FontWeight}" Foreground="{StaticResource PhoneDisabledBrush}" IsReadOnly="True" SelectionBackground="{TemplateBinding SelectionBackground}" SelectionForeground="{TemplateBinding SelectionForeground}" Template="{StaticResource PhoneDisabledTextBoxTemplate}" Text="{TemplateBinding Text}" TextAlignment="{TemplateBinding TextAlignment}" TextWrapping="{TemplateBinding TextWrapping}" /> </Border> </Grid> </ControlTemplate> </Setter.Value> </Setter> </Style> \[/code\] Khi dùng, chỉ cần \[code lang=xml\] <TextBox x:Name="testTextBox" IsReadOnly="True" Style="{StaticResource TextBoxStyle1}" Text="Hello world, afdafkj aflaskfjalk lakfaljfklak lfjlaksfjlask jfldsj lskadjfl dslfj lasjf lkasjfl" TextWrapping="Wrap" /> \[/code\] Thế là xong