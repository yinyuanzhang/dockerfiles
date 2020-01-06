FROM ubuntu:xenial
MAINTAINER Peter Hoppe <peter.hoppe@bertelsmann.de>

# Install plugins
RUN apt-get update && \
  apt-get -y install wget unzip apache2 libapache2-mod-php php-cli php-curl php-xml php-sqlite3 curl acl vim && \
  rm -rf /var/lib/apt/lists/*

# init
RUN wget -q https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb && \
  dpkg -i dumb-init_*.deb && rm dumb-init_*.deb


RUN rm -fr /var/www/html

# set www:data right
RUN setfacl -m u:www-data:rw- /var/log

ADD vhost.conf /etc/apache2/sites-available/000-default.conf

EXPOSE 80

HEALTHCHECK --interval=5m --timeout=3s CMD curl -I -s -f http://localhost:80/ || exit 1

ADD run.sh /run.sh
ADD index.php /var/www/html/index.php
ADD httpful.phar /var/www/html/httpful.phar
ADD metrics /var/www/html/metrics

RUN chmod 700 /*.sh

# Server CMD
CMD ["dumb-init", "/run.sh"]
