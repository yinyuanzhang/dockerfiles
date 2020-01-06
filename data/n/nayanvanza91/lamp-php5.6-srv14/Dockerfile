from ubuntu:14.04

MAINTAINER Nayan V. <nayanvanza91@gmail.com>

RUN apt-get update && apt-get install -y vim \
    && apt-get install -y software-properties-common \
    && apt-get install -y python-software-properties \
    && apt-get install -y build-essential \
    && apt-get install -y tcl8.5 \
    && apt-get install -y cron \
    && apt-get install -y curl \
    && apt-get install -y rsync \
    && apt-get install -y git \
    && apt-get install -y apt-transport-https \
    && apt-get install -y supervisor \
    && apt-get install -y postfix \
    && apt-get install -y openssh-server \
    && apt-get install -y psmisc \
    && apt-get install -y tree \
    && apt-get install -y unzip \
    && apt-get install -y rsyslog \
    && mkdir /var/run/sshd \
    && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
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
    && cd /tmp/ \
    && wget https://repo.percona.com/apt/percona-release_0.1-4.$(lsb_release -sc)_all.deb \
    && dpkg -i percona-release_0.1-4.$(lsb_release -sc)_all.deb \
    && apt-get -y update \
    && echo "percona-server-server-5.6 percona-server-server/root_password password secret" | sudo debconf-set-selections \
    && echo "percona-server-server-5.6 percona-server-server/root_password_again password secret" | sudo debconf-set-selections \
    && apt-get -y install percona-server-server-5.6 percona-server-client-5.6 \
    && add-apt-repository ppa:ondrej/php \
    && apt-get update \
    && apt-get install -y php5.6 \
    && apt-get install -y php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-xml php5.6-cli php5.6-gd php5.6-soap php5.6-curl\
    && apt-get install -y libapache2-mod-php5.6 \
    && cd / \
    && wget https://files.phpmyadmin.net/phpMyAdmin/4.6.4/phpMyAdmin-4.6.4-english.tar.gz \
    && tar xvzf phpMyAdmin-4.6.4-english.tar.gz \
    && mv phpMyAdmin-4.6.4-english phpmyadmin \
    && rm -rf phpMyAdmin-4.6.4-english.tar.gz \
    && cp phpmyadmin/config.sample.inc.php phpmyadmin/config.inc.php \
    && chown -R www-data:www-data phpmyadmin \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer 

ADD tools/docker/apache2/apache2.conf /etc/apache2/apache2.conf
ADD tools/docker/apache2/envvars /etc/apache2/envvars
ADD tools/docker/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
ADD tools/docker/phpmyadmin/config.inc.php /phpmyadmin/config.inc.php

ADD tools/docker/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
ADD tools/docker/supervisor/conf.d/apps.conf /etc/supervisor/conf.d/apps.conf

ADD tools/docker/scripts/start.sh /start.sh

RUN chmod +x /*.sh

EXPOSE 22 80 443 3306

#ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash", "/start.sh"]                                                                              
