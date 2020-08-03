---
title: '[Windows Store] Universal Apps across all Windows devices'
tags:
  - universal
  - windows phone
  - windows store
id: '313'
categories:
  - - C#
  - - c
    - Windows Phone
    - Windows Store App
date: 2014-04-13 09:24:26
---

Ở hội nghị BUILD 2014, Microsoft đã nhắc tới Universal App, ứng dụng có thể chạy được trên cả Windows và Windows Phone

Và ngay bây giờ, từ bản cập nhật Update 2 RC của Visual Studio 2013, bạn đã có thể xây dựng một ứng dụng như thế

![](http://farm8.staticflickr.com/7132/13789811995_025cfbd0bc_o.png)

<!-- more -->

# Cập nhật Visual Studio 2013 lên Updat 2 RC

Ngày 13-04-2014: Link tải: [http://blogs.msdn.com/b/windowsazure/archive/2014/04/09/deep-dive-visual-studio-2013-update-2-rc-and-azure-sdk-2-3.aspx](http://blogs.msdn.com/b/windowsazure/archive/2014/04/09/deep-dive-visual-studio-2013-update-2-rc-and-azure-sdk-2-3.aspx)

# Tạo Project Universal

Sau khi cài đặt xong, bạn sẽ có thêm một số tùy chọn mới trong Visual Studio

![](http://farm8.staticflickr.com/7212/13789855595_5d445495c2_o.png)

Chọn New Project

![](http://farm4.staticflickr.com/3808/13790231944_a53d45556f_o.png)

Chọn Visual C# > Store Apps > Universal Apps

Tạo project xong, bạn sẽ có một Solution như trong hình dưới

![](http://farm8.staticflickr.com/7447/13789942533_67c31f57db_o.png)

Nhìn vào là ta cũng biết ngay, Project Windows 8.1 và project Windows Phone 8.1

Còn Project “Shared” sẽ chứa các file dùng chung, cụ thể là Model và View Model

Ta sẽ tạo một ứng dụng đọc tin RSS đơn giản nhé

# Xây dựng Model và ViewModel

Tạo 2 thư mục mới tên là Model và ViewModel trong Project Shared

![](http://farm8.staticflickr.com/7414/13790305334_ae2e50f650_o.png)

Giả sử ta lấy trang này làm nguồn tin: [http://nhipsongso.tuoitre.vn/RssFeeds.aspx?ChannelID=430](http://nhipsongso.tuoitre.vn/RssFeeds.aspx?ChannelID=430)

Vậy Model sẽ bao gồm 1 title và 1 content

Ta tạo class News với 2 Properties là Title và Content, tương ứng với 2 biến là title và content

![](http://farm8.staticflickr.com/7387/13790346144_0eda252f4e_o.png)

Tạo file class trong Folder “Model”

![](http://farm8.staticflickr.com/7117/13790357494_ca7a9589b9_o.png)

Kết quả

![](http://farm8.staticflickr.com/7261/13790057603_73d1eb4d5e_o.png)

Tạo 2 biến private, dùng Resharper generate code ra Property

À mà quên, bạn phải khai báo kế thừa từ Interface INotifyPropertyChanged

![](http://farm4.staticflickr.com/3820/13790402894_fb134c2ecc_o.png)

Sau đó dùng Generate Code của Resharper

![](http://farm3.staticflickr.com/2934/13790084775_4662772e1a_o.png)

Chọn Property

![](http://farm8.staticflickr.com/7427/13790093875_eb1cc4a58d_o.png)

Chọn luôn như hình, bấm finish

![](http://farm8.staticflickr.com/7437/13790126693_3277529e49_o.png)

Thế là xong Model

Tạo class NewsViewModel trong Folder ViewModel

Trong class đó, khai báo một ObservableCollection

![](http://farm8.staticflickr.com/7440/13816583833_af8e4ff21f_o.png)

Tạo thêm một class StaticViewModels trong Folder ViewModel. File class này sẽ chứa các biến ViewModel dạng static mà ta sẽ sử dụng trong toàn App (Trước kia bạn thường khai báo chúng trực tiếp trong file App.xaml.cs, nay gom nó lại một nơi để dễ quản lý)

![](http://farm4.staticflickr.com/3811/13816896774_7eda94c0fd_o.png)

Trong file này, khai báo một Intance của NewsViewModel

![](http://farm8.staticflickr.com/7349/13817716275_cd906cb30a_o.png)

Tạo một thư mục Utilities, trong đó, tạo một class StaticMethod. Ta sẽ nhét code lấy HTML vào đây

![](http://farm8.staticflickr.com/7066/13816648423_80664aab92_o.png)

Trong này, gõ lệnh như sau

![](http://farm4.staticflickr.com/3718/13816652445_57b587715d_o.png)

Mở lại file NewsViewModel, tạo thêm method GetNewsAsyncTask

![](http://farm8.staticflickr.com/7090/13818091324_6f9567c7ce_o.png)

Thư viện HtmlDocument lấy từ HtmlAgilityPack trong Nuget, bạn phải add nó vào trong References của Project Windows 8.1

Sau khi xong, mở file MainPage.xaml của Project Windows 8.1 lên, thêm vào đó một ListBox để hiển thị danh sách tin

![](http://farm8.staticflickr.com/7396/13818053024_8a8f63e046_o.png)

Sau đó, mở file Code Behind và thêm những dòng sau:

![](http://farm6.staticflickr.com/5095/13818062924_84818d20d1_o.png)

Chạy thử

![](http://farm8.staticflickr.com/7371/13817751965_3b549082de_o.png)

# Xây dựng Template

Mở file MainPage.xaml trong Project Windows 8.1

Click chuột phải vào ListBox > Edit Additional Template > Create Empty

![](http://farm4.staticflickr.com/3794/13818117864_1bac953a3c_o.png)

Trong hộp thoại hiện ra, đặt tên nó là DataTemplate

![](http://farm8.staticflickr.com/7308/13818173834_c9983506b6_o.png)

Edit lại thành như sau

![](http://farm3.staticflickr.com/2903/13817868373_46fdd7e116_o.png)

Nhấn nút Local Machine để chạy thử

![](http://farm3.staticflickr.com/2844/13817864265_226b8940eb_o.png)

Thật tuyệt phải không?

# Tạo tương tự bên Windows Phone 8.1

Mở file MainPage.xaml của Project Windows Phone 8.1, copy và paste những thứ tương tự nhau

![](http://farm8.staticflickr.com/7457/13818218074_cfcbe1015f_o.png)

Tiếp tục mở code behind, và làm tương tự

![](http://farm4.staticflickr.com/3802/13818261174_95d475e43e_o.png)

Chọn lại Startup Project

![](http://farm8.staticflickr.com/7433/13817947335_83e0d03ede_o.png)

Ôi không, lỗi xuất hiện :’(

![](http://farm4.staticflickr.com/3809/13818652393_97c16b491e_o.png)

Khi bạn chọn Startup Project là Windows Phone, vì trong Reference của Windows Phone chưa có thư viện HtmlAgilityPack nên các tham chiếu tới thư viện này đều gặp lỗi

Ta add thêm thư viện này thông qua Nuget

![](http://farm4.staticflickr.com/3732/13818649855_10b7a8e826_o.png)

Một lỗi xuất hiện

![](http://farm4.staticflickr.com/3786/13818700683_7345a9aa07_o.png)

Nó phàn nàn là cái package này chả chứa file nào target tới Windows Phone 8.1 cả.

Vì dùng chung một bộ thư viện với Windows 8.1, Windows Phone 8.1 có khả năng add các DLL chỉ tương thích với Windows 8.1.

Chọn References > Ad References…

![](http://farm4.staticflickr.com/3793/13818743355_40d8d045a1_o.png)

Chọn mục Browse > Nhấn nút Browse, tìm đến thư mục bin > Debug của Windows 8.1 để add thư viện HtmlAgilityPack

![](http://farm8.staticflickr.com/7361/13819126364_02dda6cce9_o.png)

![](http://farm4.staticflickr.com/3763/13819120204_1aa2d2caff_o.png)

Và khi add xong, woala, mọi lỗi đã biến mất, code đã “green” trở lại

Lưu ý: Copy file Annotation.cs trong thư mục Property của Project Windows 8.1 và Paste nó vào bất kỳ chỗ nào trong Project Windows Phone (thực hiện việc Copy và Paste này trên Solution Explorer nhé). Nếu bạn có Resharper, bạn có thể để Resharper tự sinh lại file này bằng cách xóa các method OnPropertyChanged trong News Model, và để Resharper Implement lại nó

Chạy thử Project WP8.1

![](http://farm3.staticflickr.com/2891/13818903143_7951e186c4_o.png)

Done, bạn đã tự tạo một UniversalApp rồi đấy

# XAML và CodeBehind dùng chung

Như bạn có thể thấy ở hình trên, XAML và CodeBehind ở cả 2 Project rất giống nhau, hầu như không thay đổi gì cả

Cách đây rất lâu, trong một buổi training tại văn phòng Microsoft, đã có người từng hỏi “tại sao không dùng chung XAML cho cả Windows 8 và Windows Phone?”. Câu trả lời khi đó là Windows 8 và Windows Phone có bộ thư viện hơi khác nhau, nên một số control cũng khác nhau. Bây giờ, Microsoft đã đem lại khả năng “dùng chung” đó

Tạo một Folder tên View trong Project Shared

Add New một BlankPage, đặt tên nó là MainPage

![](http://farm8.staticflickr.com/7104/13819321114_2b92d23a10_o.png)

Copy và Paste code từ Project Windows Phone (cả XAML lẫn code Behind)

Ở trên cùng của XAML Editor, bạn sẽ thấy một Drop down list thú vị

![](http://farm8.staticflickr.com/7269/13819008325_d5b627d827_o.png)

Ở đây, bạn có thể thay đổi kiểu View mà Code XAML này được compile, trong hình đang chọn Windows Phone

Hãy thử chuyển nó sang Windows, bạn sẽ thấy giao diện Visual Editor thay đổi

Mở file App.xaml.cs, kéo xuống dòng 98, chỉnh sửa thành View.MainPage

![](http://farm4.staticflickr.com/3730/13819137865_97f6aea455_o.png)

Chỉnh Startup Project là Windows

![](http://farm6.staticflickr.com/5006/13819151033_e8fe2f0c54_o.png)

Chạy thử

![](http://farm3.staticflickr.com/2937/13819149935_bea2bb72da_o.png)

Chỉnh Startup Project thành Windows Phone, nhấn chạy thử

![](http://farm3.staticflickr.com/2891/13818903143_7951e186c4_o.png)

Thế là xong, bạn đã có một Page hiển thị được ở cả 2 giao diện nhé.

Trong các bài Blog sau, mình hy vọng sẽ có giải thích rõ ràng hơn về các Control dùng chung và cách hiển thị của chúng trên giao diện. Dù sao thì đây mới chỉ là Release Candidate. Sẽ còn thay đổi nhiều trong tương lai.