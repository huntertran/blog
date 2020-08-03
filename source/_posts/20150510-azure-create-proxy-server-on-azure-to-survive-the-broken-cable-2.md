---
title: >-
  [Azure] - Update - Create Proxy Server on Azure to survive the internet
  blackout or the broken cable
tags:
  - azure
  - proxy
  - đứt cáp
id: '436'
categories:
  - - Azure
date: 2015-05-10 10:55:51
---

Chào các bạn Hiện tại cáp quang AAG đang bị đứt, nhà mạng bóp băng thông, blah blah blah đủ kiểu. Update thêm, facebook đang bị chặn các kiểu con đà điểu, ở mọi nơi, trên từng cây số, từ hẻm nhỏ ra tới quốc lộ, từ vùng sâu vùng xa tới hoàng sa trường xa. Bài hướng dẫn này mình sẽ hướng dẫn các bạn cách tạo Proxy server trên Azure để chuyển hướng truy cập thông qua proxy đó nhé. WARNING: TẠO PROXY XONG KHÔNG ĐƯỢC ĐEM TEST TỐC ĐỘ VÀ SHARE LUNG TUNG NẾU KHÔNG MUỐN AZURE CỦA BẠN HẾT SẠCH TIỀN
<!-- more -->
# Test Tốc độ mạng tới Azure

Trước tiên, hãy test thử tốc độ kết nối của bạn đến một máy ảo azure gần nhất (Southeast Asia: Singapore) bằng speedtest ![](https://farm8.staticflickr.com/7717/17457900776_4470d9e230_o.png) Nếu thấy ổn thì thủ thuật này mới có tác dụng

# Tạo máy ảo Ubuntu

Vô chọn New > Compute > Virtual Machine > From Gallery ![](https://farm8.staticflickr.com/7689/17481883692_4aa624cb05_o.png) Chọn Ubuntu 14.04 Long term support nhe ![](https://farm6.staticflickr.com/5337/17297753749_b5c8d20165_o.png) Bấm next để tiếp tục nhập các thông số cho máy ảo sắp tạo ![](https://farm6.staticflickr.com/5452/17458065536_9f8b66a975_o.png) Lưu ý: Tier chọn Basic, Size chọn cấu hình thấp nhất để đỡ tốn tiền, vì VM này chỉ có nhiệm vụ là làm proxy cho mình Username nhập gì zô thì nhớ nhe Tick chọn Provide a password và nhập pass vô cho dễ đăng nhập sau này ![](https://farm8.staticflickr.com/7758/16861970254_d3723ce4fc_o.png) Màn hình này sẽ khác nhau tùy theo azure của mỗi người, nhưng chung là chọn region ở chỗ gần nhất, và tạo một endpoint có public port và private port lớn hơn 1024 Port bé hơn 1024 thì trong linux bạn phải gõ "sudo" trước câu lệnh khởi chạy các ứng dụng liên quan tới nó Sau khi đã tạo xong, bạn vào phần quick glance, mục public IP sẽ là Ip của proxy nhé

# Cấu hình cho Proxy

## Đăng nhập vào máy ảo

Để đăng nhập, ta có thể dùng Putty: [http://www.putty.org/](http://www.putty.org/) ![](https://farm8.staticflickr.com/7706/17484960575_5d4f494465_o.png) Putty nhớ để port là 22 để đăng nhập vô nhé Sau khi đăng nhập xong, lần lượt gõ các dòng lệnh sau \[code language="bash"\] sudo apt-get install squid cd /etc/squid sudo cp squid.conf squid.conf.bak sudo rm squid.conf sudo touch squid.conf sudo vim squid.conf \[/code\] sau đó gõ "a" > Enter để edit file này gõ \[code language="bash"\] http\_access allow all http\_port \[port bạn đã tạo ở trên\] dns\_nameservers 208.67.222.222 208.67.220.220 8.8.8.8 8.8.4.4 \[/code\] sau đó gõ ESC để way zề command line gõ ":wq" để save và thoát Xong rồi restart squid service: \[code language="bash"\] sudo service squid3 restart \[/code\] Restart xong, bạn sẽ thấy process của squid Vậy là xong, Proxy của bạn đã chạy, test bằng cách mở firefox và thiết lập proxy rồi kết nối thử tới google nha