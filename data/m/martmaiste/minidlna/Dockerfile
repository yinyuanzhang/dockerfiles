FROM alpine:3.7
MAINTAINER ull <mart.maiste@gmail.com>

# install minidlna
RUN apk --no-cache add minidlna

# Add config file
ADD minidlna.conf /etc/minidlna.conf
ADD run.sh /usr/local/bin/run.sh

RUN chmod +x /usr/local/bin/*

EXPOSE 1900/udp
EXPOSE 8200

ENTRYPOINT [ "run.sh" ]
