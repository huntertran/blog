Blog
---

My blog built with `hexo` and next theme

# Setting up

Install NPM

```s
npm install -g npm
```

Install Hexo CLI

```s
npm install hexo-cli -g
```

Install packages

```s
npm i
```

# commonly uses command

```s
# run local
hexo serve

# new post
hexo new post

# run the local server
hexo serve
```

# Create a symbolic link to support resources folders

For example, when writing new post, you can refer the the symbolic `images` folder

```s
New-Item -ItemType SymbolicLink -Path "images" -Target "source/images"
```
