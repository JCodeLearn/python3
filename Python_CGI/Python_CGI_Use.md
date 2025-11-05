# Python_CGI

### Apache(Web Http Server Setup)
#### 简单上手
   1. Apache 安装 <br />
       ```bash
       sudo apt update
       sudo apt install apache2
       ```    
   2. Apache 服务管理
       * 启动 Apache 服务：`sudo systemctl start apache2`
       * 设置开机自启动：`sudo systemctl enable apach2`
       * 查看 Apache 服务状态：`sudo systemctl status apache2`
   
   3. 为 Apache 配置防火墙
       * `sudo ufw allow 'Apache'`

   4. Apache 配置 CGI
       * 启用 cgid 模块：`sudo a2enmod cgid`

   5. Apache 配置文件
       * 配置文件目录：/etc/apache2/sites-available/000-default.conf
       * 配置文件添加的内容：
         ```
         ScriptAlias /solutions/ /home/code-j/data/CS/python3/Python_CGI/CGI_Scripts/
         <Directory "/home/code-j/data/CS/python3/Python_CGI/CGI_Scripts/">
            AllowOverride None
            Options +ExecCGI
            Order allow,deny
            Allow from all
         </Directory> 
         ```
      
   6. 查看 Apache 运行过程中出现的错误
       * `sudo tail -f /var/log/apache2/error.log`

   7. Linux 环境配置
      * 一般而言，是由 apache2 的默认用户 www-data 来执行这段可执行程序，由于 python 脚本是解释执行，所以要注意我们要获取的不是 python 脚本的可执行权限，而是 python 脚本的读取权限。所以要保证 www-data 用户拥有 CGI 程序的相关权限；此外，也要保证 www-data 用户能够进入 CGI 程序所在目录，即拥有该目录的执行权限。
   
#### 深入理解