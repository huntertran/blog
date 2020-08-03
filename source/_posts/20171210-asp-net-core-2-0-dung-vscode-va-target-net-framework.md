---
title: '[ASP.NET Core 2.0] - dùng VSCode và target .NET Framework'
tags:
  - .net core
  - .net framework
id: '922'
categories:
  - - c
    - ASP.NET
  - - C#
  - - VSCode
date: 2017-12-10 04:44:25
---

Nếu cảm thấy Visual Studio Community quá nặng nề, nhưng bạn vẫn muốn dev website bằng asp.net, và target .net framework, vậy tại sao bạn không sử dụng VSCode nhỉ?

Trớ trêu thay, OmniSharp chưa hỗ trợ .net core 2 trên vscode, nhưng bài viết này sẽ hướng dẫn bạn cách để vượt qua giới hạn đó

Lưu ý là cách này chỉ hoạt động trên windows nhé
<!-- more -->
*   [1\. Chuẩn bị](#1-chuẩn-bị)
*   [2\. Các bước cài đặt](#2-các-bước-cài-đặt)
    *   [2.1. Create project](#21-create-project)
    *   [2.2. chỉnh sửa project để target .NET Framework 4.7.1 (or 4.6.1)](#22-chỉnh-sửa-project-để-target-net-framework-471-or-461)
    *   [2.3. Compile, Run và Debug](#23-compile-run-và-debug)
    *   [2.4. Run and Debug](#24-run-and-debug)

# 1\. Chuẩn bị

*   VSCode :v : [https://code.visualstudio.com/](https://code.visualstudio.com/)
*   C# for Visual Studio Code (powered by OmniSharp) extension
    *   Một vài Extension khác như **Debugger for Chrome**, **Beautify**, **html css support**, **indent-rainbow**, **indenticator**, **material icon theme**, **sass lint**, **sort lines**
*   .NET Framework 4.7.1 developer pack: [https://www.microsoft.com/net/download/thank-you/net471-developer-pack](https://www.microsoft.com/net/download/thank-you/net471-developer-pack)
*   Build Tools for Visual Studio 2017 (MSBuild is licensed under the MIT license): [https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15)

> ![](https://farm5.staticflickr.com/4531/24089620797_59f8abe75b_o.png) NẾU BẠN SỬ DỤNG .NET FRAMEWORK 4.6.1 Cài thêm nuget package sau vào project để bỏ các lỗi liên quan tới intellisense \[code lang=bash\] dotnet add package NETStandard.Library.NETFramework --version 2.0.0-preview2-25405-01 \[/code\]

# 2\. Các bước cài đặt

## 2.1. Create project

\[code lang=text\] Open VSCode -> Open Folder -> trỏ tới folder sẽ chứa tất cả code của bạn Views > Integrated Terminal \[/code\] rồi gõ \[code lang=bash\] dotnet new mvc \[/code\] SDK sẽ tạo ra toàn bộ folders và files cần thiết cho bạn Các lựa chọn khác khi tạo một project: ['dotnet new' command at docs.microsoft.com](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-new?tabs=netcore2x)

## 2.2. chỉnh sửa project để target .NET Framework 4.7.1 (or 4.6.1)

Trong thư mục gốc của project mới tạo, mở file `YourProjectName.csproj` và sửa như sau \[code lang=xml\] <Project Sdk="Microsoft.NET.Sdk.Web"> <PropertyGroup> <TargetFramework>net471</TargetFramework> <!--RuntimeIdentifier is based on your local machine. A list of all available values here--> <RuntimeIdentifier>win10-x64</RuntimeIdentifier> </PropertyGroup> <ItemGroup> <!--These are nuget package targeting .net framework, dependency is .NET Standard 2.0, which is supported by .net framework 4.7.1--> <PackageReference Include="Microsoft.AspNetCore" Version="2.0.1" /> <PackageReference Include="Microsoft.AspNetCore.Mvc" Version="2.0.1" /> <PackageReference Include="Microsoft.AspNetCore.Mvc.Razor.ViewCompilation" Version="2.0.1" PrivateAssets="All" /> <PackageReference Include="Microsoft.AspNetCore.StaticFiles" Version="2.0.1" /> <PackageReference Include="Microsoft.VisualStudio.Web.BrowserLink" Version="2.0.1" /> </ItemGroup> <ItemGroup> <DotNetCliToolReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Tools" Version="2.0.1" /> </ItemGroup> </Project> \[/code\]

## 2.3. Compile, Run và Debug

1.  Debug > Settings

![](https://farm5.staticflickr.com/4563/38068269685_37649c8f9e_o.png)

1.  Chọn `.NET Core` trong danh sách
    
2.  Sửa file `launch.json` trong thư mục `.vscode` thành như sau
    

![](https://farm5.staticflickr.com/4683/27177480069_ee651b8559_o.png)

1.  Tạo một file mới cũng trong thư mục đó, với tên là `tasks.json` với đoạn code sau

\[code lang=text\] { "version": "2.0.0", "tasks": \[ { "taskName": "build", "command": "dotnet", "type": "process", "args": \[ "build", "${workspaceFolder}/StudyAspCore.csproj" \], "problemMatcher": "$msCompile" } \] } \[/code\]

## 2.4. Run and Debug

To run the application ![](https://farm5.staticflickr.com/4583/38918103882_b12ebfb671_o.png) Bạn cũng có thể chạy project bằng nút Run trên status bar ![](https://farm5.staticflickr.com/4594/38068348135_e554c5e5ca_o.png) Để debug thì chỉ cần đặt break point ngay tại nơi cần debug ![](https://farm5.staticflickr.com/4599/38238463834_bf8bc671b6_o.png)