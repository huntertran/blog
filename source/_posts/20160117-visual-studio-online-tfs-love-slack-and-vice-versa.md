---
title: '[Visual Studio Online] TFS love Slack, and vice versa'
tags:
  - online
  - slack
  - TFS
  - Visual Studio
id: '565'
categories:
  - - uncategorized
date: 2016-01-17 11:57:07
---

Bài viết này sẽ hướng dẫn bạn tích hợp TFS vào slack. Mỗi khi có hoạt động gì đó xảy ra trên TFS, sẽ có message gửi trong slack cho các thành viên cùng biết

Nghe cũng hay nhỉ?

Sau đây sẽ là các bước tích hợp
<!-- more -->
# Kích hoạt trong TFS

Mở project của bạn trong TFS ra. Thông thường sẽ có địa chỉ là "blahblahblah.visualstudio.com". Bạn sẽ phải đăng nhập, và chỉ có admin có quyền này

Chọn 1 Project mà bạn muốn tích hợp

![](https://farm2.staticflickr.com/1547/23806986773_398ba374e6_o.png)

Ở trong Project đó, click Settings để vào phần thiết lập

![](https://farm2.staticflickr.com/1693/24351380141_2d15dd5529_o.png)

Trong Settings > Service Hooks > Create the first subscription for this project

![](https://farm2.staticflickr.com/1679/23807096673_7118fe4dcd_o.png)

Kéo xuống chọn Slack rồi Next

![](https://farm2.staticflickr.com/1454/23805672984_a6c39c2d54_o.png)

Ở mục Trigger, bạn có thể chọn các sự kiện muốn thông báo. Ở đây mình sẽ chọn là code checked in. Sau khi chọn xong, nhớ kiểm tra lại đường dẫn tới project của bạn nhé

![](https://farm2.staticflickr.com/1443/24325627642_f43b136bc1_o.png)

Ở bước tiếp theo, bạn sẽ cần một thông số là Slack Webhook URL. Cái này phải vô slack mới có nhóe.

![](https://farm2.staticflickr.com/1467/24066128509_c91f25dd35_o.png)

# Lấy Slack Webhook URL

Mở slack lên, nhấn chuột vô cái dấu mũi tên đằng sau tên team > Apps and Custom Integrations

![](https://farm2.staticflickr.com/1558/23811662364_c3b2482408_o.png)

Trong trang web vừa xuất hiện, tìm app Incoming Webhook

![](https://farm2.staticflickr.com/1458/24439861585_ac197f5bc0_o.png)

Bạn có thể đăng nhập nhiều team slack và install cho những team đó luôn một lúc.

![](https://farm2.staticflickr.com/1639/24357442781_27f266d7fe_o.png)

Sau đó, chọn channel sẽ post các thông báo, rồi nhấn nút thôi

![](https://farm2.staticflickr.com/1505/24439921085_f4480688db_o.png)

Ở trang tiếp theo, bạn sẽ thấy Webhook URL. Copy nó và paste vào trong mục điền ở bước 1 nhóe

![](https://farm2.staticflickr.com/1636/24413747666_afd642068f_o.png)

Nhấn Test để test thử

![](https://farm2.staticflickr.com/1570/24144370770_a32341cdef_o.png)

Sau cùng, nhấn nút Finish, và thế là bạn đã tích hợp được TFS vào Slack nhóe

![](https://farm2.staticflickr.com/1545/24440021705_020a7008bf_o.png)

> Tips: Bạn có thể add thêm nhiều loại Trigger khác

Thế là xong :3