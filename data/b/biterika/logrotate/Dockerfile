FROM debian:stretch-slim

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y logrotate cron curl

RUN echo "0 1 * * *	/usr/sbin/logrotate /etc/logrotate.conf" >> /etc/cron.d/logrotate

RUN echo "include /etc/logrotate.d" > /etc/logrotate.conf

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]