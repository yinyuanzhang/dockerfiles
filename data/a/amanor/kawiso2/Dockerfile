FROM php:7.3-apache
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');"
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer && \
    rm -rf /tmp/composer-setup.php
RUN apt-get update && \
    apt-get install -y git unzip nano vim \
     libfreetype6-dev \
     vim \
     libjpeg62-turbo-dev \
     libmcrypt-dev \
     libpng-dev \
     libc-client-dev \
     libsqlite3-dev \
     libkrb5-dev \
     libcurl4-gnutls-dev \
     wget \
     libzip-dev \
     libzip4 \
     openssl \
     mysql-client \
     openssh-server \
     cron \
     && docker-php-ext-install -j$(nproc) iconv gd pdo_mysql pcntl pdo_sqlite zip curl bcmath opcache mbstring \
     && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
     && docker-php-ext-install -j$(nproc) gd \
     && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
     && docker-php-ext-install imap \
     && docker-php-ext-enable iconv gd pdo_mysql pcntl pdo_sqlite zip curl bcmath opcache mbstring imap \
     && apt-get autoremove -y
RUN apt-get install -y --no-install-recommends libmagickwand-dev
RUN pecl install imagick
RUN pecl install apcu
RUN pecl install mcrypt-1.0.2
RUN docker-php-ext-enable apcu mcrypt imagick
RUN pecl install -o -f redis \
&&  rm -rf /tmp/pear \
&&  echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini
COPY ./000-default.conf /etc/apache2/sites-enabled/000-default.conf
RUN a2enmod ssl
RUN a2enmod rewrite
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/ssl-cert-snakeoil.key -out /etc/ssl/certs/ssl-cert-snakeoil.pem -subj "/C=AT/ST=Vienna/L=Vienna/O=Security/OU=Development/CN=example.com"
RUN echo "memory_limit = 1G;" >> /usr/local/etc/php/php.ini
RUN echo "upload_max_filesize = 512M;" >> /usr/local/etc/php/php.ini
RUN echo "post_max_size = 507M;" >> /usr/local/etc/php/php.ini
RUN echo "opcache.memory_consumption = 1024;" >> /usr/local/etc/php/php.ini
RUN echo "opcache.max_accelerated_files = 15000;" >> /usr/local/etc/php/php.ini
RUN echo "display_errors = off;" >> /usr/local/etc/php/php.ini
RUN mkdir /root/.ssh/
ADD id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts
ADD ./demo.sql /root/
ADD ./deploy-demo.sh /root/
ADD ./deploy-empty.sh /root/
ADD ./update.sh /root/
RUN mkdir /root/controller/
ADD ./AccountingController.php /root/controller/
ADD ./InventoryController.php /root/controller/
ADD ./ProjectsController.php /root/controller/
ADD ./ResourcesController.php /root/controller/
ADD ./TodoController.php /root/controller/
RUN chmod -R 777 /root/*
ADD ./crontab /etc/cron.d/kawiso-cron
RUN chmod 0644 /etc/cron.d/kawiso-cron
RUN crontab /etc/cron.d/kawiso-cron
RUN touch /var/log/cron.log
RUN mkdir /var/run/sshd
RUN echo 'root:128btk76Aven479GU' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo "Port 22" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
CMD ["/usr/sbin/sshd", "-D"]
CMD /etc/init.d/ssh start
CMD cron && tail -f /var/log/cron.log



#VOLUME /var/www/html
#WORKDIR /var/www/html
#RUN cd /var/www/html && git clone git@bitbucket.org:webservicekaupa/hauptsystem.git .
#RUN chmod -R 777 /var/www/html

