FROM openjdk:11-jre
MAINTAINER Chris Ruettimann<chris@bitbull.ch>

ENV BLYNK_SERVER_VERSION 0.41.0
RUN mkdir /blynk
RUN curl -L https://github.com/blynkkk/blynk-server/releases/download/v${BLYNK_SERVER_VERSION}/server-${BLYNK_SERVER_VERSION}.jar > /blynk/server.jar
COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat

# Create data folder. To persist data, map a volume to /data
# Create configuration folder. To persist data, map a file to /config/server.properties
RUN mkdir /data
VOLUME ["/data"]

# IP port listing:
# 8080: Hardware without ssl/tls support
# 9443: Blynk app, https, web sockets, admin port
EXPOSE 8080 9443
WORKDIR /data

ENTRYPOINT ["docker-entrypoint.sh"]
# options: start|debug
CMD ["start"]
