FROM centos/systemd

# Enable Required Package Repositories 
RUN yum install -y epel-release; yum update -y

# Install Nginx, NodeJS, Git, Supervisor, and Wget
RUN yum install -y nginx wget git nodejs supervisor yum-utils

#Install MySQL 
RUN wget https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm && rpm -ivh mysql80-community-release-el7-1.noarch.rpm; \
yum-config-manager --disable mysql80-community; \
yum-config-manager --enable mysql57-community; \
yum install -y mysql-community-server;

# Install PHP
RUN wget http://rpms.remirepo.net/enterprise/remi-release-7.rpm && rpm -Uvh remi-release-7.rpm; \
yum-config-manager --enable remi-php71; \
yum update -y; \
yum install -y php-fpm php-cli php-pdo php-mysqlnd php-xml php-soap php-gd php-mbstring php-zip php-intl php-mcrypt php-opcache;

# Install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && php composer-setup.php; \
php -r "unlink('composer-setup.php');"; \
mv composer.phar /usr/bin/composer;

# Enable Installed Services
RUN systemctl start mysqld php-fpm nginx supervisord; \
systemctl enable mysqld php-fpm nginx supervisord; 

# Skip: Configure SELinux
# RUN yum install -y policycoreutils policycoreutils-python selinux-policy selinux-policy-targeted libselinux-utils setroubleshoot-server setools setools-console mcstrans; \
# sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/selinux/config; 
# setenforce permissive;

# Skip Prepare MySQL Database
# ENTRYPOINT ["mysql -uroot -p"]
# CMD ["grep 'temporary password' /var/log/mysqld.log"]
# RUN ALTER USER 'root'@'localhost' IDENTIFIED BY 'P@ssword123';"] 
# RUN CREATE DATABASE oro;"]
# RUN GRANT ALL PRIVILEGES ON oro.* to 'oro_user'@'localhost' identified by 'P@ssword123';
# RUN exit
# Skip : Change the MySQL Server Configuration to use the HDD
# RUN systemctl restart mysqld

# Configure Web Server
# RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.backup
COPY ["default.conf", "/etc/nginx/conf.d/"]
CMD systemctl restart nginx

# Skip: Configure Domain Name Resolution

# Configure PHP 
# Ref https://oroinc.com/orocrm/doc/current/install-upgrade/installation-quick-start-dev/crm#configure-php
CMD mv /etc/php-fpm.d/www.conf /etc/php-fpm.d/www.conf.backup
COPY ["www.conf", "/etc/php-fpm.d/"]
CMD mv /etc/php.ini /etc/php.ini.backup
COPY ["php.ini", "/etc/"]
CMD mv /etc/php.d/10-opcache.ini /etc/php.d/10-opcache.ini.backup
COPY ["10-opcache.ini", "/etc/php.d/"]

# OroCRM Community Edition Application Installation
RUN cd /usr/share/nginx/html; \
git clone -b 3.0 https://github.com/oroinc/crm-application.git oroapp; \
cd oroapp; \ 
# composer install --prefer-dist; 
# php ./bin/console oro:install --env=prod --timeout=900; 

# Add Required Permissions for the nginx User 
# do it manually

# Step 4: Post-installation Environment Configuration
# do it manually

EXPOSE 80
CMD ["/usr/sbin/init"]
