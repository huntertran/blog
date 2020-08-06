---
title: '[ASP.NET for Beginner] - Part 3 - Front end framework nào?'
tags:
  - css
  - framework
  - frontend
  - jquery
  - scss
id: '966'
categories:
  - - CSharp
    - ASP.NET
date: 2018-03-18 06:46:24
---

Trong phần 3 này chúng ta sẽ tìm hiểu về các framework front end phổ biến hiện tại
<!-- more -->
> Xem các bài viết trong series
> 
> *   [Phần 1: Mô hình MVC](https://coding4food.net/2018/03/04/asp-net-for-beginner-part-1-mvc/)
> *   [Phần 2: Connect Database và Model Binding](https://coding4food.net/2018/03/11/asp-net-for-beginner-part-2-connect-database-and-model-binding/)
> *   [Phần 3: Front end framework nào](https://coding4food.net/2018/03/18/asp-net-for-beginner-part-3-front-end-framework-nao/)
> *   [Phần 4: CRUD và Data Validation](https://coding4food.net/2018/03/25/aspnet-for-beginner-part-4-crud-va-data-validation/)

*   [1. CSS](#1-css)
    
    *   [1.1. CSS Framework](#11-css-framework)
        
        *   [1.1.1. \[Bootstrap\](http://getbootstrap.com/)](#111-bootstraphttpgetbootstrapcom)
        *   [1.1.2. \[MaterializeCSS\](http://materializecss.com/)](#112-materializecsshttpmaterializecsscom)
        *   [1.1.3. Các Grid System](#113-các-grid-system)
    *   [1.2. CSS Language Preprocessor](#12-css-language-preprocessor)
        
        *   [1.2.1. \[SCSS\](https://sass-lang.com/)](#121-scsshttpssass-langcom)
        *   [1.2.2. \[LESS\](http://lesscss.org/)](#122-lesshttplesscssorg)
*   [2. Javascript](#2-javascript)
    
    *   [2.1. jQuery](#21-jquery)
    *   [2.2. Xu hướng](#22-xu-hướng)
*   [3. HTML](#3-html)
*   [Cái nào là tốt nhất?](#cái-nào-là-tốt-nhất)

Một ứng dụng web được chia thành 2 thành phần chính là Front-end và Back-end. Về phía back end, có hàng ty tỷ ngôn ngữ và công nghệ có thể làm nên chúng. ASP.NET là một trong các công nghệ đó. Và tất cả các công nghệ / ngôn ngữ này đều phục vụ một mục đích tối thượng: Tạo ra front end

Trong một diễn biến khác, Front end chỉ có 1, được cấu thành từ 3 ngôn ngữ là `HTML`, `CSS` và `Javascript`

> Nếu bạn chưa biết cơ bản về HTML, Javascript và CSS, thì hãy học ngay \* [Học HTML](https://www.w3schools.com/html/default.asp) \* [Học CSS](https://www.w3schools.com/css/) \* [Học Javascript](https://www.w3schools.com/js/)

3 ngôn ngữ này, theo ý kiến chủ quan của mình, như mì ăn liền. Cách tổ chức khá lộn xộn, và quy chuẩn thì được áp dụng khác nhau đối với các trình duyệt khác nhau

> **Quy chuẩn của HTML** HTML có 1 bộ quy chuẩn giúp cho các nhà phát triển trình duyệt biết được chính xác phải làm gì khi hiển thị các thẻ của HTML trên trình duyệt

Để làm cho cuộc đời bớt đau khổ, các developer trên khắp thế giới đã cùng nhau phát triển thêm những framework, những ngôn ngữ hỗ trợ thêm cho bộ 3 này

# 1. CSS

## 1.1. CSS Framework

Làm sao để chia web thành các cột linh hoạt? Làm sao để khi kích thước trình duyệt thay đổi, trang web sẽ hiển thị các thành phần phù hợp? Làm sao để trang web có thể đọc được trên điện thoại di động?

Hàng tá các câu hỏi như vậy sẽ nảy ra trong đầu bạn khi bạn đang phát triển một website nào đó. Để giải quyết vấn đề đó, ta có các CSS Frameworks làm sẵn giúp bạn các công việc này, bạn chỉ cần áp dụng.

### 1.1.1. [Bootstrap](http://getbootstrap.com/)

Bootstrap có lẽ là css framework được sử dụng nhiều nhất hiện nay với bộ plugin đồ sộ + kho tàng theme thủng cực khủng của mình

Bootstrap sử dụng 1 khái niệm gọi là responsive breakdown, tức là khi bề ngang trình duyệt đạt tới 1 số lượng pixels nào đó, thì một số thành phần HTML sẽ bị ẩn đi hoặc hiện ra.

**Nhược điểm**

*   Quá phổ biến: Điều này tuy giúp ích trong quá trình phát triển, nhưng sẽ làm cho website của bạn nó...na ná với cả triệu website khác
*   Grid system dùng concrete class: Đối với mỗi size khác nhau, bạn sẽ phải thêm các class khác nhau của mỗi column vào thẻ html
*   Nặng: Bootstrap cần 1 file css, 1 file javascript, và cả cái thư viện jQuery + poper.js. Nếu website của bạn ko dùng jQuery? Thôi nghỉ chơi với boostrap nhé

### 1.1.2. [MaterializeCSS](http://materializecss.com/)

Nếu bạn có đang dùng các sản phẩm của google, thì bạn sẽ thấy họ có 1 style khá đẹp, nhất là khi nhấn vào 1 cái nút nào đó, sẽ có 1 vòng tròn tỏa ra. Cái này được gọi là Material Design

Materializecss làm theo cái design này, và open source nó cho mọi người sử dụng. Nhanh, nhẹ, đẹp, hỗ trợ tốt, cộng đồng lớn là những ưu điểm của framework này

**Nhược điểm**

*   Quá Google: website của bạn khi dùng framework này, nó sẽ cho người dùng 1 cảm giác hơi...google. Từ cái nút bấm cho tới cái ô grid
*   Chưa release: Tin hay ko thì tùy bạn, dù có hằng hà sa số website đang dùng, với gần 32k stars trên Github, nhưng framework này vẫn chưa được release version 1.0. Các nhà phát triển nó đang rất gấp rút fix bug và hoàn thiện để ra mắt phiên bản release đầu tiên của nó ;)

### 1.1.3. Các Grid System

Cái quan trọng nhất của một framework là grid system, tức là cách chia website thành các column khác nhau. Nắm bắt được điều này, kha khá framework ra đời, và chỉ chứa độc nhất 1 tính năng: chia column.

**Nhược điểm**

Nhìn chung, khi sử dụng các framework dạng này, bạn sẽ phải khá chuyên nghiệp rồi. Khi đó bạn sẽ phải tự code các thành phần css khác ko liên quan tới grid, hoặc tìm các thư viện hỗ trợ cho những thành phần mong muốn

## 1.2. CSS Language Preprocessor

Ngôn ngữ css, với một cách tổ chức tè le, là một thử thách khá khó khăn cho developer mới học. May mắn thay, đã có những ngôn ngữ thay thế cho nó

Thay thế cũng không hẳn là đúng. Các ngôn ngữ này chỉ giúp bạn viết code css dễ hiểu hơn, khoa học hơn, tổ chức tốt hơn. Sau cùng, nó vẫn generate ra file .css cho bạn sử dụng.

### 1.2.1. [SCSS](https://sass-lang.com/)

SCSS kế thừa và cải tiến CSS selector bằng các cấu trúc `{}`, `:`và `&gt;`. Khi bạn bắt tay vào học nó, bạn sẽ thấy cách select một element vô cùng tự nhiên của nó

### 1.2.2. [LESS](http://lesscss.org/)

Less giống như một phiên bản khác của Scss vậy, với cú pháp cũng khá giống nhau, các khái niệm cũng giống luôn.

> Bạn chỉ nên chọn 1, hoặc SCSS, hoặc LESS

# 2. Javascript

Ngôn ngữ HTML, vốn dĩ chỉ là các đoạn text có thêm markup và link, chỉ có thể cho phép bạn đọc text và nhấn link để nhảy sang 1 trang khác mà thôi.

Mọi chuyện thay đổi khi javascript được gắn thêm vào. Giờ đây bạn có thể thay đổi 1 khúc text mà ko cần reload, làm cho biểu tượng này xoay xoay, làm cho nút kia chuyển động, hiển thị popup, vân vân và vân vân.

> `Javascript` không hề dính dáng gì tới `Java` cả

## 2.1. jQuery

jQuery giống như 1 thư viện "phải có" vậy. Nó giúp cho việc sử dụng cả tá css framework khác trở nên đơn giản và hiệu quả.

Ví dụ: Để đổi đoạn value của thẻ input có id là "test" thành chữ khác

\[code lang=javascript\] // Before jquery document.getElementById("test").value = "Test Value";

// After jquery $("#test").val("Test Value"); \[/code\]

Vì sử dụng các khái niệm của CSS Selector, bạn có thể chọn các html element bằng jQuery y như khi bạn code css cho nó vậy.

## 2.2. Xu hướng

vì jQuery khá nặng, việc xử lý jQuery cũng đòi hỏi một phần tài nguyên của trình duyện, nên hiện đang có 1 xu hướng là bỏ hẳn jQuery ko xài nó nữa.

Nhưng từ giờ tới lúc jQuery biến mất vẫn còn xa lắm. Máy tính và điện thoại thì ngày càng mạnh mẽ hơn. jQuery hầu như đã được tải sẵn trên bất cứ trình duyệt nào bạn tìm thấy

# 3. HTML

HTML5, như đã nói ở trên, là version mới nhất của HTML, và tất cả các trình duyệt phổ biến hỗ trợ.

Nếu bạn code bằng Visual Studio, thì HTML đã được hỗ trợ khá tốt rồi. Còn nếu bạn code bằng Visual Studio Code, thì sau đây là 1 số extension mình sử dụng để việc code HTML được dễ thở hơn

*   Auto Close Tag: tự đóng các thẻ HTML. Không cần phải gõ tay nữa
*   HTML Snippets: tự nhắc các property của 1 thẻ HTML

# Cái nào là tốt nhất?

Không có câu trả lời cụ thể cho câu hỏi này, nên mình sẽ đưa ý kiến của mình, và cái mình đang sử dụng để bạn tham khảo

\[code lang=text\] CSS: SCSS CSS Framework: Materializecss Javascript: jQuery HTML: HTML5 \[/code\]

Còn bạn, bạn chọn ngôn ngữ nào?