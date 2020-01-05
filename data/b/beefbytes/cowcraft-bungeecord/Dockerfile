FROM openjdk:8u131-jre-alpine
LABEL maintainer="contact@beefbytes.com"

RUN apk add -U \
          openssl \
          lsof \
          su-exec \
          bash \
          curl iputils wget \
          mysql-client \
          vim \
          python python-dev py2-pip && \
        rm -rf /var/cache/apk/*

RUN addgroup -g 1000 mc \
    && adduser -Ss /bin/false -u 1000 -G mc -h /home/mc mc

WORKDIR /home/mc/bungeecord/

USER root
RUN chown -R mc:mc /home/mc \
    && chmod -R 774 /home/mc
USER mc

CMD ["bash", "start.sh"]
