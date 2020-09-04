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

After coming home with Microsoft, more and more good and free things come to GitHub. This time, a long awaited features are in beta, invitation only, and it is `GitHub Codespaces`

<!--more-->

<!-- TOC -->

- [Extremely short introduction](#extremely-short-introduction)
- [Using GitHub codespaces](#using-github-codespaces)
    - [Change theme](#change-theme)
    - [Settings](#settings)
    - [Install your programming language extensions](#install-your-programming-language-extensions)
    - [Work with multiple repository](#work-with-multiple-repository)
- [Some interesting things I found](#some-interesting-things-i-found)

<!-- /TOC -->

# Extremely short introduction

Codespaces, in short, is a linux virtual machine running `vscode` server, and allow you to access it via any web browser.

Microsoft introduce it codespaces first in [Visual Studio Online](https://azure.microsoft.com/en-us/services/visual-studio-online/), using your Azure account to charge. GitHub codespaces is in early access stage, so everything is free for now.

To request early access GitHub codespaces, here is the link: https://github.com/features/codespaces

# Using GitHub codespaces

When you're invited to use codespaces, your GitHub's repositories will have another options in open button

![open button](https://i.imgur.com/CB6VdCg.png)

## Change theme

The default theme for VSCode is light. Light attracting bugs. So we need to change it dark

The normal themes used by vscode is not worked, so we need to use an extension developed by GitHub called `github theme`

![themes](https://i.imgur.com/osKi6Sl.png)

Sadly, the icon theme is fixed with 1 of the 2 default set.

## Settings

Except some settings related to themes and icon that have no effect, almost all other settings are the same. You can just copy and past the settings from your local `vscode` to codespaces `vscode`

## Install your programming language extensions

I think every programming language extension worked as it should be, but first, you will need to setup the development environment in Linux.

For example, to use Java, you will need to install JDK on linux, then Java Extension Pack for a complete list of Java extensions in vscode.

C/C++ and Python extension are pre-installed

When you open a project, based on the language, some language extension will be pre-installed

## Work with multiple repository

By default, 1 codespaces can only work with 1 repository. I will use SSH key to have access to every repositories on my Github.

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

# Some interesting things I found

* The codespaces running on Debian 9.13 - `lsb_release -a`
* 4GB of RAM - `free -m`
* Using 2 core of the Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz - `less /proc/cpuinfo` and `cat /proc/cpuinfo | grep processor | wc -l`

The vscode version is the latest Insider version, so expect some errors and unstable features