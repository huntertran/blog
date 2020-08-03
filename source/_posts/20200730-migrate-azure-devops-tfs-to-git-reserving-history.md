---
title: Migrate Azure DevOps TFS to Git reserving history
tags:
  - devops
  - git
  - TFS
id: '1259'
categories:
  - - Computer Tips
  - - Others
date: 2020-07-30 00:31:02
---

Microsoft acquired GitHub, and every one have unlimited private repository. This reason alone make me want to move all my project and source code to GitHub.

*   [1. A bit of history](#1-a-bit-of-history)
*   [2. Required tools](#2-required-tools)
*   [3. Migration steps](#3-migration-steps)
    *   [3.1. Clone the TFS project](#31-clone-the-tfs-project)
    *   [3.2. Add .gitignore](#32-add-gitignore)
    *   [3.3. Push code](#33-push-code)

# A bit of history

In around 2012, developers don't have much choices in _where_ to store their code for free. Sure you can use GitHub, but it limit the number of private repository and number of collaborators. The obvious choice at that time was `Visual Studio Online`, or today `Azure DevOps`. The only source control system it's provided is Team Foundation Server (TFS).

Today, 9.99 over 10 developers will choose `git` over `tfs`, and we need a way to migrate from TFS, _with history_, to git.

# Required tools

*   [git](https://git-scm.com/)
*   [git-tfs](https://github.com/git-tfs/git-tfs)

> Alternatively, you can install git-tf with Chocolatey:
> 
> `choco install gittfs`

# Migration steps

## Clone the TFS project

git-tfs clone https://your\_organization.visualstudio.com/ $/your\_project\_name

If your project name contain whitespace, just put the whole name in quote mark

git-tfs clone https://your\_organization.visualstudio.com/ "$/your project name"

This will clone the project to the folder you run the command

## Add .gitignore

Now the project is like any other git project, with a `.git` folder. You should add a `.gitignore` file to prevent commit unwanted files.

A sample `.gitinore` file here: [Visual Studio Git Ignore](https://www.toptal.com/developers/gitignore/api/visualstudio)

## Push code

The final step is to push code to your favorite git service.