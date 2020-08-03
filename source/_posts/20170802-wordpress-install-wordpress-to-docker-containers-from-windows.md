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
**Contents**

*   [1\. Install Apache](#1-install-apache)
*   [2\. Install MySQL](#2-install-mysql)
    *   [2.1. Install mysql-server](#21-install-mysql-server)
*   [3\. Install PHP](#3-install-php)
*   [4\. Setup Wordpress](#4-setup-wordpress)
    *   [4.1. Create MySQL database and user](#41-create-mysql-database-and-user)
    *   [4.2. Install wordpress](#42-install-wordpress)
    *   [4.3. Config](#43-config)

# 1\. Install Apache

Login to Docker container with SuperPutty / Putty \[code lang=text\] apt-get update \[/code\] \[code lang=text\] apt-get install apache2 \[/code\] (type y to confirm installation) \[code lang=text\] apache2ctl configtest \[/code\] If output is \[code lang=text\] AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message Syntax OK \[/code\] Meaning: apache cannot get the reliably server domain name

IT JUST A WARNING

To fix: edit `apache2.conf`

> Recommended: Map network drive to easily config or copy file to container [Download](https://github.com/dokan-dev/dokany/releases) + install Dolkan [Download](https://github.com/Foreveryone-cz/win-sshfs/releases) + install win-sshfs follow the step to map ![mapping instruction](http://farm5.staticflickr.com/4344/36326087365_4a8b8a7418_o.png)

open `/etc/apache2/apache2.conf` in your favorite editor add this line at the end of the file \[code lang=text\] ServerName localhost \[/code\] type `apache2ctl configtest` again to see warning is disappeared

# 2\. Install MySQL

## 2.1. Install mysql-server

\[code lang=text\] apt-get install mysql-server \[/code\] In the installation process, type password for root user

# 3\. Install PHP

\[code lang=text\] apt-get install php libapache2-mod-php php-mcrypt php-mysql \[/code\] Config apache priority for index.php instead of index.html Because dir.conf presented as folder, so we have to edit with linux nano \[code lang=text\] nano /etc/apache2/mods-enabled/dir.conf \[/code\] It should look like this ![dir.conf](http://farm5.staticflickr.com/4403/36326087315_f9a2a593a3_o.png) Type `Ctrl + X` to exit nano, type y to save Restart Apache2 server \[code lang=text\] service apache2 restart \[/code\] To test PHP server (REMOVE the file after test because it will show your server info) Create new file `info.php` in `/var/www/html/` Insert some PHP code \[code lang=php\] <?php phpinfo(); ?> \[/code\] Then you can access [http://your\_domain\_name/info](http://your_domain_name/info) ![phpinfo](http://farm5.staticflickr.com/4426/36326087275_5e74efdb8a_o.png)

# 4\. Setup Wordpress

## 4.1. Create MySQL database and user

Start MySQL server \[code lang=text\] /etc/init.d/mysql start \[/code\] Login into mysql \[code lang=text\] mysql -u root -p \[/code\] Enter your password Your console windows will now start with `mysql&gt;` Type in to create database for wordpress (database name can be customize) \[code lang=sql\] CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8\_unicode\_ci; \[/code\] SQL query must end with semicolon(;) Create a separate account to manage wordpress database \[code lang=sql\] GRANT ALL ON wordpress.\* TO 'admin'@'localhost' IDENTIFIED BY 'admin'; \[/code\] Flush the current Privileges, so MySQL will know about the recent changes \[code lang=sql\] FLUSH PRIVILEGES; \[/code\] Exit MySQL \[code lang=sql\] EXIT; \[/code\] Adjust Apache configuration to allow for .htaccess override and rewrites Open apache configuration file to edit \[code lang=text\] /etc/apache2/apache2.conf \[/code\] You can use Ubuntu nano editor, or if you’ve mapped the network drive before (step 4), open the file like any other file on windows Nano \[code lang=text\] nano /etc/apache2/apache2.conf \[/code\] Network Drive ![network drive edit file](http://farm5.staticflickr.com/4323/36326087335_f70a215f0f_o.png) Search for this part and change \[code lang=text\] . . . <Directory /var/www/html/> AllowOverride All </Directory> . . . \[/code\] Save and close the file Enable rewrite module \[code lang=text\] a2enmod rewrite \[/code\] Enable changes \[code lang=text\] apache2ctl configtest \[/code\] Restart apache2 service \[code lang=text\] service apache2 restart \[/code\]

## 4.2. Install wordpress

Download wordpress at: [https://wordpress.org/](https://wordpress.org/) Extract to a folder Copy the content of folder “wordpress” to folder “/var/www/html” on container Permission and .htaccess Show hidden files and folder on WinSCP \[code lang=text\] Open WinSCP > Option > References… \[/code\] ![show hidden file](http://farm5.staticflickr.com/4300/36326087085_a8c29ef11e_o.png) Create .htaccess file Right click on an empty space > New File > enter .htaccess ![create .htaccess](http://farm5.staticflickr.com/4441/36326087035_022f35bffa_o.png) Set Read / Write permission for .htaccess Right click on .htaccess > Properties ![permissions for .htaccess](http://farm5.staticflickr.com/4325/35517228003_73383a8bcc_o.png) Set permission recursively for all 3 folders ![permissions for all 3 folders](http://farm5.staticflickr.com/4409/35490057164_0d1ff22807_o.png)

## 4.3. Config

Open `wp-config.php` and fill in these info \[code lang=php\] // \*\* MySQL settings - You can get this info from your web host \*\* // /\*\* The name of the database for WordPress \*/ define('DB\_NAME', 'wordpress'); /\*\* MySQL database username \*/ define('DB\_USER', 'admin'); /\*\* MySQL database password \*/ define('DB\_PASSWORD', 'admin'); /\*\* MySQL hostname \*/ define('DB\_HOST', 'localhost'); /\*\* Database Charset to use in creating database tables. \*/ define('DB\_CHARSET', 'utf8'); /\*\* The Database Collate type. Don't change this if in doubt. \*/ define('DB\_COLLATE', ''); \[/code\] Open link and copy the code show up then replace them ![salt](http://farm5.staticflickr.com/4388/36326086765_8627dd85cc_o.png) Add this line (to enable wordpress can modify files and folder directly \[code lang=php\] define('FS\_METHOD', 'direct'); \[/code\] It’s done, open your `domain:port` to config wordpress using web interface