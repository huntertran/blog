---
title: Wordpress - Install Wordpress to Docker containers from Windows
tags:
  - apache
  - container
  - docker
  - php
  - ubuntu
  - wordpress
id: '887'
categories:
  - - Others
date: 2017-08-02 00:18:56
---

In this tutorial, I will guide your through on how to install wordpress on a container of docker. The same step can be use to install wordpress on an acture Ubuntu machine, with some small changes
<!-- more -->

<!-- TOC -->

- [1. Install Apache](#1-install-apache)
- [2. Install MySQL](#2-install-mysql)
    - [2.1. Install mysql-server](#21-install-mysql-server)
- [3. Install PHP](#3-install-php)
- [4. Setup Wordpress](#4-setup-wordpress)
    - [4.1. Create MySQL database and user](#41-create-mysql-database-and-user)
    - [4.2. Install wordpress](#42-install-wordpress)
    - [4.3. Config](#43-config)

<!-- /TOC -->

# 1. Install Apache
<a id="markdown-install-apache" name="install-apache"></a>

Login to Docker container with SuperPutty / Putty

```s
apt-get update
apt-get install apache2
```

(type y to confirm installation)

```s
apache2ctl configtest
```

If output is

```s
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message Syntax OK
```

Meaning: apache cannot get the reliably server domain name

_**IT JUST A WARNING**_

To fix: edit `apache2.conf`

> Recommended: Map network drive to easily config or copy file to container [Download](https://github.com/dokan-dev/dokany/releases) 
> + install Dolkan [Download](https://github.com/Foreveryone-cz/win-sshfs/releases)
> + install win-sshfs follow the step to map
> ![mapping instruction](http://farm5.staticflickr.com/4344/36326087365_4a8b8a7418_o.png)

open `/etc/apache2/apache2.conf` in your favorite editor

add this line at the end of the file

```s
ServerName localhost
```

type `apache2ctl configtest` again to see warning is disappeared

# 2. Install MySQL
<a id="markdown-install-mysql" name="install-mysql"></a>

## 2.1. Install mysql-server
<a id="markdown-install-mysql-server" name="install-mysql-server"></a>

```s
apt-get install mysql-server
```

In the installation process, type password for root user

# 3. Install PHP
<a id="markdown-install-php" name="install-php"></a>

```s
apt-get install php libapache2-mod-php php-mcrypt php-mysql
```

Config apache priority for index.php instead of index.html

Because dir.conf presented as folder, so we have to edit with linux nano

```s
nano /etc/apache2/mods-enabled/dir.conf
```

It should look like this

![dir.conf](http://farm5.staticflickr.com/4403/36326087315_f9a2a593a3_o.png)

Type `Ctrl + X` to exit nano, type y to save

Restart Apache2 server

```s
service apache2 restart
```

To test PHP server (REMOVE the file after test because it will show your server info)

Create new file `info.php` in `/var/www/html/`

Insert some PHP code

```php
<?php phpinfo(); ?>
```

Then you can access [http://your\_domain\_name/info](http://your_domain_name/info)

![phpinfo](http://farm5.staticflickr.com/4426/36326087275_5e74efdb8a_o.png)

# 4. Setup Wordpress
<a id="markdown-setup-wordpress" name="setup-wordpress"></a>

## 4.1. Create MySQL database and user
<a id="markdown-create-mysql-database-and-user" name="create-mysql-database-and-user"></a>

Start MySQL server

```s
/etc/init.d/mysql start
```

Login into mysql

```s
mysql -u root -p
```

Enter your password

Your console windows will now start with `mysql&gt;`

Type in to create database for wordpress (database name can be customize)

```sql
CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
```

SQL query must end with semicolon(;)

Create a separate account to manage wordpress database

```sql
GRANT ALL ON wordpress.* TO 'admin'@'localhost' IDENTIFIED BY 'admin';
```

Flush the current Privileges, so MySQL will know about the recent changes

```sql
FLUSH PRIVILEGES;
```

Exit MySQL

```sql
EXIT;
```

Adjust Apache configuration to allow for `.htaccess` override and rewrites

Open apache configuration file to edit

```s
/etc/apache2/apache2.conf
```

You can use Ubuntu nano editor, or if you’ve mapped the network drive before (step 4), open the file like any other file on windows

Nano

```s
nano /etc/apache2/apache2.conf
```

Network Drive

![network drive edit file](http://farm5.staticflickr.com/4323/36326087335_f70a215f0f_o.png)

Search for this part and change

```xml
. . .
 
<Directory /var/www/html/>
    AllowOverride All
</Directory>
 
. . .
```

Save and close the file

Enable rewrite module

```s
a2enmod rewrite
```

Enable changes

```s
apache2ctl configtest
```

Restart apache2 service

```s
service apache2 restart
```

## 4.2. Install wordpress
<a id="markdown-install-wordpress" name="install-wordpress"></a>

Download wordpress at: [https://wordpress.org/](https://wordpress.org/)

Extract to a folder

Copy the content of folder “wordpress” to folder “/var/www/html” on container

Permission and .htaccess Show hidden files and folder on WinSCP

```s
Open WinSCP > Option > References…
```

![show hidden file](http://farm5.staticflickr.com/4300/36326087085_a8c29ef11e_o.png)

Create `.htaccess` file

Right click on an empty space > New File > enter `.htaccess`

![create .htaccess](http://farm5.staticflickr.com/4441/36326087035_022f35bffa_o.png)

Set Read / Write permission for .htaccess

Right click on .htaccess > Properties

![permissions for .htaccess](http://farm5.staticflickr.com/4325/35517228003_73383a8bcc_o.png)

Set permission recursively for all 3 folders

![permissions for all 3 folders](http://farm5.staticflickr.com/4409/35490057164_0d1ff22807_o.png)

## 4.3. Config
<a id="markdown-config" name="config"></a>

Open `wp-config.php` and fill in these info

```php
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');
 
/** MySQL database username */
define('DB_USER', 'admin');
 
/** MySQL database password */
define('DB_PASSWORD', 'admin');
 
/** MySQL hostname */
define('DB_HOST', 'localhost');
 
/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');
 
/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');
```

Open link and copy the code show up then replace them

![salt](http://farm5.staticflickr.com/4388/36326086765_8627dd85cc_o.png)

Add this line (to enable wordpress can modify files and folder directly

```php
define('FS_METHOD', 'direct');
```

It’s done, open your `domain:port` to config wordpress using web interface