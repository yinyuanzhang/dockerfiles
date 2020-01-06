# Setting packages version
ARG OPENJDK_VERSION="13"

FROM library/openjdk:$OPENJDK_VERSION-alpine

LABEL maintainer="Gerardo Junior <me@gerardo-junior.com>"
LABEL url="https://github.com/gerardo-junior/datomic-docker.git"

ENV DATOMIC_PATH /opt/datomic
ENV DATOMIC_PORT 4334

WORKDIR /tmp

ARG DATOMIC_VERSION="0.9.5703"
ARG DATOMIC_SHA256="22b83d1f2baefaee3e7941ad57df6d77635c3fdbc02a37bdb1cc281d9e7bb3a8"
ARG DATOMIC_SOURCE_URL="https://my.datomic.com/downloads/free"
RUN set -xe && \
    wget ${DATOMIC_SOURCE_URL}/${DATOMIC_VERSION} && \
    if [ -n "$DATOMIC_SHA256" ]; then \
	    echo "${DATOMIC_SHA256}  ${DATOMIC_VERSION}" | sha256sum -c - \
    ; fi
    
RUN set -xe && \
    mkdir -p ${DATOMIC_PATH} && \
    unzip ${DATOMIC_VERSION} && \   
    rm ${DATOMIC_VERSION} && \
    mv /tmp/datomic-free-${DATOMIC_VERSION}/* ${DATOMIC_PATH} && \
    cd ${DATOMIC_PATH} && \
    mkdir -p /run/datomic && \
    cp config/samples/free-transactor-template.properties transactor.properties && \
    sed "s/data-dir=data/data-dir=\/run\/datomic/1" -i transactor.properties && \
    sed "s/log-dir=log/log-dir=\/proc\/self\/fd/1" -i transactor.properties && \
    sed "s/host=localhost/host=0.0.0.0/" -i transactor.properties

COPY ./tools /opt/tools
RUN chmod -R +x /opt/tools/

# Setting project directory
VOLUME [$DATOMIC_PATH, "/run/datomic"]
WORKDIR $DATOMIC_PATH
EXPOSE $DATOMIC_PORT 4335 4336
ENTRYPOINT ["/bin/sh" , "/opt/tools/entrypoint.sh"]
