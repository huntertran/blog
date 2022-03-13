---
title: '[Windows 10] Prevent your app from being hidden on Windows Store'
tags:
  - hidden
  - search
  - store
  - windows
id: '595'
categories:
  - - CSharp
    - Windows 10
date: 2016-02-23 01:28:47
---

Trong những tháng vừa rồi, Window Store đang tiến hành thanh lọc Store, bỏ các app rác, đẩy các app tốt lên feature. Tuy nhiên, theo phản ánh của khá nhiều developer tại Việt Nam, Store đang tiến hành xử trảm khá nhiều app tốt của dev VN và các nước khác. Vậy phải làm thế nào?

Bài viết này cung cấp cho bạn những thông tin và các gợi ý để app của bạn mãi mãi nằm trên store, hiện trong search và leo lên tóp.
<!-- more -->

# 1. App của bạn, nội dung của bạn, hình ảnh của bạn, ý tưởng của bạn luôn

App này do bạn tạo ra, và bạn sở hữu tất cả các nội dung có trong app đó, ví dụ như hình ảnh, nhạc, video, vân vân và vân vân. Việc trùng ý tưởng với một app khác cũng không quan trọng lắm trong vấn đề này, nhưng phải chắc chắn rằng app của bạn hay hơn app "con nhà người ta", và con nhà người ta chưa đăng ký bản quyền cho cái ý tưởng đó.

Ví dụ như bạn làm một app có tính năng quản lý Page trên facebook. Rồi bạn lấy cái logo facebook gắn vô. Có thể trước kia người xét duyệt app lên Store họ ko thèm để ý vấn đề này, nhưng ngày hôm nay đã khác rồi, app của bạn sẽ fail ngay và luôn. Và các app khác trên Store có trường hợp tương tự cũng sẽ bị gỡ bỏ.

Một trường hợp khác, App của bạn bình thường, hình ảnh Free, nội dung hoàn toàn do bạn sáng tạo ra, nhưng cái tên lại có các từ dễ gây hiểu lầm. Đây là trường hợp mình gặp đối với 1 app của mình luôn. Đây là link tới App: [https://www.microsoft.com/store/apps/9nblggh5zchk](https://www.microsoft.com/store/apps/9nblggh5zchk). Lúc đầu mình đặt tên app này là "Windows Universal Logo Maker". Fail, fail và fail. Sau cùng, mình gửi message tới tester hỏi, và họ trả lời là chữ "Windows Universal" sẽ gây cho người dùng nhầm lẫn rằng app này là một app chính thức của Windows 10, do Microsoft phát hành, và họ cũng suggest mình đổi lại thành "Universal Logo Maker for Windows" -> Pass ngay tắp lự.

Một ghi chú nhỏ khác là không những tên app, mà tất cả các thông tin khác trong App description cũng phải mô tả tính năng của app đó, và không có các từ ngữ thuộc về các app nổi tiếng khác nhằm mục đích câu view, câu like, câu search cho app bạn.

Có qua cũng phải có lại. Nếu app của bạn thực sự tốt, nội dung độc đáo, tạo ra giá trị hữu ích cho người dùng, dần dần app của bạn sẽ được xếp lên đầu các kết quả tìm kiếm, thậm chí chỉ cần gõ từ khóa là app sẽ hiện ra ngay dưới khung suggestion luôn.

![](https://farm2.staticflickr.com/1572/24579499753_e6d445c1db_o.png)

Khuyến cáo: Sử dụng app Universal Logo Maker for Windows để tạo ra bộ Icon cho App của bạn trong 5 nốt nhạc.

# 2. App hay và độc đáo

Có hàng trăm ngàn app trên Store. Khi các chiêu trò câu view, câu like, câu search không còn tác dụng, thì bạn phải làm gì để người dùng tìm ra và download app của bạn?

Câu trả lời đến từ logo, screenshot, và tính năng của app bạn. App đó càng đẹp, càng độc đáo, càng hữu ích cho người dùng, thì khả năng họ tìm ra nó cũng càng cao. Có một từ ngữ vui để gọi hiện tượng này, là "hiệu ứng trái banh tuyết". App hay -> người dùng xài nhiều -> họ giới thiệu cho người khác -> Review tích cực nhiều -> lại càng dễ tìm trên Store -> càng nhiều người dùng hơn

Ví dụ, bạn làm một app Calculator chỉ với các tính năng cơ bản mà mấy cái app Calculator khác cũng có, thì 99% là sẽ chả có ai thèm để ý tới cái Calculator của bạn, bởi vì những cái app Calculator khác đang đứng đầu trên store và họ sẽ chọn những cái app đó.

# 3. Build 1 app hay thay vì build một chục app nhỏ tương tự

Ví dụ như bạn làm một game đua xe cho một chục thị trường khác nhau. Mỗi thị trường sẽ là một ngôn ngữ khác nhau. Điều này sẽ dễ dàng dẫn tới toàn bộ app giống giống nhau như thế fail một lượt. Thay vào đó, nếu bạn làm 1 app, với ngôn ngữ thay đổi tùy thuộc vào thị trường, thì app của bạn vẫn sẽ an toàn ở lại trên store, trong search, vân vân và vân vân.

App nhỏ:

![](http://az648995.vo.msecnd.net/win/2016/01/2_fr.png) ![](http://az648995.vo.msecnd.net/win/2016/01/3_es.png)

Kết hợp lại thành app bự với tính năng chọn ngôn ngữ, hoặc lấy theo ngôn ngữ hiện tại của hệ điều hành

![](http://az648995.vo.msecnd.net/win/2016/01/4_generic.png)

# 4. Giữ profile Windows Dev Center của bạn luôn luôn tốt

Điều cuối cùng mình muốn nhắn nhủ với các bạn Dev ngoài kia là hãy luôn cố gắng submit các app chất lượng cao lên Store. Trước khi làm một app gì, hãy search thử Store xem đã có app tương tự chưa để né tránh các trường hợp kể trên. Điều này giống như profile vay vốn ngân hàng vậy. Bạn càng "trong sạch" bao nhiêu, thì khả năng app của bạn lên top càng cao bấy nhiu.

# 5. Nếu app không lên Store sau khi submit thành công

Cố gắng chờ thêm 24 tiếng nữa. App thường sẽ xuất hiện trên Store bằng cách nhấn vào direct link sau khi submit thành công khoảng 24 tiếng. Và mất khoảng 8-24 tiếng để có thể hiện lên trên kết quả search.

Nếu chờ wài ko thấy lên, bạn có thể yêu cầu support tại: [support ticket](https://support.microsoft.com/en-us/getsupport?locale=EN-US&supportregion=EN-US&ccfcode=US&pesid=14654&oaspworkflow=start_1.0.0.0&tenant=store&supporttopic_L1=31762156&supporttopic_L2=31762179&ccsid=635888242224279047)

# 6. Nếu app bị ẩn, chỉ có direct link, không search được trên Store

Kiểm tra kỹ lại các gợi ý phía trên, đảm bảo rằng app của bạn không vi phạm bất kỳ điều gì, rùi gửi support ticket tại đây: [support ticket](https://support.microsoft.com/en-us/getsupport?locale=EN-US&supportregion=EN-US&ccfcode=US&pesid=14654&oaspworkflow=start_1.0.0.0&tenant=store&supporttopic_L1=31762156&supporttopic_L2=31762179&ccsid=635888242224279047). Bạn có thể yêu cầu họ giải thích chi tiết lý do tại sao (sử dụng ngôn từ lịch sự, nhã nhặn)

# 7. Promote app

Một khi app đã lên, promote nó nhìu lên cho mọi người biết, download và đánh giá tốt cho nó. App của bạn sẽ càng nặng ký hơn khi có nhiều user từ các nước khác nhau ngoài Việt Nam

Chúc app bạn lên Store suôn sẻ :D