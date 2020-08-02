---
title: '[Windows] Implement In-App Purchase for Windows 10'
tags:
  - iap
  - in-app purchase
  - monetization
  - windows 10
id: '570'
categories:
  - - C#
  - - c
    - Windows 10
    - Windows Store App
date: 2016-01-18 05:05:10
---

Bạn có một app thặc là tuyệt zời ông mặt trời, tính năng độc đáo, hấp dẫn. Người dùng không thể nào rời mắt khỏi app của bạn. Và bạn quyết định kiếm tiền từ nó. Thế là bạn tìm hiểu cách implement tính năng In-App Purchase của Windows 10 và nhận ra…nó quá phức tạp. Cùng nhau bơi zô nhé.
<!-- more -->
*   [Official Documents](#official-documents)
*   [Keywords](#keywords)
*   [The Un-official (yet worked) ways](#the-un-official-yet-worked-ways)
    *   [Step 1: Publish your app to the Store](#step-1-publish-your-app-to-the-store)
    *   [Step 2: Create IAP (aka In-App Purchase)](#step-2-create-iap-aka-in-app-purchase)
    *   [Step 3: The tricky](#step-3-the-tricky)
        *   [Sử dụng CurrentAppSimulator](#sử-dụng-currentappsimulator)
        *   [Hiện giá (và các thông tin khác) của sản phẩm](#hiện-giá-và-các-thông-tin-khác-của-sản-phẩm)
        *   [Mua In-App Purchase](#mua-in-app-purchase)
    *   [Step 4: Change the test code to actual code](#step-4-change-the-test-code-to-actual-code)

# Official Documents

Microsoft có tài liệu cho vụ này, thậm chí có cả sample code, nhưng nó sẽ không giúp ích được gì cho bạn. Tất cả đều khá chung chung, khơi khơi, mù mờ

*   Enable In-App Purchase: [https://msdn.microsoft.com/en-us/library/windows/apps/mt219684.aspx](https://msdn.microsoft.com/en-us/library/windows/apps/mt219684.aspx)
*   Enable consumable in-app product purchases: [https://msdn.microsoft.com/en-us/library/windows/apps/mt219683.aspx](https://msdn.microsoft.com/en-us/library/windows/apps/mt219683.aspx)
*   Manage a large catalog of in-app products (Not really): [https://msdn.microsoft.com/en-us/library/windows/apps/mt219686.aspx](https://msdn.microsoft.com/en-us/library/windows/apps/mt219686.aspx)

Đọc từng câu từng chữ trong 3 cái tài liệu trên, tất cả những gì bạn có thể viết trong code là ít vô cùng. Hy vọng rằng trong tương lai điều này sẽ thay đổi. Giờ hãy thử theo cách khác nhóe

# Keywords

Phần này chứa các keywords mà bạn hay nhầm lẫn khi implement tính năng này

*   Consumables: User có thể mua loại này bao nhiu tùy thích (tiu bỉu cho thể loại này là tiền trong game, quyền truy cập vào kho sách – nhạc – blah blah blah trong 6 tháng) ![](https://farm2.staticflickr.com/1479/24372150901_025d567d60_o.png)
    
*   Durables: User mua thể loại này một lần rồi là sẽ sở hữu nó mãi mãi. Ví dụ như level mới, màn chơi mới, vật phẩm
    
*   ProductID: chính là ID của product của bạn. Đây sẽ là thông số đầu tiên khi tạo một In-App Purchase mới trên Dev Center

# The Un-official (yet worked) ways

## Step 1: Publish your app to the Store

Việc đầu tiên bạn muốn làm sẽ là publish app của bạn lên Store. "Nhưng app vẫn đang trong giai đoạn dev, chưa publish được" – "App chưa có gì cả" – "App vẫn chưa hoàn thiện hết các tính năng" Không sao cả. Store cho phép bạn publish app của bạn, và ẩn khỏi ô tìm kiếm. Chỉ những ai có deep link (link dẫn trực tiếp tới app của bạn) mới có thể tải về và sử dụng. Như vậy bạn đã có thể ngăn chặn người dùng tìm ra app của bạn và tải nó về, tận hưởng những thứ đáng lẽ ra phải mua bằng Obama. \\\[caption id="" align="aligncenter" width="1108"\\\]![](https://farm2.staticflickr.com/1563/24454812865_46046851ea_o.png) Hide this app in the Store\[/caption\]

## Step 2: Create IAP (aka In-App Purchase)

In-App Purchase hoàn toàn riêng biệt với app của bạn. Và cũng sẽ được xét duyệt như 1 app, nhưng thường chỉ mất khoảng 1 tiếng đồng hồ cho quá trình đó (quá chậm) Các bước tạo In-App Purchase, cũng như publish app, thì mỗi thời mỗi khác. Tóm lại là cứ làm theo hướng dẫn trên màn hình là được \\\[caption id="" align="aligncenter" width="653"\\\]![](https://farm2.staticflickr.com/1538/24087084229_5b67cc60ea_o.png) Tạo một In-App Purchase\[/caption\]

## Step 3: The tricky

In-App Purchase sẽ ko chạy khi bạn có 1 trong các điều kiện sau

*   In-App Purchase vừa mới tạo xong, chưa kịp lên đã lật đật đòi test
*   Chưa có sản phẩm trên In-App Purchase trong Dev Center

Bạn sẽ nghĩ: quá đơn giản, chỉ cần tạo sản phẩm trên In-App Purchase, chờ 1 tiếng đồng hồ để nó lên, sau đó vào lại app, chuyển sang chế độ Release là xong. Tuy nhiên

*   Đặt Break-point ở các dòng code liên quan tới In-App Purchase sẽ không xem được data
*   Dù đã có sản phẩm, nhưng vẫn ko liệt kê ra khi hiển thị lên màn hình (count == 0)

Và đây sẽ là cách. Lưu ý làm theo đúng thứ tự được trình bày trong blog này

### Sử dụng CurrentAppSimulator

Trong method khởi tạo hoặc load data cho app của bạn, đặt các dòng code sau \[code lang=csharp\] StaticData.license = CurrentAppSimulator.LicenseInformation; StaticData.listings = await CurrentAppSimulator.LoadListingInformationAsync(); \[/code\] StaticData là một class chứa các biến Static, có thể truy cập ở mọi class khác Ngay sau khi chạy đoạn code này, Visual Studio sẽ tạo ra 1 file XML giả ở C:\\Users\\\\AppData\\Local\\Packages\\\\LocalState\\Microsoft\\Windows Store\\ApiData\\WindowsStoreProxy.xml Bạn mở nó lên, và sửa các giá trị sau \[code lang=xml\] <App> <IsActive>true</IsActive> <IsTrial>false</IsTrial> </App> \[/code\] Mục Product ID, sửa lại cho trùng với Product ID bạn đã đặt trên Dev Center

### Hiện giá (và các thông tin khác) của sản phẩm

Như bạn đã thấy rõ, StaticData.listings chứa toàn bộ In-App Purchase của bạn. Mọi sản phẩm đều có mặt trong này. Như vậy, để gắn giá lên một sản phẩm nào đó, ngoài việc có template, model ra, bạn sẽ cần phải chạy một vòng lặp \[code lang=csharp\] foreach (KeyValuePair<string, ProductListing> productListing in StaticData.listings.ProductListings) { if (productListing.Key.TrimStart('0') == issue.id) { issue.billing.price = productListing.Value.FormattedPrice; } } \[/code\] Trong đoạn code trên, Product ID của mình là 0154, và issue.id là "154" FormattedPrice sẽ bao gồm cả đơn vị tiền tệ mà hệ thống đang sử dụng. Bạn cũng có thể đọc các thông tin khác như Description, Tag, vân vân và vân vân

### Mua In-App Purchase

Nhờ sự giúp đỡ của CurrentAppSimulator, bạn có thể test mua thoải mái. Chỉ cần chỉnh sửa các giá trị trong file WindowsStoreProxy.xml để test đi test lại Về cơ bản, đoạn code mua một vật phẩm bằng In-App Purchase sẽ như sau \[code lang=csharp\] if (!StaticData.license.ProductLicenses\[\_selectedIssue.billing.iapKey\].IsActive) { try { // Người dùng chưa từng mua cái này // Hiện hộp thoại mua await CurrentAppSimulator.RequestProductPurchaseAsync(\_selectedIssue.billing.iapKey); //Kiểm tra lại xem đã mua thành công chưa if (StaticData.license.ProductLicenses\[\_selectedIssue.billing.iapKey\].IsActive) { //Nếu mua thành công thì làm trò mèo gì đó } } catch (Exception) { // Mua bị lỗi // an error occurred. } } else { // Đã mua cái này rồi, tiếp tục trò mèo } \[/code\] Và khi test thử, lúc gọi đoạn code này, một hộp thoại nhỏ hiện ra, cho phép bạn giả lập các trường hợp có thể xảy ra khi dùng thật ![](https://farm2.staticflickr.com/1616/23825747414_ddb694db19_o.png) Có vẻ tốt rồi. Tới bước cuối cùng nhé

## Step 4: Change the test code to actual code

Step này khá đơn giản, chỉ cẩn thay tất cả những chỗ dùng CurrentAppSimulator thành CurrentApp là được. Và chạy lại app một lần nữa, lần này, khi bấm mua, sẽ có một hộp thoại thật hiện ra đòi bạn nhập mã PIN để tiến hành mua app. Tới bước này coi như là thành công ![](https://farm2.staticflickr.com/1461/23829331723_6f852496b8_o.png)

> Tips: Bạn nên submit In-App Purchase trên Dev Center trước 1-2 ngày để đảm bảo code thực sẽ chạy tốt (mình đã từng submit xong chờ 1 tiếng để nó lên, rồi chạy code thực thì lại báo là không có in-app purchase nào trên dev center =.=)