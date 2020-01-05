FROM ubuntu:xenial

MAINTAINER Szabolcs Hegedus <szabolcs.hegedus@gmail.com>


ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends --yes \
    software-properties-common \
    net-tools \
    supervisor \
    htop \
    mc \
    nload \
    ncdu \
    mysql-client \
    cron

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php

RUN apt-get update && apt-get install --no-install-recommends --yes \
        apache2 \
        ca-certificates\
        php7.1 \
        php7.1-mysql

COPY files /

RUN \
  groupadd cbpolicyd && \
  useradd -g cbpolicyd cbpolicyd && \
  apt-get update && \
  apt-get -o Dpkg::Options::=--force-confdef -y install gettext-base postfix-cluebringer postfix-cluebringer-mysql postfix-cluebringer-webui -y nano && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/* /etc/cluebringer && \
  mkdir --mode=0775 /etc/cluebringer && \
  cp /usr/share/doc/postfix-cluebringer/database/policyd-db.mysql.gz /tmp/ && \
  cp -r /usr/share/postfix-cluebringer-webui/webui/* /var/www/html/ && \
  gunzip /tmp/policyd-db.mysql.gz && \
  sed -i -e 's/TYPE=InnoDB/ENGINE=InnoDB/g' /tmp/policyd-db.mysql && \
  chmod -R 0755 /hooks && \
  chmod -R 0777 /var/www/html && \
  chmod 0666 /var/log/cbpolicyd.log

RUN a2enmod rewrite && \
    a2enmod rewrite expires && \
    a2enmod remoteip

RUN touch /etc/apache2/conf-available/remoteip.conf && \
    echo "RemoteIPHeader X-Forwarded-For" >> etc/apache2/conf-available/remoteip.conf && \
    echo "RemoteIPTrustedProxy 10.0.0.0/8" >> etc/apache2/conf-available/remoteip.conf && \
    ln -rs /etc/apache2/conf-available/remoteip.conf /etc/apache2/conf-enabled/remoteip.conf


RUN chmod 600 /var/spool/cron/crontabs/root
RUN chown root:crontab /var/spool/cron/crontabs/root
RUN touch /var/log/cleanscript.log

ENV MYSQL_ROOT_PASSWORD=root_password \
    MYSQL_DATABASE=cluebringer \
    MYSQL_USER=cluebringer \
    MYSQL_PASSWORD=user_password \
    CLUEBRINGER_DB_BACKEND=mysql \
    CLUEBRINGER_DB_PORT=3306 \
    CLUEBRINGER_DB_HOST=mysql \
    WEBUI_PASSWORD=webui_password \
    TZ=Europe/Budapest

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN rm /var/www/html/index.html

ENTRYPOINT ["/bin/bash", "-e", "/init/entrypoint"]

CMD ["run"]

EXPOSE 80 443 10031
