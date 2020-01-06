FROM ubuntu:xenial
MAINTAINER Emre <e@emre.pm>

ENV DEBIAN_FRONTEND noninteractive

RUN \
    apt-get update -qq && \
    apt-get install -y mysql-client curl vim cron && \
    apt-get install -y php-cli php-curl php-mysql php-bcmath php-gd php-gmp php-intl php-json php-mbstring php-mcrypt php-mysqlnd php-opcache php-pear php-pspell php-soap php-xml php-imagick php-zip php-memcached && \
    apt-get clean && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/* && \
    rm -rf /etc/cron.daily/* /etc/cron.hourly/* /etc/cron.monthly/* /etc/cron.weekly/* && \
    groupadd -g 80 www && \
    useradd -g 80 -u 80 www

ENTRYPOINT ["/usr/sbin/cron", "-f"]
