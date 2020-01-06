FROM nerelohw/docker-mariadb-abuild as mariadb-abuild


FROM nerelohw/docker-alpine:edge

##----
# curl perl
# get-mysqltunerpl

## mode:master/slave/none

## MODE:master|slave|none
ENV REPLICATION_MODE none
## if MODE:master
ENV MASTER_SERVER_ID ""

## if MODE:slave
ENV SLAVE_SERVER_ID ""
ENV REPLICATION_HEALTH_GRACE_PERIOD 3
ENV REPLICATION_HEALTH_TIMEOUT 10
ENV MASTER_HOST ""
ENV MASTER_PORT 3306


## if MODE:slave|master
ENV REPLICATION_USER replication
ENV REPLICATION_PASSWORD replication_ssap

##RUN apk -U add perl perl-doc procps curl pwgen tzdata 
RUN mkdir -p /usr/src/mariadb-apks
COPY --from=mariadb-abuild /mariadb-apks/mariadb-common-10.3.*.apk /usr/src/mariadb-apks
COPY --from=mariadb-abuild /mariadb-apks/mariadb-10.3.*.apk /usr/src/mariadb-apks
COPY --from=mariadb-abuild /mariadb-apks/mariadb-client-10.3.*.apk /usr/src/mariadb-apks
RUN cd /usr/src/mariadb-apks \
&& apk --no-cache add --allow-untrusted *.apk 

RUN mkdir -p /var/run/mysqld \
&& chown mysql:mysql /var/run/mysqld \
&& mkdir -p /var/log/mysql \
&& chown mysql:mysql /var/log/mysql \
&& mkdir -p /etc/mysql/conf.d \
&& chown mysql:mysql /etc/mysql/conf.d \
&& mkdir -p /var/lib/mysql \
&& chown -R mysql:mysql /var/lib/mysql 
##&& rm /etc/mysql/my.cnf


VOLUME /var/lib/mysql


RUN mkdir /docker-entrypoint-initdb.d && mkdir -p /etc/mysql/tools/mysqltuner

## master/slave mode
COPY rootfs/_docker-entrypoint-initdb.d/*       /docker-entrypoint-initdb.d/
COPY rootfs/_usr_local_bin/* /usr/local/bin/
COPY rootfs/_etc_mysql/my.cnf.tmpl /etc/mysql/my.cnf.tmpl
COPY rootfs/_etc_mysql/conf.d/* /etc/mysql/conf.d/

RUN chmod a+x /usr/local/bin/* \
&& rm -rf /var/cache/apk/* \
&& rm -rf /usr/src/mariadb-apks/*

ENTRYPOINT ["docker-mode-entrypoint.sh"]
EXPOSE 3306
CMD ["mysqld"]

