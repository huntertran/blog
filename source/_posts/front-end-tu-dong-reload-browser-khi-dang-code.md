---
title: '[Front-end] Tự động reload browser khi đang code'
tags:
  - browsersync
  - css
  - html
  - live reload
  - visual studio code
id: '702'
categories:
  - - c
    - ASP.NET
date: 2017-04-12 04:56:00
---

Mỗi lần nói tới CSS, là các front-end developer lại thấy chán nản mệt mỏi các kiểu Thử nghĩ xem, mỗi lần sửa CSS (hoặc SCSS), bạn sẽ phải quay lại web browser, nhấn reload / F5 / Ctrl + F5 Nếu có cách để browser tự động reload mỗi khi có thay đổi code thì sao nhỉ Bài viết này sẽ hướng dẫn các bạn dùng Visual Studio Code kèm với NodeJs để có tự động reload web khi có code thay đổi
<!-- more -->
**Mục lục**

*   [Bước 1: Cài đặt môi trường](#bước-1-cài-đặt-môi-trường)
*   [Bước 2: Cài đặt các nodejs package](#bước-2-cài-đặt-các-nodejs-package)
*   [Bước 3: Cài đặt ở local folder](#bước-3-cài-đặt-ở-local-folder)
*   [Bước 4: Cài đặt BrowserSync](#bước-4-cài-đặt-browsersync)
*   [Bước 5: Tạo gulp task](#bước-5-tạo-gulp-task)
*   [Chạy tasks](#chạy-tasks)

# Bước 1: Cài đặt môi trường

Sẽ có một số phần mềm cần bạn cài đặt. Những phần mềm này khá phổ biến

*   [https://nodejs.org](https://nodejs.org)
*   [https://code.visualstudio.com/](https://code.visualstudio.com/)

_Bạn có thể chọn bản LTS, viết tắt cho chữ Long term support. Đây thường là phiên bản ổn định, ít lỗi lặt vặt_ ![Chọn LTS cho ít lỗi lặt vặt](https://farm3.staticflickr.com/2894/33833478232_a59cce160b_o.png)

# Bước 2: Cài đặt các nodejs package

**Mở Visual Studio Code** **Mở Terminal Windows** Bật Terminal Windows trong Visual Studio Code bằng cách nhấn Ctrl + \` hoặc View > Integrated Terminal ![](https://farm3.staticflickr.com/2814/33234696593_9fcee9f965_o.png) **Cài đặt trình biên dịch SASS/LESS** \[code lang=text\] npm install -g node-sass less \[/code\] Tham số -g là để cài đặt trên môi trường global ![](https://farm3.staticflickr.com/2873/33889703622_3cbc71f1cc_o.png) _Sau khi cài đặt SASS/LESS compiler_ **Cài đặt gulp toolkit** Cài đặt gulp toolkit để tự động hóa quá trình biên dịch \[code lang=text\] npm install -g gulp \[/code\] ![](https://farm3.staticflickr.com/2885/33234839763_71ffba8cfd_o.png) _Bạn có thể bỏ qua các warning khi cài đặt gulp_ **Initialize Node.Js** Nếu trước đó, bạn chưa bao giờ cài đặt NodeJs package manager, bạn sẽ gặp lỗi như sau ![](https://farm3.staticflickr.com/2829/33662078970_a1aaf77d2c_o.png) Gõ lệnh \[code lang=text\] npm init \[/code\] để init các tham số cần thiết cho npm và làm theo hướng dẫn trên màn hình. Nếu bạn không nhập gì cả và nhấn enter, npm sẽ dùng tham số default ![](https://farm3.staticflickr.com/2902/33235009203_a69320020e_o.png)

# Bước 3: Cài đặt ở local folder

Mặc dù bạn đã cài gulp ở global, nhưng bạn vẫn sẽ cần gulp được "copy" vào folder có chứa project của bạn. Lý do là khi gulp global được upgrade, hoặc bị xóa mất, gulp local của bạn vẫn chạy bình thường với một bản sao ổn định trong project folder của bạn Cài đặt gulp local \[code lang=text\] npm install gulp --save-dev \[/code\] Cài đặt gulp plugin \[code lang=text\] npm install gulp gulp-sass gulp-less \[/code\]

# Bước 4: Cài đặt BrowserSync

BrowserSync chính là thứ sẽ giúp chúng ta tự động reload trình duyệt Cũng trong Terminal Windows của Visual Studio, gõ lệnh \[code lang=text\] npm install browser-sync gulp --save-dev \[/code\] Tương tự, bạn cũng có thể bỏ qua các đoạn warning, thông báo ![](https://farm4.staticflickr.com/3703/33662203760_71636d02d3_o.png)

# Bước 5: Tạo gulp task

Gulp task là một file .json có chứa các lệnh, tham số cần thiết để thiết lập cho gulp

*   Trong Visual Studio Code, mở folder có chứa project HTML/CSS/JavaScript của bạn

\[code lang=text\] File > Open Folder > \[Chọn folder\] \[/code\]

*   Tạo một file tên "gulpfile.js" trong root folder của project
*   Gõ nội dung sau:

\[code lang=javascript\] var gulp = require('gulp'); var sass = require('gulp-sass'); var browserSync = require('browser-sync'); // compile task var gulp = require('gulp'); var sass = require('gulp-sass'); var browserSync = require('browser-sync'); // compile task gulp.task('sass', function () { gulp.src('css/\*.scss') .pipe(sass()) .on('error', swallowError) .pipe(gulp.dest(function (f) { return f.base; })) .pipe(browserSync.stream()); }); // browser sync init gulp.task('browser-sync', \['sass'\], function () { browserSync.init({ server: { baseDir: "./" } }); }); // watch for changes in html, css, scss gulp.task('default', \['browser-sync'\], function () { gulp.watch('css/\*.scss', \['sass'\]); gulp.watch('\*.html') .on('change', browserSync.reload); }) // skip if error occured function swallowError(error) { console.log(error.toString()) this.emit('end') } \[/code\]

*   Tạo tasks.json tasks.json giúp cho Visual Studio code biết cách chạy task gulp khi được ra lệnh
    *   Nhấn Ctrl + Shift + P và gõ "Configure Task Runner" rồi nhấn enter
    *   Chọn Others trong danh sách
    *   Gõ vào đoạn code sau

\[code lang=javascript\] { "version": "0.1.0", "command": "gulp", "isShellCommand": true, "tasks": \[ { "taskName": "default", "isBuildCommand": true, "showOutput": "always", "isBackground": true } \] } \[/code\]

# Chạy tasks

*   Tạo file "index.html" trong thư mục gốc. Mặc định BrowserSync sẽ theo dõi file này
*   Trong Visual Studio Code, nhấn **Ctrl + Shift + B** để bắt đầu chạy tasks
*   Bật tính năng Autosave cho Visual Studio Code

\[code lang=text\] File > Autosave \[/code\]