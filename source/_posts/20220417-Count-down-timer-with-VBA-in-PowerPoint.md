---
title: Count down timer with VBA in PowerPoint
tags:
  - office
categories:
  - - Office
date: 2022-04-17 19:50:01
---


Learn how you can create a simple count-down timer for a PowerPoint presentation with Visual Basic for Application (VBA).

<!--more-->

| Disclaimer: VBA ended its life cycle a very loooooong time ago. The alternative is [`Office.js`](https://docs.microsoft.com/en-us/office/dev/add-ins/develop/understanding-the-javascript-api-for-office)

First, enable the `Developer` tab by right-clicking anywhere on the ribbons > Customize the Ribbon...

![customize the ribbon](https://i.imgur.com/aHg35kK.png)

Then tick the checkbox `Developer` > OK

![developer checkbox](https://i.imgur.com/dfBmCb7.png)

Now we need to add new Macros. Click the `Developer` tab on the ribbon, then click `Macros.`

![macro](https://i.imgur.com/fJXNbzC.png)

Enter an easy to remember name > Create

![macro name](https://i.imgur.com/gsKwll5.png)

In the above picture, there are two existing macros

A new window appears, allowing you to start writing the macro's code.

Enter the following code, then click save

```vb
Sub TwoMinCountDown()
    Dim time As Date
    time = Now()
    
    Dim count As Integer
    count = 120 '120 seconds ~ 2 minutes
    
    time = DateAdd("s", count, time)
    
    Do Until time < Now()
        DoEvents
        ActivePresentation.SlideShowWindow.View.Slide.Shapes("TwoMinCountDown").TextFrame.TextRange = Format((time - Now()), "hh:mm:ss")
    Loop
End Sub

Sub TenMinCountDown()
    Dim time As Date
    time = Now()
    
    Dim count As Integer
    count = 600 '600 seconds ~ 10 minutes
    
    time = DateAdd("s", count, time)
    
    Do Until time < Now()
        DoEvents
        ActivePresentation.SlideShowWindow.View.Slide.Shapes("TenMinCountDown").TextFrame.TextRange = Format((time - Now()), "hh:mm:ss")
    Loop
End Sub
```

Now a few things to notice here. In this line:

```vb
ActivePresentation.SlideShowWindow.View.Slide.Shapes("TenMinCountDown").TextFrame.TextRange = Format((time - Now()), "hh:mm:ss")
```

The text `TenMinCountDown` is the name of the shape that this macro affects.

Now to apply this macro, head back to your slide.

On the `Home` tab, near the end of the ribbon, click `Select` > `Selection Pane`

![selection pane](https://i.imgur.com/7XzG7to.png)

Now draw a simple textbox, or a shape you want, then double click its name in `Selection Pane.` Change its name to the name of the shape in the macro's code.

![draw shape](https://i.imgur.com/kVWd4Rk.png)

 When you click on the shape, the timer will count down, and clicking it again will reset it.

 That's it.