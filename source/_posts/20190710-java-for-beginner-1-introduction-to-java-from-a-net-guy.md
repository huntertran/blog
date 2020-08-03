---
title: Java for Beginner - 1 - Introduction to Java from a .NET guy
tags:
  - java for beginner
id: '1193'
categories:
  - - Java
date: 2019-07-10 20:11:54
---

Coming to Java world, from a .NET guy, is like going from a full feature-rich and comfortable car to a basic bike with a lot of space for extension and customization.  
In this series, I will walk you through (hopefully) a small part of Java world, just enough for you to continue your exploration.
<!-- more -->
*   [1. Intro](#1-intro)
    *   [1.1. What it can do](#11-what-it-can-do)
    *   [1.2. Write one, run anywhere](#12-write-one-run-anywhere)
*   [2. Versions and Tools](#2-versions-and-tools)
    *   [2.1. Versions](#21-versions)
    *   [2.2. Tools](#22-tools)
    *   [2.3. Terms](#23-terms)
*   [3. Frameworks](#3-frameworks)

# 1. Intro

## 1.1. What it can do

When a person decided to study some new programming language or platform, the first question could be the purpose. Why do you want to study this language/platform? What it can do compared to xyz language?

The answer: almost anything!

From mobile application to huge software used in banking, super-computer and satellite in the sky.

## 1.2. Write one, run anywhere

Ideally, a Java developer can write the code one, and run it anywhere that can run Java Virtual Machine (JVM). But we live in an un-ideal world. There are differences between devices and operating systems, so there are different versions of JVM implementation. The famous title became

> Write one, debug everywhere

# 2. Versions and Tools

## 2.1. Versions

Java have different versions for different purpose

*   Java ME: Java Micro Edition. Optimized for mobile, embedded devices (like outdoor billboard, TV boxes, printers, etc.). The SDK for Java ME haven't had update since Jan 2018 (as of July 2019)
*   Java SE: Java Standard Edition. The name says it all. You can develop desktops and servers applications using this version. The [latest version](https://www.oracle.com/technetwork/java/javase/overview/index.html) is 12.0.1 (as of July 2019)
*   Java EE: Java Enterprise Edition. Support a lot more APIs like JSON processing, annotations, contexts and dependency injections. The [latest version](https://www.oracle.com/technetwork/java/javaee/overview/index.html) is 8u1 (I know, the version number is strange)
*   Java Embedded, Java TV, Java Card: Seem like different version of Java ME with a much more updated SDK. More info [here](https://www.oracle.com/technetwork/java/embedded/javame/index.html)

## 2.2. Tools

Come along with Java are a lot of tools

*   IDE: [Eclipse](https://www.eclipse.org/), [Netbeans](https://netbeans.org/), [VSCode with extensions](https://code.visualstudio.com/docs/languages/java) (free), [Jetbrains's IntelliJ IDEA](https://www.jetbrains.com/idea/)
*   Servers (only for Java EE): [Wildfly](https://github.com/wildfly/wildfly) open source by Redhat, [GlassFish](https://github.com/eclipse-ee4j/glassfish) open source (part of eclipse-ee4j), [Apache Tomcat](https://github.com/apache/tomcat) open source.

## 2.3. Terms

*   JRE: Java Runtime Environment
*   JDK: Java Development Kits. JDK has multiple implementation because of a long and complicated relationships between big firms
*   JFX: or JavaFX. Things get strange from here. "OpenJFX is an open source, next generation client application platform for desktop, mobile and embedded systems built on Java" they said. But to be honest, I don't understand what is the difference between the "normal" java and the "next generation" java, since both are in active development.

# 3. Frameworks

In Microsoft world, .NET is the framework. If you want full-feature, compatible with old system, use .NET Framework (latest 4.8). If you want cross-platform (yes, including Linux), use .NET Core. And if you wait long enough, you can use [.NET 5](https://devblogs.microsoft.com/dotnet/introducing-net-5/), as they said "There will be just one .NET going forward, and you will be able to use it to target Windows, Linux, macOS, iOS, Android, tvOS, watchOS and WebAssembly and more."

Things are different in Java world. Java first created by Sun Microsystem, then bought by Oracle (then oracle sue Google for using some lines of code in Android). A lot of community driven frameworks has been developed for Java. There is no "one framework to fit all" like .NET. This bend the learning curve, make it difficult for a developer to jump from one framework to another.

For a beginner, the curve even worst. A lot of names and terms to familiar, and then you must choose a framework to "dive in". Reader beware, silly names are coming.

1.  Apache Struts: MVC pattern, open source.
2.  Spring Boot: MVC pattern, reliable, big community
3.  Grails: Built on top of Sprint Boot easy to learn, use, has excellent document with a lot of plugin

The problems are, each of these frameworks implement a slightly different conventions and introduce different concepts. Too much for "write one, run anywhere" ei?

Another problem: you will never know if a framework is about to abandon, so stick to a single framework seem risky (for me at least, since in .net, I know that specific version of .net framework will continue to be supported and easily upgraded to newer version with minimum effort)

That's all for introduction of Java. See you in next post.