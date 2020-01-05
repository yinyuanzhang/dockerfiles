FROM iwaydev/base-php-cron-7.1-dev

WORKDIR /var/www/driver2

#cron table
RUN touch /etc/cron.d/crontab
RUN chmod 777 /etc/cron.d/crontab
RUN touch /var/log/cron.log
ENTRYPOINT ["docker/builds/php-cron/docker-entrypoint.sh"]

RUN apt-get autoremove && apt-get clean

