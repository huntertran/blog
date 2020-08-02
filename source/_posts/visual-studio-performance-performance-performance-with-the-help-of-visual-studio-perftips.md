---
title: >-
  [Visual Studio] Performance, performance, performance (with the help of Visual
  Studio “PerfTips”)
tags:
  - performance
  - perftips
  - stopwatch
  - Visual Studio
id: '500'
categories:
  - - uncategorized
date: 2015-10-22 03:39:19
---

For Visual Studio 2015 Từ xưa tới nay, khi debug bằng Visual Studio, hầu như ai cũng biết chọt con chuột lên trên một biến nào đó và một cái bảng nho nhỏ hiện ra hiển thị toàn bộ dữ liệu của biến đó. Bài post này sẽ hướng dẫn bạn cách sử dụng những công cụ mới của Visual Studio 2015 để cải thiện hiệu suất cho ứng dụng của bạn.
<!-- more -->
# Tại sao lại là hiệu suất?

Trong Visual Studio 2015 có khá nhiều công cụ giúp bạn cải thiện hiệu suất ứng dụng của mình, làm nó chạy nhanh hơn, chiếm ít bộ nhớ hơn, giao diện đẹp hơn, blah blah blah. Tuy nhiên, rất nhìu bạn trẻ dùng phần lớn thời gian để làm cho các tính năng của ứng dụng chạy đúng như bạn mong muốn. Bạn hiểu rằng đoạn code bạn viết có performance không cao, nhưng bạn không có thời gian để nghiên cứu, nghiền ngẫm nó hoặc chạy các công cụ hỗ trợ phân tích hiệu suất cho tới khi hiệu suất là một vấn đề lớn của bạn. Ngoài ra, khi bạn cần nghiên cứu hiệu suất của một đoạn code nào đó, vì sức mạnh kinh khủng của Visual Studio, bạn lại nhét vào code của mình một cái Stopwatch để đo xem đoạn code đó chạy mất bao lâu. Nói tóm lại, developer thường làm những chuyện sau:

*   Chèn code vào trong ứng dụng (kiểu như System.Diagnostics.Stopwatch) để đo thời gian chạy. Càng lúc càng nhiều Stopwatch được chèn đi chèn lại trong nhiều khúc của code.
*   Debug từng dòng code một để xem thử có dòng nào "chạy lâu" wá không
*   Nhấn "Break All" ("Pause") để coi thử code chạy tới đâu gòi (đặc biệt là trong mấy vòng lặp)
*   Rút gọn code quá đà mà không để ý tới performance (giống như không xài Linq cho tất cả mọi thứ)

# PerfTips là gì?

Khi bạn đặt breakpoint cho một dòng code nào đó, và app chạy tới breakpoint này, Visual Studio sẽ hiện một đoạn chữ nhỏ nhỏ, mờ mờ ngay cuối dòng, và nó chính là PerfTips ![](https://farm6.staticflickr.com/5643/22190175850_d39fa83775_o.png) Bấm vào nó (chỗ <= 1ms elapsed), sẽ hiện ra công cụ phân tích ![](https://farm6.staticflickr.com/5816/22190283100_3900ce5068_o.png)

# Dùng PerfTips

Chúng ta sẽ sử dụng một sample đơn giản, một đoạn code dùng để load hình Thay vì chèn 2 đoạn code Stopwatch vào đầu và cuối của phương thức này, bạn chỉ cần đặt 2 breakpoint vào chỗ đó ![](https://farm6.staticflickr.com/5713/22378430175_006386fcd1_o.png) Nhấn F5 để chạy, và Visual Studio dừng lại ngay chỗ Breakpoint đầu tiên ![](https://farm1.staticflickr.com/570/22190464430_6f893119e5_o.png) Nhấn F5 (hoặc continue) để Visual Studio chạy tiếp tới breakpoint thứ 2, và bạn sẽ thấy PerfTips hiện ra ![](https://farm1.staticflickr.com/683/22190602900_3927a739c8_o.png) Như vậy ta có thể thấy, method LoadImages chạy mất 2780 milisecond. Bây giờ chạy lại toàn bộ một lần nữa, nhưng dừng lại ở từng dòng code một để xem dòng nào tốn nhiều thời gian nhất. Nhấn F10 để chạy từng dòng code một. Vài dòng đầu tiên, mỗi dòng không quá 20 ms, quá tốt. ![](https://farm1.staticflickr.com/688/22352672686_50a793488b_o.png) Thế như tới dòng GetImageFromCloud tốn tới 1391 ms ![](https://farm6.staticflickr.com/5791/22352751386_5a52119746_o.png) Và dòng LoadImagesFromDisk tốn tới 1361 ms ![](https://farm6.staticflickr.com/5718/22190832080_f489be8d8a_o.png) Vậy tại sao ta không cho 2 method này chạy song song với nhau nhỉ? Đổi code thành như sau ![](https://farm6.staticflickr.com/5624/22378857485_c2d338a7d3_o.png) Trong hình trên, bạn có thể thấy cả method LoadImages chạy mất 2079 ms, giảm cỡ 700 ms, tương đương 25%. Quá tuyệt phải không? Bây giờ, khi bạn đã biết cách xài PerfTips, chúng ta sẽ tiếp tục với một vài Best Practices khi dùng nó

# Best Practices

## Đo nhiều lần

Thời gian chạy, hiệu suất code có thể khác nhau cho mỗi lần chạy. Thông thường một đoạn code chạy lần đầu tiên lúc nào cũng chậm hơn khi chạy lần 2, 3, n. Lý do là ở lần đầu tiên, nó phải load các dll, khởi tạo bộ nhớ đệm. Đo nhiều lần sẽ cho bạn một khoảng thời gian chính xác hơn

## Xác nhận lại lúc Release

Code chạy lúc build ở chế độ Debug lúc nào cũng chậm hơn hẳn so với code build ở chế độ Release. Nếu bạn muốn tối ưu hóa các đoạn code chạy nhanh hơn 50 ms, thì nên chuyển sang chế độ release để tối ưu hóa nó. Lúc này, bạn mới thấy rõ sự khác biệt. Thế là xong. Hẹn gặp lại ở các bài blog tiếp theo nhóe.