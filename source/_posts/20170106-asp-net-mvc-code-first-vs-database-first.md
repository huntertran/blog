---
title: '[ASP.NET MVC] Code first vs Database First'
tags:
  - code first
  - database first
id: '669'
categories:
  - - c
    - ASP.NET
date: 2017-01-06 08:30:52
---

Lúc mới làm ASP.NET, chắc bạn nào cũng sẽ hỏi câu hỏi này. Như kiểu nên làm quả trứng trước, sau đó để nó nở ra con gà, hay làm con gà trước, rồi để nó đẻ ra quả trứng?

Chọn cách nào đi chăng nữa, vẫn sẽ có một số sự khác biệt mà bạn cần biết để chọn cho đúng, xong rồi phóng lao để đâm theo

![original](https://cuoilennaocacban2.files.wordpress.com/2017/01/original.jpg)
<!-- more -->
# Giải thích

  

**Code First**

**Database First**

Viết các class Model bằng code C# Generate Database từ class Model

Generate Model từ Database Các class Model sẽ ko được phép chỉnh sửa

# Ưu điểm và nhược điểm

  

**Code First**

**Database First**

Ưu điểm

Rất phổ biến (vì các lập trình viên thường không thích thiết kế DB, nhưng thích thiết kế class)

Kiểm soát hoàn toàn code model, thêm xóa sửa thuộc tính vô cùng dễ dàng

Không phải nặng đầu suy nghĩ về DB. Đối với cách tiếp cận này, DB chỉ là cái "cục" data, lôi ra xài thôi

Có thể version control Database

Ít phổ biến hơn

DB có thể được develop riêng

Dùng được DB có sẵn

Entity Framework sẽ tạo ra các Entity class cho bạn

Nhược điểm

Các thay đổi cấu trúc trực tiếp trên DB sẽ mất

Khó kiểm soát những column sẽ tạo trên Db

Hơi khó khi kết hợp với Db có sẵn

Không thể thay đổi code đã được Generate (nó sẽ mất trong lần chỉnh sửa cấu trúc DB tiếp theo)

Khó khăn khi muốn thêm các DataAttribute và DisplayAttribute cho các class model

Bạn phải nhức đầu suy nghĩ khi muốn biểu diễn các kiểu quan hệ cha con của class Mỗi lần thay đổi cấu trúc DB, bạn sẽ phải update lại EDMX và tạo lại các class Model để phản ánh sự thay đổi đó

# Tương lai nào cho ASP.NET Core?

Tại thời điểm viết bài viết này, ASP.NET Core vẫn sẽ support Database First lâu dài, nhưng gặp một số lỗi rất khó chịu khiến bạn hơi khó khăn khi tạo Entities Class từ Database có sẵn

Có thể tạm kết luận là: Code first là tương lai, nhưng nếu thích, bạn vẫn có thể dùng Database First nhóe

Hết rồi :D