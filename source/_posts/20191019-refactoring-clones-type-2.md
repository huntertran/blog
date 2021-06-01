---
title: '[java] Refactoring Clones type 2'
tags:
  - clone
  - refactor
id: '1232'
categories:
  - - CSharp
  - - Java
date: 2019-10-19 16:10:18
---

Removing clones in code maybe is the most challenging type of refactoring action. In this post, I will show you how to refactor a clone type 2 using Functional Interface in Java and delegate in C#

<!-- more -->

# Type of clones

There are 4 types of clones:

> _**Type 1:**_ The codes cloned are identical, except the name of variables, add or remove of comment.
> 
> _**Type 2:**_ code fragments are structurally and syntactically identical except for variations in identifiers, literals, types, in addition to Type I differences.
> 
> _**Type 3:**_ code fragments are copies with further modifications. Statements can be changed, added, or removed in addition to Type II differences.
> 
> _**Type 4:**_ two or more code fragments perform the exact computation but are implemented through different syntactic variants.
> 
> S. Bellon, R. Koschke, G. Antoniol, J. Krinke and E. Merlo, Comparison and Evaluation of Clone DetectionTools, Transactions on Software Engineering, 33(9):577-591 (2007)

# Removing clones

Type 1: just remove the second fragment of code and use the first one

Type 3: Based on the function of the code fragment (usually clone codes are in methods), you can perform other refactors like break the method into smaller ones (`extract method`), then consider if you can transform type 3 clone into type 2.

Type 4: This one is the most difficult to detect. To eliminate it is easy, just use one of them.

I believe to detect this kind of clone, you can inspect the before and after the condition of the questioned methods. If they are the same (use the same set of parameters, return the same result, verified by unit tests), then the function of these methods is identical.

For type 2 clone, we will try to transform it to type 1, then introduce the parameter in a new common method by using a language-specific feature called `FunctionalInterface` in Java and `delegate` in C#

# Examples

Consider these lines of code:

public void drawVerticalLine(int length, View currentView){
    DrawOptions drawOptions = currentView.getVerticalOptions();
    currentView.draw(length, drawOptions);
}

public void drawHorizontalLine(int length, View currentView){
    DrawOptions drawOptions = currentView.getHorizontalOptions();
    currentView.draw(length, drawOptions);
}

In the 2 methods above, both draw a line to screen; the difference is the `drawOptions` variable.

To introduce parameters to "transform" this type of clone to type 1, we can do as follow:

/\* For JAVA \*/

public void drawVerticalLine(int length, View currentView){
    drawLine(length, currentView, () -> currentView.getVerticalOption());
}

public void drawHorizontalLine(int length, View currentView){
    drawLine(length, currentView, () -> currentView.getHorizontalOption());
}

@FunctionalInterface
private interface DrawOption {
    int getDrawOption();
}

public void drawLine(int length, View currentView, DrawOption drawOption){
    int options = drawOption.getDrawOption();
    currentView.draw(length, options)
}

and for C#

public void drawVerticalLine(int length, View currentView){
    drawLine(length, currentView, () => currentView.getVerticalOption());
}

public void drawHorizontalLine(int length, View currentView){
    drawLine(length, currentView, () => currentView.getHorizontalOption());
}

public void drawLine(int length, View currentView, Func<int> drawOption){
    int option = drawOption();
    currentView.draw(length, option);
}

## Using a tool

If you are using Eclipse, [JDeodorant](https://github.com/tsantalis/JDeodorant) plug-in by [Associate Professor Nikos Tsantalis](https://users.encs.concordia.ca/~nikolaos/) can automatically `extract` the clone into common method for you.

1.  Identify the cloned methods
2.  Select the method in Eclipse, right-click and choose `Refactor duplicate code...`

![](https://i.imgur.com/ndLJ8Iz.png)