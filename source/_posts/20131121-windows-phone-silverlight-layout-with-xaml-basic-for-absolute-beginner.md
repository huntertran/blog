---
title: '[Basic for Absolute Beginner] - [Part 1] - Layout with XAML'
tags:
  - auto
  - column
  - columndefinition
  - grid
  - stackpanel
  - star size
id: '273'
categories:
  - - CSharp
    - Windows Phone
    - Windows Store App
date: 2013-11-21 12:53:45
---

Trong thời gian qua, nhất là khi Nokia tổ chức nhiều cuộc thi với giải thưởng là những cái điện thoại hấp dẫn, rất nhiều bạn đã PM mình để hỏi một số vấn đề cơ bản về các control hiển thị giao diện trong Windows Phone.

Bài viết này sẽ giúp các bạn có một khái niệm chung về giao diện và biết cách sử dụng nó trong lập trình Windows Phone nhé

![xaml](/images/flickr/819/40941396061_a7abc65129_o.png)

Trong phạm vi bài viết này, tôi sẽ giới thiệu cho các bạn những điều cơ bản nhất về giao diện trong XAML
<!-- more -->

# Trong cùng series:

[\[Basic for Absolute Beginner\] – \[Part 1\] – Layout with XAML 1](https://huntertran.ca/2013/11/21/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner/)

[\[Basic for Absolute Beginner\] – \[Part 2\] – Layout with XAML 2](https://huntertran.ca/2014/01/21/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner-part-2/) 

[\[Basic for Absolute Beginner\] – \[Part 3\] – App’s Structure and how to customize it](https://huntertran.ca/2014/02/26/basic-for-absolute-beginner-part-3-apps-structure-and-how-customized-it/)

[\[Basic for Absolute Beginner\] – \[Part 4\] – Basic Steps for a new app](https://huntertran.ca/2014/03/31/basic-for-absolute-beginner-part-4-basic-steps-for-a-new-app/)

[\[Basic for Absolute Beginner\] – \[Part 5\] – Analytics for your apps](https://huntertran.ca/2014/04/04/basic-for-absolute-beginner-part-5-analytics-for-your-apps/)

[\[Basic for Absolute Beginner\] - \[Part 6\] - Source Control](https://huntertran.ca/2014/05/02/basic-for-absolute-beginner-part-6-source-control/)

# Mục lục

*   [1. Basic Control – Nest Control](#1-basic-control--nest-control)
    *   [1.1. Grid.ColumnDefinition and Grid.RowDefinition](#11-gridcolumndefinition-and-gridrowdefinition)
        *   [1.1.1. Fixed Size](#111-fixed-size)
        *   [1.1.2. Auto Size](#112-auto-size)
        *   [1.1.3. Star Size](#113-star-size)
    *   [1.2. Nested Grid – A "Gridception" :3](#12-nested-grid -a-gridception-3)
*   [2. StackPanel](#2-stackpanel)
    *   [2.1. Bản chất của StackPanel](#21-bản-chất-của-stackpanel)
    *   [2.2. Hiển thị StackPanel vượt quá màn hình](#22-hiển-thị-stackpanel-vượt-quá-màn-hình)

# 1. Basic Control – Nest Control

Trong XAML, bạn có 2 control chính dùng để "chứa" các control khác, đó là **`Grid`** và **`StackPanel`**

2 control này khá khác nhau, ở bảng dưới

| Grid                                 	| StackPanel                                                        	|
|--------------------------------------	|-------------------------------------------------------------------	|
| Các control con có thể đè lên nhau   	| Các   control con xếp theo hàng dọc hoặc ngang, không đè lên nhau 	|
| Có thể chia thành dòng và cột        	| Không có                                                          	|
| Tự động mở rộng theo control chứa nó 	| Mở rộng   theo nội dung bên trong nó                              	|

Hãy tạo một Project Windows Phone mới và thử nghiệm những gì Grid có thể làm được

Trong MainPage.xaml, hãy để ý giao diện mở đầu của nó.

![](/images/2013/11/112213_0144_windowsphon2.png)

Bây giờ, hãy mạnh dạn Delete hết, chỉ chừa lại cái "LayoutRoot" Grid thôi nhé

![](/images/2013/11/112213_0144_windowsphon3.png)

Đây là Grid Control, nó có thể chứa các control khác bên trong, và các control này mặc định sẽ nằm đè lên nhau.

Thêm những dòng sau đây vào LayoutRoot Grid

![](/images/2013/11/112213_0144_windowsphon4.png)

Và để ý sự thay đổi ở giao diện

![](/images/2013/11/112213_0144_windowsphon5.png)

Như bạn có thể thấy, 2 dòng TextBlock với FontSize khác nhau này nằm đè lên nhau trong giao diện

Khoan đã, tại sao tôi lại cần tới khả năng này của Grid? Tôi không cần bất cứ control nào nằm đè lên nhau trong ứng dụng của tôi cả.

Có đấy bạn: Hãy xem hình dưới đây

![](/images/2013/11/112213_0144_windowsphon6.png)

Logo Windows nằm chìm bên dưới, dòng chữ Hello world nổi lên trên, cũng khá hay phải không. Tôi tin chắc rằng bạn sẽ tìm ra nhiều cách hay ho hơn để tận dụng khả năng này của Grid

## 1.1. Grid.ColumnDefinition and Grid.RowDefinition

Như trong bảng so sánh ở trên, Grid Control có thể chia không gian bên trong nó ra thành nhiều dòng và cột

![](/images/2013/11/112213_0144_windowsphon7.png)

Grid.RowDefinition là một tag định nghĩa chia dòng cho Grid RowDefintion đi liền với thuộc tính Height Các con số trong thuộc tính Height là số Pixel mà Row đó được định nghĩa Danh sách các Row được đánh số thứ tự, bắt đầu từ 0

Trong các control con bên trong Grid, ta khai báo nó thuộc về dòng nào bằng cách khai báo thêm thuộc tính Grid.Row="Số thứ tự dòng"

Và đây là giao diện

![](/images/2013/11/112213_0144_windowsphon8.png)

Tương tự như vậy với ColumnDefintion

![](/images/2013/11/112213_0144_windowsphon9.png)

Cùng điểm lại một chút. Trong thuộc tính Width của ColumnDefinition hoặc thuộc tính Height của RowDefinition, bạn sẽ thấy ngoài việc xác lập một con số, ta còn có thể xác lập nó thành "Auto" hoặc "\*". Đâu là điểm khác biệt giữa các xác lập này?

### 1.1.1. Fixed Size

Fixed Size là một con số. Như bạn thấy ở hình trên, ta có 3 column, column 0 = 60 pixel, column 1 = 70 pixel, column 2 = 150 pixel

Điều này có nghĩa là dù bạn làm gì giao diện đi nữa, ta vẫn luôn luôn có 3 cột với 3 "số đo" như trên.

Điều gì xảy ra khi bạn mở rộng màn hình, đối với Windows Phone là bạn có 1 devices có độ phân giải cao hơn nhiều?

Đối với các ứng dụng WPF và Silverlight, kích thước mà hình không được định sẵn, khi mở rộng, 3 cột với 3 số đo như trên vẫn sẽ giữ nguyên không thay đổi. Tức là bạn sẽ có một vùng đen rất rộng phía bên phải, và 3 cột chen chúc nhau ở bên trái

Đối với Windows Phone, theo như một số tài liệu MSDN, 3 cột này sẽ giữ nguyên vị trí, ứng dụng của bạn đơn giản chỉ là được scale up bằng độ phân giải của máy thôi.

### 1.1.2. Auto Size

Đối với cột Auto, ta sẽ có 1 thứ khác. Hãy thử thay đổi cột đầu tiên thành Auto, và bạn sẽ thấy rõ.

Cột đầu tiên được mở rộng đúng bằng với chiều rộng dòng chữ bên trong nó phải không? Đó chính là công dụng của Auto Size.

Auto sẽ cho phép tạo ra cột với độ rộng bằng nội dung chứa bên trong nó. Nhưng hãy cẩn thận, khi nội dung quá dài, cột sẽ tự động mở rộng và đôi khi vượt quá màn hình của máy

### 1.1.3. Star Size

Star Size lại là một chuyện vui. Hãy thử vui một chút, tạo thật nhiều Grid con bên trong một grid lớn và xem chuyện gì xảy ra nhé

![](https://farm6.staticflickr.com/5488/10986643416_2fe9f2c287_o.png)

3 cột đầu tiên, mỗi cột có fixed size = 50 pixel

Cột thứ 4 có Width = "\*" => Cột thứ 4 sẽ chiếm hết toàn bộ chiều rộng còn lại.

Bây giờ, hãy thay đổi code một chút, nhiều điều thú vị đang chờ bạn

![](https://farm4.staticflickr.com/3720/10986785764_6181e246a7_o.png)

Một con số trước dấu \* mang ý nghĩa phần. 1 + 2 + 3 + 4 = 10 phần, và cột đầu tiên chiếm 1/10, cột thứ 2 chiếm 2/10, cột 3 chiếm 3/10, cột 4 chiếm 4/10. Cho dù thiết bị của bạn có độ phân giải cao đến đâu, hoặc Grid mẹ có kích thước như thế nào, phần trăm mỗi cột chiếm dụng là không đổi. Thật tuyệt phải không

## 1.2. Nested Grid – A "Gridception" :3

Hãy thử vui một chút, tạo thật nhiều Grid con bên trong một grid lớn và xem chuyện gì xảy ra nhé

![](/images/2013/11/112213_0144_windowsphon10.png)

Màu sắc chói lóa. Như vận bạn có thể thấy, trong một Grid có thể chứa thêm nhiều Grid khác nữa, và trong các Grid con lại có thể chứa thêm các Grid con. Điều này là vô hạn miễn là máy bạn đủ khả năng render ra hình ảnh. Nhưng tôi đoán chắc các bạn không cần nhiều hơn 5 lớp Grid đâu

# 2. StackPanel

StackPanel khá giống với Grid ở mặt chứa được nhiều control khác bên trong nó, nhưn stackpanel không thể chia dòng và cột

Sửa lại như sau

![](/images/2013/11/112213_0144_windowsphon11.png)

Khoan, tất cả các Grid màu đi đâu hết rồi :(

Hãy quay lại với bản chất của StackPanel

## 2.1. Bản chất của StackPanel

Mặc định, StackPanel sẽ có chiều rộng / chiều cao đúng bằng nội dung chứa bên trong nó.

Như vậy, với 4 cái Grid ở trên đều không có kích thước, tức là sẽ có kích thước mặc định. Nếu 4 Grid đó được chứa trong 1 Grid lớn, thì nó sẽ được tự động bung ra tràn đầy Grid mẹ. Nhưng với StackPanel, 4 Grid này sẽ bị thu nhỏ lại thành 0.

Bằng cách lập kích thước cho mỗi Grid, ta sẽ thấy điều kỳ diệu xảy ra

![](https://farm8.staticflickr.com/7406/10986838364_70a4e51924_o.png)

4 Grid của chúng ta đã hiển thị, và xếp hàng theo chiều dọc. Bây giờ, bạn thêm thuộc tính Orientation="Horizontal" vào StackPanel, và sửa Height thành Width

![](https://farm4.staticflickr.com/3737/10986918494_709849b7f9_o.png)

Như vậy, ta có thể thấy StackPanel sẽ thu gọn tối đa theo chiều chính, và mở rộng ra hết control mẹ ở chiều còn lại.

## 2.2. Hiển thị StackPanel vượt quá màn hình

![](https://farm4.staticflickr.com/3795/10986793265_e22218b72b_o.png)

Tôi đang chọn một vật thể nằm ngoài màn hình.

Thêm một ScrollViewer sẽ giải quyết vấn đề

![](https://farm8.staticflickr.com/7410/10987169593_dbaab3425c_o.png)