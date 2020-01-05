FROM elcom/angular
MAINTAINER LWB

ENV DSN_CORE=DSN
ENV DSN_ARCHIVE=DSN
ENV DSN_ARCHIVE_GBGR=DSN
ENV DSN_PHONE=DSN
ENV DSN_SAPRECHTE=DSN

COPY 000-default.conf /etc/apache2/sites-available/

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD /usr/sbin/apache2ctl -D FOREGROUND
