# lnmp
#/* define the version of nginx, php, mysql, phpmyadmin */#
arg NGINX_VERSION=latest
arg PHP_VERSION=7.1
arg MYSQL_VERSION=5.6
arg PMA_VERSION=latest

from php:$PHP_VERSION as phpso_stage

from mysql:$MYSQL_VERSION as mysqlfs_stage

from phpmyadmin/phpmyadmin:$PMA_VERSION as phpmyadmin_stage

from nginx:$NGINX_VERSION as nginx_stage

shell ["/bin/bash", "-c"]

workdir ~

run echo ${NGINX_VERSION} > ~/nginx_version

run echo ${PHP_VERSION} > ~/php_version

run echo ${MYSQL_VERSION} > ~/mysql_version

run echo ${PMA_VERSION} > ~/phpmyadmin_version

run alias ll="ls -al"

run apt-get update && apt-get install -y vim

run echo "<div> \
    NGINX INDEX \
    </div> " > /usr/share/nginx/html/index.html

expose 80/tcp 
expose 8080/tcp 
expose 1992/tcp 
expose 3306/tcp