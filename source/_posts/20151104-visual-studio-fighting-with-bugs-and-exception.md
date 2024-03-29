---
title: '[Visual Studio] Fighting with Bugs and Exceptions'
tags:
  - advanced
  - bugs
  - exception
  - Visual Studio
id: '522'
categories:
  - - uncategorized
date: 2015-11-04 23:19:10
---

Lập trình bằng Visual Studio, tới một thời điểm nào đó ai cũng sẽ gặp bug và Exception. Đối với một số exception, Visual Studio sẽ bôi vàng đoạn code gây ra exception, nhưng đối với một số exception khác, Visual Studio lại nhảy hẳn ra ngoài. Vì sao vậy? Tại sao không cho tôi biết code chỗ nào bị lỗi.

Visual Studio 2015 có một cải tiến đáng giá giúp lập trình viên biết chính xác chỗ code nào bị exception, và một số cải tiến vô cùng đáng giá khác khi debug một đoạn code

<!-- more -->

# 1. Advanced Debugging

Tất cả mọi người đều biết, để debug một đoạn code, bạn thường đặt một break point. Khi code chạy tới đó, nó sẽ dừng ngay tại Breakpoint đó. The end. Hết phim. Tuy nhiên, nếu bạn đọc bài blog này: [\[Visual Studio\] Performance, performance, performance (with the help of Visual Studio "PerfTips")](https://cuoilennaocacban2.wordpress.com/2015/10/22/visual-studio-performance-performance-performance-with-the-help-of-visual-studio-perftips/), bạn sẽ thấy một công dụng nữa của Breakpoint dành cho việc đo đạc thời gian chạy một đoạn code. Ngoài ra, Breakpoint còn có một số công dụng khác nữa

## 1.1. Output Log with Breakpoint

![](/images/flickr/5628/22152610574_b5e8c867c4_o.png)

Trong vòng lặp trên, bạn sẽ thấy có dòng "Debug.WriteLine" dùng để xuất một thông tin gì đó ra màn hình Output. Thông tin này sẽ giúp bạn biết code đã chạy tới dòng này, và xuất ra các giá trị mà bạn mong muốn.

![](/images/flickr/618/22152668514_87a33835e7_o.png)

Từ giờ, bạn không cần phải làm thủ công như vậy nữa.

Đưa chuột lại gần Breakpoint, một menu nhỏ xíu hiện ra, nhấn vào dấu răng cưa

![](/images/flickr/706/22775443405_64dfbcf543_o.png)

Một cái cửa sổ hiện ra, chèn vào giữa đoạn code đặt breakpoint của bạn. Tick chọn ô Action. Bạn sẽ thấy tính năng "Log a message to output Windows"

![](/images/flickr/5649/22761956172_d042077119_o.png)

Gõ vào trong ô đó những thứ bạn muốn xuất ra cửa sổ output. Biến thì để trong dấu ngoặc nhọn. Thế là xong

![](/images/flickr/5813/22154779113_ab9acf18e1_o.png)

Khi chạy lại app, cửa sổ output sẽ là

![](/images/flickr/5803/22762522502_765d5041fe_o.png)

Bạn thấy con số nằm trong ngoặc kép là vì nó là kiểu string, không phải int. Nên khi hiển thị, Visual Studio sẽ đưa nó vào trong ngoặc kép

Bây giờ, hãy so sánh một chút

  

|  | **Breakpoint "Action"** | **Debug.WriteLine()** |
|---|---|---|
| **Lợi** | Nhanh chóng, đơn giản<br><br>Không thay đổi code<br>Có thể chỉnh sửa khi ứng dụng đang chạy<br>Có thể kết hợp với Condition của Breakpoint<br>Có thể quản lý tập trung trong cửa sổ Debug | Sử dụng linh hoạt<br><br>Trực quan, dễ hiểu<br>Có thể chèn nhiều dòng |
| **Bất lợi** | Chỉ xuất ra được 1 dòng (mình chưa tìm được cách xuống dòng) | Phải thay đổi code<br><br>Không thể chỉnh sửa khi app đang chạy<br>Dùng Debug.WriteLineIf() để thêm điều kiện<br>Muốn tìm phải dùng Ctrl + F để tìm kiếm phrase như thông thường<br>Giảm hiệu suất (không đáng kể, và không ảnh hưởng khi Release) |

## 1.2. Condition Breakpoint

Tiếp tục tick chọn ô Condition, cửa sổ được mở rộng ra để lộ nhiều tùy chọn hơn cho bạn

![](/images/flickr/757/22588283440_b481c716fc_o.png)

Bạn có nhiều tùy chọn để quyết định xem là Visual Studio có dừng lại ở Breakpoint này hay không. Trong số đó có

*   Conditional Expression: Biểu thức điều kiện: Sẽ dừng ở breakpoint khi điều kiện đúng

*   Hit Count: Số lần chạy qua: Cứ mỗi lần chạy qua breakpint này, Visual Studio sẽ tính là một hit. Khi đạt tới số lượng hit nhất định do bạn đặt thì sẽ dừng.
*   Filter: Sẽ dừng ở Breakpoint khi một số điều kiện đặc biệt được thỏa mãn (ví dụ như MachineName, ProcessId, vân vân)

Đối với App Windows, bạn sẽ cần dùng 2 cái đầu tiên nhiều nhất

Giả sử mình muốn dừng lại ở lần chạy thứ 9, và xuất ra màn hình biến ở lần chạy này, thì thiết lập như sau:

![](/images/flickr/5675/22787742791_38aeba8663_o.png)

# 2. The new Exception Settings

Đã bao giờ bạn gặp phải cái lỗi ở cái dòng lạ hoắc như vầy chưa?

![](/images/flickr/778/22155676943_b38eeef94c_o.png)

DISABLE\_XAML\_BREAK\_ON\_UNHANDLED\_EXCEPTION

Global::System.Diagnostics.Debugger.Break();

Cái này là gì

Hoặc lỗi như vầy

![](/images/flickr/5810/22776832185_80b555ab2f_o.png)

"An exception of type "Blah blah blah" occurred in Yourappname.exe but was not handled in user code", và kèm theo đó là Visual Studio dừng ở một dòng lạ hoắc, và bạn biết chắc chắn là lỗi xảy ra ở chỗ khác, không phải dòng này.

Đó là lý do ta sẽ dùng Exception Setting để nhảy tới đúng chỗ code sinh ra lỗi

Bạn vào Debug > Windows > Exception Settings…

![](/images/flickr/750/22788116721_a7e75bc800_o.png)

Copy tên của Exception, trong trường hợp trên là "System.Exception" và paste nó vào ô tìm kiếm. Tíck chọn kết quả hiện ra

![](/images/flickr/592/22588970370_394a956f21_o.png)

Chạy lại app. Và bây giờ, Visual Studio sẽ nhảy tới đúng dòng bị lỗi

![](/images/flickr/5829/22763429822_fe3f21d523_o.png)

Quá tuyệt, phải không

Đón xem các bài blog tiếp theo về các tính năng cực kute của Visual Studio nhé.