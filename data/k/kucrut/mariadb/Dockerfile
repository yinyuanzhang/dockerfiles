FROM alpine:3.7
LABEL Maintainer="Dzikri Aziz <kvcrvt@gmail.com>" \
      Description="Minimalist MariaDB 10.1 container on Alpine Linux."

RUN apk update && apk upgrade && \
    apk add bash tzdata mariadb mariadb-client && \
    apk add gosu --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ && \
    rm -rf /var/cache/apk/*

RUN mkdir /docker-entrypoint-initdb.d

RUN sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf && \
    rm -rf /var/lib/mysql &&\
    mkdir -p /var/lib/mysql /run/mysqld && \
    chown -R mysql:mysql /var/lib/mysql /run/mysqld && \
    chmod 777 /run/mysqld

# comment out a few problematic configuration values
# don't reverse lookup hostnames, they are usually another container
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \
  && echo -e 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
  && mv /tmp/my.cnf /etc/mysql/my.cnf

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld"]
