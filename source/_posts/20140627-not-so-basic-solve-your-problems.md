---
title: '[Not so Basic] – Solve your problems'
tags:
  - problem
  - solve
id: '337'
categories:
  - - CSharp
date: 2014-06-27 07:25:45
---

Okie, bạn đã có trong tay hầu như mọi thứ cần thiết để tạo ra ứng dụng của mình:

[\[Basic for Absolute Beginner\] – \[Part 1\] – Layout with XAML](http://cuoilennaocacban2.wordpress.com/2013/11/22/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner/)

[\[Basic for Absolute Beginner\] – \[Part 2\] – Layout with XAML](http://cuoilennaocacban2.wordpress.com/2014/01/21/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner-part-2/)

[\[Basic for Absolute Beginner\] – \[Part 3\] – App's Structure and how customized it](http://cuoilennaocacban2.wordpress.com/2014/02/26/basic-for-absolute-beginner-part-3-apps-structure-and-how-customized-it/)

[\[Basic for Absolute Beginner\] – \[Part 4\] – Basic Steps for a new app](http://cuoilennaocacban2.wordpress.com/2014/03/31/basic-for-absolute-beginner-part-4-basic-steps-for-a-new-app/)

[\[Basic for Absolute Beginner\] – \[Part 5\] – Analytics for your apps](http://cuoilennaocacban2.wordpress.com/2014/04/04/basic-for-absolute-beginner-part-5-analytics-for-your-apps/)

[\[Basic for Absolute Beginner\] – \[Part 6\] – Source Control](http://cuoilennaocacban2.wordpress.com/2014/05/02/basic-for-absolute-beginner-part-6-source-control/)

Và trong lúc làm, bạn gặp phải một vấn đề gì đó. Làm thế nào để giải quyết nó?

Đây sẽ là bài viết cuối cùng trước khi thi của mình

# Vấn đề của bạn là gì?

Bạn đang làm một ứng dụng xem tin tức. Và bạn muốn những tin mà người đọc xem rồi sẽ không xuất hiện lại nữa.

Bạn muốn sắp xếp theo thứ tự một mảng dài 500 000 phần tử.

Bạn muốn tìm kiếm một phần tử trong mảng 1 triệu phần tử.

Vân vân và vân vân.

Đây là loại vấn đề mà bạn cần phải giải quyết trước khi tiếp tục xây dựng ứng dụng của mình

![](https://farm6.staticflickr.com/5536/14517912312_3f2977f5e1_o.jpg)
<!-- more -->
# Giải quyết vấn đề của bạn

Bước đầu tiên, một phương pháp ultimate để giải quyết rất nhiều vấn đề, từ ngớ ngẩn đến phức tạp. Google nó.

## Search Google

### Search bằng tiếng anh cho vấn đề của bạn.

Cái này chỉ là kinh nghiệm cá nhân. Bạn sẽ dễ dàng bắt gặp vấn đề của mình hơn, và khả năng cao là đã có người giải quyết được. Tuy nhiên, cái này đỏi hỏi bạn phải có khả năng tiếng anh tốt

### Tham khảo các đoạn code mẫu từ các nguồn uy tín

Một trang diễn đàn không tên tuổi sẽ không thể nào đánh bại một câu trả lời được đánh dấu và bình chọn trong StackOverflow. Một đoạn code nằm lưng chừng không thể nào bằng một bài viết trong Nokia Developer.

Và uy tín hơn hết tất cả các thứ trên cộng lại, đó chính là thư viện tham khảo MSDN. Tuy nhiên thư viện này chỉ là một bộ tài liệu khổng lồ cho Microsoft Technologies. Hoạt động không khác gì một quyển từ điển. Bạn có thể tra cứu định nghĩa hàm, chức năng, tham số, giá trị. Vân vân và vân vân.

### Từ khóa, từ khóa, từ khóa

Từ khóa đóng một vai trò quan trọng khi tìm kiếm vấn đề của bạn.

Ví dụ như cùng một vấn đề, trên Windows có thể sẽ dùng thuật toán này, nhưng Windows Phone sẽ dùng thuật toán khác. Vì Windows Phone có nguồn tài nguyên giới hạn hơn rất nhiều lần so với Windows. Vì vậy hãy thêm từ khóa: Windows Phone vào

Mà khoan. Các công nghệ .NET của Microsoft phát triển liên tục. Vì vậy bạn phải kèm theo luôn số phiên bản của nền tảng bạn đang lập trình.

Ví dụ: Querry SQL database in Windows Phone 8.1

## Ask

Khi bạn gặp một vấn đề về kỹ thuật, mà chỉ có người tạo ra kỹ thuật đó mới có thể giài quyết, cách tốt nhất là "hỏi".

Tuy nhiên, hỏi ở đây không có nghĩa là bạn bắt tay vào hỏi liền tại chỗ. Kiểu này rất hay gặp đối với sinh viên Việt Nam. Bạ đâu cũng hỏi. Hỏi cũng cần phải có văn hóa riêng.

Giả sử như bạn đang gặp một vấn đề về kết nối mạng. Bạn mới thử chừng 1-2 cách nhưng chưa cách nào thành công. Bạn liền kiếm ngay một đàn anh, một chiên za, ít ra cũng là một người có hiểu biết về vấn đề này để hỏi. Nếu họ lịch sự, họ sẽ trả lời. Nếu không, họ sẽ im lặng, và bạn đánh giá họ là "không nhiệt tình".

### Why? You asked?

Vì mục tiêu chính của bạn không phải là học hỏi. Mà là lợi dụng sự hiểu biết của họ để giải quyết vấn đề cho mình. Có hẳn một công việc trả lương cho nó, đó là "Tư vấn". Đặc biệt là tư vấn kỹ thuật giá rất mắc, mà bạn đang muốn miễn phí ư? No way.

Ít ra bạn cũng phải cho họ biết tường tận vấn đề của mình, bạn đã thử những cách nào, kết quả ra sao, chuẩn đoán của bạn là gì (phải thử chừng 10 cách rồi hẵng hỏi), và đừng bắt họ phải trả lời ngay. Rất có thể trong những cách mà bạn thử nghiệm, có nhiều cách hay ho mới lạ sẽ mở đường cho một hướng đi mới, một công nghệ mới, hoặc sẽ là bình minh của cả một ngành khoa học mới. Và người được hỏi sẽ rất có hứng thú trả lời câu hỏi của bạn, thậm chí mời bạn tới trao đổi thêm.

Bạn có biết một nhà khoa học khi cố gắng chứng minh một tiên đề Euclid, ông ấy đã thử một cách mà trở thành một ngành toán học mới, gọi là "Hình học phi Euclid". Nhà khoa học đó tên là Lobachevsky.

Và điều tối quan trọng là **"Search trước khi hỏi".** Vấn đề đối với bạn là lạ hoắc, nhưng đối với những người khác thì vô cùng cơ bản, và đã có câu trả lời nằm chình ình ở một chỗ nào đó.

## Brainstorm

Đối với các vấn đề mà chỉ có mình bạn giải quyết được. Thì Brainstorm là giải pháp duy nhất.

Tại sao chỉ có mình bạn giải quyết được nó? Vì bạn là người duy nhất suy nghĩ về nó. Hãy thử 40 phương pháp sáng tạo (google it). Hãy thử đảo ngược vấn đề, hãy thử suy nghĩ theo một hướng khác.

## Share your idea

Chia sẻ vấn đề của bạn, ý tưởng của bạn, và bạn sẽ có những cải tiến đáng giá, ít ra là những khuyết điểm mà bạn không hề nhận thức rằng nó tồn tại. Đối với các loại vấn đề, bạn có thể sẽ gặp những cách giải quyết vô cùng sáng tạo. Tuy nhiên, hãy đề phòng nạn "đạo ý tưởng", xảy ra ở khắp mọi nơi trên thế giới. Vì vậy, chỉ chia sẻ cho những người mà bạn biết rằng họ sẽ không ăn cắp ý tưởng của mình, trừ phi bạn có đăng ký bảo hộ ý tưởng đó :3