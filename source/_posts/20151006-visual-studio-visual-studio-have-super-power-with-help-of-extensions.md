---
title: '[Visual Studio] Visual Studio have Super Power with help of Extensions'
tags:
  - app
  - C#
  - hero
  - indent
  - resharper
  - Visual Studio
id: '488'
categories:
  - - uncategorized
date: 2015-10-06 07:07:30
---

Phải rồi, bạn đọc nó đúng rồi đó. Visual Studio có sức mạnh siu nhơn, và sau đây là lý do mà tôi nói nó có.

Bài viết này bao gồm các thủ thuật, tiện ích và hướng dẫn sử dụng những tính năng cực hay ho nhưng khá ít người biết tới của Visual Studio.
<!-- more -->
# Super Power 1: JetBrains ReSharper

ReSharper là một extension cực khủng của JetBrains. Nó sẽ đảm nhiệm vai trò dọn dẹp, trang điểm cho code của bạn đẹp như thơ, tăng hiệu suất làm việc, tăng khả năng maintenance, tăng tính tái sử dụng code vào nhiều project khác nhau. Bạn chưa tin ư, hãy xem phần [1.4. Các tính năng](#_Các_tính_năng)

## Nếu bạn là sinh viên

JetBrains ReSharper miễn phí cho sinh viên (họ còn miễn phí toàn bộ các sản phẩm khác nữa). Tuy nhiên, chương trình miễn phí này được giấu khá kỹ trên trang chủ của nó.

*   Truy cập vào link sau: [https://www.jetbrains.com/student/](https://www.jetbrains.com/student/)
*   Nhấn Apply Now ở khúc dưới
*   Bạn có nhiều tùy chọn chứng minh mình là sinh viên. Cách dễ nhất: dùng email đuôi .edu
    
    ![](https://farm6.staticflickr.com/5692/21937216876_1c6c37ee27_o.png)
    
    Ngoài ra còn có thể dùng thẻ sinh viên quốc tế hoặc giấy tờ chứng minh (lâu hơn một chút)
    
*   Một email gửi tới cho bạn, hướng dẫn cách thực hiện tiếp theo

## Nếu bạn không còn là sinh viên

Chia buồn với bạn, bạn sẽ phải mua bộ công cụ này nếu muốn sử dụng (có cờ rắc, nhưng ko khuyến khích)

## Cài đặt

Sau khi đã có license, bạn tiến hành cài đặt nó. File cài đặt khoảng hơn 100 MB. Tắt Visual Studio trước khi cài.

Sau khi cài xong, mở Visual Studio lên, và bạn sẽ thấy có nhiều khác biệt

## Các tính năng tuyệt zời

### Phân tích code

Khi mở một file .cs lên, ReSharper sẽ tự động phân tích code có trong file này và đưa ra các đề xuất hợp lý.

Nhìn bên phải, bạn sẽ thấy thanh cuộn mặc định được "tô điểm" bởi các vạch màu vàng đỏ xanh tùm lum. Đó là các điểm đánh dấu code "có vấn đề".

![](https://farm6.staticflickr.com/5822/21974855122_55a238a346_o.png)

Những vạch dọc:

*   Màu xanh lá cây: Những đoạn code đã được lưu
*   Màu vàng: Những đoạn code vừa mới chỉnh sửa hoặc thêm mới, chưa lưu

Những vạch ngang:

*   Màu cam: code bị thừa
*   Màu đỏ: code lỗi
*   Màu xanh lá cây: code có thể rút gọn

### Xóa code thừa

Click chuột vào một trong các vạch màu cam

![](https://farm6.staticflickr.com/5625/21799037180_ed7ddb0910_o.png)

Con trỏ sẽ nhảy tới ngay vị trí code đang có vấn đề

Bấm vào hình cái bóng đèn > Chọn dòng đầu tiên để sửa lỗi (đối với đa số trường hợp, dòng gợi ý đầu tiên là dòng gợi ý hợp lý nhất)

![](https://farm1.staticflickr.com/756/21975015462_1b21541615_o.png)

Như hình trên, khai báo "this." bị thừa. ReSharper sẽ giúp bạn loại bỏ chữ "this" bị thừa này.

> Bạn cũng có thể thực hiện việc xóa bỏ này hàng loạt. Nhấn dấu mũi tên nhỏ bên cạnh dòng đầu tiên để thấy nhiều tùy chọn hơn.

![](https://farm1.staticflickr.com/568/21799451878_dcd4f58000_o.png)

> Bạn cũng có thể thử dòng gợi ý thứ 2: Xóa bỏ toàn bộ code thừa trong file này. Bạn có thể bấm dấu mũi tên bên cạnh để thấy nhiều tùy chọn hơn
> 
> Visual Studio từ phiên bản 2015 cũng có một vài gợi ý tương tự.

Trỏ chuột vào hình bóng đèn sát bên dưới code > Show potential fixes

![](https://farm6.staticflickr.com/5759/21987321125_8800ff4578_o.png)

Cá nhân mình thấy cách làm của ReSharper hiện đại hơn, dễ nhìn hơn.

### Code đúng chuẩn

ReSharper giúp bạn code theo đúng chuẩn, thu gọn code, thay thế bằng các đoạn code dễ hiểu hơn, vân vân và vân

### Tự hoàn thành code khi đang gõ

Giả sử bạn muốn khai báo một biến string, kiểu private. Bạn chỉ cần gõ như hình dưới rồi nhấn ";"

![](https://farm6.staticflickr.com/5835/21997218621_deb4160238_o.png)

Bạn muốn sử dụng một method nào đó mà chưa khai báo namespace. Đối với Visual Studio, bạn sẽ phải gõ đầy đủ tên method. Sau đó phải click chuột vài lần thì Visual mới tự thêm namespace cho bạn. Đối với ReSharper, bạn chỉ cần gõ một phần của tên method. Khi method đó đã được tô sáng lên trong danh sách gợi ý, bạn chỉ cần gõ một trong các ký tự đặc biệt như dấu chấm, khoảng trắng, enter là mọi việc còn lại sẽ được hoàn tất.

![](https://farm6.staticflickr.com/5617/21961282096_1aeb6374f4_o.png)

### Thu gọn code

Nhấn vào một vạch ngang xanh lá cây bất kỳ trên thanh cuộn. Con trỏ sẽ nhảy tới dòng code có thể rút gọn.

Những đoạn code có thể rút gọn được gạch chân màu xanh lá cây. Click chuột vào đó > Click cái bóng đèn > Chọn dòng gợi ý đầu tiên

![](https://farm1.staticflickr.com/757/21799838418_c2efe59d5b_o.png)

![](https://farm6.staticflickr.com/5781/21800801089_3c639bb3b0_o.png)

Kết quả

![](https://farm1.staticflickr.com/652/21975514002_75edfe0026_o.png)

### Tự sinh code

Tạo một model mới như hình sau

![](https://farm1.staticflickr.com/677/21799893208_38cf1e1de1_o.png)

Khai báo Interface cho nó là "INotifyPropertyChanged" (chỉ cần gõ "INotiyPr" rồi enter là xong)

![](https://farm6.staticflickr.com/5702/21364996524_5d4864b173_o.png)

Sau khi nhấn enter, rõ rang model đã bị thiếu nhìu thứ quan trọng của INotifyPropertyChanged.

Nhấn chuột vào cái bóng đèn màu đỏ > Implement INotifyPropertyChanged

![](https://farm6.staticflickr.com/5806/21365175364_bd9f5fd1ff_o.png)

Và kết quả (trong lần thực hiện đầu tiên, ReSharper sẽ hỏi bạn cho phép nó thêm một số file vào thư mục Properties. Cứ cho phép nó nhé)

![](https://farm1.staticflickr.com/670/21975835712_8937950fbf_o.png)

### Code Generation

Sử dụng TestModel, bạn hãy thêm vào vài biến lấy lệ để test tính năng Code Generation

![](https://farm1.staticflickr.com/608/21988308215_a65b97951d_o.png)

Bạn vào menu ReSharper > Edit > Generate Code… (Menu này nằm ngang hàng với File – Edit – View - …)

Một ô nhỏ hiện ra, bạn chọn Properties

![](https://farm6.staticflickr.com/5747/21367253303_a2908587db_o.png)

Bạn chọn tất cả các trường muốn tạo Property > Tick luôn khai báo Notify On Property Changed (để tiện cho mô hình MVVM) rồi nhấn Finish

![](https://farm6.staticflickr.com/5673/21365647334_beb81dc63a_o.png)

Kết quả:

![](https://farm1.staticflickr.com/592/21365674894_e92e09147e_o.png)

Thật tuyệt phải ko?

### Đổi tên class – method – Hàm, vân vân và vân vân

ReSharper hỗ trợ bạn đổi tên bất kỳ thứ gì, và tên được đổi đó sẽ được thay đổi ở tất cả các file có sử dụng nó. Giả sử class TestModel này được sử dụng ở 3 file, và bạn muốn đổi tên nó thành NotTestModel, thì cả 3 file kia sẽ được cập nhật tên mới.

Đưa con trỏ chuột vào tên class TestModel

Chọn Menu ReSharper > Refactor > Rename…

![](https://farm1.staticflickr.com/656/21800814760_9f5904c298_o.png)

Một hộp thoại nhỏ hiện ra

![](https://farm6.staticflickr.com/5774/21367460363_e9ae701a09_o.png)

Sửa tên lại. Nếu bạn muốn có tính năng Undo, tick chọn bên dưới rồi Next

### Đưa string vào Resource

Bạn này làm app có Localization (aka: dịch các string trong app ra các ngôn ngữ khác nhau cho các thị trường khác nhau), hẳn là sẽ rất khổ sở khi phải đưa từng string từng string một vào Resource để dịch. Có bạn áp dụng phương pháp cuốn chiếu, làm tới đâu thêm string vào Resource tới đó. File Resource lúc nào cũng mở sẵn. Có bạn chọn cách làm xong app rồi mới đưa từng string một vào Resource bằng cách Copy > Paste rất thủ công

Và anh hùng ReSharper xuất hiện.

Để đưa một đoạn string vào Resource, bạn đưa con trỏ chuột vào string đó, chọn menu ReSharper > Refactor > Move…

![](https://farm6.staticflickr.com/5683/21962745436_65d58e77a8_o.png)

Một hộp thoại nhỏ hiện ra. Tại đây bạn có thể lựa chọn, thay đổi các thông số

![](https://farm1.staticflickr.com/708/21976791272_ee5c4dda71_o.png)

Nhấn Next và chiêm ngưỡng thành quả

![](https://farm6.staticflickr.com/5683/21963312926_2d5fb88a26_o.png)

Tuy nhiên, Method GetValue này đã lỗi thời rồi, phải sửa nó một chút như hình sau

![](https://farm6.staticflickr.com/5750/21801691668_e341198c6a_o.png)

> tính năng này cũng dùng được cho các đoạn string trong code XAML nhé

ReSharper còn hàng hàng tính năng khác chờ bạn khám phá

# Super Power 2: XAML Styler

Có khi nào bạn cảm thấy khó chịu khi code giao diện bằng XAML, và các thuộc tính cứ nằm luôn tuồn trên một hàng, kéo wá kéo lại quá vất vả?

Có khi nào bạn nhìn đống code XAML, và chẳng biết phải tìm thuộc tính mình cần ở đâu?

XAML Styler đã đến. Và nó sẽ giúp bạn format code XAML tuyệt đẹp.

## Cài đặt

Vào Menu Tools > Extension and Updates…

![](https://farm1.staticflickr.com/759/21801774968_c0b7347871_o.png)

Tiếp tục chọn mục Online > Visual Studio Gallery > Nhập "XAML Styler" vào ô tìm kiếm và cài đặt XAML Styler

![](https://farm1.staticflickr.com/574/21989659205_849101bec2_o.png)

## Thiết lập thuộc tính

Vào menu Tools > Option > kéo xuống dưới cùng chọn XAML Styler

Chỉnh các thuộc tính như hình

![](https://farm1.staticflickr.com/685/21990196465_9187c0695b_o.png)

Chắc các bạn thắc mắc tại sao lại phải chỉnh như vậy :3. Đó là theo kinh nghiệm cá nhân của mình để tăng hiệu suất và giảm sai sót thôi.

## Sử dụng

Sử dụng rất đơn giản: bạn mở code XAML lên > click chuột phải > Format XAML

Before

![](https://farm6.staticflickr.com/5782/21367559744_f92258543e_o.png)

After

![](https://farm1.staticflickr.com/754/21990346995_70aa6b546e_o.png)

# Super Power 3: Indent Guide và C# Outline

## Indent Guide

Qua hình chụp screenshot nãy giờ, chắc các bạn cũng thắc mắc các đường kẻ dọc trong screenshot có mà Visual Studio của bạn không có? Đó chính là Indent Guide Extension. Chức năng của nó rất đơn giản, vẽ ra các đường kẻ dọc để code bạn dễ nhìn hơn, canh theo đúng hàng đúng lối.

![](https://farm1.staticflickr.com/590/21369345023_260fea1079_o.png)

Ngay khi cài xong, khởi động lại Visual Studio, mở một Project bất kỳ và bạn sẽ thấy thành quả

![](https://farm6.staticflickr.com/5799/21803058558_994e9e1edc_o.png)

## C# Outline

Nhìn hình trên, chắc bạn cũng thấy lạ là tại sao cấu trúc if cũng có một dấu "-" nho nhỏ để đóng ra mở vô. Đó chính là khả năng của Extension C# Outline.

C# Outline giúp bạn tạo một code block ở mọi dấu ngoặc nhọn. Như vậy bạn có thể đóng mở tất cả các cấu trúc khác nhau như If then else, while do, switch case, vân vân và vân vân

> tên chính thức của nó là C# outline 2015, dành cho Visual Studio 2015 nhé bạn

![](https://farm6.staticflickr.com/5724/21804181309_0c316434c3_o.png)

Hết gòi, hẹn gặp lại bạn ở bài sau