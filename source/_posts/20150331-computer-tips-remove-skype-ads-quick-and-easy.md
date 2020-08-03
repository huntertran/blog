---
title: '[Computer Tips] Remove Skype Ads Quick and Easy'
tags:
  - tips
id: '430'
categories:
  - - Computer Tips
date: 2015-03-31 04:07:22
---

Xài Skype, chắc ai cũng khó chịu với mấy cái quảng cáo lặp đi lặp lại chán phèo của Skype nhỉ

Và đây là cách loại bỏ mấy cái quảng cáo đó.
<!-- more -->
# 1\. Tắt thiết lập trong Skype

Vào Skype > Tools > Options > Privacy > Privacy Settings > Bỏ chọn "Allow Microsoft targeted ads blah blah blah"

# 2\. Tiếp tục chặn server quảng cáo

Control Panel -> Internet Options -> Security -> Restricted Sites -> Sites -> thêm g.msn.com và apps.skype.com

# 3\. Chỉnh sửa giao diện khung chat để loại bỏ quảng cáo

C:\\users\\youruser\\AppData\\Roaming\\Skype\\yourskypeuser\\config.xml

Kiếm dòng <AdvertPlaceholder>1</AdvertPlaceholder> rồi xóa hẳn nó luôn :3