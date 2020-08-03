---
title: '[SOLID] - S - Single responsibility princinple'
tags:
  - oop
  - principle
  - solid
id: '1028'
categories:
  - - C#
---

Code cũng đã lâu rồi, bạn tự hỏi làm thế nào để code mình xịn hơn, code đỡ vất vả hơn?

Hóa ra cũng đã có người nghĩ giống bạn, và cho ra đời quy tắc SOLID.
<!-- more -->
#Giới thịu

SOLID là viết tắt tên của 5 quy tắc mà bạn sẽ áp dụng cho những dòng code của mình, chính xác là:

*   _S_ingle responsibility principle
*   _O_pen - Closed principle
*   _L_iskov substitution principle
*   _I_nterface segregation principle
*   _D_ependency inversion principle

Nội dung cụ thể của từng quy tắc sẽ được mình trải dài ra trong 5 bài viết liên tiếp nhau, mỗi bài sẽ là giải thích và kinh nghiệm áp dụng chúng vào project thực tế của mình.

let's go

#Single Responsibility Princinple - Giải thích

> method/function should have one responsibility only phương thích chỉ nên làm một nhiệm vụ duy nhất (aka chỉ có 1 lý do duy nhất để thay đổi 1 phương thức nào đó)

Điều này có thể hiểu rằng một method hoặc function chỉ nên đảm nhiệm một vai trò duy nhất.

#Ví dụ Hãy tưởng tượng bạn có một chương trình tên `bóng đèn`. Bạn viết một phương thức tên `bật đèn`. Khi gọi phương thức này, đèn sáng, chấm hết. Đó chính là điều mà quy tắc này mong muốn.

_Từ ấy trong bạn bừng nắng hạ_ _Mặt trời chân lý chói qua tim_ bạn

Bỗng nhiên, tháng sau, khách hàng muốn mỗi lần cái bóng đèn được bật, một bản nhạc nhẹ nhàng được phát ra.

"Có hề gì, ta sẽ làm nó trong một nốt nhạc" - bạn nghĩ. Bạn mở code của method `bật đèn`, chèn thêm một dòng code

\[code lang=csharp\] public void TurnOnTheLight { light.TurnOn(); music.Play(); } \[/code\]

Bấm nút deploy, ngả người ra sau ghế, nhấm nháp ly cafe highlands, hạnh phúc với những gì mình đang làm.

Mọi chuyện ko có gì để bàn, cho tới tháng sau, bạn bàn giao project `bóng đèn` cho đồng nghiệp.

"WTF" - đông nghiệp hét lên, vì khi gọi cái method bật đèn, tiếng nhạc ma quái phát ra.

Nhìn qua tên các method, không hề có method nào đảm nhận vai trò bật nhạc cả

Trên đây là một ví dụ điển hình của việc vi phạm quy tắc Single responsibility

#Sửa chữa lỗi lầm

Vậy với ví dụ trên, làm sao để sửa

Bạn sẽ phải tách method kia ra thành 2, một là `bật đèn`, một là `bật nhạc`.

uhuh, nhưng khách vẫn muốn bật đèn thì có nhạc phát ra.

Thêm một method nữa tên là `bật đèn rồi phát nhạc`, xong trong này bạn gọi 2 method kia.

#Đặt tên