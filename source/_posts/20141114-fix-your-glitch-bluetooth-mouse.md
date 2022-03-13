---
title: Fix your glitch Bluetooth mouse (or any bluetooth devices)
tags:
  - tips
id: '362'
categories:
  - - Computer Tips
date: 2014-11-14 09:46:24
---

[![2_5F00_77B60B43](https://cuoilennaocacban2.files.wordpress.com/2014/11/2_5f00_77b60b43.jpg)](https://cuoilennaocacban2.files.wordpress.com/2014/11/2_5f00_77b60b43.jpg)

You have an excellent Bluetooth mouse. Heavy, comfort for your hand, BlueTrack Technology, etc. Everything is great, but... the mouse got frozen or lagged sometimes.

How to fix this?

<!-- more -->

# Root cause

The root cause of this problem, after so many searches, is because Windows is allowed to turn off some devices when they're not active after a while to save battery.

# Solution

Right-click on Start button > Device Manager

![](https://farm9.staticflickr.com/8661/15167914553_df323bc4bd_o.png)

Find `Bluetooth` category, find the devices with "Adaptor" in the name

![](https://farm6.staticflickr.com/5609/15601546119_b9cc814b86_o.png)

Right-click on that device > Properties > Power Management > Uncheck "Allow the computer to turn off this device to save power."

![](https://farm8.staticflickr.com/7513/15788949452_8f09bede17_o.png)

That's it :3