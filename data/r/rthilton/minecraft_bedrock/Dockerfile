FROM ubuntu:latest
LABEL maintainer="ryan@pnwdc.com"

RUN apt-get -y update && apt-get -y dist-upgrade && apt-get -y install unzip curl wget libxml2-utils && mkdir /data && groupadd -g 1000 minecraft && useradd -u 1000 -g 1000 -r minecraft

RUN wget -O /opt/bedrock_server.zip https://minecraft.azureedge.net/bin-linux/bedrock-server-1.14.1.4.zip
ADD start.sh /opt/start.sh
RUN chown -R minecraft:minecraft /data && chmod +x /opt/start.sh

USER minecraft:minecraft
RUN cd /data

VOLUME /data
WORKDIR /data

EXPOSE 19132
EXPOSE 19132/udp

CMD ["/opt/start.sh"]
