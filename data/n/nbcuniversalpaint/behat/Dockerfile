FROM centos:7
ENV BEHAT_PARAMS='{"extensions": {"Behat\\MinkExtension" : {"selenium2" : {"wd_host" : "http://selenium-hub:4444/wd/hub"}}}}' \
    COMPOSER_ALLOW_SUPERUSER=1

COPY docker-entrypoint.sh /etc/docker-entrypoint.sh

RUN yum -y -e0 update && \
    yum -y -e0 install epel-release wget which && \
    rpm -Uvh https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y -e0 update && \
    yum -y -e0 install php56u && \
    yum -y -e0 install composer

WORKDIR /app

CMD ["bash", "/etc/docker-entrypoint.sh"]
