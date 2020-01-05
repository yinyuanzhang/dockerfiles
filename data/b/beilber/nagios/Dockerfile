FROM sameersbn/ubuntu:14.04.20150504

ENV NAGIOS_TIMEZONE utc

RUN sed -i 's/universe/universe multiverse/' /etc/apt/sources.list
RUN apt-get update && apt-get install -y nagios3 nagios-plugins nagios-images nagios-nrpe-server iputils-ping netcat snmp snmpd snmp-mibs-downloader php5-cli apache2 libapache2-mod-php5 runit bc postfix bsd-mailx
RUN ( egrep -i  "^${NAGIOS_GROUP}" /etc/group || groupadd $NAGIOS_GROUP ) && ( egrep -i "^${NAGIOS_CMDGROUP}" /etc/group || groupadd $NAGIOS_CMDGROUP )
RUN ( id -u $NAGIOS_USER || useradd --system $NAGIOS_USER -g $NAGIOS_GROUP -d $NAGIOS_HOME ) && ( id -u $NAGIOS_CMDUSER || useradd --system -d $NAGIOS_HOME -g $NAGIOS_CMDGROUP $NAGIOS_CMDUSER )

RUN mkdir -p /usr/share/snmp/mibs && chmod 0755 /usr/share/snmp/mibs && touch /usr/share/snmp/mibs/.foo

#RUN echo "use_timezone=$NAGIOS_TIMEZONE" >> /etc/nagios3/nagios.cfg && echo "SetEnv TZ \"${NAGIOS_TIMEZONE}\"" >> /etc/nagios3/apache2.conf

RUN sed -i.bak 's,/var/www/html,/usr/share/nagios3/htdocs,g' /etc/apache2/sites-available/000-default.conf

RUN echo "Alias /stylesheets /etc/nagios3/stylesheets" >> /etc/nagios3/apache2.conf

RUN echo "Alias /nagiosql  /usr/share/nagios3/htdocs/nagiosql32" >> /etc/nagios3/apache2.conf

RUN download-mibs && echo "mibs +ALL" > /etc/snmp/snmp.conf

RUN sed -i 's,/bin/mail,/usr/bin/mail,' /etc/nagios3/commands.cfg && \
  sed -i 's,/usr/usr,/usr,' /etc/nagios3/commands.cfg

RUN cp /etc/services /var/spool/postfix/etc/

RUN mkdir -p /etc/sv/nagios && mkdir -p /etc/sv/apache && rm -rf /etc/sv/getty-5 && mkdir -p /etc/sv/postfix
ADD nagios.init /etc/sv/nagios/run
ADD apache.init /etc/sv/apache/run
ADD postfix.init /etc/sv/postfix/run
ADD postfix.stop /etc/sv/postfix/finish

ADD start.sh /usr/local/bin/start_nagios

ENV APACHE_LOCK_DIR /var/run
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

#RUN wget  -O nagiosql_320.tar.gz http://downloads.sourceforge.net/project/nagiosql/nagiosql/NagiosQL%203.2.0/nagiosql_320.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fnagiosql%2Ffiles%2Fnagiosql%2FNagiosQL%25203.2.0%2F&ts=1432841105&use_mirror=hivelocity && tar -zxf nagiosql_320.tar.gz -C /usr/share/nagios3/htdocs && rm -f nagiosql_320.tar.gz

VOLUME /etc/nagios3/conf.d

CMD ["/usr/local/bin/start_nagios"]
