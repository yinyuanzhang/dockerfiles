FROM ubuntu:18.04

LABEL maintainer="Jinghui Hu" version="1.0"

ADD assets /assets
RUN /assets/setup.sh

EXPOSE 22
EXPOSE 1521
EXPOSE 8080
VOLUME /oradata

CMD /usr/sbin/startup.sh && tail -f /dev/null
