ARG JRE_VERSION=jre11

FROM foyer/base:$JRE_VERSION

ARG MC_VERSION=1.14.4
ARG PAPERMC_VERSION=176
ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.schema-version="1.0.0" \
      org.label-schema.name=paper \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://git.foyer.cool/docker-paper" \
      org.label-schema.vcs-ref=$VCS_REF \
      cool.foyer.minecraft.version=$MC_VERSION \
      cool.foyer.paper.version=$PAPERMC_VERSION

USER root

RUN curl -Lo /usr/libexec/paper.jar https://papermc.io/api/v1/paper/${MC_VERSION}/${PAPERMC_VERSION}/download && chmod 755 /usr/libexec/paper.jar

# pre-download server jars
USER minecraft
RUN java -jar /usr/libexec/paper.jar --version
USER root

ADD paper /bin/paper
CMD [ "paper" ]

USER minecraft

EXPOSE 25565

RUN mkdir /minecraft/worlds /minecraft/config /minecraft/plugins
RUN echo eula=true > /minecraft/eula.txt
ADD log4j2.xml /minecraft

RUN for f in help.yml \
             permissions.yml \
             commands.yml \
             banned-ips.json \
             banned-players.json \
             ops.json \
             usercache.json \
             version_history.json \
             whitelist.json \
             ; \
    do \
        ln -s config/$f /minecraft/$f; \
    done
