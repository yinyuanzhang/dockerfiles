FROM aesopagency/phpfpm:1.1.0

RUN apt-get install -y --force-yes \
    php5-mysql

ADD config/phpfpm-start.sh /opt/bin/phpfpm-start.sh
RUN chmod u=rwx /opt/bin/phpfpm-start.sh

ENTRYPOINT ["/opt/bin/phpfpm-start.sh"]
