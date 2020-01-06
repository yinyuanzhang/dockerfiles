FROM centos/php-71-centos7
ARG PHP_IDE_CONFIG="serverName=bootstrap-rest-api.localhost"
ARG XDEBUG_REMOTE_HOST="10.0.75.1"
ARG XDEBUG_ENABLED="false"

# Configuration XDEBUG pour le path mapping des batchs en mode cli
ENV PHP_IDE_CONFIG=$PHP_IDE_CONFIG

USER root

# Ajout des repo utiles
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
&& rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \
&& rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm

# Parametrage Yum
RUN cp /etc/yum.conf /etc/yum.conf.save \
&& echo 'http_caching=packages' >> /etc/yum.conf

# Installation des packages
RUN yum install -y git \
                   mod_php71w php71w-intl php71w-opcache php71w-mbstring php71w-dom php71w-pdo php71w-mysql php71w-pecl-xdebug php71w-soap php71w-bcmath \
 && yum --enablerepo=remi-php71 -y install php71-php-pecl-rdkafka \
 && yum install -y php71-php-ast \
 && yum update -y

# Parametrage PHP
RUN echo 'date.timezone=Europe/Paris' > /etc/php.d/00-docker-php-date-timezone.ini

# xdebug.ini. Activer les directives selon les besoins
RUN echo 'xdebug.remote_enable=1' >> /etc/php.d/xdebug.ini \
 && echo 'xdebug.remote_connect_back=0' >> /etc/php.d/xdebug.ini \
 && echo "xdebug.remote_host=$XDEBUG_REMOTE_HOST" >> /etc/php.d/xdebug.ini \
 && echo 'xdebug.remote_autostart=1' >> /etc/php.d/xdebug.ini \
 && echo 'xdebug.remote_log=/opt/app-root/src/var/logs/xdebug.log' >> /etc/php.d/xdebug.ini

# Désactivation xdebug selon ENV
RUN if [ "$XDEBUG_ENABLED" == "false" ]; then mv /etc/php.d/xdebug.ini /etc/php.d/xdebug.ini.off; fi

# Extension rdkafka
RUN cp /opt/remi/php71/root/lib64/php/modules/rdkafka.so /usr/lib64/php/modules/rdkafka.so \
 && echo 'extension=/usr/lib64/php/modules/rdkafka.so' >> /etc/opt/rh/rh-php71/php.d/50-rdkafka.ini

# Installation composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# Restauration du fichier yum.conf d'origine
RUN cp /etc/yum.conf.save /etc/yum.conf

# Vide le dossier temporaire
RUN rm -rf /tmp/*

# Copy des ressources
COPY ressources /

#EXPOSE 80 8080 443

#CMD /run-httpd.sh

USER 1001

WORKDIR /opt/app-root/src
