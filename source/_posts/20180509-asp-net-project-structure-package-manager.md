---
title: '[ASP.NET] - Project Structure & Package Manager'
tags:
  - architech
  - manager
  - package
  - project
  - structure
id: '1025'
categories:
  - - c
    - ASP.NET
date: 2018-05-09 13:05:37
---

Bạn tổ chức thư mục, tập tin như thế nào? Có nên tách ra thành nhiều project con? Có nên dùng package manager?

Trong phần này, mình sẽ trình bày kinh nghiệm cá nhân về các tổ chức và quản lý projects, và dùng package manger nhóe
<!-- more -->
*   [1. Project & Solution](#1-project--solution)
    
    *   [1.1. Lý do](#11-lý-do)
        
        *   [1.1.1. Dùng lại](#111-dùng-lại)
        *   [1.1.2. Phân phối](#112-phân-phối)
        *   [1.1.3. Triển khai](#113-triển-khai)
        *   [1.1.4. You name it](#114-you-name-it)
    *   [1.2. Phân chia projects](#12-phân-chia-projects)
*   [2. Package Manager](#2-package-manager)
    
    *   [2.1. For backend - NUGET](#21-for-backend---nuget)
    *   [2.2. For front-end - Yarn](#22-for-front-end---yarn)
        
        *   [2.2.1. Tính phụ thuộc](#221-tính-phụ-thuộc)
        *   [2.2.2. Sources](#222-sources)
        *   [2.2.3. Tái tạo](#223-tái-tạo)

# 1. Project & Solution

Cách dễ nhất, cũng như đơn giản nhất, là chỉ bao gồm 1 project mà thôi. Ở Part 1, bạn cũng đã có "kinh nghiệm" gõ lệnh tạo project.

Visual Studio thì lại không như vậy, nó ép bạn phải xài một khái niệm gọi là "Solution". Theo đó, một hoặc nhiều project sẽ nằm trong 1 solution. Khi bạn mở project được tạo bởi dòng lệnh `dotnet new *` trong Visual Studio, nó cũng sẽ tạo ra một cái Solution ất ơ nào đấy rồi nhét cái project của bạn vào.

Sẽ là một thói quen tốt khi bạn tạo nhiều project ứng với các mục đích khác nhau, phục vụ cho dự án phần mềm của bạn nói chung và ASP.NET nói riêng

## 1.1. Lý do

Bạn thắc mắc là tại sao mình lại phải chia nhiều project như vậy? Để chung luôn thì có đỡ công include thư viện biết bao nhiêu không?

### 1.1.1. Dùng lại

Khi một số code có chức năng riêng biệt nào đó được bạn tách ra thành 1 project riêng, thì nó sẽ rất dễ dàng để dùng lại nó vào những dự án khác.

Giả sử bạn có 1 số helpers và class giúp việc kết nối tới database rất nhanh chóng và gọn lẹ. Khi nó ở 1 project riêng, bạn có thể dễ dàng up nó lên git, rồi các project khác cứ thế mà clone về xài thôi. Khi bạn update project trên git đó, toàn bộ các clone của nó sẽ đều được update theo.

### 1.1.2. Phân phối

Cũng ví dụ trên, project của bạn đã nằm ở mức library, tức là một thư viện rồi. Bạn có thể dụ bạn bè mình xài nó, phát triển thêm, đóng góp cho nó, pack nó lại thành nuget package, blah blah blah và blah blah blah

### 1.1.3. Triển khai

1 công ty nọ thấy lib version 1.0 của bạn quá hay, họ quyết định tải zìa và xài trong dự án cực khủng của họ. 10 năm sau, bạn cập nhật cái lib của mình lên version 2.0, dùng lại toàn bộ các method và hàm sẵn có, chẳng qua là thay đổi thuật toán cho nó chạy nhanh lên thôi. Công ty chỉ cần bỏ ra 1 chi phí tối thiểu để clone cái lib của bạn về, build và replace cái lib đang chạy trên production của họ. Thế là xong. Không cần phải build lại cả project, không cần phải deploy lại.

### 1.1.4. You name it

Khi bạn đã dấn thân vào nghiệp code càng lâu năm, bạn sẽ phát hiện ra càng nhiều lợi ích khác của việc chia tách này.

## 1.2. Phân chia projects

Ở mô hình MVC, cả Model-View-ViewModel đều gắn liền với nhau, nên chúng ta không tách

> Tuy nhiên, có một số công ty tách cái Model ra một project riêng. Điều này giúp bạn dễ quản lý code hơn. Đôi khi cũng tách luôn cái Controller thành 1 project

1 nguyên tắc mình hay dùng để tách project là dựa trên tính năng của nó. Ví dụ:

*   Unit Test -> **Tách**
*   Data Connection Layer -> **Tách**
*   Encryption / Decryption -> **Tách**
*   Encryption _đứng riêng_ -> **KHÔNG tách**

# 2. Package Manager

Làm web có 2 phần, front-end và back-end. Và cả 2 phần này đều có package manager (với ASP.NET)

## 2.1. For backend - NUGET

Về phía backend, thì lợi ích của việc sử dụng package manager (nuget) là quá rõ ràng. Bạn chỉ cần "**search & install**", không còn cảnh đêm hôm khuya khoắt ngồi lọ mọ crack IDM để download một cái lib nào đấy có đuôi .dll, rồi mò mẫm trong đống file đã download để import nó vào project.

Nó sẽ triệt tiêu luôn cái vấn đề tương thích platform với lib (lib build cho x64 chỉ chạy được trên x64 và tương tự cho x86)

## 2.2. For front-end - Yarn

> Bower đã bị ngừng hỗ trợ

Về phía front-end thì sao? Chẳng phải chỉ cần thêm file .css và .js vào là web chạy ngon lành sao

**đúng rồi, NHƯNG**

*   nguồn không thống nhất
*   lib này phụ thuộc lib kia, lib kia phụ thuộc lib nọ
*   nó có chạy trên máy tui mà sao không chạy được trên máy khác

và front-end package manager được tạo ra để giải quyết mấy vấn đề này

Vậy đó, nếu ASP.NET chỉ có 1 (vài) package manager như Nuget, thì trong thế giới front-emd ta có cả chục. Mình sẽ giới thiệu sơ qua về 1 tân binh mới nổi, và đang rất hot - YARN

### 2.2.1. Tính phụ thuộc

`JQuery` là một lib rất phổ biến, và ty tỷ lib khác được xây dựng mà cần tới nó. Nhưng JQuery có cũng kha khá phiên bản khác nhau, và các lib khác nhau lại dùng các version khác nhau của JQuery.

Yarn sẽ giúp bạn loại bỏ vấn đề này. Khi JQuery được cài đặt qua Yarn, sẽ chỉ có 1 version duy nhất, và tất cả package khác đều sẽ dựa trên version này.

### 2.2.2. Sources

Toàn bộ package được host trên yarn, thì bạn chỉ cần lên Yarn lấy về là xong, không cần phải vào từng website của từng lib, rồi kiếm cái nút download nữa.

### 2.2.3. Tái tạo

Yarn sử dụng một file package.json để lưu trữ thông tin các package đã được cài đặt. Dùng file này, trên bất kỳ máy nào, nó sẽ tạo ra chính xác các file cần thiết để project của bạn có thể chạy ngon lành y như lúc dev vậy

![worked on my machine](https://farm1.staticflickr.com/966/27130244167_1f468f1efa_o.png)

Thế nhé bạn ;)