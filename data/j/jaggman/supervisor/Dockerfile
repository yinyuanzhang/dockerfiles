FROM jaggman/php

RUN apt-get update && \
apt-get install -y supervisor && \
ln -sf /dev/stdout /var/log/supervisor/supervisord.log

ADD supervisord.conf /etc/supervisor/supervisord.conf

VOLUME [ "/etc/supervisor/conf.d/", "/etc/cron.d/" ]

CMD ["/usr/bin/supervisord", "-n"]