# references
# https://github.com/eliotjordan/docker-geoserver
# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
# https://docs.geoserver.org/stable/en/user/installation/linux.html
# http://docs.geonode.org/en/master/tutorials/advanced/geonode_production/adv_gsconfig/gsproduction.html

FROM ubuntu:18.04

ENV GS_VERSION=2.14.5
ARG GS_ARCHIVE_FILENAME=geoserver-${GS_VERSION}-bin.zip
ARG GS_URL=https://downloads.sourceforge.net/project/geoserver/GeoServer/${GS_VERSION}/${GS_ARCHIVE_FILENAME}
# for correct cpu/memory detection inside a container
ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap"
ENV GEOSERVER_HOME=/opt/geoserver
ENV GEOSERVER_DATA_DIR=/opt/geoserver/data_dir

WORKDIR /tmp

COPY startup-geoserver-base.sh /startup-geoserver-base.sh

RUN groupadd --gid 999 geoserver \
    && useradd --no-create-home --shell /bin/false --uid 999 --gid geoserver geoserver \
    && apt-get update && apt-get install -y \
        wget \
        unzip \
        openjdk-8-jre-headless \
    # install Microsoft core fonts
    && echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections \
    && apt-get install -y ttf-mscorefonts-installer \
    # download and extract geoserver archive
    && wget "$GS_URL" \
    && unzip "$GS_ARCHIVE_FILENAME" \
    && mkdir -p "/opt" \
    && mv "geoserver-$GS_VERSION" "$GEOSERVER_HOME" \
    && chmod +x "${GEOSERVER_HOME}/bin/startup.sh" \
    && chown -R geoserver:geoserver "${GEOSERVER_HOME}" \
    # clean up
    && rm "$GS_ARCHIVE_FILENAME" \
    && apt-get purge -y \
        wget \
        unzip \
    && rm -rf /var/lib/apt/lists/*

USER geoserver

EXPOSE 8080
ENTRYPOINT ["/startup-geoserver-base.sh"]
