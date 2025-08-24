---
title: Optimize list of bool values in C#
tags:
  - csharp
  - bool
  - boolean
  - bitwise
  - optimize
date: 2022-04-23 20:47:44
---


Boolean data type represents the `true`/`false` value. If you create a class with multiple booleans, here are some tips and tricks to optimize them. This will include using bitwise operations and how to flatten them for display on UI.

<!-- more -->

<!-- TOC -->

- [1. The basic - Using bit to store multiple booleans](#1-the-basic---using-bit-to-store-multiple-booleans)
    - [1.1. Hotel example](#11-hotel-example)
    - [1.2. Bitwise operation comes to the rescue](#12-bitwise-operation-comes-to-the-rescue)
    - [1.3. Storing booleans](#13-storing-booleans)
    - [1.4. Retrieving booleans](#14-retrieving-booleans)
- [2. FlagsAttribute in C# - They already did it for you](#2-flagsattribute-in-c---they-already-did-it-for-you)
    - [2.1. Storing data](#21-storing-data)
    - [2.2. Retrieving data](#22-retrieving-data)
- [3. Mind the limit of int](#3-mind-the-limit-of-int)
- [4. Flatten the value](#4-flatten-the-value)

<!-- /TOC -->

# 1. The basic - Using bit to store multiple booleans
<a id="markdown-the-basic---using-bit-to-store-multiple-booleans" name="the-basic---using-bit-to-store-multiple-booleans"></a>

## 1.1. Hotel example
<a id="markdown-hotel-example" name="hotel-example"></a>

Let's jump into an example.

It's summer here in Montréal, and you want to book a hotel there for travel. The hotel's rooms have multiple amenities. Some rooms have a TV; others have an oven, etc.

Naturally, when representing these rooms in the database, we would need some boolean values (or `bit` data type in SQL). The class should look like this:

```csharp
public class Room
{
    public int RoomNumber { get; set; }
    
    public bool HasTV { get; set; }

    public bool HasMicrowave { get; set; }

    public bool HasOven { get; set; }
}
```

All good if your hotel's room only has that three amenities. What if the room has 10, 30, or even 100 amenities? Store each of them in a new `bool` property? How about the database?

> Suddenly, the manager wants to add a new amenity: A face mask dispenser. How would you deal with it? Would you add a new column in the database, a new property in the class, etc?

## 1.2. Bitwise operation comes to the rescue
<a id="markdown-bitwise-operation-comes-to-the-rescue" name="bitwise-operation-comes-to-the-rescue"></a>

We all know that:

```c
AND operator
0 & 0 => 0
0 & 1 => 0

OR operator
0 | 0 => 0
0 | 1 => 1
```

We can exploit these bitwise to store our boolean values.

First, we set up an enum class. Notice the value of enum is the power of **`2`**

```csharp
public enum Facility
{
    None         = 0,
    HasTV        = 1,
    HasMicrowave = 2,
    HasOven      = 4,
}
```

By doing this, when storing enum, these values will have the binary as follow:

```csharp
None         = 000
HasTV        = 001
HasMicrowave = 010
HasOven      = 100
```

The **`1`** character is in a different location on each value. When applying the `AND` or `OR` bitwise operator on these values, the combined value will have the `0` or `1` placed in the exact location.

For example:

```csharp
    HasTV           001
|   HasMicrowave    010  <-- OR operator
-----------------------
                    011  <-- equal to 3 in decimal
```

We can store all the booleans in a single `int` value using this.

The `AND` operator with the targeted value will replace with `1` character with `0`:

```csharp
    value           011  <-- 3 in decimal, from above
&   HasTV           001  <-- AND operator
-----------------------
    Has TV?         001  <-- equal to enum value 1: HasTV




    value           011  <-- 3 in decimal
&   HasMicrowave    010  <-- AND operator
-----------------------
    Has microwave?  010  <-- equal to enum value 2: HasMicrowave
```

How about `HasOven`?

```csharp
    value           011  <-- 3 in decimal
&   HasOven         100  <-- AND operator
-----------------------
    Has oven?       000  <-- equal to enum value 0: None
```

## 1.3. Storing booleans
<a id="markdown-storing-booleans" name="storing-booleans"></a>

As you can guess, storing booleans is doing an `OR` operator on the values.

```csharp
var facilities = Facility.HasTV | Facility.HasMicrowave;

// facilities = 3
```

## 1.4. Retrieving booleans
<a id="markdown-retrieving-booleans" name="retrieving-booleans"></a>

To retrieve the bool values, we can do `AND` operator with the targeted enum and test if the result > 0

```csharp
var isHasTV = (facilities & Facility.HasTV) > 0 ? true : false;
```

# 2. FlagsAttribute in C# - They already did it for you
<a id="markdown-flagsattribute-in-c%23---they-already-did-it-for-you" name="flagsattribute-in-c%23---they-already-did-it-for-you"></a>

To make life easier for developers, Microsoft has a [`FlagsAttribute`](https://docs.microsoft.com/en-us/dotnet/api/system.flagsattribute) that you can decorate your enum.

> This will _indicates that an enumeration can be treated as a bit field; that is, a set of flags._

```csharp
[Flags]
public enum Facility
{
    None         = 0,
    HasTV        = 1,
    HasMicrowave = 2,
    HasOven      = 4,
}
```

## 2.1. Storing data
<a id="markdown-storing-data" name="storing-data"></a>

Using the same `OR` bitwise operator to store the data

```csharp
var roomFacility = Facility.HasTV | Facility.HasMicrowave;
```

## 2.2. Retrieving data
<a id="markdown-retrieving-data" name="retrieving-data"></a>

Use [`HasFlag`](https://docs.microsoft.com/en-us/dotnet/api/system.enum.hasflag) method to retrieve data

```csharp
var hasTV = roomFacility.HasFlag(Facility.HasTV);

// hasTV = true
```

# 3. Mind the limit of `int`
<a id="markdown-mind-the-limit-of-int" name="mind-the-limit-of-int"></a>

There are 4 data type you can use to store `int` value in [SQL Server](https://docs.microsoft.com/en-us/sql/t-sql/data-types/int-bigint-smallint-and-tinyint-transact-sql):

| **Data type** | **Range** | **Storage** |
|---|---|---|
| `bigint` | -2^63 (-9,223,372,036,854,775,808) to 2^63-1 (9,223,372,036,854,775,807) | 8 Bytes |
| `int` | -2^31 (-2,147,483,648) to 2^31-1 (2,147,483,647) | 4 Bytes |
| `smallint` | -2^15 (-32,768) to 2^15-1 (32,767) | 2 Bytes |
| `tinyint` | 0 to 255 | 1 Byte |

8 bits = 1 byte. So for 1 byte of storage, you can store up to 8 boolean values (theoretically).

The default `int` primitive type in C# is 32 bits or 4 bytes

> What if you want to store more than 32 boolean values?

In this case, I would strongly recommend you to re-design your class and data structure to split it into smaller ones

# 4. Flatten the value
<a id="markdown-flatten-the-value" name="flatten-the-value"></a>

What if you want to flatten the boolean values compressed into a flat class with actual `bool` properties?

Of course you can do it with `HasFlag()` method, and a bunch of `if` statements. However, writing `if` 10 times in a row is not very maintainable.

Luckily we have `reflection`, a way to read the class meta data.

First, we need to create a new attribute class ([full source code with comment here](https://github.com/huntertran/flag-flattener/blob/master/FlattenedFlagAttribute.cs)):

```csharp
[AttributeUsage(AttributeTargets.Property, AllowMultiple = false)]
public class FlattenedFlagAttribute : Attribute
{
    public Enum enumProperty;

    public FlattenedFlagAttribute(Facility facility)
    {
        this.enumProperty = facility;
    }

    // This method allow us "flatten" the compacted data into the property which is decorated with the same Facility data type
    public static void Flatten(object o, Enum enumData)
    {
        var props = o.GetType().GetProperties();

        foreach (var prop in props)
        {
            var attr = prop.GetCustomAttributes(typeof(FlattenedFlagAttribute), false);

            if (attr.GetLength(0) > 0)
            {
                prop.SetValue(o, enumData.HasFlag(((FlattenedFlagAttribute)attr[0]).enumProperty));
            }
        }
    }
}
```

Now, we can simply decorate the flatten properties with this attribute:

```csharp
public class FlattenedRoom
{
    public int RoomNumber { get; set; }

    [FlattenedFlag(Facility.HasTV)]
    public bool HasTV { get; set; }

    [FlattenedFlag(Facility.HasMicrowave)]
    public bool HasMicrowave { get; set; }

    [FlattenedFlag(Facility.HasOven)]
    public bool HasOven { get; set; }

    public FlattenedRoom(int roomNumber, Facility facility)
    {
        RoomNumber = roomNumber;
        FlattenedFlagAttribute.Flatten(this, facility);
    }
}
```

When you construct a new `FlattenedRoom`, simple feed it with the compacted `Facility` value, and everything will be correctly set.

Head over here for the full source code: [https://github.com/huntertran/flag-flattener](https://github.com/huntertran/flag-flattener)