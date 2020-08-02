---
title: '[Windows Phone] Where to put load data method?'
tags:
  - data
  - loaded
  - onnavigatedto
id: '255'
categories:
  - - c
    - Windows Phone
date: 2013-11-02 00:28:37
---

Lập trình ứng dụng cho Windows Phone, bắt buộc phải load data và hiển thị chúng lên giao diện. ![](https://farm8.staticflickr.com/7339/10619092335_673c78c2fc_o.png) Vậy cách nào là tối ưu để load data?
<!-- more -->
*   [Cách 1: this.Loaded event handler](#cách-1-thisloaded-event-handler)
    *   [Hoạt động](#hoạt-động)
    *   [Cách dùng](#cách-dùng)
    *   [Ưu điểm](#ưu-điểm)
    *   [Nhược điểm](#nhược-điểm)
    *   [Kết luận](#kết-luận)
*   [Cách 2: OnNavigatedTo](#cách-2-onnavigatedto)
    *   [Hoạt động](#hoạt-động-1)
    *   [Cách dùng](#cách-dùng-1)
    *   [Ưu điểm](#ưu-điểm-1)
    *   [Nhược điểm](#nhược-điểm-1)
    *   [Kết luận](#kết-luận-1)
*   [Tóm lại](#tóm-lại)

Khi tạo mới một page trong Windows Phone, bạn có 1 số phương thức được khởi tạo sẵn ![](https://farm8.staticflickr.com/7314/10619173056_305079cfe7_o.png) Đây là phương thức khởi tạo (Contructor) Phương thức khởi tạo có chức năng chính là…construct, hay xây dựng, thi công nên trang mà mình mong muốn. Một sai lầm cơ bản là mọi người thường load dữ liệu ngay dưới phương thức này. ![](https://farm8.staticflickr.com/7430/10619462526_9716012411_o.png) Giả sử như data của bạn nhiều, LoadData chạy khá lâu. Lúc đó thì page của bạn sẽ chỉ xuất hiện khi toàn bộ Contructor đã chạy xong. Tức là từ page cũ, bấm sang page này, sẽ có một khoảng thời gian ứng dụng bị "đơ", đó chính là thời gian cần thiết để chạy phương thức khởi tạo page. Windows Phone ko hoạt động theo kiểu HTML, một khi tất cả đã sẵn sàng trong RAM, nó mới vẽ page đó ra trên màn hình, trong khi HTML là có cái jì là nó vẽ cái đó :3 Rất nhiều người sử dụng cách này, vì trong một số đoạn video và hầu hết các tài liệu chính thức trên MSDN, MS hướng dẫn bạn theo cách này =='

# Cách 1: this.Loaded event handler

## Hoạt động

Loaded event sẽ được gọi ngay khi vẽ xong giao diện của page lên màn hình (sau khi khởi tạo xong) và khi có một sự thay đổi về giao diện (thêm bớt các element)

## Cách dùng

![](https://farm4.staticflickr.com/3794/10619772596_db30767db0_o.png) Dùng như hình trên

## Ưu điểm

Windows Phone sử dụng cơ chế DataBinding, giao diện sẽ tự động thay đổi khi dữ liệu thay đổi. Hãy thử tưởng tượng từng item xuất hiện trong list, và bạn có thể tương tác với chúng. Phương pháp này làm được việc đó Việc khởi tạo page vô cùng nhanh chóng, ứng dụng của bạn sẽ không bị đơ, đảm bảo tương tác với người dùng

## Nhược điểm

Bất kỳ khi nào có một sự thay đổi về giao diện (thêm bớt các element), phương thức này sẽ được gọi lại. Như vậy, ta không thể đảm bảo được rằng trong suốt quá trình tương tác trên page, phương thức này chỉ được gọi 1 lần. Gọi nhiều lần hàm load sẽ dẫn tới những kết cục không mong muốn, chưa kể đến sự hao phí tài nguyên và năng lượng Giả sử nếu bạn cần thời gian rất lâu để load dữ liệu, mà dữ liệu của bạn chưa được binding trước khi load xong, thì sẽ có 1 hiện tượng là page đã vẽ xong, nhưng nội dung thì vẫn trống trơn. Dù vẫn phản hồi tốt, người dùng sẽ tưởng app lỗi và rate thấp :3

## Kết luận

Nếu page của bạn, bạn chắc chắn không có sự thêm bớt về giao diện, có thể dùng phương thức này. Một lưu ý nhỏ là hãy binding dữ liệu trước khi tiến hành load dữ liệu lên. Binding lên một Collection không có phần tử hoàn toàn không sao cả. (không phải collection null nhé)

> Nếu dùng phương thức này mà gặp một số lỗi lạ về dữ liệu, hãy nghĩ tới trường hợp event được gọi nhiều lần

# Cách 2: OnNavigatedTo

## Hoạt động

OnNavigatedTo được gọi khi một page trở thành page active trong frame. Như vậy có nghĩa là nó sẽ được gọi trước khi event loaded xảy ra. Thứ tự: Contructor => OnNavigatedTo => Loaded

## Cách dùng

![](https://farm4.staticflickr.com/3668/10620480973_e2599e3065_o.png)

## Ưu điểm

OnNavigatedTo có một số tham số liên quan tới việc chuyển page. Bạn có thể dùng các tham số này để xác định các thành phần sẽ hiển thị lên page như thế nào

## Nhược điểm

Page cũ sẽ bị đơ trước khi chuyển

## Kết luận

Chỉ dùng phương thức này khi thời gian đơ là không đáng kể. Nếu bạn load 2 dòng dữ liệu thì okie, còn nếu 20000 dòng thì nên dùng Loaded

# Tóm lại

Tùy và lượng dữ liệu, cũng như thời gian mà bạn sử dụng linh hoạt 1 trong 2 phương pháp