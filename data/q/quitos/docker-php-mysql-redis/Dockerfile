FROM library/debian:stretch
MAINTAINER Kenneth Peiruza <kenneth.peiruza@gmail.com>
RUN     apt-get update && \
        apt-get install -y libapache2-mod-php7.0 apache2 php7.0 php-redis php-mysql && \
        rm -rf /var/lib/dpkg /var/lib/apt /var/cache/apt /var/www/html/index.html &&\
        ln -sf /dev/stdout /var/log/apache2/access.log &&\
        ln -sf /dev/stderr /var/log/apache2/error.log &&\
        sed -i 's/session.save_handler = files/session.save_handler = redis/g' /etc/php/7.0/apache2/php.ini &&\
        sed -i '/session.save_handler/a session.save_path = "tcp://redis"' /etc/php/7.0/apache2/php.ini

COPY index.php /var/www/html/index.php

ENTRYPOINT [ "/usr/sbin/apache2ctl", "-D", "FOREGROUND" ]

