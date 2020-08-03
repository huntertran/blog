---
title: '[Visual Studio] XAML Element Inspector with Visual Studio 2015 [en-US]'
tags:
  - Visual Studio
  - xaml
id: '456'
categories:
  - - c
    - Windows 10
date: 2015-08-02 07:41:51
---

Chào các bạn, kể từ bài blog này, mình sẽ viết bằng tiếng Anh nhé. Bạn có thể dùng Google Translate hoặc Bing Translate để dịch sang tiếng Việt nhé :3

Các bài viết trước mình cũng sẽ viết lại bằng tiếng Anh.

Hello guys, from this post forward, I will write in English. You can use "Google Translate" or "Bing Translate" to read it in Vietnamese

In the latest release of Visual Studio (aka Visual Studio 2015), Microsoft has introduce some cutting edge features called "Live Visual Tree" and "Live Property Explorer". Using this features, you can easily inspect and edit you XAML element on the fly.
<!-- more -->
# Live Visual Tree

For using Live Visual Tree, open any XAML project. It could be Windows 8, 8.1 App, Windows Universal App, or Universal Application Platform (UAP, aka App developed for Windows 10)

Press Build (F5) to compile and deploy the app. Then come back to Visual Studio. You will see a new small toolbar called "Live Visual Tree". Click on it to expand

![](https://farm1.staticflickr.com/543/20216853242_f1655e2c2e_o.png)

Now click on the small docking icon to make it stick there, make it easier to use

![](http://cuoilennaocacban2.files.wordpress.com/2015/08/080215_1141_windowsxaml1.png)

Now in this windows, click on the small icon that have the small triangle pointed to a rectangle. This is the Inspector, just like Google Chrome element inspector. Comeback to running app, you will wherevers the pointer, there will be a dotted box around it, cover the element under the pointer

![](http://cuoilennaocacban2.files.wordpress.com/2015/08/080215_1141_windowsxaml2.png)

Click once, and the Live Visual Tree will jump to the exact element.

![](https://farm1.staticflickr.com/528/19602618384_1423c50319_o.png)

You can click on other elements in the Live Visual Tree, and the red dotted box will jump to that element on your running app. In this way, you can see exactly how the element is drawn on your app.

You can also search for an element by its name or by type.

![](https://farm1.staticflickr.com/438/20038725589_1b8097c624_o.png)

# Live Property Explorer

With the element selected in Live Visual Tree, look on the right side of Visual Studio, you will see "Live Property Explorer", click on it to expand and click the dock button to make it stick there

![](https://farm1.staticflickr.com/425/20037363128_c89bbbe6d5_o.png)

Now it a lot fewer property than normal, right? Expand the "Default" group and you will see the rest.

The good things about this Live Property Explorer is, you can actually change the value, and observe the change in your running app

I will try to change the Height to 100, and see what happened on the app

![](https://farm1.staticflickr.com/504/20199163156_3fc683e0c9_o.png)

And now the app

![](https://farm1.staticflickr.com/555/20231217491_5d41f98c4f_o.png)

Wonderful isn't it? You can change almost everything, except some grey out property in the Live Property Explorer.

That's it. Now you know how to use the Live Visual Tree to inspect the XAML element on your apps, and Live Property Explorer to change the value of that element, and watch the change happened on the fly.

Stay toon for other cool feature of the new Visual Studio 2015