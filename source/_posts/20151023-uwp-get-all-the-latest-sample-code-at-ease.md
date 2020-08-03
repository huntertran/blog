---
title: '[UWP] Get all the latest sample code at ease'
tags:
  - code
  - git
  - github
  - sample
  - sourcetree
  - uwa
  - uwp
  - windows 10
id: '509'
categories:
  - - c
    - Windows 10
date: 2015-10-23 01:01:30
---

English version available at: [https://tuanmsp.wordpress.com/2015/10/23/uwp-get-all-the-latest-sample-code-at-ease/](https://tuanmsp.wordpress.com/2015/10/23/uwp-get-all-the-latest-sample-code-at-ease/) Hồi xưa, nếu bạn muốn có sample code cho một tính năng nào đó, thì quy trình là Google Search > MSDN Page > Download cái sample code đó zìa > giải nén > mở file solution để xem. Ngày hôm nay đã khác rồi, Microsoft đã toẹt zời trở lại. Tất cả Sample code bạn cần cho lập trình Windows 10 hiện đã có trên GitHub, và được UPDATE hàng ngày. Vì vậy, bạn sẽ luôn có những đoạn code mới nhất, do chính mấy ông kỹ sư viết ra tính năng đó viết. Quá chuẩn? Sau đây là cách lấy code.
<!-- more -->
# A really good Git Source Control software

Vì tất cả code đều nằm trên GitHub, nên bạn sễ cần một phần mềm Source Control tốt để:

*   Download tất cả code
*   Update code với 1 click
*   Xem phiên bản code và tên của từng phiên bản

Nếu bạn quyết định ko xài phần mềm Source Control, bạn vẫn có thể download toàn bộ code dưới dạng file .zip, rồi extract nó ra và xài như hồi xưa. Vậy cái nào tốt? Of course it's your choice. Use whatever you're familiar with. Don't let me tell you what to do. But if you insisted, here they are Tất nhiên là lựa chọn của bạn. Xài cái nào thấy wen là được. Nhưng mà vẫn muốn biết một cái tốt (theo ý mình), thì đọc tiếp nhé.

## GitHub Desktop – Not that good

Link: [https://desktop.github.com/](https://desktop.github.com/) ![](https://farm6.staticflickr.com/5663/21778229224_3e5b23876f_o.png) GitHub Desktop, phát triển bới chính dòng họ nhà mều bạch tuộc GitHub, chả tốt tẹo nào. Vì sao áh? Vì nó quá đơn giản, và thiếu nhiều nút cơ bản như Pull, Push, Fetch, Sync, blah blah blah. GitHub Desktop mong muốn mọi thứ đơn giản nhất có thể. Nhưng họ lại bỏ hết mấy từ quen thuộc trong Git rồi.

## SourceTree – More complex, have all the functions

My favorite: [https://www.sourcetreeapp.com/](https://www.sourcetreeapp.com/) ![](https://farm1.staticflickr.com/685/22214151369_9ae2265273_o.png) SourceTree, phát triển bởi Atlassian, là một phần mềm git source control khá tốt (theo ý cá nhân). Bạn có thể làm mọi thứ bạn muốn với nó. Thậm chí nó còn có cả Command Lind cho ai thích gõ lệnh như hacker nhé.

# Setting up

> Giờ, có thể bạn đã nghe thiên hạ đồn là Microsoft mở mã nguồn bộ .NET. Thực ra thì thiên hạ đồn quả nhiên ko sai, mà còn thiếu. Không chỉ .NET không, mà còn khá nhiều thứ khác cũng được "mở". Nói bạn rồi, Microsoft đã chịu chơi trở lại. Bạn có thể tìm thấy kha khá thứ hay ho ở link sau: [https://github.com/Microsoft](https://github.com/Microsoft)

Để thiếp lập, bạn sẽ cần tới "clone link", là 1 trong 3 cái bên dưới. Chọn HTTPS cho nó đơn giản HTTPS: [https://github.com/Microsoft/Windows-universal-samples.git](https://github.com/Microsoft/Windows-universal-samples.git) SSH: [git@github.com:Microsoft/Windows-universal-samples.git](mailto:git@github.com:Microsoft/Windows-universal-samples.git) Subversion: [https://github.com/Microsoft/Windows-universal-samples](https://github.com/Microsoft/Windows-universal-samples) Mở SourceTree (hoặc phần mềm mà bạn thích) > Clone/New ![](https://farm1.staticflickr.com/747/22214019219_1e3d2d0867_o.png) Copy / Paste cái link HTTPS vô "Source Path / URL", và SourceTree sẽ tự động điền mấy chỗ khác. Nếu bạn muốn customize cái gì thì cứ thoải mái chọt zô mà sửa đổi. ![](https://farm1.staticflickr.com/761/22374909436_1a8188ffc0_o.png) Cuối cùng, click Clone. Thế là xong, tất cả code Sample đã nằm trên máy tính.

# Keep the code up-to-date

Giờ bạn đã có code rồi, làm gì nữa? Để update code, đơn giản là mở SourceTree lên, rồi nhấn Fetch > Pull hoặc nhấn Sync luôn từ đầu. Trong SourceTree, click Fetch ![](https://farm1.staticflickr.com/604/21779962253_cb809d0635_o.png) Bạn có thấy con số đỏ lấp ló trên đầu nút Pull không? Đó chính là số lượng phiên bản mới (commit) đã có trên server của GitHub, nhưng chưa có trên máy của bạn. Nhấn Pull để lôi cổ tụi nó về máy. và bạn lại tiếp tục có code mới

> Tips: Bạn có thể nhấn Pull để Fetch và Pull luôn.

Chúc đọc code vui vẻ :3