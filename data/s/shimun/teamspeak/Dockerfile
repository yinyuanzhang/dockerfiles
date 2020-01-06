FROM frolvlad/alpine-glibc

RUN apk update && \
    apk add --no-cache bash wget tar coreutils
RUN wget --no-check-certificate -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-init_1.0.1_amd64

RUN chmod +x /usr/bin/dumb-init && \
    mkdir -p /tpl

COPY init.sh /usr/bin/init.sh
COPY ts3server.ini /tpl/ts3server.ini
COPY ts3db_mysql.ini /tpl/ts3db_mysql.ini

VOLUME ["/opt/teamspeak3"]
EXPOSE 10011 30033 9987/udp

ENV TS_VERSION=3.2.0
ENV ARCH=amd64
ENV CHECKSUM=f1e267334e8863342e8eb90ae22203b761b54d9d4400a25ed1fd34fce2187f57

ENV TS3DB_TYPE=SQLITE


CMD ["/usr/bin/dumb-init","/usr/bin/init.sh"]
