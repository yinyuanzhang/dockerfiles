FROM openjdk:8u201-jre-alpine

LABEL maintainer="Nicolas.F <nicolas.f@n-agency.fr>"

ARG PAPERMC_VERSION=1.8.8
ARG PAPERMC_BUILD=443
ARG PAPERMC_DOWNLOAD_URL=https://papermc.io/ci/job/Paper/${PAPERMC_BUILD}/artifact/Paperclip.jar

RUN apk --update add bash && apk --no-cache add dos2unix wget curl

WORKDIR /paper/server

RUN mkdir -p /opt/{scripts}
RUN mkdir -p /{paper/{config/,server/{plugins,logs}}}

VOLUME ["/paper/config", "/paper/server/logs", "/paper/server/plugins"]

EXPOSE 25565

ADD $PAPERMC_DOWNLOAD_URL /paper/paper.jar

COPY scripts/* /opt/scripts/

COPY files/bukkit.yml /paper/config/bukkit.yml
COPY files/paper.yml /paper/config/paper.yml
COPY files/spigot.yml /paper/config/spigot.yml
COPY files/server.properties /paper/config/server.properties

RUN dos2unix /opt/scripts/* && chmod +x /opt/scripts/*

ENTRYPOINT ["/opt/scripts/docker-entrypoint.sh"]