FROM alexcheng/apache2-php5:5.5.30

ENV MAGENTO_VERSION 1.8.1.0

RUN a2enmod rewrite

ENV INSTALL_DIR /var/www/html

RUN cd /tmp && \
    curl https://codeload.github.com/OpenMage/magento-mirror/tar.gz/$MAGENTO_VERSION -o $MAGENTO_VERSION.tar.gz && \
    tar xvf $MAGENTO_VERSION.tar.gz && \
    mv magento-mirror-$MAGENTO_VERSION/* magento-mirror-$MAGENTO_VERSION/.htaccess $INSTALL_DIR

RUN chown -R www-data:www-data $INSTALL_DIR

RUN apt-get update && \
    apt-get install -y mysql-client-5.7 libxml2-dev libmcrypt4 libmcrypt-dev libpng-dev libjpeg-dev libfreetype6 libfreetype6-dev

RUN docker-php-ext-install soap
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mcrypt
RUN docker-php-ext-configure gd --with-jpeg-dir=/usr/lib/ --with-freetype-dir=/usr/lib/ && \
    docker-php-ext-install gd

COPY ./bin/install-magento /usr/local/bin/install-magento
RUN chmod +x /usr/local/bin/install-magento

RUN bash -c 'bash < <(curl -s -L https://raw.github.com/colinmollenhour/modman/master/modman-installer)'
RUN mv ~/bin/modman /usr/local/bin

WORKDIR $INSTALL_DIR

#COPY redis.conf /var/www/html/app/etc/
