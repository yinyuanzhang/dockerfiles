FROM alpine

LABEL MAINTAINER "iLemonrain <ilemonrain@ilemonrain.com>" \
      ARCHITECTURE "amd64"

ENV ROOT_PASSWORD="alpine" \
    APK_MIRROR="dl-cdn.alpinelinux.org" \
    APK_MIRROR_SCHEME="http" \
    MYSQL_DATABASE="typecho" \
    MYSQL_USER="typecho" \
    MYSQL_PASSWORD="typecho" \
    MYSQL_ROOT_PASSWORD="lamp_root" \
    WEBSITE_INSTALL_NAME="Typecho 1.1 (17.10.30)" \
    WEBSITE_INSTALL_URL="http://typecho.org/downloads/1.1-17.10.30-release.tar.gz"
    

RUN (echo "" ;\
     echo "*********************************************" ;\
     echo "*                                           *" ;\
     echo "* LAMP AIO Docker Image (Alpine Linux core) *" ;\
     echo "*                                           *" ;\
     echo "*   Docker Image Builder (Build 20180212)   *" ;\
     echo "*                                           *" ;\
     echo "*********************************************" ;\
     echo "" ;\
     echo "Start Building the Docker Image, Please Wait ...";\
     echo "" ;\
     echo -e "\033[33m -> Modifing APK reposiroties config ...\033[0m" ;\
     sed -i "s/dl-cdn.alpinelinux.org/${APK_MIRROR}/g" /etc/apk/repositories ;\
     sed -i "s/http/${APK_MIRROR_SCHEME}/g" /etc/apk/repositories ;\
     echo "" ;\
     echo -e "\033[33m -> Updating APK repositories ...\033[0m" ;\
     apk update ;\
     echo "" ;\
     echo -e "\033[33m -> Upgrading System ...\033[0m" ;\    
     apk upgrade ;\
     echo "" ;\
     echo -e "\033[33m -> Installing Base Package ...\033[0m" ;\
     apk add curl pwgen ;\
     echo "" ;\
     echo -e "\033[33m -> Installing Apache2 ...\033[0m" ;\
     apk add php7-apache2 ;\
     echo "" ;\
     echo -e "\033[33m -> Installing PHP7 & PHP Extensions ...\033[0m" ;\
     apk add php7-cli php7-json php7-phar php7-openssl php7-zlib php7-bcmath \
             php7-dba php7-enchant php7-gd php7-intl php7-json php7-mbstring \
             php7-mysqlnd php7-opcache php7-pdo php7-pdo_mysql php7-soap \
             php7-ctype php7-session ;\
    echo "" ;\
    echo -e "\033[33m -> Installing PHP Composer ...\033[0m" ;\
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer ;\
    echo "" ;\
    echo -e "\033[33m -> Installing MariaDB (MySQL) ...\033[0m" ;\
    apk add mysql mysql-client ;\
    echo "" ;\
    echo -e "\033[33m -> Applying setting for Apache2 ...\033[0m" ;\
    sed -i "s/AllowOverride none/AllowOverride All/" /etc/apache2/httpd.conf ;\
    mkdir /run/apache2/ ;\
    echo -e "\033[33m -> Deleting default Apache index.html ...\033[0m" ;\   
    rm -f /var/www/localhost/htdocs/index.html ;\
    echo "" ;\
    echo -e "\033[33m -> Cleaning up  ...\033[0m" ;\
    rm -rf /var/cache/apk/* /tmp/* ;\
    echo "" ;\
    echo -e "\033[33m -> Finishing Package Installtion ...\033[0m" ;\
    echo "This may take a while, please wait docker finish the work ..." ;\
    echo "")

ADD scripts/ /scripts/
ADD scripts/_install.sh /var/www/localhost/htdocs/_install.sh
ADD wwwroot/ /var/www/localhost/htdocs/

RUN (rm -f /var/www/localhost/htdocs/index.html ;\
    echo -e "\033[33m -> Downloading ${WEBSITE_INSTALL_NAME} ...\033[0m" ;\
    cd /var/www/localhost/htdocs/ ;\
    sh _install.sh ;\
    rm -f _install.sh ;\
    cd / ;\
    echo "" ;\
    echo -e "\033[33m -> Changing privilege for /var/www/localhost/htdocs/ ...\033[0m" ;\
    chown -R apache:apache /var/www/localhost/htdocs/ ;\
    echo "" ;\
    echo -e "\033[33m -> Changing privilege for /scripts/ ...\033[0m" ;\
    chmod -R 755 /scripts/ ;\
    echo "" ;\
    echo "*********************************************" ;\
    echo "" ;\    
    echo -e "\033[33m --== Image Build Success ==-- \033[0m" ;\
    echo "" )

EXPOSE 80

VOLUME ["/var/lib/mysql"]
VOLUME ["/var/www/localhost/htdocs/"]

ENTRYPOINT [ "sh", "/scripts/entrypoint.sh" ]
