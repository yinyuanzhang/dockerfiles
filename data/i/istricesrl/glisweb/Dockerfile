# immagine di partenza
FROM debian:latest

# informazioni sull'immagine
LABEL mantainer="Fabio Mosti <fabio.mosti@gmail.com>"
LABEL description="immagine per la distribuzione di GlisWeb"

# ambiente non interattivo
# ENV DEBIAN_FRONTEND noninteractive

# variabili d'ambiente per apache
ENV APACHE_RUN_USER  www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR   /var/log/apache2
ENV APACHE_PID_FILE  /var/run/apache2/apache2.pid
ENV APACHE_RUN_DIR   /var/run/apache2
ENV APACHE_LOCK_DIR  /var/lock/apache2

# espongo la porta 80
EXPOSE 80/tcp

# aggiorno il sistema e installo i pacchetti
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq > /dev/null \
    && apt-get install -qq -y --no-install-recommends apt-utils \
    && apt-get upgrade -qq -y > /dev/null \
    && apt-get install -qq -y \
        mc \
        cron \
        gzip \
        composer > /dev/null

# creo le cartelle dell'applicazione
# RUN mkdir -p /var/www/html/var \
#     && mkdir -p /var/www/html/src \
#     && mkdir -p /var/www/html/var/log/apache \
#     && touch /var/www/html/var/log/apache/error.log \
#     && touch /var/www/html/var/log/apache/access.log

# setto la cartella di lavoro
WORKDIR /var/www/html

# mount point
# VOLUME /var/www/html/var

# copio i file dell'applicazione
COPY / /var/www/html/

# installo apache
RUN apt-get install -qq -y apache2 > /dev/null

# elimino i file inutili
RUN rm -f /var/www/html/index.html

# configuro apache
RUN a2enmod deflate \
    && a2enmod headers \
    && a2enmod rewrite

# creo le cartelle di apache, copio la configurazione del sito e configuro i permessi
RUN mkdir -p $APACHE_RUN_DIR \
    && mkdir -p $APACHE_LOCK_DIR \
    && mkdir -p $APACHE_LOG_DIR \
    && chown -Rf $APACHE_RUN_USER:$APACHE_RUN_GROUP $APACHE_LOG_DIR \
    && chmod -Rf 775 $APACHE_LOG_DIR \
    && cp -f /var/www/html/_usr/_apache2/000-docker.conf /etc/apache2/sites-available/000-default.conf \
    && echo "ServerName localhost" > /etc/apache2/conf-enabled/servername.conf \
    && chown -Rf $APACHE_RUN_USER:$APACHE_RUN_GROUP /var/www \
    && chmod -Rf 775 /var/www

# installo PHP
RUN apt-get install -qq -y \
    php \
    php-common \
    php-curl \
    php-dev \
    php-gd \
    php-ldap \
    php-mbstring \
    php-memcache \
    php-mysql \
    php-pear \
    php-pgsql \
    php-redis \
    php-xml \
    php-yaml \
    php-zip

# eseguo composer
RUN composer update

# mount point
# VOLUME /var/www/html/var
# VOLUME /var/www/html/src

# attivo lo schedulatore
# RUN cat /var/www/html/_usr/_crontab/crontab >> /etc/crontab

# esecuzione cron
# CMD ["cron", "-f"]

# ambiente interattivo
# ENV DEBIAN_FRONTEND teletype

# demone da lanciare
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D","FOREGROUND"]
