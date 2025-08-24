---
title: Java for Beginner - 2 - Hello World in Java
tags:
  - hello world
  - java for beginner
id: '1205'
categories:
  - - Java
date: 2019-07-12 12:40:13
---

After getting yourself familiar with names and terms in Java in [part 1](https://huntertran.ca/2019/07/11/java-for-beginner-1-introduction-to-java-from-a-net-guy/), now it's time for you to create your first program in Java.

<!-- more -->

*   [1. Setup](#1-setup)
    *   [1.1. Required Tools](#11-required-tools)
    *   [1.2. Set environment variables](#12-set-environment-variables)
*   [2. Start coding](#2-start-coding)
    *   [2.1. Hello World in Java](#21-hello-world-in-java)
    *   [2.2. Run and Debug](#22-run-and-debug)
*   [3. Java Build Tools](#3-java-build-tools)

# 1. Setup

For a beginner, tools and supports from those tools is quite vital. Someone will said that you should _learn_ new language by using a basic text editor like Notepad. In my opinion, don't do it. Use a IDE, or at least VSCode with supporting extensions, and re-type any code that you read, don't copy and paste them.

## 1.1. Required Tools

1.  [Visual Studio Code](https://code.visualstudio.com/) - Cross platform, fast and beautiful (especially dark theme is an ease for your eye).
2.  [Java Extension Pack (GitHub)](https://github.com/Microsoft/vscode-java-pack) - [install](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack&ssr=false) - a set of extensions for VSCode to work with Java
3.  [Prebuilt OpenJDK by Adopt OpenJDK (free)](https://adoptopenjdk.net/) - including JVM. This project is community backed with short and easy explanation, perfect for beginner.
4.  Some other tools that will be install on-the-fly

## 1.2. Set environment variables

Set `JAVA_HOME` to the folder you have install JDK

Start > type `advanced system settings` > Environment Variables…

![advanced system settings](https://i.imgur.com/WokUE7n.png)

Then add a new System Variable

JAVA\_HOME

C:\\Program Files\\Java\\jdk1.8.0\_161

# 2. Start coding

## 2.1. Hello World in Java

Unlike .NET, JAVA required a specific folder structure. Each .java file should contain only 1 class, and that class must declare `package` with the name of the folder.

Open VSCode and create the following folder structure

```
<your_project_name>
|-src
| |-main
| | |-java
| | | |-hello
```

Inside hello folder, create `Application.java`, then type the following code

```java
package main.hello;

public class Application {

    public static void main(String args) {
        String hello = "Hello World!";
        System.out.print(hello);
    }
}
```

## 2.2. Run and Debug

Create configuration file (VSCode will automatically do this)

![config](https://i.imgur.com/r1j33Ht.png)

`.vscode` folder added to folder structure, with `launch.json` file created, the content should look like this

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Debug (Launch) - Current File",
            "request": "launch",
            "mainClass": "${file}"
        },
        {
            "type": "java",
            "name": "Debug (Launch)-Application",
            "request": "launch",
            "mainClass": "main.hello.Application"
        }
    ]
}
```

Press F5 (or that green arrow button), and the word `Hello World!` will be printed on debug console

![hello world](https://i.imgur.com/lopZQwM.png)

To debug, put a break point in line 7

![break point](https://i.imgur.com/fSl61GO.png)

Then press F5 again

![debug](https://i.imgur.com/hJHvv44.png)

# 3. Java Build Tools

To build a java file, you need a build tool. In the tutorial above, VSCode has already done that for you. The most widely used build tool for Java right now is Gradle and Maven. Both can be use in VSCode terminal window and integrated in VSCode task (in fact, what doesn't?)

*   [Gradle](https://gradle.org/) - fast, chosen by Google to use as default build tool for Android.
*   [Maven](https://maven.apache.org/) - easier to understand and use.

> VSCode Java Extension Pack support Maven naturally. But maybe you still need to install maven manually.

That's it. See you next time.
