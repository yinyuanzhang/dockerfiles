FROM centos:6

ENV TIMEZONE="Europe/Moscow"
ENV BITRIX_MAX_MEMORY=524288
ENV ROOT_SSH_PASS="4EyahtMj"
ENV BITRIX_SSH_PASS="XW7ur3TB"
ENV PHP_REPOSITORY_NAME=remi-php56
ENV PHP_REPOSITORY_LOCATION=/etc/yum.repos.d/remi.repo
ENV MULTISITE_ID=0

ADD scripts/bitrix-env.sh /tmp/

ADD configs/php.d /tmp/php.d

ADD scripts/php-prepare.sh /tmp/
ADD scripts/node-prepare.sh /tmp/
ADD scripts/software-prepare.sh /tmp/

RUN chmod +x /tmp/bitrix-env.sh
RUN chmod +x /tmp/php-prepare.sh
RUN chmod +x /tmp/node-prepare.sh
RUN chmod +x /tmp/software-prepare.sh

RUN /tmp/bitrix-env.sh && /tmp/php-prepare.sh
RUN /tmp/node-prepare.sh
RUN /tmp/software-prepare.sh

WORKDIR /
ADD scripts/start.sh /
RUN chmod +x /start.sh
ENTRYPOINT exec /start.sh