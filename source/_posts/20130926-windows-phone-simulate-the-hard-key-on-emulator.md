---
title: '[Windows Phone] Simulate the hard key on Emulator'
tags:
  - emulator
  - keyboard shotcuts
  - windows phone
id: '231'
categories:
  - - CSharp
    - Windows Phone
date: 2013-09-26 10:09:06
---

Windows Phone SDK đi kèm với một chiếc máy ảo tiện lợi: Windows Phone Emulator.

Nhưng nó có 1 điểm phiền toái. Làm thế nào để “bấm” được các phím cứng, ngoài 3 phím mặc định là Back, Start và Search?

![phone](/images/2013/09/volume-power-button-charge-battery-htc-windows-phone-8x.jpg)

Có 1 cách, và nó đã được tích hợp sẵn
<!-- more -->
Windows Phone SDK đã tích hợp sẵn rất nhiều phím tắt để bạn có thể giả lập các phím cứng. Dưới đây sẽ là danh sách

| Phím | Phím cứng trên điện thoại | Ý nghĩa trên điện thoại |
|---|---|---|
| F1 | Back | Tương đương phím back. Bạn có thể nhấn giữ (hold) |
| F2 | Start | Tương đương phím Start. Có thể hold |
| F3 | Search |  |
| F6 | Camera Half | Nhấn một nửa phím Camera. Dùng để lấy tiêu cự |
| F7 | Camera Full | Nhấn toàn bộ phím Camera, dùng để chụp hình |
| F9 | Volumn Up |  |
| F10 | Volumn Down |  |
| F12 | Power | Phím nguồn. Nhấn để tắt/mở màn hình |
| ESC | Back | Như F1 |
| PAUSE/BREAK | Toggle Keyboard | Kích hoạt/Ẩn bàn phím cứng. (Cần phân biệt với bàn phím ảo) |
| PAGE UP | Keyboard Up | Dùng bàn phím ảo |
| PAGE DOWN | Keyboard Down | Dùng bàn phím máy tính thay cho bàn phím ảo |

\[youtube=http://www.youtube.com/watch?v=MprFcKyrTAA&w=448&h=252&hd=1\]