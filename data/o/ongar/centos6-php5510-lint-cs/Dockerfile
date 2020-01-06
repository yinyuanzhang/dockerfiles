FROM centos:6

USER root

RUN yum update -y
RUN yum install -y wget

RUN yum install -y epel-release
RUN yum install -y gcc libxml2-devel openssl-devel libcurl-devel libjpeg-devel libpng-devel php-mcrypt libmcrypt-devel

RUN yum install -y http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-git-release-6-1.noarch.rpm
RUN yum install -y git

RUN wget http://jp2.php.net/get/php-5.5.10.tar.gz/from/this/mirror

RUN mv mirror php-5.5.10.tar.gz

RUN tar -xvf php-5.5.10.tar.gz

RUN cd ./php-5.5.10 && ./configure --prefix=/usr/local/php55 --bindir=/usr/bin  --disable-debug --enable-sigchild --enable-inline-optimization --enable-sysvsem --enable-sysvshm --enable-bcmath --enable-ftp --enable-sockets --enable-exif --enable-soap --with-zlib-dir=/usr --with-zlib --with-gd --with-jpeg-dir=/usr --with-png-dir=/usr  --with-iconv --enable-mbstring --with-mcrypt --with-curl --with-openssl --enable-zip

RUN cd ./php-5.5.10 && make && make install

RUN rm -rf ./php-5.5.10.tar.gz ./php-5.5.10

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php --install-dir=/usr/bin --filename=composer
RUN php -r "unlink('composer-setup.php');"

RUN composer global require overtrue/phplint
RUN composer global require squizlabs/php_codesniffer

ENV PATH "$PATH:/root/.composer/vendor/bin"

RUN yum install -y svn

RUN yum clean all
