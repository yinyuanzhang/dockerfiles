FROM ubuntu:14.04

RUN apt-get update && apt-get install -y software-properties-common

RUN apt-get update && apt-get install -y \
    supervisor \
    apache2 \
    libapache2-mod-php5 \
    php5 \
    php5-gd \
    php5-curl \
    php5-mysql \
    wget

RUN echo mysql-server mysql-server/root_password password 123456 | debconf-set-selections;\
  echo mysql-server mysql-server/root_password_again password 123456 | debconf-set-selections;\
  apt-get install -y mysql-server mysql-client libmysqlclient-dev

COPY conf/site.conf /etc/apache2/sites-available/000-default.conf
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

CMD ["/usr/bin/supervisord"]