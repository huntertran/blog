---
title: '[Computer Tips] [Part 2] Be an Advanced user with Web Browser'
tags:
  - add-on
  - noscript
  - ublock
id: '448'
categories:
  - - Computer Tips
date: 2015-07-17 03:07:53
---

Part 1 ở đây: [Phần 1](https://cuoilennaocacban2.wordpress.com/2015/07/13/computer-tips-part-1-be-an-advanced-user-of-web-browser/)

Sau khi đã có một trình duyệt web sạch sẽ, cùng các addon hữu ích, chắc bạn sẽ tự hỏi: "Còn gì hay ho nữa không"

Cộng đồng phát triển add-on cho Firefox và Chrome là vô cùng bự, và bạn sẽ tìm thấy kha khá những add-on phù hợp với mình.

Bài viết này sẽ hướng dẫn cách sử dụng một số addon kỳ quái khác, giúp trải nghiệm duyệt web của bạn đã hơn nữa

Việc sử dụng không đúng cách các Addon này sẽ khiến trang web không hiển thị được, hoặc thiếu tính năng.

Có một số add-on chỉ có Firefox mới có, và ngược lại
<!-- more -->
*   [Các addon nâng cao](#các-addon-nâng-cao)
    *   [NoScript – Firefox only](#noscript--firefox-only)
        *   [Thiết lập](#thiết-lập)
        *   [Sử dụng](#sử-dụng)
        *   [Blacklist một đoạn Script](#blacklist-một-đoạn-script)
        *   [Tips and Tricks](#tips-and-tricks)
        *   [Lợi và hại](#lợi-và-hại)
    *   [uBlock – Firefox và Chrome](#ublock--firefox-và-chrome)

# Các addon nâng cao

## NoScript – Firefox only

Một website được hiển thị trên màn hình của bạn dựa trên 3 yếu tố: HTML, CSS và JavaScript. HTML sẽ chứa nội dung, CSS sẽ định dạng cho nội dung đó (canh chỉnh lề, màu sắc, kích thước) và JavaScript sẽ chịu trách nhiệm tính toán, hiệu ứng, tất tần tật mọi thứ khác. Vấn đề nằm ở chỗ, khi load một website, không phải đoạn Script nào cũng cần thiết để web hoạt động, có các đoạn Script hoàn toàn không liên quan như theo dõi hành vi người dùng, tải quảng cáo, phân tích dữ liệu cho các bộ máy tìm kiếm. Đó là lý do NoScript ra đời Theo mặc định, NoScript sẽ chặn tất cả, và chỉ chừa lại các đoạn Script bạn cho nó chạy mà thôi. Tải tại đây: [https://addons.mozilla.org/en-us/firefox/addon/noscript/](https://addons.mozilla.org/en-us/firefox/addon/noscript/) Sau khi cài đặt, đây sẽ là hình ảnh các bạn nhận được khi mở bất kỳ trang web nào, khá khó chịu phải ko? ![](https://farm1.staticflickr.com/264/19575563008_f13b274796_o.png)

### Thiết lập

Để thiết lập cho NoScript, click chuột vào nó và chọn Option ![](https://farm1.staticflickr.com/436/19763863685_538c579046_o.png) Chọn thẻ Notification để bỏ dòng thông báo xuất hiện bên dưới trình duyệt Bỏ chọn các dòng được đánh dấu bằng mũi tên ![](https://farm1.staticflickr.com/481/19768621411_6022b4cf6a_o.png) Vậy là xong bước thiết lập

### Sử dụng

Quay trở lại google, khi vào google, bạn sẽ không còn thấy thanh thông báo script đã bị chặn nữa. Thử tìm kiếm một từ khóa nào đó, bạn sẽ thấy có nhiều hiện tượng lạ khác với google bình thường Đầu tiên là google quay trở về cái giao diện cổ xưa cũ rích ![](https://farm1.staticflickr.com/511/19577369119_a5df6cf9d9_o.png) Tính năng Instant Search cũng mất luôn. Chuyện gì đang xảy ra? Đơn giản là bạn đang chặn toàn bộ JavaScript của google, và đây là tất cả những gì mà Google có thể làm được khi thiếu JavaScript Để cho phép JavaScript của google hoạt động, rê chuột lên biểu tượng của NoScript ![](https://farm1.staticflickr.com/527/19141449444_642fd3f5ce_o.png) Và chọn Allow google.com Thế là google tự động reload, và giao diện quen thuộc đã quay trở lại ![](https://farm1.staticflickr.com/407/19141472164_c0f391e0fb_o.png) Biểu tượng NoScript giờ biến thành chữ S, nhưng vẫn có một dấu chặn đỏ nho nhỏ bên dưới. Đó là vì vẫn còn Script bị chặn, bạn nên rê chuột lên để kiểm tra thử ![](https://farm1.staticflickr.com/539/19577487129_8a934d4edc_o.png) Vẫn còn 1 Script là gstatic.com đang bị chặn. Bạn có muốn cho phép nó hay ko là tùy bạn. Nên nhớ, một số đoạn Script cần thiết phải cho phép để website hoạt động đúng như những gì nó được sinh ra để làm Một ví dụ khác. Trang [http://news.zing.vn/](http://news.zing.vn/) Ở trang này, lúc đầu cũng như google, tuy nhiên, khi rê chuột lên icon noscript, bạn sẽ thấy điều khác biệt ![](https://farm1.staticflickr.com/357/19764202055_ea391aa0ce_o.png) Đoạn Script gì đây? Adtimaserver.vn là gì? Đầu tiên hãy cho phép zing.vn Trang news.zing.vn hiện ra đẹp đẽ, nhưng nhìn có vẻ hơi trống trải. Bạn tự hỏi những chỗ trống đó là gì? ![](https://farm1.staticflickr.com/525/19757017192_23fab3b91b_o.png) Bây giờ hãy tiếp tục cho phép adtimaserverv.vn và cảm nhận điều khác biệt ![](https://farm1.staticflickr.com/260/19141748024_f1c4f57d76_o.png) Bắt đầu lag, quảng cáo tràn ngập khắp mọi nơi. Và đó chính là chức năng của đoạn Script đó. Nếu bạn để ý, sẽ thấy ngoài 2 script ban đầu, còn rất nhiều script khác được chêm vô. Điều đó không có gì ngạc nhiên, một đoạn JavaScript có thể gọi thêm nhiều đoạn JavaScript khác hỗ trợ cho nó. Như vậy, quyết định cho đoạn Script nào chạy, đoạn nào không là ở bạn.

### Blacklist một đoạn Script

Sau khi biết chắc một đoạn script nào đấy chỉ dành cho quảng cáo, hoặc chỉ dùng để theo dõi người dùng, bạn có thể đưa nó vào blacklist ngay và luôn để từ lần sau, NoScript sẽ chặn nó mà không hỏi ý kiến bạn nữa Đưa chuột vào Icon NoScript, chọn Untrusted > chọn đoạn script muốn blacklist ![](https://farm1.staticflickr.com/308/19577587378_2f862f7a44_o.png) Cẩn thận không blacklist nhầm các đoạn script quan trọng nhé Sau cùng, khi toàn bộ script trên một trang web đã được xử lý (cho phép hoặc bị đưa vào blacklist), biểu tượng NoScript sẽ biến thành như này ![](https://farm1.staticflickr.com/433/19758359822_686a2ecf41_o.png)

### Tips and Tricks

*   Để tạm thời cho phép toàn bộ script của một trang, bạn có thể chọn Temporarily allow all on this page
*   Trong một số trường hợp, trang web bị redirect (aka: chuyển qua một trang khác) quá nhanh trước khi bạn kịp "Allow" một đoạn script của trang đó, bạn có thể sử dụng tính năng "Recently Blocked Script" để cho phép các đoạn script bị block gần đây.
*   Bạn có thể Export / Import toàn bộ thiết lập của NoScript trong option của nó
*   Một số trang web không cho bạn blacklist các JavaScript của nó bằng một thủ thuật tinh vi là steal focus, làm cho bạn không thể nào click được Untrust. Bấm F12, chọn thẻ Debugging > Bấm vào nút pause (có hình 2 cái vạch giống vầy || ), là bạn có thể untrust các đoạn script của nó
    
*   Gõ about:config trên trình duyệt, tìm noscript.untrusted để xem toàn bộ các script đang bị blacklist. Bạn có thể copy danh sách này và paste nó cho bạn bè của mình. Của mình là
    

```

"admicro.vn adtimaserver.vn doubleclick.net google-analytics.com googlesyndication.com googletagmanager.com googletagservices.com microad.net scorecardresearch.com http://admicro.vn http://adtimaserver.vn http://doubleclick.net http://google-analytics.com http://googlesyndication.com http://googletagmanager.com http://googletagservices.com http://microad.net http://scorecardresearch.com https://admicro.vn https://adtimaserver.vn https://doubleclick.net https://google-analytics.com https://googlesyndication.com https://googletagmanager.com https://googletagservices.com https://microad.net https://scorecardresearch.com"
```

### Lợi và hại

Lợi

Hại

Thời gian load trang nhanh hơn

Thiết lập phức tạp

Trang web đỡ rối mắt hơn

Phải thiết lập cho từng trang web một

Đỡ tốn tiền Internet (nếu bạn dùng gói xài nhiu trả nhiu)

Web chạy mượt mà hơn

Loại bỏ theo dõi hành vi người dùng của các website

Ngăn ngừa các nguy cơ bảo mật kiểu "Click vào đây để nhận quà", click vào thì dính virus

Chặn luôn các thủ thuật câu like của các trang web (nút like ẩn dưới các chức năng bẫy người dùng click vô)

## uBlock – Firefox và Chrome

Không khuyến khích sử dụng Add-on này, vì nó sẽ chặn quảng cáo, là cần câu cơm của các trang web Bạn có bao giờ khó chịu khi mở một website lên mà quảng cáo tràn ngập, không thấy nội dung đâu hết? Các pop up hiện ra liên tục với cường độ cao, các bẫy click mà khi click vào thì quảng cáo nhảy xổ ra tràn ngập màn hình? Đã đến lúc chấm dứt cơn ác mộng đấy, bằng một add-on gọi là uBlock Tải tại đây:

*   Chrome: [https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
*   Firefox: [https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)

Trước khi sử dụng nó, khuyến cáo bạn nên gỡ tất cả các add-on chặn quảng cáo khác Cách sử dụng rất đơn giản, bấm vào biểu tượng của nó > bật / tắt cái nút xanh to đùng để bật / tắt quảng cáo Trước khi cài / khi bật quảng cáo ![](https://farm1.staticflickr.com/544/19143668994_c079ef0d7a_o.png) Sau khi cài / Khi tắt quảng cáo bằng cách kích hoạt uBlock ![](https://farm1.staticflickr.com/548/19578291190_af7efd9481_o.png) Bạn có thể đọc thêm về hướng dẫn sử dụng tại đây [https://github.com/gorhill/uBlock#documentation](https://github.com/gorhill/uBlock#documentation) Happy surfing the Internet