FROM t3kit/ubuntu18.04-php7.2-apache:1.2.0 AS apachephp

ENV COMPOSER_ALLOW_SUPERUSER = 1

RUN apt-get update && \
apt-get install zip openssh-client -y && \
composer global require hirak/prestissimo
