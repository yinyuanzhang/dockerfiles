FROM pvpin/ubuntu:latest
MAINTAINER wolfg1969 "wolfg1969@qq.com"

ENV REFRESHED_AT 20170112

RUN apt-get -y update
RUN apt-get -y install git wget

RUN mkdir /opt/pmmp
RUN useradd -r pmmp
RUN chown -R pmmp:pmmp /opt/pmmp

USER pmmp:pmmp

RUN cd /opt/pmmp && wget -q -O - https://raw.githubusercontent.com/pmmp/php-build-scripts/master/installer.sh | bash -s -

VOLUME /opt/pmmp
WORKDIR /opt/pmmp

EXPOSE 19132

CMD ["./start.sh", "--no-wizard", "--enable-rcon=on"]
