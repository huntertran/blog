---
title: GitHub codespaces - write code in web browser
date: 2020-09-03 16:02:21
tags:
    - github
    - vscode
categories:
    - - Computer Tips
    - - Others
---

After comming home with Microsoft, more and more good and free things come to GitHub. This time, a long awaited features are in beta, invitation only, and it is `GitHub Codespaces`

<!--more-->

<!-- TOC -->

- [1. Extremely short introduction](#1-extremely-short-introduction)
- [2. Using GitHub codespaces](#2-using-github-codespaces)
- [3. Some interesting things I found](#3-some-interesting-things-i-found)

<!-- /TOC -->

# 1. Extremely short introduction
<a id="markdown-extremely-short-introduction" name="extremely-short-introduction"></a>

Codespaces, in short, is a linux virtual machine running `vscode` server, and allow you to access it via any web browser.

Microsoft introduce it codespaces first in [Visual Studio Online](https://azure.microsoft.com/en-us/services/visual-studio-online/), using your Azure account to charge. GitHub codespaces is in early access stage, so everything is free for now.

To request early access GitHub codespaces, here is the link: https://github.com/features/codespaces

# 2. Using GitHub codespaces
<a id="markdown-using-github-codespaces" name="using-github-codespaces"></a>

When you're invited to use codespaces, your github's repositories will have another options in open button

![open button](https://i.imgur.com/CB6VdCg.png)

**Change theme**

The default theme for VSCode is light. Light attracting bugs. So we need to change it dark

The normal themes used by vscode is not worked, so we need to use an extension developed by GitHub called `github theme`

![themes](https://i.imgur.com/osKi6Sl.png)

Sadly, the icon theme is fixed with 1 of the 2 default set.

**Settings**

Except some settings related to themes and icon that have no effect, almost all other settings are the same. You can just copy and past the settings from your local `vscode` to codespaces `vscode`

**Install your programming language extensions**

I think every programming language extension worked as it should be, but first, you will need to setup the development environment in Linux.

For example, to use Java, you will need to install JDK on linux, then Java Extension Pack for a complete list of Java extensions in vscode.

C/C++ and Python extension are pre-installed

# 3. Some interesting things I found
<a id="markdown-some-interesting-things-i-found" name="some-interesting-things-i-found"></a>

* The codespaces running on Debian 9.13 - `lsb_release -a`
* 4GB of RAM - `free -m`
* Using 2 core of the Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz - `less /proc/cpuinfo` and `cat /proc/cpuinfo | grep processor | wc -l`

The vscode version is the latest Insider version, so expect some errors and unstable features