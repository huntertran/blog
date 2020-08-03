---
title: '[Windows Phone – Silverlight] Uniform to fill, centered'
tags:
  - centered image
  - stretch
  - uniform
  - uniformtofill
id: '197'
categories:
  - - c
    - Windows Phone
date: 2013-09-11 22:54:45
---

Hiển thị hình ảnh trong các ứng dụng Silverlight, bạn thường sử dụng Image Control. Image Control có một số thuộc tính về hiển thị như Stretch, Fill, Uniform, UniformToFill. Uniform To Fill sẽ mở rộng tấm hình ra cho vừa kích thước của control, và thực tế là nó cắt mất một góc trái trên của tấm hình, cho ta có cảm giác như tấm hình được canh giữa ![perfect](http://cuoilennaocacban2.files.wordpress.com/2013/09/steeve2.png) Làm sao đạt được tấm hình “Tuyệt vời”
<!-- more -->
# Stretch Property

Image Control có 4 trạng thái của Stretch Property (Hình minh họa)

*   **None:** không resize hình
*   **Fill:** Hình bị scale lại để vừa với kích thước control
*   **Uniform:** Hình cũng bị Scale lại, nhưng giữ nguyên tỷ lệ
*   **Uniform To Fill:** Hình bị scale, giữ nguyên tỷ lệ và fill đầy control. Nếu control có tỷ lệ khác với Image, một phần góc trái và góc phải sẽ bị cắt mất

# Giải pháp

Thêm một Border bọc ngoài Image Control \[code lang=xml\] <border Width="200" Height="200"> <Image Source="/your\_source" Stretch="UniformToFill"> </border> \[/code\] Ngay khi thêm border, bạn sẽ thấy nó hiển thị một kết quả như khi không có border. Cũng như ko =.= Tuy nhiên, Image control sẽ bị giới hạn bởi Border bọc bên ngoài nó có kích thước nhất định. Bây giờ, bạn có thể canh chỉnh bằng thuộc tính HorizontalAlignment và VerticalAlignment để chỉnh vị trí của ImageControl. Áp dụng "Center" cho cả hai, bạn sẽ có tấm hình "Tuyệt vời"