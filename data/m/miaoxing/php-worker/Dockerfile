FROM miaoxing/php-fpm:latest

# Install supervisor, cron, rsyslog
RUN apt-get update \
    && apt-get -y --no-install-recommends install supervisor cron rsyslog \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

COPY ./supervisord.conf /etc/supervisor/supervisord.conf

# Execute "php" in cron
RUN ln -s /usr/local/bin/php /usr/bin/php

COPY ./cmd.sh /

CMD ["/cmd.sh"]
