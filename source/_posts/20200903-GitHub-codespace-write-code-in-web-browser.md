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

After coming home with Microsoft, more and more good and free things come to GitHub. This time, a long-awaited features are in beta, invitation-only, and it is `GitHub Codespaces`.

<!--more-->

<!-- TOC -->

- [1. Extremely short introduction](#1-extremely-short-introduction)
- [2. Using GitHub codespaces](#2-using-github-codespaces)
    - [2.1. Change theme](#21-change-theme)
    - [2.2. Settings](#22-settings)
    - [2.3. Install your programming language extensions](#23-install-your-programming-language-extensions)
    - [2.4. Work with multiple repository](#24-work-with-multiple-repository)
- [3. Some interesting things I found](#3-some-interesting-things-i-found)

<!-- /TOC -->

# 1. Extremely short introduction
<a id="markdown-extremely-short-introduction" name="extremely-short-introduction"></a>

Codespaces, in short, is a Linux virtual machine running `vscode` server and allows you to access it via any web browser.

Microsoft introduces its codespaces first in [Visual Studio Online](https://azure.microsoft.com/en-us/services/visual-studio-online/), using your Azure account to charge. "GitHub codespaces" is in the early access stage, so everything is free for now.

To request early access to GitHub codespaces, here is the link: https://github.com/features/codespaces

# 2. Using GitHub codespaces
<a id="markdown-using-github-codespaces" name="using-github-codespaces"></a>

When you're invited to use codespaces, your GitHub's repositories will have another option in open button

![open button](https://i.imgur.com/CB6VdCg.png)

## 2.1. Change theme
<a id="markdown-change-theme" name="change-theme"></a>

The default theme for VSCode is light. Light attracting bugs. So we need to change it to dark

The typical themes used by vscode is not working, so we need to use an extension developed by GitHub called `github theme`

![themes](https://i.imgur.com/osKi6Sl.png)

Sadly, the icon theme is fixed with 1 of the two default set.

## 2.2. Settings
<a id="markdown-settings" name="settings"></a>

Except for some settings related to themes and icons that have no effect, almost all other settings are the same. You can just copy and paste the settings from your local `vscode` to codespaces `vscode`

## 2.3. Install your programming language extensions
<a id="markdown-install-your-programming-language-extensions" name="install-your-programming-language-extensions"></a>

I think every programming language extension worked as it should be, but first, you will need to set up the development environment in Linux.

For example, to use Java, you will need to install JDK on Linux, then Java Extension Pack for a complete list of Java extensions in vscode.

C/C++ and Python extensions are pre-installed

When you open a project, based on the language, some language extension will be pre-installed

## 2.4. Work with multiple repository
<a id="markdown-work-with-multiple-repository" name="work-with-multiple-repository"></a>

By default, one codespace can only work with one repository. I will use the SSH key to have access to every repository on my Github.

1. Generate SSH key

```s
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

2. Add ssh key to ssh agent

```s
$ eval "$(ssh-agent -s)"
> Agent pid xxxxx
$ ssh-add ~/.ssh/id_rsa
```

3. Add the public key to GitHub

Add the key to settings at [SSH settings](https://github.com/settings/keys)

4. Change repo remote URL from HTTPS to SSH

```s
git remote set-url origin git@github.com:<Username>/<Project>.git
```

That's it

# 3. Some interesting things I found
<a id="markdown-some-interesting-things-i-found" name="some-interesting-things-i-found"></a>

* The codespaces running on Debian 9.13 - `lsb_release -a`
* 4GB of RAM - `free -m`
* Using 2 core of the Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz - `less /proc/cpuinfo` and `cat /proc/cpuinfo | grep processor | wc -l`

The vscode version is the latest Insider version, so expect some errors and unstable features