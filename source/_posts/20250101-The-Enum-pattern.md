---
title: The Enum pattern
date: 2025-01-01 16:08:01
tags:
    - Angular
categories:
  - - JavaScript and TypeScript
---

An enum (short for "Enumeration") is a value type that represents a set of named constants. This type allow you to define a set of named values that have underlying values, usually numeric ones.

In this post, we will discuss on how to extent this type to store more data, and use them in a simple Angular select list.

<!--more-->

# Enum in different languages

In TypeScript, you can set enum value to a string

```ts
export enum Color {
    Red = 'red',
    Green = 'green',
    Blue = 'blue'
}
```

You can also get value of the enum by a function. Head [here](https://www.typescriptlang.org/docs/handbook/enums.html) for more info. But be careful while using these. This is pretty wild, and prone to cause problems when the project get larger, and multiple devs joined.

Enum in TypeScript is different from most of the other programming languages, where you can only set value of enum with numeric values like int, uint, long, etc.

What if you want to include more data into your enum. In the above example, how can you add the hex color code, along side with a short description?

# The Enum pattern

Simply put, you can declare your enum as a class with static property, then use them as a normal enum

```ts
// for TypeScript

export class Color {
    public static Red = new Color(1, "red", "#FF0000", "A vibrant, bold, and attention-grabbing color");
    public static Green = new Color(2, "green", "#00FF00", "A calming, soothing, and trustworthy color.");
    public static Blue = new Color(3, "blue", "#0000FF", "A fresh, natural, and balancing color.");

    public get Id(): number { return this.id; }
    public get Name(): string { return this.name; }
    public get Hex(): string { return this.hex; }
    public get Description(): string { return this.description; }

    constructor(private id: number, private name: string, private hex: string, private description: string) { }
}
```

When you want to use it, you need to include the property you want to get

```ts
let color: Color = Color.Red;
console.log(color.Description);

// A vibrant, bold, and attention-grabbing color
```

In C#, the code is a little bit more complicated, and covered in this excellent article: [Use enumeration classes instead of enum types](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/enumeration-classes-over-enum-types)

That's all for today. See you next time ;)