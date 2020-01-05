FROM nextcloud:12

RUN apt-get update && apt-get -y install cron

ADD configs/cron.conf /var/www/nextcloud_cron
RUN crontab -u www-data /var/www/nextcloud_cron
ADD configs/run.sh /
RUN chmod 0744 /run.sh

RUN chsh -s /bin/bash www-data

ENTRYPOINT "/run.sh"
