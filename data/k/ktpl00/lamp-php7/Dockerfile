from ubuntu:16.04

MAINTAINER Nayan V. <nayan@krishtechnolabs.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y sudo \
    && apt-get install -y vim \
    && apt-get install -y rsyslog \
    && apt-get install -y software-properties-common \
    && apt-get install -y python-software-properties \
    && apt-get install -y build-essential \
    && apt-get install -y tcl8.5 \
    && apt-get install -y cron \
    && apt-get install -y curl \
    && apt-get install -y rsync \
    && apt-get install -y git \
    && apt-get install -y psmisc \
    && apt-get install -y apt-transport-https \
    && apt-get install -y supervisor \
    && apt-get install -y lsb \
    && echo "postfix postfix/mailname string root" | debconf-set-selections \
    && echo "postfix postfix/main_mailer_type string No configuration" | debconf-set-selections \
    && apt-get install -y postfix mailutils libsasl2-2 libsasl2-modules \
    && apt-get install -y openssh-server \
    && mkdir /var/run/sshd \
    && sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && apt-get install -y language-pack-en-base \
    && apt-get update \
    && locale-gen en_US.UTF-8 \
    && export LANG=en_US.UTF-8 \
    && LC_ALL=en_US.UTF-8 \
    && apt-get update \
    && add-apt-repository ppa:ondrej/apache2 \
    && apt-get install -y apache2 \
    && a2enmod rewrite \
    && cd /etc/apache2/conf-available \
    && printf "<Directory "/phpmyadmin">\nAllowOverride all\nRequire all granted\n</Directory>\nAlias /phpmyadmin /phpmyadmin" > phpmyadmin.conf \
    && a2enconf phpmyadmin.conf \
    && apt-get install -y debconf-utils \
    && cd /tmp/ \
    && wget https://repo.percona.com/apt/percona-release_0.1-4.$(lsb_release -sc)_all.deb \
    && dpkg -i percona-release_0.1-4.$(lsb_release -sc)_all.deb \
    && apt-get -y update \
    && echo "percona-server-server-5.7 percona-server-server/root_password password secret" | debconf-set-selections \
    && echo "percona-server-server-5.7 percona-server-server/root_password_again password secret" | debconf-set-selections \
    && apt-get -y install percona-server-server-5.7 percona-server-client-5.7 \
    && add-apt-repository ppa:ondrej/php \
    && apt-get update \
    && apt-get install -y libapache2-mod-php7.0 php7.0 php7.0-mysql \
    && apt-get install -y php7.0-common php7.0-gd php7.0-mcrypt php7.0-curl php7.0-intl php7.0-xsl php7.0-soap \
    && apt-get install -y php7.0-mbstring php7.0-zip php7.0-bcmath php7.0-iconv php7.0-imagick \
    && cd / \
    && wget https://files.phpmyadmin.net/phpMyAdmin/4.6.4/phpMyAdmin-4.6.4-english.tar.gz \
    && tar xvzf phpMyAdmin-4.6.4-english.tar.gz \
    && mv phpMyAdmin-4.6.4-english phpmyadmin \
    && rm -rf phpMyAdmin-4.6.4-english.tar.gz \
    && chown -R www-data:www-data phpmyadmin \
    && cp phpmyadmin/config.sample.inc.php phpmyadmin/config.inc.php \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer \
#    && curl -L https://packagecloud.io/varnishcache/varnish5/gpgkey | sudo apt-key add - \
#    && echo "deb https://packagecloud.io/varnishcache/varnish5/ubuntu/ xenial main" | sudo tee -a /etc/apt/sources.list.d/varnishcache5.list \
    && apt-get update \
    && apt-get install -y varnish \
    && apt-get install -y redis-server \
    && apt-get install -y vsftpd \
    && apt-get -y update \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer \
    && curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \
    && apt-get install -y nodejs \
    && npm install -g grunt-cli
#    && cd / \
#    && wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
#    && dpkg -i erlang-solutions_1.0_all.deb \
#    && apt-get -y update \
#    && echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list \
#    && wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add - \
#    && apt-get -y update \
#    && apt-get install -y rabbitmq-server

ADD tools/docker/apache2/ports.conf /etc/apache2/ports.conf
ADD tools/docker/apache2/apache2.conf /etc/apache2/apache2.conf
ADD tools/docker/apache2/envvars /etc/apache2/envvars
ADD tools/docker/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
ADD tools/docker/php7/apache2/php.ini /etc/php/7.0/apache2/php.ini
ADD tools/docker/php7/cli/php.ini /etc/php/7.0/cli/php.ini
ADD tools/docker/phpmyadmin/config.inc.php /phpmyadmin/config.inc.php
ADD tools/docker/postfix/main.cf /etc/postfix/main.cf

ADD tools/docker/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
ADD tools/docker/supervisor/conf.d/apps.conf /etc/supervisor/conf.d/apps.conf

ADD tools/docker/scripts/entrypoint.sh /entrypoint.sh
ADD tools/docker/scripts/start.sh /start.sh

RUN chmod +x /*.sh

EXPOSE 21 22 80 443 3306 8080 9200

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["/bin/bash", "/start.sh"]
