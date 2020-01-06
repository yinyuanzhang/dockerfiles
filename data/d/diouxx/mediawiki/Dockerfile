#On choisit Debian
FROM debian:10.2

MAINTAINER DiouxX "github@diouxx.be"

#Ne pas poser de question à l'installation
ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
&& apt -y install \
apache2 \
php \
php-mysql \
php-ldap \
php-apcu \
imagemagick \
php-imagick \
php-gd \
php-curl \
php-intl \
php-mbstring \
php-xml \
wget \
python-pygments \
git

#Copy and run mediwiki start script
COPY wiki-start.sh /opt
RUN chmod +x /opt/wiki-start.sh
#WORKDIR /var/www/html
ENTRYPOINT ["/opt/wiki-start.sh"]

#Ports
EXPOSE 80 443
