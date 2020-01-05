# php7.2.17镜像
# 包含扩展：
# redis 4.2.0
# mongo 1.5.3
# event
# swoole 4.2.9   | 查看安装情况 php --ri swoole
# composer
#
# PHP version 7.2.18
# oddoson/basephp:7.2
# nginx 文件路径 /usr/share/nginx/html/
# docker build -t  oddoson/basephp:7.2 .
# Use: docker build --rm -t  basephp:7.2 .
# 打包提交
# docker tag basephp:7.2 oddoson/basephp:7.2
# docker push basephp:7.2
#
# 查看已安装扩展： # php --info 或者 php-fpm -m  或者  /usr/local/php/bin/php -m
# /etc/php.ini 
# 拓展配置文件位置：/etc/php.d
# php-fpm 配置文件：/usr/local/php/etc/php-fpm.conf ， /usr/local/php/etc/php-fpm.d/*.ini

# 坑： 不能使用 yum install php-xxxx 安装php扩展。默认会下载php5.4，而不是想要的版本

FROM oddoson/basephp:base
MAINTAINER "odd"
LABEL author="odd" \
      description="nginx" 
 
RUN cd /home && wget http://cn2.php.net/distributions/php-7.2.18.tar.gz \
&& tar -xf php-7.2.18.tar.gz \
&& cd php-7.2.18 \
&& ./configure \
#指定 php 安装目录
--prefix=/usr/local/php \
--bindir=/usr/local/php/bin \
--with-config-file-path=/etc \
#扩展配置文件
--with-config-file-scan-dir=/etc/php.d \ 
--enable-fpm \
--with-fpm-user=www \
--with-fpm-group=www \
--enable-inline-optimization \
--disable-debug \
--disable-rpath \
--enable-shared \
--enable-soap \
--with-libxml-dir \
--with-xmlrpc \
--with-openssl \
--with-mcrypt \
--with-mhash \
--with-pcre-regex \
--with-sqlite3 \
--with-zlib \
--enable-bcmath \
--with-iconv \
--with-bz2 \
--enable-calendar \
--with-curl \
--with-cdb \
--enable-dom \
--enable-exif \
--enable-fileinfo \
--enable-filter \
--with-pcre-dir \
--enable-ftp \
--with-gd \
--with-openssl-dir \
--with-jpeg-dir \
--with-png-dir \
--with-webp-dir \
--with-zlib-dir \
--with-freetype-dir \
--enable-gd-native-ttf \
--enable-gd-jis-conv \
--with-gettext \
--with-gmp \
--with-mhash \
--enable-json \
--enable-mbstring \
--enable-mbregex \
--enable-mbregex-backtrack \
--with-libmbfl \
--with-onig \
--enable-pdo \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
--with-zlib-dir \
--with-pdo-sqlite \
--with-readline \
--enable-session \
--enable-shmop \
--enable-simplexml \
--enable-sockets \
--enable-sysvmsg \
--enable-sysvsem \
--enable-sysvshm \
--enable-wddx \
--with-libxml-dir \
--with-xsl \
--enable-zip \
--enable-mysqlnd-compression-support \
--with-pear \
--enable-opcache \
--enable-pcntl \
--enable-posix \
# --enable-swoole \
&& make && make install \
&& \cp -f /usr/local/php/bin/pear /usr/bin \
&& \cp -f /usr/local/php/bin/peardev /usr/bin \
&& \cp -f /usr/local/php/bin/pecl /usr/bin \
&& \cp -f /usr/local/php/bin/phar /usr/bin \
&& \cp -f /usr/local/php/bin/phar.phar /usr/bin \
&& \cp -f /usr/local/php/bin/php /usr/bin \
&& \cp -f /usr/local/php/bin/php-cgi /usr/bin \
&& \cp -f /usr/local/php/bin/php-config /usr/bin \
&& \cp -f /usr/local/php/bin/phpize /usr/bin \
&& \cp -f /usr/local/php/sbin/php-fpm /usr/bin \
&& ln -s -f /usr/local/php/ /usr/include/php \
# Php-fpm 开机启动
&& chmod +x /etc/rc.d/rc.local && echo "/usr/local/php/sbin/php-fpm start" >>/etc/rc.d/rc.local \
# 添加PHP环境变量
&& echo -e '\n export PATH=/usr/local/php/bin:/usr/local/php/sbin:$PATH\n' >> /etc/profile \
&& source /etc/profile \
&& /home/php-7.2.18/build/shtool install -c ext/phar/phar.phar /usr/local/php/bin \
&& cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf \ 
&& sed -i 's/;pid = run\/php-fpm.pid/pid = run\/php-fpm.pid/g' /usr/local/php/etc/php-fpm.conf && sed -i 's/listen = 127.0.0.1:9000/listen = 0.0.0.0:9000/g' /usr/local/php/etc/php-fpm.conf \

############### 安装php扩展start ###############
&& /usr/local/php/bin/pecl channel-update pecl.php.net  && /usr/local/php/bin/pecl config-set php_bin /usr/local/php/bin/php && /usr/local/php/bin/pecl config-set php_dir /usr/local/php && /usr/local/php/bin/pecl config-set ext_dir /usr/local/php/lib/php/extensions/no-debug-non-zts-20170718 \ 
#安装mongodb扩展
&& pecl install mongodb-1.5.3  \
#安装redis扩展
&& pecl install redis-4.2.0 \
#安装event 扩展
&& echo no | pecl install  event \

# swoole扩展,要手动安装，pecl会自动开启日志。。
&&  wget https://pecl.php.net/get/swoole-4.2.9.tgz && tar zxvf swoole-4.2.9.tgz && cd swoole-4.2.9 && phpize \
&& yum install -y nghttp2 && ./configure --enable-coroutine --enable-openssl   --enable-sockets --enable-mysqlnd  \
&& make clean && make &&  make install \

#安装composer
&& wget https://dl.laravel-china.org/composer.phar -O /usr/local/bin/composer && chmod a+x /usr/local/bin/composer \

&& mkdir -p /etc/php.d/ \
&& echo 'extension=redis.so' > /etc/php.d/redis.ini \
&& echo 'extension=mongodb.so' > /etc/php.d/mongo.ini \
&& echo 'extension=event.so' > /etc/php.d/30-event.ini \
&& echo 'extension=swoole.so' > /etc/php.d/swoole.ini \
############### 安装php扩展end ###############


############### 配置 ###############
# data folder
&& mkdir /data && chmod -R 777 /data \
&& yum -y remove wget \
&& rm -rf /home/* \
&& pecl clear-cache \
&& yum clean all && rm -rf /var/cache/yum

ADD ./www.fpm.conf /usr/local/php/etc/php-fpm.d/www.conf
ADD ./php.ini /etc/php.ini
VOLUME [ "/usr/share/nginx/html/","/usr/local/php/etc/php-fpm.d/" ]
EXPOSE 9000
CMD ["php-fpm","-c /etc/php.ini","-F"]