---
title: '[Basic for Absolute Beginner] - [Part 2] - Layout with XAML'
tags:
  - layout
  - listbox
  - template
  - windows phone
  - xaml
id: '299'
categories:
  - - CSharp
    - Windows Phone
date: 2014-01-20 22:55:07
---

Đây là phần 2 của loạt bài viết Layout with XAML – Basic for Absolute Beginner

Bài 1 ở đây: [[Windows Phone – Silverlight] Layout with XAML – Basic for AbsoluteBeginner - Part 1](http://cuoilennaocacban2.wordpress.com/2013/11/22/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner/ "[Windows Phone – Silverlight] Layout with XAML–Basic for AbsoluteBeginner - Part 1")

![](http://farm8.staticflickr.com/7369/11949617853_c885ed2f42_o.png")

Như các bạn đã biết, ngoài Stackpanel và Grid ra, XAML còn có 1 control cơ bản khác, đó là ListBox (và GridView, ListView, nếu bạn đang lập trình cho Windows 8 hay các ứng dụng WPF)

Trong phạm vi bài viết này, mình sẽ đề cập tới ListBox cùng cách thiết kế nó trên giao diện.

<!-- more -->

# Trong cùng series:
<a id="markdown-trong-c%C3%B9ng-series%3A" name="trong-c%C3%B9ng-series%3A"></a>

[\[Basic for Absolute Beginner\] – \[Part 1\] – Layout with XAML 1](https://huntertran.ca/2013/11/21/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner/)

[\[Basic for Absolute Beginner\] – \[Part 2\] – Layout with XAML 2](https://huntertran.ca/2014/01/21/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner-part-2/) 

[\[Basic for Absolute Beginner\] – \[Part 3\] – App’s Structure and how to customize it](https://huntertran.ca/2014/02/26/basic-for-absolute-beginner-part-3-apps-structure-and-how-customized-it/)

[\[Basic for Absolute Beginner\] – \[Part 4\] – Basic Steps for a new app](https://huntertran.ca/2014/03/31/basic-for-absolute-beginner-part-4-basic-steps-for-a-new-app/)

[\[Basic for Absolute Beginner\] – \[Part 5\] – Analytics for your apps](https://huntertran.ca/2014/04/04/basic-for-absolute-beginner-part-5-analytics-for-your-apps/)

[\[Basic for Absolute Beginner\] - \[Part 6\] - Source Control](https://huntertran.ca/2014/05/02/basic-for-absolute-beginner-part-6-source-control/)

# Mục lục
<a id="markdown-m%E1%BB%A5c-l%E1%BB%A5c" name="m%E1%BB%A5c-l%E1%BB%A5c"></a>

<!-- TOC -->

- [1. Trong cùng series:](#1-trong-c%C3%B9ng-series)
- [2. Mục lục](#2-m%E1%BB%A5c-l%E1%BB%A5c)
- [3. LISTBOX CONTROL](#3-listbox-control)
    - [3.1. Các thuộc tính quan trọng](#31-c%C3%A1c-thu%E1%BB%99c-t%C3%ADnh-quan-tr%E1%BB%8Dng)
        - [3.1.1. ItemsSource](#311-itemssource)
        - [3.1.2. SelectedIndex](#312-selectedindex)
        - [3.1.3. SelectedItem](#313-selecteditem)
        - [3.1.4. DataConext – ngữ cảnh dữ liệu](#314-dataconext--ng%E1%BB%AF-c%E1%BA%A3nh-d%E1%BB%AF-li%E1%BB%87u)
    - [3.2. Thử nghiệm](#32-th%E1%BB%AD-nghi%E1%BB%87m)
- [4. DataBinding – Phương pháp tuyệt vời để hiển thị dữ liệu](#4-databinding--ph%C6%B0%C6%A1ng-ph%C3%A1p-tuy%E1%BB%87t-v%E1%BB%9Di-%C4%91%E1%BB%83-hi%E1%BB%83n-th%E1%BB%8B-d%E1%BB%AF-li%E1%BB%87u)
    - [4.1. Chuẩn bị](#41-chu%E1%BA%A9n-b%E1%BB%8B)
    - [4.2. Kiểu dữ liệu](#42-ki%E1%BB%83u-d%E1%BB%AF-li%E1%BB%87u)
    - [4.3. Nguồn dữ liệu](#43-ngu%E1%BB%93n-d%E1%BB%AF-li%E1%BB%87u)
    - [4.4. Nạp dữ liệu](#44-n%E1%BA%A1p-d%E1%BB%AF-li%E1%BB%87u)
    - [4.5. Binding](#45-binding)
    - [4.6. DataTemplate](#46-datatemplate)
- [5. Event Handling](#5-event-handling)

<!-- /TOC -->

# 1. LISTBOX CONTROL
<a id="markdown-listbox-control" name="listbox-control"></a>

ListBox control dùng để hiện thị một danh sách các item.

Danh sách này sẽ có một giao diện nhất định, một kiểu dữ liệu nhất định tùy bạn chọn

Ví dụ: "Top 30 video được xem nhiều nhất trên youtube" là một dạng dữ liệu mà ta sẽ dùng ListBox để hiển thị

## 1.1. Các thuộc tính quan trọng
<a id="markdown-c%C3%A1c-thu%E1%BB%99c-t%C3%ADnh-quan-tr%E1%BB%8Dng" name="c%C3%A1c-thu%E1%BB%99c-t%C3%ADnh-quan-tr%E1%BB%8Dng"></a>

![](http://farm8.staticflickr.com/7352/11957902726_0aa577d3c4_o.png)

### 1.1.1. ItemsSource
<a id="markdown-itemssource" name="itemssource"></a>

ItemsSource là nguồn dữ liệu. Listbox này sẽ hiển thị dữ liệu từ đâu?

ItemsSource có thể là một List hoặc một ObservableCollection, ta sẽ nói đến nó ở phần sau

### 1.1.2. SelectedIndex
<a id="markdown-selectedindex" name="selectedindex"></a>

Cái tên đã nói lên tất cả. Đây là item đang được chọn trong listbox của bạn. Trong quá trình khởi tạo, giá trị này sẽ là -1

Lưu ý rằng item bắt đầu từ số 0 trở đi. Giả sử bạn có 5 items, thì nó sẽ được đánh số từ 0 tới 4

### 1.1.3. SelectedItem
<a id="markdown-selecteditem" name="selecteditem"></a>

Đây lại là một thuộc tính khác. Giá trị của thuộc tínhnày bằng null khi khởi tạo. Và khi người dùng chọn một item nào đó trong listbox, item đó sẽ được phản xạ sang thuộc tính này.

Thuộc tính này có kiểu dữ liệu là Object, khi dùng bạn phải ép kiểu sang kiểu dữ liệu của danh sách

### 1.1.4. DataConext – ngữ cảnh dữ liệu
<a id="markdown-dataconext-%E2%80%93-ng%E1%BB%AF-c%E1%BA%A3nh-d%E1%BB%AF-li%E1%BB%87u" name="dataconext-%E2%80%93-ng%E1%BB%AF-c%E1%BA%A3nh-d%E1%BB%AF-li%E1%BB%87u"></a>

DataContext sẽ được dùng trong một số trường hợp advance binding, hiện tại thì bạn chưa cần phải quan tâm tới nó

## 1.2. Thử nghiệm
<a id="markdown-th%E1%BB%AD-nghi%E1%BB%87m" name="th%E1%BB%AD-nghi%E1%BB%87m"></a>

Tạo một project Windows Phone

Trong LayoutRootGrid, tạo một Listbox

![](http://farm3.staticflickr.com/2858/11958105964_af2da41349_o.png)

Chọn thẻ Property khi đang select listbox này

![](http://farm4.staticflickr.com/3749/11957691795_1e3ce3c8ef_o.png)

Trong mục Items, bạn thêm mới một số item cho listbox

![](http://farm4.staticflickr.com/3665/11958004856_387a1bbb07_o.png")

Sau đó, chọn Listbox Item, rồi nhấn nút Add

![](http://farm4.staticflickr.com/3717/11958010686_b3baba9d9d_o.png")

Như bạn có thể thấy, một item với index = xuất hiện cùng thuộc tính của nó

![](http://farm4.staticflickr.com/3679/11957481983_4c4a040752_o.png")

Rồi thêm vào content như hình sau:

![](http://farm8.staticflickr.com/7414/11957661595_36e5271615_o.png")

Nhấn nút chạy thử, và bạn sẽ thấy cách hoạt động của listbox

[http://youtu.be/8cu_REIkxPQ](http://youtu.be/8cu_REIkxPQ)

Bây giờ bạn đã nắm cách thức Listbox hoạt động cơ bản nhất. Ta hãy cùng "Đào sâu" vào thế giới XAML nhé

# 2. DataBinding – Phương pháp tuyệt vời để hiển thị dữ liệu
<a id="markdown-databinding-%E2%80%93-ph%C6%B0%C6%A1ng-ph%C3%A1p-tuy%E1%BB%87t-v%E1%BB%9Di-%C4%91%E1%BB%83-hi%E1%BB%83n-th%E1%BB%8B-d%E1%BB%AF-li%E1%BB%87u" name="databinding-%E2%80%93-ph%C6%B0%C6%A1ng-ph%C3%A1p-tuy%E1%BB%87t-v%E1%BB%9Di-%C4%91%E1%BB%83-hi%E1%BB%83n-th%E1%BB%8B-d%E1%BB%AF-li%E1%BB%87u"></a>

Listbox được dùng nhiều nhất với kỹ thuật DataBinding này (tạm dịch là gắn kết dữ liệu đi)

Kỹ thuật này cho phép bạn hiển thị dữ liệu từ một nguồn nào đó lên trên listbox. Nguồn đó có thể là một List, hoặc một Observable Collection

Nhiều người khi nghĩ tới DataBinding, họ sẽ nghĩ ngay tới mô hình MVVM.

Khoan đã, trong vai một người mới học, hẳn bạn cũng sẽ không biết MVVM là cái gì, mặt mũi nó ra sao.

Vì vậy, hãy tìm hiểu một số khái niệm và cách thức cơ bản trước đã

## 2.1. Chuẩn bị
<a id="markdown-chu%E1%BA%A9n-b%E1%BB%8B" name="chu%E1%BA%A9n-b%E1%BB%8B"></a>

Để thực hiện theo bài viết này, bạn cần có các công cụ sau:

Visual Studio, chắc cái này bạn có rồi

ReSharper: hỗ trợ cho bạn tự động hóa các công việc nhàm chán nhưng cần thiết. Lưu ý đây là phần mềm thương mại

Sau khi cài ReSharper, hãy tiếp tục bài viết nhé

## 2.2. Kiểu dữ liệu
<a id="markdown-ki%E1%BB%83u-d%E1%BB%AF-li%E1%BB%87u" name="ki%E1%BB%83u-d%E1%BB%AF-li%E1%BB%87u"></a>

Để gắn dữ liệu lên ListBox, ta cần phải có một "Nguồn dữ liệu", và nguồn dữ liệu đó phải được tạo ra bởi một kiểu dữ liệu nào đó, vì nó là một danh sách các item

Ví dụ: một danh sách các chuỗi, một danh sách các số nguyên

Tuy nhiên, bạn cũng có thể tạo ra kiểu dữ liệu riêng của mình, như kiểu "Danh sách các món ăn"

Vậy tạo ra kiểu dữ liệu như thế nào?

Tạo một Folder mới, đặt tên là Model

![](http://farm6.staticflickr.com/5535/11958266823_83eee63384_o.png")

Hãy tạo một file class mới trong folder đó với tên gọi DataStructure

![](http://farm8.staticflickr.com/7418/11958284923_ed6b439987_o.png")

Một class DataStructure mới được tạo ra. Bạn có thể xóa nó đi, và bắt đầu định nghĩa cho class riêng của mình

![](http://farm4.staticflickr.com/3769/11958468354_7b160fd49c_o.png")

Theo như hình trên, bạn có 3 thuộc tính private. Khoan đã, private không thể truy cập ngoài class, nên ta cần tạo các public property cho chúng

Trước khi tạo các public property, ta nên làm một chuyện khác, đó là khai báo Interface `INotifyPropertyChanged`

Interface này giúp cho việc binding dữ liệu lên giao diện được "liên tục". Tức là khi có một sự thay đổi về mặt dữ liệu trong nguồn dữ liệu, sự thay đổi đó sẽ lập tức được hiển thị trên giao diện.

Giả sử như bạn có 5 FoodItem, với 5 tên khác nhau. Bạn muốn thay đổi tên của item thứ 2, bạn chỉ cần truy xuất tới item 2 và thay đổi giá trị của thuộc tính foodName, trên giao diện sẽ tự động thay đổi theo mà không cần thêm một dòng code nào cả

Okie, khai báo thuộc tính nào

![](http://farm8.staticflickr.com/7448/11958537464_42bf1c99d6_o.png")

Bạn phải bắt buộc khai báo thêm 1 event và một Method trong class của mình sau khi khai báo Interface

```csharp
protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
{
    PropertyChangedEventHandler handler = PropertyChanged;

    if (handler != null)
    {
      handler(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

Nếu bạn có ReShaper, thì mọi việc đơn giản hơn nhiều

![](http://farm8.staticflickr.com/7353/11958604664_35f1789b07_o.png")

Tiếp tục chọn Yes nhé

![](http://farm8.staticflickr.com/7389/11958614374_ec6174c194_o.png")

Và bạn sẽ thấy kết quả

![](http://farm8.staticflickr.com/7396/11958478293_516b79813d_o.png")

Lưu ý là ReSharper sẽ thêm một file vào Property của Project bạn đang viết

![](http://farm3.staticflickr.com/2886/11958202385_53fea80434_o.png")

File Dropbox cho bạn nào không có ReSharper: [https://db.tt/ycsvjt1S](https://db.tt/ycsvjt1S)

Rồi, bây giờ ta sẽ tạo các Public Property

Một lần nữa, ReSharper sẽ giúp ích chúng ta.

Đặt con trỏ vào dưới các thuộc tính Private, chọn ReShaper > Edit > Generate Code…

![](http://farm8.staticflickr.com/7350/11958249665_5a3716b5f1_o.png")

Chọn Property cho hộp thoại hiện ra

![](http://farm4.staticflickr.com/3771/11958694544_91d3348748_o.png")

Check cả 3 thuộc tính, check luôn tùy chọn "Notify on Property Changes"

![](http://farm3.staticflickr.com/2884/11958705564_54415bb772_o.png")

Thế là bạn có 3 thuộc tính đúng chuẩn như sau

![](http://farm8.staticflickr.com/7290/11958720644_183a2247f4_o.png")

## 2.3. Nguồn dữ liệu
<a id="markdown-ngu%E1%BB%93n-d%E1%BB%AF-li%E1%BB%87u" name="ngu%E1%BB%93n-d%E1%BB%AF-li%E1%BB%87u"></a>

Bạn đã có 1 kiểu dữ liệu, bây giờ bạn sẽ cần 1 nguồn dữ liệu

Tạo một Folder mới tên Data

![](http://farm6.staticflickr.com/5471/11959227656_5759b227f4_o.png")

Tạo một class mới tên StaticData trong Folder đó

![](http://farm4.staticflickr.com/3671/11958698323_1b848ffb0a_o.png")

Khai báo một biến static ObservableCollection

![](http://farm8.staticflickr.com/7447/11959251496_b5da65d4fc_o.png")

Khi có ReSharper, nó sẽ tự động thêm các Namespace cần thiết cho bạn. Ở đây, class FoodItem thuộc namespace TestAd.Model

Kết quả là bạn có như sau:

![](http://farm3.staticflickr.com/2879/11958878734_06cb55d64e_o.png")

## 2.4. Nạp dữ liệu
<a id="markdown-n%E1%BA%A1p-d%E1%BB%AF-li%E1%BB%87u" name="n%E1%BA%A1p-d%E1%BB%AF-li%E1%BB%87u"></a>

Bây giờ, ta sẽ nạp dữ liệu vào ObservableCollection này

Mở file code behind của page có chứa listbox mà bạn đã tạo trong phần 1

Khai báo như sau, bạn sẽ thấy kiểu khai báo này quen thuộc trong bài: [[Windows Phone] Where to put LoadData method](http://cuoilennaocacban.blogspot.com/2013/11/windows-phone-where-to-put-load-data.html)

![](http://farm6.staticflickr.com/5472/11961364684_421975edb5_o.png")

Bước 1: kiểm tra dữ liệu đã tồn tại

Đặc trưng cơ bản của cách khai báo LoadData như thế này là khi ta navigate tới trang này, hoặc có sự thay đổi về elements trên giao diện, event OnLoaded sẽ được gọi lại.

Vì vậy, ta chỉnh sửa event OnLoaded để ngăn ngừa việc load lại dữ liệu như sau:

```csharp
private void OnLoaded(object sender, RoutedEventArgs routedEventArgs)
{ 
  if (StaticData.FoodItemCollection.Count == 0)
  {
    LoadData();
  }
}
```

Thêm một số code như sau vào hàm LoadData

```csharp
private void LoadData() 
{ 
  for (int i =0;i <5;i++)
  { 
    FoodItem foodItem =new FoodItem();
    foodItem.Id = i;
    foodItem.FoodName ="Food Name is " +i;
    foodItem.ImageLink ="FoodItem_" + i + "_imageLink";
    StaticData.FoodItemCollection.Add(foodItem);
  }
}
```

Mục tiêu của đoạn code trên là add 5 item giả vào FoodItemCollection.

## 2.5. Binding
<a id="markdown-binding" name="binding"></a>

Vậy ta đã có dữ liệu, có nguồn dữ liệu, có luôn listbox, bây giờ ta sẽ tiến hành binding dữ liệu này vào listbox

Việc này được thực hiện bởi 1 dòng code duy nhất.

Đặt tên cho listbox của bạn:

![](http://farm4.staticflickr.com/3740/11961472144_46f86145ef_o.png")

Sửa event OnLoaded lại như sau:

```csharp
private void OnLoaded(object sender, RoutedEventArgs routedEventArgs)
{
  if (StaticData.FoodItemCollection.Count == 0)
  { 
    LoadData();
    FoodListBox.ItemsSource = StaticData.FoodItemCollection;
  }
}
```

Sau đó, bấm chạy thử trên Emulator hay trên Device tùy thích

![](http://farm4.staticflickr.com/3712/11961887436_8c77ca2cce_o.png")

Và đây chính là thành quả của các bạn

![](http://farm4.staticflickr.com/3826/11961917396_bb27d31e3c_o.png")

## 2.6. DataTemplate
<a id="markdown-datatemplate" name="datatemplate"></a>

Vậy là dữ liệu đã được hiển thị trên giao diện, nhưng không theo cách bạn mong muốn

Chính vì thế, ta sẽ tạo một DataTemplate cho Listbox, mục đích là để "định nghĩa" cách hiển thị dữ liệu

Vào code XAML của bạn, bấm chọn Document Outline

![](http://farm8.staticflickr.com/7314/11961424713_95b6a4b3de_o.png")

Document Outline là nơi thể hiện toàn bộ mọi thứ có trên giao diện của bạn dưới dạng cây

Bấm chuột phải vào ListBox của bạn và chọn

![](http://farm6.staticflickr.com/5535/11961470493_0b1b86675f_o.png")

![](http://farm4.staticflickr.com/3666/11962019876_076607132c_o.png")

Đặt tên cho DataTemplate của bạn rồi nhấn OK

![](http://farm8.staticflickr.com/7324/11961488143_d9af248312_o.png")

Nếu bạn chọn Define in Application, DataTemplate này có thể được dùng ở mọi page trong project của bạn mà không cần phải khai báo lại

Trong lúc thiết kế, bạn có thể thấy thiết kế của mình được hiển thị trực quan

![](http://farm8.staticflickr.com/7405/11961742983_933fc0557f_o.png")

Nhấn chạy một lần nữa, và mọi thứ sẽ đúng như ý bạn

![](http://farm8.staticflickr.com/7397/11961908164_dfe6879e28_o.png")

# 3. Event Handling
<a id="markdown-event-handling" name="event-handling"></a>

Vậy là bạn đã có 1 listbox, bây giờ ta sẽ áp dụng một số sự kiện cho nó để thông báo cho người dùng biết họ đã chọn Listbox nào

Trong Property của FoodListBox, chọn nút Event

![](http://farm4.staticflickr.com/3678/11961483605_78ff2960f3_o.png")

Double Click vào event "Selection Changed" để khai báo event

Thêm đoạn code sau vào event mới được tạo

```csharp
if (FoodListBox.SelectedIndex != –1)
{
  FoodItem foodItem = FoodListBox.SelectedItem as FoodItem;
  MessageBox.Show(foodItem.FoodName);
}
```

Chạy thử và chọn một item bất kỳ

![](http://farm4.staticflickr.com/3751/11962377686_6b9e9bdb79_o.png")

Thật tuyệt vời phải không

Vậy là hết rồi, hẹn gặp lại các bạn ở episode tiếp theo của Series Absolute Beginner nhé