FROM alpine:latest

MAINTAINER Michał Jaskólski <michal@jaskolski.online>

RUN apk add --no-cache mysql su-exec

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /usr/local/bin/

RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh
#ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306
#CMD ["mysqld"]

