---
title: '[Basic for Absolute Beginner] – [Part 6] – Source Control'
tags:
  - source control
  - Team foundation
id: '317'
categories:
  - - C#
  - - c
    - Windows Phone
    - Windows Store App
date: 2014-05-02 09:55:19
---

Hãy thử tưởng tượng, bạn đã làm xong một thành phần nào đó trong ứng dụng của mình. Bạn tiếp tục làm thêm một thứ gì đó, và nhấn Run. Và đột nhiên, mọi thứ báo lỗi, bug xuất hiện khắp nơi, bạn xóa những đoạn code mới thêm vào, nhưng lỗi vẫn còn, và hình như bạn còn thiếu gì đó? Tưởng tượng tiếp, Team của bạn đang làm một dự án nào đó, nhưng mỗi thành viên lại ở một chỗ khác nhau, và các bạn không có cách gì gặp nhau được. Làm thế nào để làm việc cùng nhau trên một dự án? Tất cả câu hỏi đó, và nhiều câu hỏi khác, được trả lời bằng một tính năng gọi là “Team Foundation Server” của Visual Studio ![](https://i2.wp.com/farm6.staticflickr.com/5032/14076910292_20d9511445_o.png)
<!-- more -->
*   [Khái niệm](#khái-niệm)
*   [Đăng ký tài khoản](#đăng-ký-tài-khoản)
*   [Trên Service](#trên-service)
    *   [Tạo Project](#tạo-project)
    *   [Quản lý thành viên](#quản-lý-thành-viên)
        *   [Trong một Project](#trong-một-project)
        *   [Trong toàn bộ các Project](#trong-toàn-bộ-các-project)
*   [Trên Visual Studio](#trên-visual-studio)
    *   [Connect tới tài khoản của bạn](#connect-tới-tài-khoản-của-bạn)
    *   [Thêm Project vào Source Control](#thêm-project-vào-source-control)
    *   [Chỉnh sửa và Check in](#chỉnh-sửa-và-check-in)
    *   [Get Latest Version – Get Specific Version – Undo Pending Change](#get-latest-version--get-specific-version--undo-pending-change)

Các phần cũ: [\[Basic for Absolute Beginner\] – \[Part 1\] – Layout with XAML 1](https://cuoilennaocacban2.wordpress.com/2013/11/22/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner/ "[Basic for Absolute Beginner] - [Part 1] Layout with XAML 1") [\[Basic for Absolute Beginner\] – \[Part 2\] – Layout with XAML 2](https://cuoilennaocacban2.wordpress.com/2014/01/21/windows-phone-silverlight-layout-with-xaml-basic-for-absolute-beginner-part-2/ "[Basic for Absolute Beginner] – [Part 2] – Layout with XAML 2") [\[Basic for Absolute Beginner\] – \[Part 3\] – App’s Structure and how to customize it](https://cuoilennaocacban2.wordpress.com/2014/02/26/basic-for-absolute-beginner-part-3-apps-structure-and-how-customized-it/) [\[Basic for Absolute Beginner\] – \[Part 4\] – Basic Steps for a new app](https://cuoilennaocacban2.wordpress.com/2014/03/31/basic-for-absolute-beginner-part-4-basic-steps-for-a-new-app/) [\[Basic for Absolute Beginner\] – \[Part 5\] – Analytics for your apps](https://cuoilennaocacban2.wordpress.com/2014/04/04/basic-for-absolute-beginner-part-5-analytics-for-your-apps/)

# Khái niệm

Source Control là một cách để quản lý source code của bạn. Quản lý có nghĩa là bạn có thể xem các phiên bản, lưu trữ, phục hồi, chia sẻ, vân vân và vân vân. Khi code nhầm một cái gì đó, bạn có thể phục hồi lại đoạn code trước đó. Bạn có thể tạo một project mới từ source có sẵn, bạn có thể cho phép một thành viên mới tải toàn bộ source code về để làm việc chung trên một dự án, và người này cũng có thể xem, xóa, lưu phiên bản, vân vân đối với các phần code của họ Ở mức cơ bản nhất, bài blog này sẽ hướng dẫn bạn sử dụng Team Foundation Server để quản lý phiên bản source code của bạn

# Đăng ký tài khoản

Team Foundation Server của Microsoft, hiện tại đã được đổi tên thành Visual Studio Online, là một dịch vụ miễn phí. Bạn có thể tạo bao nhiêu Project tùy thích, nhưng tất cả các Project, bạn chỉ được thêm tối đa 5 thành viên miễn phí. Như vậy, khi đăng ký tài khoản Visual Studio Online (VSO), bạn sẽ được cấp một vùng lưu trữ không giới hạn (đúng rồi, không giới hạn), tối đa 5 thành viên, không giới hạn số project, và nhiều công cụ khác đòi hỏi phải có kiến thức chuyên sâu để sử dụng [http://www.visualstudio.com/](http://www.visualstudio.com/) Vào trang trên, bấm nút Get Started for Free màu tím ![](https://i2.wp.com/farm8.staticflickr.com/7423/14077027941_131d9fe8b9_o.png) Bạn sẽ được đưa đến một trang, dùng tài khoản Microsoft để đăng nhập trang này ![](https://i0.wp.com/farm8.staticflickr.com/7042/14077110182_67ddb90db7_o.png) Bạn điền thêm một số thông tin cần thiết, hoặc trả lời bất kỳ câu hỏi nào mà nó đưa ra ![](https://i1.wp.com/farm8.staticflickr.com/7426/14057171186_c1f58d0d92_o.png) Sau khi đăng nhập, bạn đã có thể tạo Project đầu tiên của mình

# Trên Service

## Tạo Project

![](https://i1.wp.com/farm3.staticflickr.com/2939/14077138942_7fc7d459e9_o.png) Bấm vào nút New để tạo một Project mới ![](https://i1.wp.com/farm8.staticflickr.com/7337/13893692388_453e4325a5_o.png) Điền vào các thông tin cần thiết và bấm nút Create Project Sau khi tạo xong, bấm nút Navigate to Project để tới trang quản lý Project của bạn Trang này chứa nhiều thông tin, hiện tại bạn chỉ cần quan tâm tới mục Member ![](https://i0.wp.com/farm8.staticflickr.com/7306/14100357193_a79e22a996_o.png) Tại đây sẽ hiển thị toàn bộ thành viên có trong project của bạn. Bấm nút Manage… để thêm hoặc bớt các thành viên

## Quản lý thành viên

### Trong một Project

![](https://i0.wp.com/farm3.staticflickr.com/2937/13893748200_d0b2bfd795_o.png) Ở tên mỗi người có một nút Remove. Bấm vào đây để xóa một thành viên. Bấm nút Add để thêm mới Thành viên bắt buộc phải sử dụng một tài khoản Microsoft để sử dụng dịch vụ này

### Trong toàn bộ các Project

Ở trang đầu tiên, nhấn vào nút Users để xem danh sách toàn bộ thành viên có trong tài khoản của bạn ![](https://i0.wp.com/farm8.staticflickr.com/7426/14077207562_e677848f77_o.png) Hiện tại có nhiều loại tài khoản, VS Utimate with MSDN là tài khoản của các bạn Microsoft Student Parter, Early Adopter là tài khoản miễn phí, sau này sẽ được đổi thành Basic ![](https://i2.wp.com/farm8.staticflickr.com/7420/14080365235_3f8073d7a7_o.png) Nếu bạn là một MSP, bạn có thể dùng MSDN Subscription của mình để đăng ký VSO. Bạn có thể thêm không giới hạn các tài khoản VS Ultimate with MSDN. Nhưng bạn chỉ được thêm tối đa 5 tài khoản Basic thôi. Hình dưới đây sẽ thể hiện điều đó ![](https://i1.wp.com/farm6.staticflickr.com/5455/13893764527_924181318e_o.png) Vậy là xong, Bây giờ, hãy mở Visual Studio lên để thiết lập nhé

# Trên Visual Studio

## Connect tới tài khoản của bạn

Chọn Menu > Team > Connect to Team Foudation Server Đăng nhập bằng chính tài khoản Microsoft bạn đã dùng để tạo Online ![](https://i2.wp.com/farm8.staticflickr.com/7181/14080415865_cea0f2115b_o.png) Server có dạng: [https://nickname.visualstudio.com](https://nickname.visualstudio.com) Sau khi đăng nhập, tất cả các Project có sẵn trên Server sẽ được hiện ra. Tick vào các Project bạn muốn connect (các project bạn đang làm việc) và nhấn Connect

## Thêm Project vào Source Control

Bạn mở Solution của mình lên ![](https://i0.wp.com/farm8.staticflickr.com/7386/13893812187_43fc27c6e2_o.png) Sau khi mở ra, nhấn chuột phải vào Solution > Add Solution to Source Control…, bạn sẽ được hỏi sử dụng dịch vụ nào. ![](https://i0.wp.com/farm3.staticflickr.com/2928/14065466846_0be4d81154_o.png) Git là một dịch vụ miễn phí, và khó sử dụng hơn so với Team Foundation. Một bản hiện ra, bạn chọn Project bạn vừa tạo trên Web, rồi nhấn OK ![](https://i1.wp.com/farm6.staticflickr.com/5443/13902073928_3a5166bb42_o.png) Quá trình thêm vào diễn ra âm thầm. Có thể bạn sẽ cảm nhận được Visual Studio bị đơ 2-3 giây. Sau đó, trước mỗi file trong Solution, sẽ có 1 biểu tượng dấu + ![](https://i1.wp.com/farm8.staticflickr.com/7400/13902049219_54c1ce6b04_o.png) Lúc này, Project của bạn đã được quản lý bởi Source Control Team Foundation Server. Tuy nhiên, đây mới chỉ là “thay đổi”. Bạn cần phải Check in để các thay đổi này được lưu lại. Bấm chuột phải vào Solution > Check In… ![](https://i1.wp.com/farm8.staticflickr.com/7068/14065573286_3388d5ff11_o.png) Trong ô Comment, bạn nhập vào chú thích của lần check in này ![](https://i2.wp.com/farm8.staticflickr.com/7451/13902095378_6c8b207a01_o.png) Mục Included Changes (number) là nơi liệt kê các tập tin trong Solution đã bị thay đổi và sẽ được lưu lại Source Control trong lần check in này Sau khi kiểm tra tất cả các chi tiết, bạn nhấn Check in ![](https://i2.wp.com/farm6.staticflickr.com/5527/14085562102_33c66105e1_o.png) Sau khi check in thành công, một thông báo nhỏ xuất hiện, thông báo số changeset. Bạn sẽ cần con số này để phục hồi về sau ![](https://i0.wp.com/farm6.staticflickr.com/5488/13902099877_0f0a7e14ab_o.png) Quay trở lại Solution Explorer, bạn sẽ thấy trước mỗi file có hình một chiếc khóa, biểu hiện cho việc file này từ lần check in trước chưa bị thay đổi ![](https://i1.wp.com/farm6.staticflickr.com/5484/14108858123_8884d622d9_o.png)

## Chỉnh sửa và Check in

Khi bạn bắt đầu chỉnh sửa một file nào đó, biểu tượng chiếc khóa bị thay đổi ![](https://i0.wp.com/farm3.staticflickr.com/2905/14085667152_399a036b26_o.png) Để thay đổi này lưu vào Source Control, bạn nhấn chuột phải lên nó và chọn Check in. Lưu ý, khi thay đổi nhiều file trong Project, bạn có thể chọn cả Project để check in. Nếu thay đổi trong nhiều Project, bạn có thể chọn cả Solution để check in. Thông thường, chọn cả Solution sẽ đảm bảo bạn không “Check in” thiếu thứ gì. Team Foundation sẽ tự động tìm ra các file bị thay đổi của bạn

## Get Latest Version – Get Specific Version – Undo Pending Change

Nếu bạn làm trong một dự án nhiều thành viên, và các thành viên kia hoàn tất phần code của họ và Check in lên Server. Bạn sẽ phải lấy các phần code mới nhất về Nhấn chuột phải vào phần bạn muốn cập nhật > Get Latest Version (Recursive) ![](https://i1.wp.com/farm3.staticflickr.com/2933/13902262929_2db6b4718f_o.png)

*   Recursive tức là đệ quy. Tất cả các file bên trong nó cũng sẽ được cập nhật theo

Khi bạn dùng lệnh này mà một số file của bạn có thay đổi chưa check in, nếu Team Foundation thấy có thể xử lý, nó sẽ xử lý giúp bạn luôn bằng cách gộp chung các thay đổi này với nhau. Tuy nhiên nếu có các thay đổi xung đột nhau, bạn sẽ có tùy chọn xem các xung đột để ra quyết định

*   Get Specific version lại là một cách khác để đưa Project hoặc file nào đó về hiện trạng y hệt như một lần check in nào đó. Bạn có thể dùng số Changeset, hoặc ngày tháng để tìm kiếm toàn bộ các lần check in và quyết định “phục hồi”
    
*   Undo Pending Change xóa bỏ toàn bộ các thay đổi của bạn, và đưa Project hoặc file về lần Check in gần nhất.
    

Như vậy, bạn đã có trong tay một cỗ máy thời gian thần kỳ để kiểm soát Source Code của mình, đồng thời hợp tác làm Team một các hiệu quả