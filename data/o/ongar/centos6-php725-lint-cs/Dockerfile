FROM centos:6

USER root

RUN yum update -y
RUN yum install -y wget

RUN yum install -y epel-release
RUN yum install -y gcc libxml2-devel openssl-devel libcurl-devel libjpeg-devel libpng-devel php-mcrypt libmcrypt-devel

RUN yum install -y http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-git-release-6-1.noarch.rpm
RUN yum install -y git

RUN wget http://jp2.php.net/get/php-7.2.5.tar.gz/from/this/mirror

RUN mv mirror php-7.2.5.tar.gz

RUN tar -xvf php-7.2.5.tar.gz

RUN cd ./php-7.2.5 && ./configure --prefix=/usr/local/php55 --bindir=/usr/bin  --disable-debug --enable-sigchild --enable-inline-optimization --enable-sysvsem --enable-sysvshm --enable-bcmath --enable-ftp --enable-sockets --enable-exif --enable-soap --with-zlib-dir=/usr --with-zlib --with-gd --with-jpeg-dir=/usr --with-png-dir=/usr  --with-iconv --enable-mbstring --with-mcrypt --with-curl --with-openssl --enable-zip

RUN cd ./php-7.2.5 && make && make install

RUN rm -rf ./php-7.2.5.tar.gz ./php-7.2.5

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') === '93b54496392c062774670ac18b134c3b3a95e5a5e5c8f1a9f115f203b75bf9a129d5daa8ba6a13e2cc8a1da0806388a8') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php --install-dir=/usr/bin --filename=composer
RUN php -r "unlink('composer-setup.php');"

RUN composer global require overtrue/phplint
RUN composer global require squizlabs/php_codesniffer

ENV PATH "$PATH:/root/.composer/vendor/bin"

RUN yum install -y svn

RUN yum clean all
