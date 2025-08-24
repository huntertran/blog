---
title: Java for Beginner - 3 - Java from C# cheats sheet
tags:
  - cheats sheet
  - java for beginner
id: '1215'
categories:
  - - Java
date: 2019-07-13 21:15:56
---

Doing C# long enough, you get yourself familiar with C# concepts and syntax. That's fine, but sometime when you need "the same" concepts in Java, it's quite difficult. This cheat sheet here to tackle that problem.

<!-- more -->

You can view other posts in the series here:

1.  [Introduction](https://huntertran.ca/2019/07/11/java-for-beginner-1-introduction-to-java-from-a-net-guy/)
2.  [Hello World](https://huntertran.ca/2019/07/12/java-for-beginner-2-hello-world-in-java/)
3.  Cheats sheet (this post)

Table of Content

*   [1. Classes](#1-classes)
    *   [1.1. Some keywords](#11-some-keywords)
    *   [1.2. Generic Class](#12-generic-class)
    *   [1.3. Interface Implement](#13-interface-implement)
*   [2. Variables](#2-variables)
*   [3. Methods](#3-methods)
    *   [3.1. Extension Method](#31-extension-method)
    *   [3.2. Safely use resource](#32-safely-use-resource)
    *   [3.3. Class Properties](#33-class-properties)

# 1. Classes

## 1.1. Some keywords

C#

Java

Explanation for Java

: (to extend the class)

extends

Java use the keyword `extends` to extend a class

base

super

To access the base class methods

namespace

package

Java class belongs to a package, which is the name of the folder contains the .java file

internal

Java use the concept of package. More complicated convertion is [here](https://stackoverflow.com/a/40437191/4506315)

using

import

**Java Example**

// File Animal.java, inside folder animals
package main.java.animals;

import RandomPackage.\*;
import RandomPackage.RandomSubPackage.\*;

public class Animal {
    ... other methods and properties ...
    public Double getWeight() {
        return weight;
    }
    ... other methods and properties ...
}

// File Pig.java, inside folder animals
package main.java.animals;

public class Pig extends Animal {
    ... other methods and properties ...

    // override the getWeight method
    public Double getWeight() {
        // do your override stuffs
        return super.getWeight();
    }
    ... other methods and properties ...
}

## 1.2. Generic Class

Generic class with constraint

**C# Example**

public class GenericClass<T> where T: SomeBase
{
}

**Java Example**

public class GenericClass<T extends SomeBase>
{
}

## 1.3. Interface Implement

**Java Example**

public class Pig implements IAnimal {
    public void Run() {
        ...your code to make the pig run...
    }
}

# 2. Variables

C#

Java

Explanation for Java

string

java.lang.String

`string` in both is a immutable class (cannot change instance of object after create)

object

java.lang.Object

decimal

java.math.BigDecimal

**Java Example**

String hello = "Hello World!";
System.out.print(hello);

# 3. Methods

## 3.1. Extension Method

In C#, you can write extension to an object, there is no equivalent to this in Java.

**C#**

public static class StringExtension
{
    public static string GetFirstThreeLetters(this string targetString)
    {
        // your code here to do the job
        // for example:
        // string result = targetString.SubString(0,3);
        return result;
    }
}

public class TestClass
{
    public void TestMethod()
    {
        string randomString = "This is so random";
        Console.WriteLine(randomString.GetFirstThreeLetters);
    }
}

// Console Output
// Thi

But in Java, you need to have the full static class

public final class StringUtils {
    public static String GetFirstThreeLetters(String stringToGet) {
        // your code here to do the job
        // for example:
        // String result = stringToGet.substring(0,3);
        return result;
    }
}

public class TestClass
{
    private void TestMethod()
    {
        String randomString = "This is so random";
        StringUtils.GetFirstThreeLetters(randomString);
    }
}

// Console Output
// Thi

## 3.2. Safely use resource

In C#, you can use a resource safely with the keyword `using`

**C# Example**

using(MyResource myResource = new MyResource())
{
    myResource.DoSomething();
}

In Java, you will use a different keyword: `try`

**Java Example**

try(MyResource myResource = new MyResource()) {
    myResource.DoSomething();
}

## 3.3. Class Properties

It is very convenient for C# developers to create and use `property` with auto-property, property with private backing fields.

**C# Example**

public class Animal
{
    // Auto-property
    public int Height { get; set; }

    // Property with private backing field

    // {rivate field
    private int \_weight;

    // Exposed with public property
    public int Weight
    {
        get
        {
            return \_weight;
        }
        set
        {
            // do some check to validate the value
            if(value > 0)
            {
                \_weight = value;
            }
        }
    }
}

// using in other class
public void RandomMethod()
{
    Animal pig = new Animal();
    pig.Weight = 500;

    Console.WriteLine("Pig weight: " + pig.Weight);
}

There is no equivalent to this in Java, you need to create 2 normal methods for get and set value of a private field

**Java Example**

public class Animal {
    private int \_weight;

    public void setWeight(int weight) {
        if(weight > 0) {
            \_weight = weight;
        }
    }

    public int getWeight() {
        return \_weight;
    }
}

// using in other class
public void RandomMethod() {
    Animal pig = new Animal();
    pig.setWeight(500);

    System.out.print("Pig weight: " + pig.getWeight());
}

Other different is just one google search result away ;) See you next post