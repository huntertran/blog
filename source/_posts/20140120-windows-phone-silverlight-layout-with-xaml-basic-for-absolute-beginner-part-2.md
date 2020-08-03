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
  - - c
    - Windows Phone
date: 2014-01-20 22:55:07
---

Đây là phần 2 của loạt bài viết Layout with XAML – Basic for Absolute Beginner Bài 1 ở đây: [\[Windows Phone – Silverlight\] Layout with XAML – Basic for AbsoluteBeginner - Part 1](http://cuoilennaocacban2.wordpress.com/2013/11/22/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner/ "[Windows Phone – Silverlight] Layout with XAML–Basic for AbsoluteBeginner - Part 1") ![](http://farm8.staticflickr.com/7369/11949617853_c885ed2f42_o.png") Như các bạn đã biết, ngoài Stackpanel và Grid ra, XAML còn có 1 control cơ bản khác, đó là ListBox (và GridView, ListView, nếu bạn đang lập trình cho Windows 8 hay các ứng dụng WPF) Trong phạm vi bài viết này, mình sẽ đề cập tới ListBox cùng cách thiết kế nó trên giao diện.
<!-- more -->
*   [**1 LISTBOX CONTROL**](#1-listbox-control)
    *   [**1.1 Các thuộc tính quan trọng**](#11-các-thuộc-tính-quan-trọng)
        *   [**1.1.1 ItemsSource**](#111-itemssource)
        *   [**1.1.2 SelectedIndex**](#112-selectedindex)
        *   [**1.1.3 SelectedItem**](#113-selecteditem)
        *   [**1.1.4 DataConext – ngữ cảnh dữ liệu**](#114-dataconext--ngữ-cảnh-dữ-liệu)
    *   [**1.2 Thử nghiệm**](#12-thử-nghiệm)
*   [**DataBinding – Phương pháp tuyệt vời để hiển thị dữ liệu**](#databinding--phương-pháp-tuyệt-vời-để-hiển-thị-dữ-liệu)
    *   [**2.1 Chuẩn bị**](#21-chuẩn-bị)
    *   [**2.2 Kiểu dữ liệu**](#22-kiểu-dữ-liệu)
    *   [**2.3 Nguồn dữ liệu**](#23-nguồn-dữ-liệu)
    *   [**2.4 Nạp dữ liệu**](#24-nạp-dữ-liệu)
    *   [**2.5 Binding**](#25-binding)
    *   [**2.6 DataTemplate**](#26-datatemplate)
*   [**Event Handling**](#event-handling)

# **1 LISTBOX CONTROL**

ListBox control dùng để hiện thị một danh sách các item. Danh sách này sẽ có một giao diện nhất định, một kiểu dữ liệu nhất định tùy bạn chọn Ví dụ: "Top 30 video được xem nhiều nhất trên youtube" là một dạng dữ liệu mà ta sẽ dùng ListBox để hiển thị

## **1.1 Các thuộc tính quan trọng**

![](http://farm8.staticflickr.com/7352/11957902726_0aa577d3c4_o.png)

### **1.1.1 ItemsSource**

ItemsSource là nguồn dữ liệu. Listbox này sẽ hiển thị dữ liệu từ đâu? ItemsSource có thể là một List hoặc một ObservableCollection, ta sẽ nói đến nó ở phần sau

### **1.1.2 SelectedIndex**

Cái tên đã nói lên tất cả. Đây là item đang được chọn trong listbox của bạn. Trong quá trình khởi tạo, giá trị này sẽ là -1 Lưu ý rằng item bắt đầu từ số 0 trở đi. Giả sử bạn có 5 items, thì nó sẽ được đánh số từ 0 tới 4

### **1.1.3 SelectedItem**

Đây lại là một thuộc tính khác. Giá trị của thuộc tínhnày bằng null khi khởi tạo. Và khi người dùng chọn một item nào đó trong listbox, item đó sẽ được phản xạ sang thuộc tính này. Thuộc tính này có kiểu dữ liệu là Object, khi dùng bạn phải ép kiểu sang kiểu dữ liệu của danh sách

### **1.1.4 DataConext – ngữ cảnh dữ liệu**

DataContext sẽ được dùng trong một số trường hợp advance binding, hiện tại thì bạn chưa cần phải quan tâm tới nó

## **1.2 Thử nghiệm**

Tạo một project Windows Phone Trong LayoutRootGrid, tạo một Listbox ![](http://farm3.staticflickr.com/2858/11958105964_af2da41349_o.png) Chọn thẻ Property khi đang select listbox này ![](http://farm4.staticflickr.com/3749/11957691795_1e3ce3c8ef_o.png) Trong mục Items, bạn thêm mới một số item cho listbox ![](http://farm4.staticflickr.com/3665/11958004856_387a1bbb07_o.png") Sau đó, chọn Listbox Item, rồi nhấn nút Add ![](http://farm4.staticflickr.com/3717/11958010686_b3baba9d9d_o.png") Như bạn có thể thấy, một item với index = xuất hiện cùng thuộc tính của nó ![](http://farm4.staticflickr.com/3679/11957481983_4c4a040752_o.png") Rồi thêm vào content như hình sau: ![](http://farm8.staticflickr.com/7414/11957661595_36e5271615_o.png") Nhấn nút chạy thử, và bạn sẽ thấy cách hoạt động của listbox [http://youtu.be/8cu\_REIkxPQ](http://youtu.be/8cu_REIkxPQ) Bây giờ bạn đã nắm cách thức Listbox hoạt động cơ bản nhất. Ta hãy cùng "Đào sâu" vào thế giới XAML nhé

# **DataBinding – Phương pháp tuyệt vời để hiển thị dữ liệu**

Listbox được dùng nhiều nhất với kỹ thuật DataBinding này (tạm dịch là gắn kết dữ liệu đi) Kỹ thuật này cho phép bạn hiển thị dữ liệu từ một nguồn nào đó lên trên listbox. Nguồn đó có thể là một List, hoặc một Observable Collection Nhiều người khi nghĩ tới DataBinding, họ sẽ nghĩ ngay tới mô hình MVVM. Khoan đã, trong vai một người mới học, hẳn bạn cũng sẽ không biết MVVM là cái gì, mặt mũi nó ra sao. Vì vậy, hãy tìm hiểu một số khái niệm và cách thức cơ bản trước đã

## **2.1 Chuẩn bị**

Để thực hiện theo bài viết này, bạn cần có các công cụ sau: Visual Studio, chắc cái này bạn có rồi ReSharper: hỗ trợ cho bạn tự động hóa các công việc nhàm chán nhưng cần thiết. Lưu ý đây là phần mềm thương mại Sau khi cài ReSharper, hãy tiếp tục bài viết nhé

## **2.2 Kiểu dữ liệu**

Để gắn dữ liệu lên ListBox, ta cần phải có một "Nguồn dữ liệu", và nguồn dữ liệu đó phải được tạo ra bởi một kiểu dữ liệu nào đó, vì nó là một danh sách các item Ví dụ: một danh sách các chuỗi, một danh sách các số nguyên Tuy nhiên, bạn cũng có thể tạo ra kiểu dữ liệu riêng của mình, như kiểu "Danh sách các món ăn" Vậy tạo ra kiểu dữ liệu như thế nào? Tạo một Folder mới, đặt tên là Model ![](http://farm6.staticflickr.com/5535/11958266823_83eee63384_o.png") Hãy tạo một file class mới trong folder đó với tên gọi DataStructure ![](http://farm8.staticflickr.com/7418/11958284923_ed6b439987_o.png") Một class DataStructure mới được tạo ra. Bạn có thể xóa nó đi, và bắt đầu định nghĩa cho class riêng của mình ![](http://farm4.staticflickr.com/3769/11958468354_7b160fd49c_o.png") Theo như hình trên, bạn có 3 thuộc tính private. Khoan đã, private không thể truy cập ngoài class, nên ta cần tạo các public property cho chúng Trước khi tạo các public property, ta nên làm một chuyện khác, đó là khai báo Interface INotifyPropertyChanged Interface này giúp cho việc binding dữ liệu lên giao diện được "liên tục". Tức là khi có một sự thay đổi về mặt dữ liệu trong nguồn dữ liệu, sự thay đổi đó sẽ lập tức được hiển thị trên giao diện. Giả sử như bạn có 5 FoodItem, với 5 tên khác nhau. Bạn muốn thay đổi tên của item thứ 2, bạn chỉ cần truy xuất tới item 2 và thay đổi giá trị của thuộc tính foodName, trên giao diện sẽ tự động thay đổi theo mà không cần thêm một dòng code nào cả Okie, khai báo thuộc tính nào ![](http://farm8.staticflickr.com/7448/11958537464_42bf1c99d6_o.png") Bạn phải bắt buộc khai báo thêm 1 event và một Method trong class của mình sau khi khai báo Interface \[code lang=csharp\] protected virtual void OnPropertyChanged(\[CallerMemberName\] string propertyName = null) { PropertyChangedEventHandler handler = PropertyChanged; if (handler != null) handler(this, new PropertyChangedEventArgs(propertyName)); } \[/code\] Nếu bạn có ReShaper, thì mọi việc đơn giản hơn nhiều ![](http://farm8.staticflickr.com/7353/11958604664_35f1789b07_o.png") Tiếp tục chọn Yes nhé ![](http://farm8.staticflickr.com/7389/11958614374_ec6174c194_o.png") Và bạn sẽ thấy kết quả ![](http://farm8.staticflickr.com/7396/11958478293_516b79813d_o.png") Lưu ý là ReSharper sẽ thêm một file vào Property của Project bạn đang viết ![](http://farm3.staticflickr.com/2886/11958202385_53fea80434_o.png") File Dropbox cho bạn nào không có ReSharper: [https://db.tt/ycsvjt1S](https://db.tt/ycsvjt1S) Rồi, bây giờ ta sẽ tạo các Public Property Một lần nữa, ReSharper sẽ giúp ích chúng ta. Đặt con trỏ vào dưới các thuộc tính Private, chọn ReShaper > Edit > Generate Code… ![](http://farm8.staticflickr.com/7350/11958249665_5a3716b5f1_o.png") Chọn Property cho hộp thoại hiện ra ![](http://farm4.staticflickr.com/3771/11958694544_91d3348748_o.png") Check cả 3 thuộc tính, check luôn tùy chọn "Notify on Property Changes" ![](http://farm3.staticflickr.com/2884/11958705564_54415bb772_o.png") Thế là bạn có 3 thuộc tính đúng chuẩn như sau ![](http://farm8.staticflickr.com/7290/11958720644_183a2247f4_o.png")

## **2.3 Nguồn dữ liệu**

Bạn đã có 1 kiểu dữ liệu, bây giờ bạn sẽ cần 1 nguồn dữ liệu Tạo một Folder mới tên Data ![](http://farm6.staticflickr.com/5471/11959227656_5759b227f4_o.png") Tạo một class mới tên StaticData trong Folder đó ![](http://farm4.staticflickr.com/3671/11958698323_1b848ffb0a_o.png") Khai báo một biến static ObservableCollection ![](http://farm8.staticflickr.com/7447/11959251496_b5da65d4fc_o.png") Khi có ReSharper, nó sẽ tự động thêm các Namespace cần thiết cho bạn. Ở đây, class FoodItem thuộc namespace TestAd.Model Kết quả là bạn có như sau: ![](http://farm3.staticflickr.com/2879/11958878734_06cb55d64e_o.png")

## **2.4 Nạp dữ liệu**

Bây giờ, ta sẽ nạp dữ liệu vào ObservableCollection này Mở file code behind của page có chứa listbox mà bạn đã tạo trong phần 1 Khai báo như sau, bạn sẽ thấy kiểu khai báo này quen thuộc trong bài: [\[Windows Phone\] Where to put LoadData method](http://cuoilennaocacban.blogspot.com/2013/11/windows-phone-where-to-put-load-data.html) ![](http://farm6.staticflickr.com/5472/11961364684_421975edb5_o.png") Bước 1: kiểm tra dữ liệu đã tồn tại Đặc trưng cơ bản của cách khai báo LoadData như thế này là khi ta navigate tới trang này, hoặc có sự thay đổi về elements trên giao diện, event OnLoaded sẽ được gọi lại. Vì vậy, ta chỉnh sửa event OnLoaded để ngăn ngừa việc load lại dữ liệu như sau: \[code lang=csharp\] private void OnLoaded(object sender, RoutedEventArgs routedEventArgs) { if (StaticData.FoodItemCollection.Count == 0) { LoadData(); } } \[/code\] Thêm một số code như sau vào hàm LoadData \[code lang=csharp\] private void LoadData() { for (int i =0;i <5;i++) { FoodItem foodItem =new FoodItem(); foodItem.Id = i; foodItem.FoodName ="Food Name is " +i; foodItem.ImageLink ="FoodItem\_"+i +"\_imageLink"; StaticData.FoodItemCollection.Add(foodItem); } } \[/code\] Mục tiêu của đoạn code trên là add 5 item giả vào FoodItemCollection.

## **2.5 Binding**

Vậy ta đã có dữ liệu, có nguồn dữ liệu, có luôn listbox, bây giờ ta sẽ tiến hành binding dữ liệu này vào listbox Việc này được thực hiện bởi 1 dòng code duy nhất. Đặt tên cho listbox của bạn: ![](http://farm4.staticflickr.com/3740/11961472144_46f86145ef_o.png") Sửa event OnLoaded lại như sau: \[code lang=csharp\] private void OnLoaded(object sender, RoutedEventArgs routedEventArgs) { if (StaticData.FoodItemCollection.Count == 0) { LoadData(); FoodListBox.ItemsSource = StaticData.FoodItemCollection; } } \[/code\] Sau đó, bấm chạy thử trên Emulator hay trên Device tùy thích ![](http://farm4.staticflickr.com/3712/11961887436_8c77ca2cce_o.png") Và đây chính là thành quả của các bạn ![](http://farm4.staticflickr.com/3826/11961917396_bb27d31e3c_o.png")

## **2.6 DataTemplate**

Vậy là dữ liệu đã được hiển thị trên giao diện, nhưng không theo cách bạn mong muốn Chính vì thế, ta sẽ tạo một DataTemplate cho Listbox, mục đích là để "định nghĩa" cách hiển thị dữ liệu Vào code XAML của bạn, bấm chọn Document Outline ![](http://farm8.staticflickr.com/7314/11961424713_95b6a4b3de_o.png") Document Outline là nơi thể hiện toàn bộ mọi thứ có trên giao diện của bạn dưới dạng cây Bấm chuột phải vào ListBox của bạn và chọn ![](http://farm6.staticflickr.com/5535/11961470493_0b1b86675f_o.png") ![](http://farm4.staticflickr.com/3666/11962019876_076607132c_o.png") Đặt tên cho DataTemplate của bạn rồi nhấn OK ![](http://farm8.staticflickr.com/7324/11961488143_d9af248312_o.png") Nếu bạn chọn Define in Application, DataTemplate này có thể được dùng ở mọi page trong project của bạn mà không cần phải khai báo lại Trong lúc thiết kế, bạn có thể thấy thiết kế của mình được hiển thị trực quan ![](http://farm8.staticflickr.com/7405/11961742983_933fc0557f_o.png") Nhấn chạy một lần nữa, và mọi thứ sẽ đúng như ý bạn ![](http://farm8.staticflickr.com/7397/11961908164_dfe6879e28_o.png")

# **Event Handling**

Vậy là bạn đã có 1 listbox, bây giờ ta sẽ áp dụng một số sự kiện cho nó để thông báo cho người dùng biết họ đã chọn Listbox nào Trong Property của FoodListBox, chọn nút Event ![](http://farm4.staticflickr.com/3678/11961483605_78ff2960f3_o.png") Double Click vào event "Selection Changed" để khai báo event Thêm đoạn code sau vào event mới được tạo \[code lang=csharp\] if (FoodListBox.SelectedIndex != –1) { FoodItem foodItem = FoodListBox.SelectedItem as FoodItem; MessageBox.Show(foodItem.FoodName); } \[/code\] Chạy thử và chọn một item bất kỳ ![](http://farm4.staticflickr.com/3751/11962377686_6b9e9bdb79_o.png") Thật tuyệt vời phải không Vậy là hết rồi, hẹn gặp lại các bạn ở episode tiếp theo của Series Absolute Beginner nhé