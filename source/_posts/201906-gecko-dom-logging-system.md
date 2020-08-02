---
title: '[Research] - Gecko Dom Logging system'
tags:
  - DOM API
  - firefox
  - Log
id: '1166'
categories:
  - - C++
date: 2019-06-14 00:12:17
---

The purpose of this documentation is to record all the findings and my progress while exploring Firefox source code, in order to log how many time a DOM API is called when visit a single website, or multiple common website.

This require a deep modification in Firefox's implementation of DOM API.
<!-- more -->
*   [1\. Setup and initialization](#1-setup-and-initialization)
*   [2\. Source code structure](#2-source-code-structure)
    *   [2.1. Built-in extensions](#21-built-in-extensions)
    *   [2.2. JavaScript Engine (SpiderMonkey)](#22-javascript-engine-spidermonkey)
*   [3\. Understanding DOM](#3-understanding-dom)
    *   [3.1. DOM Levels](#31-dom-levels)
        *   [3.1.1. DOM Level 1](#311-dom-level-1)
        *   [3.1.2. DOM Level 2](#312-dom-level-2)
        *   [3.1.3. DOM Level 3](#313-dom-level-3)
    *   [3.2. Shadow DOM and Virtual DOM](#32-shadow-dom-and-virtual-dom)
        *   [3.2.1. Shadow DOM](#321-shadow-dom)
        *   [3.2.2. Virtual DOM](#322-virtual-dom)
*   [4\. Modifying Firefox's DOM method implementation](#4-modifying-firefoxs-dom-method-implementation)
    *   [4.1. Logging Framework](#41-logging-framework)
    *   [4.2. Analyze](#42-analyze)
*   [5\. Development](#5-development)
    *   [5.1. Design solution](#51-design-solution)
    *   [5.2. Firefox integration](#52-firefox-integration)

# 1\. Setup and Initialization

In short, to get the latest version of Firefox source code, one could follow the official instruction on [Building Firefox for Windows](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Build_Instructions/Windows_Prerequisites)

> One small modification in which will decrease the time needed to build the source code: You will not need the "Game development with C++" while installing/modifying Visual Studio 2019

# 2\. Source code structure

Mozilla use Gecko to render web content.

> More than that, Gecko is also used to render the firefox user interface.
> 
> On Windows, Gecko use Microsoft COM, on other platforms, Gecko use XPCOM to render user interface.

The whole source code is mentioned as Gecko, and mirrored in [Mozilla's Github Repository](https://github.com/mozilla/gecko-dev)

## 2.1. Built-in extensions

Firefox contains 2 built-in extension: PDF.js and Shumway.

*   [PDF.js](https://github.com/mozilla/pdf.js): To open and read PDF files inside firefox, without opening another software
*   [Shumway](https://github.com/mozilla/shumway): provide a way to render swf (Shock Wave Flash) file, which is quite popular in older websites to display animations, game, effects. These files has been replaced with HTML5, and considered as a security vulnerable in modern websites.

## 2.2. JavaScript Engine (SpiderMonkey)

Located in `js\src`, the Firefox's JavaScript Engine is called SpiderMonkey, and is in active development at [mozilla-central/file/tip/js/src](https://hg.mozilla.org/mozilla-central/file/tip/js/src)

> Beside the interpreter, SpiderMonkey contains a compiler , a garbage collector and a Just-in-time compiler.

# 3\. Understanding DOM

DOM stands for Document Object Model. To understand what DOM is, first we need to understand the basic of a website

Websites are a combination of HTML, CSS and Javascript. HTML is a structured documents, and can be mapped by using a tree structure, starting with `html` tag as root.

> The DOM represents a document with a logical tree. Each branch of the tree ends in a node, and each node contains objects. DOM methods allow programmatic access to the tree; with them you can change the document's structure, style, or content. Nodes can also have event handlers attached to them; once an event is triggered, the event handlers get executed.
> 
> [Document Object Model - Mozilla Developer Docs](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

## 3.1. DOM Levels

Document Object Model API is implemented in level. The lower the level, the more basic and simple functions it defined. Currently there are 3 levels, which are mostly implemented by all modern browsers (Partly implemented for Level 3)

### 3.1.1. DOM Level 1

Provide interface to represent any structured document, as well as accessing and manipulating nodes.

In level 1, DOM also define extended interfaces that counted as part of the specification, but not necessary for a HTML-only implementation of DOM specification.

> The `getElementsByTagName` method is defined in level DOM 1 specification.

### 3.1.2. DOM Level 2

Provide 6 separated specifications:

*   Core: Extend the functionalities of Level 1.
*   Views: Allows programs and scripts to dynamically access and update the content of a representation of a document.
*   Events: Define basic of event system, including the concept of event flow, listening, bubbling, cancellation.
*   Styles: Access and update stylesheet.
*   Traversal and Range: Allow programs and scripts to dynamically walk-through and identify a range of contents in a document, as well as creation, insertion, modification and deletion of a range of contents.
*   HTML: Extend the interfaces defined in Level 1, using the Core level 2 possibilities.

Most of the famous JavaScripts functions are defined in level 2

*   `getElementById` in **Core**
*   `addEventListener` and `handleEvent` in **Events**
*   `getComputedStyle` in **Styles**
*   `NodeIterator` and `TreeWalker` in **Traversal and Range**
*   `contentDocument` property in **HTML**

### 3.1.3. DOM Level 3

Unlike level 1 and 2, only a few methods and properties in DOM level 3 are supported. Level 3 provide advanced functionalities to manipulate DOM and XML. Firefox divide DOM Level 3 in 5 separated part, with different level of support

*   Core: Only a few methods and properties are supported.
*   Load and Save: dynamically load XML documents into DOM or serialize DOM to XML docs. None supported
*   Validation: Update content and ensure validity. Firefox not support this interface
*   Events: Keyboard events and how to handle them. Partly supported.
*   XPath: Simple functionalities to access DOM tree using XPath.

## 3.2. Shadow DOM and Virtual DOM

### 3.2.1. Shadow DOM

Shadow DOM is an complete dom tree hidden inside an dom node. All the markups, structures, styles or behaviors are separated from actual/normal dom. The reason for this concept is to develop low level web components that will have default user interface/behaviors across websites (e.g `<video></video>` tag with default control buttons provided by browsers)

### 3.2.2. Virtual DOM

In short, Virtual DOM is an abstraction of DOM. It represent for a small subset of DOM, and update the actual DOM accordingly. Virtual DOM is implemented not by browsers, but by high level javascript libraries (eg React, asm-dom, etc)

Virtual DOM libraries compare changed nodes with actual node in DOM tree. If there are differences, it will update the actual DOM. By optimizing the comparison algorithm, it can perform extremely fast since it does not need to search the whole DOM tree for nodes and properties.

# 4\. Modifying Firefox's DOM method implementation

## 4.1. Logging Framework

Firefox provide a "simple" logging service, located at `dom\accessible\Logging.h` (header file). This is recommended way to log anything to Firefox's browser console.

To use it, you need to do the following:

#include "mozilla/Logging.h"
static mozilla::LazyLogModule sFooLog("foo");

LazyLogModule will be initialized safely, even if the current class is already initialize an instance of LazyLogModule.

Later, using these method appropriately to log:

from https://developer.mozilla.org/en-US/docs/Mozilla/Developer\_guide/Gecko\_Logging

Name

Description

MOZ\_LOG(module, level, message)

Outputs the given message if the module has the given log level enabled.  
\+ module - The log module to use.  
\+ level - The log level of the message.  
\+ message - A printf-style message to output. Must be enclosed in parentheses.

MOZ\_LOG\_TEST(module, level)

Checks if the module has the given level enabled.  
\+ module - The log module to use.  
\+ level - The output level of the message.

## 4.2. Analyze

The requirement for my project is simple: To know how many time a dom method is called (for a specific website, and average for a set of common website)

In fact, I cannot use Firefox own logging framework, because of these problems:

1.  Gecko source code is full of old logs and developer notes.
2.  Each log must provide a log level, which is not applicable for my project.
3.  Cannot count the logged text without writing another piece of tool.

Example of old logs and developer notes from `mozilla-central\dom\base\nsINode.cpp`, [line 2585 to line 2609](https://dxr.mozilla.org/mozilla-central/rev/4a63f0a3a1f26e2a377ffbd477ba050e16577445/dom/base/nsINode.cpp#2585)

Element\* nsINode::GetElementById(const nsAString& aId) {
  MOZ\_ASSERT(!IsShadowRoot(), "Should use the faster version");
  MOZ\_ASSERT(IsElement() || IsDocumentFragment(),
             "Bogus this object for GetElementById call");
  if (IsInUncomposedDoc()) {
    MOZ\_ASSERT(IsElement(), "Huh? A fragment in a document?");
    return FindMatchingElementWithId(aId, \*AsElement(), \*OwnerDoc());
  }

  if (ShadowRoot\* containingShadow = AsContent()->GetContainingShadow()) {
    MOZ\_ASSERT(IsElement(), "Huh? A fragment in a ShadowRoot?");
    return FindMatchingElementWithId(aId, \*AsElement(), \*containingShadow);
  }

  for (nsIContent\* kid = GetFirstChild(); kid; kid = kid->GetNextNode(this)) {
    if (!kid->IsElement()) {
      continue;
    }
    nsAtom\* id = kid->AsElement()->GetID();
    if (id && id->Equals(aId)) {
      return kid->AsElement();
    }
  }
  return nullptr;
}

# 5\. Development

## 5.1. Design solution

My solution is simple. Log into an array, then count for each time a function name is repeated.

First, I created a class to hold each record

class DomLogNode
{
public:
    DomLogNode();

    void setNode(string name, int count);
    int increaseCount();
    bool compareName(string nameToCompare);
    int getCount();
    string getName();

private:
    string functionName;
    int count;
};

Then, I created another class to hold the list of record. This class is static

static class DomLog
{
public:
    void recordLog(string functionName);
    void pushNewName(string functionName, int initialCount = 1);
    void getDomLogs();
    void exportFile(string path);

private:
    vector<DomLogNode> domLogs;
} domLog;

Method `exportFile(string path)` write the list to a csv file, using simple c++ file library.

**Get the caller method name**  
In cpp, to get the current method name, we can use the static variable `__func__` as stated here: https://docs.microsoft.com/en-us/cpp/cpp/func

> You can get the whole source code at my Github [repository](https://github.com/huntertran/gecko-dom-log.git)

## 5.2. Firefox integration

Unfortunately, the Firefox source code system (using mercurial source control) is buggy lately. It close the connection way before the clone process finished.

Firefox implement DOM API all over the source code. For example, the API `getElementById` is implemented in 3 different places:

*   `dom\base\AnonymousContent.h` with corresponding implementation
*   `dom\base\DocumentOrShadowRoot.h` with corresponding implementation
*   `dom\base\nsINode.h` with corresponding implementation

The method inside `nsdINode` have a comment

// Document and ShadowRoot override this with its own (faster) version.
// This should really only be called for elements and document fragments.

This mean, to correctly record how many time the GetElementById is called, we have to modify the code of all 3 methods.

domLog.recordLog(\_\_func\_\_);

This quickly getting out of hand, since there are hundreds of DOM API we need to log, and I am still looking for another solution.