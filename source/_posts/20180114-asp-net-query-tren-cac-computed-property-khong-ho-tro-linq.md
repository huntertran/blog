---
title: '[asp.net] - Query trên các computed property không hỗ trợ LINQ'
tags:
  - Computed Property
  - LINQ
  - Query
id: '938'
categories:
  - - CSharp
    - ASP.NET
date: 2018-01-14 11:18:05
---

Trong một project gần đây ở công ty, tôi bàng hoàng nhận ra rằng:

> LINQ và Entity Framework không hỗ trợ query trên các property được tính toán dựa trên các field khác

Vậy giờ ta phải làm sao? May mắn là vẫn có cách

<!-- more -->

<!-- TOC -->

- [1. Computed Property](#1-computed-property)
- [2. Simple LINQ](#2-simple-linq)
- [3. Solution](#3-solution)
    - [3.1. [Slow performance] Gọi ToList](#31-slow-performance-g%E1%BB%8Di-tolist)
    - [3.2. [DRY Principle violated] Viết biểu thức](#32-dry-principle-violated-vi%E1%BA%BFt-bi%E1%BB%83u-th%E1%BB%A9c)
- [4. The best solution](#4-the-best-solution)
- [5. Make life easier](#5-make-life-easier)

<!-- /TOC -->

# 1. Computed Property
<a id="markdown-computed-property" name="computed-property"></a>

Là một property chỉ có hàm get, và trong get đó, giá trị trả về được tính toán dựa trên các property khác

```cs
public class TestViewModel
{
    [Required]
    [MaxLength(10, ErrorMessage = "Length must fewer than {1}")]
    public string FirstName { get; set; }
 
    [Required]
    [StringLength(10)]
    public string LastName { get; set; }
 
    // Computed Property
    [NotMapped]
    public string FullName => FirstName + LastName;
}
```

Theo các chuẩn thiết kế database, một column phải chứa dữ liệu mà không thể được suy ra từ các dữ liệu khác. Đoạn Attribute `[NotMapped]` phục vụ cho việc đó. EF sẽ không sinh ra code generate column `FullName` nếu bạn dùng code first, không cố gắng tìm column `FullName` trong table nếu bạn dùng database first

# 2. Simple LINQ
<a id="markdown-simple-linq" name="simple-linq"></a>

Để query một giá trị nào đó trong Database dùng Entity Framework, bạn có thể dùng LINQ rất đơn giản như sau

```cs
// TableNameWithS is your table name in plural
 
var names = dbContext.TableNameWithS.Where(x => x.FirstName.Contains("test"));
```

Nhưng cũng đoạn code đó sẽ gây lỗi nếu bạn cố gắn dùng nó với Property `FullName`

```cs
// BUG BUG BUG

var names = dbContext.TableNameWithS.Where(x => x.FullName.Contains("test"));
```

# 3. Solution
<a id="markdown-solution" name="solution"></a>

> TL;DR: [The best solution](#4-the-best-solution)

## 3.1. [Slow performance] Gọi ToList
<a id="markdown-%5Bslow-performance%5D-g%E1%BB%8Di-tolist" name="%5Bslow-performance%5D-g%E1%BB%8Di-tolist"></a>

```cs
var names = dbContext.TableNameWithS.ToList().Where(x => x.FullName.Contains("test"));
```

Gọi ToList sẽ làm Entity Framework gọi tới database, thực thi bất kỳ đoạn query nào trước đó, rồi mới thực thi tới đoạn LINQ có computed property của bạn

Nhược điểm của nó là EF sẽ query ra kết quả nhiều hơn so với cần thiết, làm giảm performance của ứng dụng

## 3.2. [DRY Principle violated] Viết biểu thức
<a id="markdown-%5Bdry-principle-violated%5D-vi%E1%BA%BFt-bi%E1%BB%83u-th%E1%BB%A9c" name="%5Bdry-principle-violated%5D-vi%E1%BA%BFt-bi%E1%BB%83u-th%E1%BB%A9c"></a>

Một cách khác là thay vì sử dụng computed property, ta có thể viết thẳng biểu thức của property đó vào câu query

```cs
var names = dbContext.TableNameWithS.Where(x => (x.FirstName + x.LastName).Contains("test"));
```

Nhược điểm của cách này là bạn đã vi phạm nguyên tắc "DRY" - Don't repeat yourself. Một biểu thức mà phải code tới 2 lần. Nếu sau này bạn thay đổi biểu thức đó ở 1 chỗ, thì ở chỗ còn lại bạn cũng sẽ phải đổi theo. Nếu bạn quên -> BUG ngay và luôn

> The DRY principle is stated as "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system"
> 
> _Source: [https://en.wikipedia.org/wiki/Don%27t_repeat_yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)_

# 4. The best solution
<a id="markdown-the-best-solution" name="the-best-solution"></a>

[DelegateDecompiler](https://github.com/hazzik/DelegateDecompiler) - Một bộ thư viện cực khủng giúp bạn decompile biểu thức của computed property, và translate chúng thành LINQ, EF sau đó sẽ translate nó thành câu lệnh SQL.

Nhược điểm của nó là nó không thể dịch được khi bạn sử dụng các method, class mà bạn tự định nghĩa, không nằm trong .NET Framework

Sử dụng nó thì không còn gì dễ hơn

Bước 1: Cài đặt nuget DelegateDecompiler

```s
Install-Package DelegateDecompiler
```

Bước 2: Trang trí property với attribute `[Computed]`

```cs
public class TestViewModel
{
    [Required]
    [MaxLength(10, ErrorMessage = "Length must fewer than {1}")]
    public string FirstName { get; set; }
 
    [Required]
    [StringLength(10)]
    public string LastName { get; set; }
 
    // Computed Property
    [NotMapped]
    [Computed]
    public string FullName => FirstName + LastName;
}
```

Bước 3: Gọi method Decompile

```cs
var names = dbContext.TableNameWithS
                     .ToList()
                     .Where(x => x.FullName.Contains("test")).Decompile();

```

> Thư viện này thậm chí còn hỗ trợ async, các advanced functions của EF như `Include`, `AsNoTracking` với phần mở rộng [DelegateDecompiler.EntityFramework](https://nuget.org/packages/DelegateDecompiler.EntityFramework)

# 5. Make life easier
<a id="markdown-make-life-easier" name="make-life-easier"></a>

Bạn cũng có thể cấu hình cho asp tự xử lý các property có \[NotMapped\]

Tạo một class `Configuration`

```cs
public class DelegateDecompilerConfiguration : DefaultConfiguration
{
    public override bool ShouldDecompile(MemberInfo memberInfo)
    {
        // Automatically decompile all NotMapped members
        return base.ShouldDecompile(memberInfo) || memberInfo.GetCustomAttributes(typeof(NotMappedAttribute), true).Length > 0;
    }
}
```

Rồi đăng ký nó trong method Startup như sau

```cs
DelegateDecompiler.Configuration
                  .Configure(new DelegateDecompilerConfiguration());
```