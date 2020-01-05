FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive 

RUN apt-get -y update && \
    apt-get -y install composer curl git gitlab-cli jq php7.2 php7.2-dom php7.2-mbstring php7.2-zip && \
    apt-get -y autoremove && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo "memory_limit=1G" >> /etc/php/7.2/cli/conf.d/00-memory_limit.ini

RUN git clone --depth=1 https://github.com/honzahommer/satis-gitlab.git /opt/satis-gitlab && \
    composer install --no-ansi --no-interaction --no-progress --prefer-dist --working-dir=/opt/satis-gitlab && \
    ln -s /opt/satis-gitlab/bin/satis-gitlab /usr/bin/

WORKDIR /opt/satis-gitlab
