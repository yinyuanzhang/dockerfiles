FROM phusion/baseimage
MAINTAINER kaufmann@netcloud.ch version: 0.1
RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get update && apt-get install -y php-dev php-cli php php-curl php-mongodb apache2 smarty3 vim libapache2-mod-php vim php7.0-ldap
RUN rm -rf /var/lib/apt/lists/*
EXPOSE 80
VOLUME /var/www/html/
CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["apachectl"]
