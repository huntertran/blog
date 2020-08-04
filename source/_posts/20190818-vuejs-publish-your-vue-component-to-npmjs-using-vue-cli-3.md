---
title: '[vuejs] - Publish your vue component to npmjs using vue-cli 3'
tags:
  - component
  - vue
  - vue-cli
  - vuejs
id: '1220'
categories:
  - - c
    - ASP.NET
  - - JavaScript and TypeScript
  - - VSCode
date: 2019-08-18 14:54:08
---

Using Vuejs, sometime you need to publish your awesome `component` with the world. Sure you can share the `.vue` file, but how can you publish it to `npmjs`, for the ease of installation and usage of others?
<!-- more -->
With the release of Vue CLI 3, build target `-lib` is supported, but no tutorials available "out there", so here is one (and hopfully not the last).

<!-- TOC -->

- [1. Requirements](#1-requirements)
- [2. Steps](#2-steps)
    - [2.1. Setup your project](#21-setup-your-project)
    - [2.2. Add config for vue.js](#22-add-config-for-vuejs)
    - [2.3. Edit package.json](#23-edit-packagejson)
- [3. Build, Test and Publish](#3-build-test-and-publish)
    - [3.1. Build](#31-build)
    - [3.2. Test](#32-test)
    - [3.3. Publish](#33-publish)
- [4. Test the published package](#4-test-the-published-package)

<!-- /TOC -->

# 1. Requirements
<a id="markdown-requirements" name="requirements"></a>

*   Of course you will need an `npmjs` account. Go register one.
*   vue-cli 3 (as the time this tutorial was written), install it globally using

npm install -g @vue/cli

*   vue cli-service-global add-on for quick project prototype, install it globally using

npm install -g @vue/cli-service-global

*   Your component source code
*   A text editor of your choice (VSCode is my personal suggestion)

# 2. Steps
<a id="markdown-steps" name="steps"></a>

## 2.1. Setup your project
<a id="markdown-setup-your-project" name="setup-your-project"></a>

For instruction purpose, just a simple hello world project will do.

1.  Create a new folder, let call it `my_component`
2.  Open that folder using vscode, press Ctrl + Shift + \` to open a new terminal inside root folder
3.  Create your project, and choose your preferred options.

vue create .

> if you want to create a new project including root folder, type `vue create your-folder-name`

your project structure should basically look like this if you choose all default

![project structure](https://i.imgur.com/tpVcVBM.png)

type `npm run serve` will build the project and serve it using a local server

![hello world](https://i.imgur.com/KHn5jsf.png)

## 2.2. Add config for vue.js
<a id="markdown-add-config-for-vue.js" name="add-config-for-vue.js"></a>

Add a new file to root folder with the name `vue.config.js`. In this file, you will be able to setup the build to include all your components `*.css` in a separated file or inside the component `.js` file. Each option have it pro and cons.

For simplicity, I choose to include inside the `.js` file.

module.exports = {
    css: { extract: false }
}

## 2.3. Edit `package.json`
<a id="markdown-edit-package.json" name="edit-package.json"></a>

**Add build command**  
Open `package.json` and add the following line under `scripts` section

"build:helloworld": "vue-cli-service build --target lib --name my\_component ./src/components/HelloWorld.vue",

It will look like this

![package json](https://i.imgur.com/KXP6ymW.png)

**Pointing to output**

Add the target for npm to `package.json`

"main": "./dist/my\_component.udm.js",

**Add file attribute**

This settings indicate which file types should be uploaded to `npmjs`

"files": \[
  "dist/\*.js"
  "dist/\*.css"
\],

**Other information for `npmjs`**

"description": "A hello world vuejs components",
"author": "Hunter Tran",
"license": "MIT",

> If your component use other components or packages, you need to specify them in `dependencies`, [here](https://docs.npmjs.com/creating-a-package-json-file) is more info on npmjs.com

# 3. Build, Test and Publish
<a id="markdown-build%2C-test-and-publish" name="build%2C-test-and-publish"></a>

## 3.1. Build
<a id="markdown-build" name="build"></a>

Build your project using the new command

npm run build:helloworld

## 3.2. Test
<a id="markdown-test" name="test"></a>

  
The build command above will create a `dist` folder, including a `demo.html` site. Open that file using a browser to test your newly created component.

> You may need to modify that file a bit if your components is not _ready to use_ and require some setup (like require data to run)

## 3.3. Publish
<a id="markdown-publish" name="publish"></a>

Simple enough, just type

npm publish

and follow the instruction.

# 4. Test the published package
<a id="markdown-test-the-published-package" name="test-the-published-package"></a>

Finally, you can try your newly published package in a new "Hello World" vue cli project, or use the built `yourpackagename.common.js` file directly in your `<head></head>` section.