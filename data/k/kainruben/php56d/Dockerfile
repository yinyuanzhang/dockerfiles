# Imagen a utilizar para el container
FROM php:5.6-apache 

MAINTAINER rubenromero.tk <ruromeroc@gmail.com>

#Actualizamos
RUN apt-get -y update && apt-get -y upgrade

# Install tools && libraries 
RUN apt-get -y install --fix-missing apt-utils nano wget dialog \ 
build-essential git curl libcurl3 libcurl3-dev zip \ 
libmcrypt-dev libsqlite3-dev libsqlite3-0 mysql-client \ 
zlib1g-dev libicu-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev \ 
&& rm -rf /var/lib/apt/lists/* # Composer 


RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer # PHP5 Extensions 

RUN docker-php-ext-install curl \
&& docker-php-ext-install tokenizer \
&& docker-php-ext-install json \
&& docker-php-ext-install mcrypt \
&& docker-php-ext-install pdo_mysql \
&& docker-php-ext-install pdo_sqlite \
&& docker-php-ext-install mysqli \
&& docker-php-ext-install zip \
&& docker-php-ext-install -j$(nproc) intl \
&& docker-php-ext-install mbstring \
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
&& docker-php-ext-install -j$(nproc) gd \
&& pecl install xdebug-2.5.5 && docker-php-ext-enable xdebug \
&& echo "xdebug.remote_enable=1" >> /usr/local/etc/php/php.ini

# install GIT
RUN apt-get install -y git

# install CURL
RUN apt-get install -y curl

#  install Python PIP for EBS-CLI Si queremos python-pip
# RUN apt-get install -y python-pip
# RUN pip install --upgrade pip

# install EBS-CLI para trabajar con EBS de AWS
# RUN pip install --upgrade --user awsebcli

# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

 ## Creamos el usuario 
RUN useradd -ms /bin/bash  usuario
RUN mkdir /home/usuario/logs
RUN mkdir /home/usuario/www
RUN echo "<?php phpinfo(); ?>" >/home/usuario/www/__info.php
RUN echo "" > /home/usuario/logs/error.apache.log
RUN echo "" > /home/usuario/logs/access.apache.log
RUN echo "" > /home/usuario/logs/php.error.log
RUN chown -R usuario:usuario /home/usuario
RUN chmod 777 /home/usuario/logs/*

# Agregamos la configuracion de apache para limpiar todo
RUN a2dismod mpm_event && \
    a2enmod mpm_prefork \
            ssl \
            rewrite && \
#    a2ensite default-ssl && \
    ln -sf /home/usuario/logs/acceso-apache /var/log/apache2/access.log && \
    ln -sf /home/usuario/logs/error-apache /var/log/apache2/error.log

# Manually set up the apache environment variables
ENV APACHE_RUN_USER usuario
ENV APACHE_RUN_GROUP usuario

WORKDIR /home/usuario

#upload
#RUN echo "file_uploads = On\n" \
#         "memory_limit = 500M\n" \
#         "upload_max_filesize = 500M\n" \
#         "post_max_size = 500M\n" \
#         "max_execution_time = 600\n" \
#         > /etc/php/5.6/cli/conf.d/uploads.ini

##php errors log
#RUN echo "error_reporting = E_ALL\n" \
#         "logs_errors = On\n" \
#         "error_log = /home/usuario/logs/php.error.log\n" \
#         > /etc/php/5.6/cli/conf.d/logerrors.ini


RUN sed -i 's/^ServerSignature/#ServerSignature/g' /etc/apache2/conf-enabled/security.conf; \
    sed -i 's/^ServerTokens/#ServerTokens/g' /etc/apache2/conf-enabled/security.conf; \
    echo "ServerSignature Off" >> /etc/apache2/conf-enabled/security.conf; \
    echo "ServerTokens Prod" >> /etc/apache2/conf-enabled/security.conf; \
    a2enmod headers; \
    echo "SSLProtocol ALL -SSLv2 -SSLv3" >> /etc/apache2/apache2.conf

ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf
#ADD 001-default-ssl.conf /etc/apache2/sites-enabled/001-default-ssl.conf

#Cleaning a little bt=it the container to make it slimmer.
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#We open port 80 y port 443
EXPOSE 80
#EXPOSE 443

#We start Apache2 at the moment of starting the server
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
