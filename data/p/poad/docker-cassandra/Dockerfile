ARG CASSANDRA_VERSION="3.11.5"
ARG CASSANDRA_ESUM="d559d351309ab4b702975abffae0663ffe6378cf7402c4bcb2f9b2b2f42ac7d017d7aa05f89ee523cab72d89c79d9fbc5ef692dfbb3f56d3993acd1f34cf1285"
ARG ZULU_VERSION="11.35.15"
ARG JAVA_VERSION="11.0.5"
ARG JAVA_SHA256SUM="fd82ffca6ee8f5a6de327ebc1bf98e326d9be2a7483ebafdc30eb126c712bd0e"

ARG CASSANDRA_HOME="/usr/local/cassandra"
ARG JAVA_HOME="/usr/lib/jvm/java-${JAVA_VERSION}-openjdk-amd64"

FROM alpine:3 as Downloader

ARG CASSANDRA_VERSION
ARG CASSANDRA_ESUM
ARG JAVA_SHA256SUM
ARG ZULU_VERSION
ARG JAVA_VERSION
ARG ZULU_ARCH="zulu${ZULU_VERSION}-ca-jre${JAVA_VERSION}-linux_musl_x64.tar.gz"
ARG JAVA_URL="https://cdn.azul.com/zulu/bin/${ZULU_ARCH}"
ARG JAVA_HOME

WORKDIR /tmp

RUN apk --update add --no-cache --virtual .build-deps \
    curl \
 && rm -rf /var/cache/apk/* \
 && curl -sSLo /tmp/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz https://archive.apache.org/dist/cassandra/${CASSANDRA_VERSION}/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz \
 && sha512sum /tmp/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz \
 && echo "${CASSANDRA_ESUM}  /tmp/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz" | sha512sum -c - \
 && tar xf /tmp/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz \
 && rm -rf /tmp/apache-cassandra-${CASSANDRA_VERSION}/doc /tmp/apache-cassandra-${CASSANDRA_VERSION}/javadoc \
 && rm -rf /tmp/apache-cassandra-${CASSANDRA_VERSION}/NOTICE.txt /tmp/apache-cassandra-${CASSANDRA_VERSION}/NEWS.txt \
 && rm -rf /tmp/apache-cassandra-${CASSANDRA_VERSION}/CASSANDRA-14092.txt /tmp/apache-cassandra-${CASSANDRA_VERSION}/CHANGES.txt

ARG TMP_FILE=/tmp/openjdk.tar.gz

ENV JAVA_HOME ${JAVA_HOME}

RUN echo "Download from ${JAVA_URL}" \
 && INSTALL_DIR=$( dirname ${JAVA_HOME} ) \
 && ZULU_DIR=$( basename ${ZULU_ARCH} .tar.gz ) \
 && curl -sSLo ${ZULU_ARCH} ${JAVA_URL} \
 && mkdir -p ${INSTALL_DIR} \
 && echo "${JAVA_URL}" \
 && echo "${JAVA_SHA256SUM}  ${ZULU_ARCH}" | sha256sum -c - \
 && tar -xf ./${ZULU_ARCH} -C ${INSTALL_DIR} \
 && rm -f ${ZULU_ARCH} \
 && mv ${INSTALL_DIR}/${ZULU_DIR} ${JAVA_HOME}


FROM python:3-alpine

LABEL maintainer="Kenji Saito<ken-yo@mbr.nifty.com>"

ARG JAVA_HOME

ENV LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    JAVA_HOME=${JAVA_HOME} \
    PATH=/root/.local/bin:${PATH}:${JAVA_HOME}/bin

ARG BIN_DIR=/usr/bin
ARG MAN_DIR=/usr/share/man/man1

ARG CASSANDRA_VERSION
ARG CASSANDRA_HOME

COPY --from=downloader ${JAVA_HOME} ${JAVA_HOME}
COPY --from=Downloader /tmp/apache-cassandra-${CASSANDRA_VERSION} ${CASSANDRA_HOME}

RUN rm -f ${CASSANDRA_HOME}/conf/jvm.options \
 && rm -f ${CASSANDRA_HOME}/conf/cassandra.yaml

RUN addgroup -g 1000 -S cassandra \
 && adduser -u 1000 -S  cassandra -G cassandra

COPY --chown=cassandra:cassandra assets/conf/cassandra.yaml ${CASSANDRA_HOME}/conf/cassandra.yaml
COPY --chown=root:root assets/conf/jvm.options ${CASSANDRA_HOME}/conf/jvm.options
COPY --chown=cassandra:cassandra assets/docker-entrypoint.sh /docker-entrypoint.sh
COPY --chown=cassandra:cassandra assets/requirements.txt /tmp/requirements.txt
COPY --chown=cassandra:cassandra assets/create_keyspace.py /create_keyspace.py

ENV PATH=${CASSANDRA_HOME}/bin:${CASSANDRA_HOME}/tools/bin:${PATH}

HEALTHCHECK CMD [ "java", "-version" ]

RUN cd ${BIN_DIR} \
 && find ${JAVA_HOME}/bin -type f -perm -a=x -exec ln -s {} . \; \
 && mkdir -p ${MAN_DIR} \
 && cd ${MAN_DIR} \
 && find ${JAVA_HOME}/man/man1 -type f -name "*.1" -exec ln -s {} . \;

RUN mkdir -p /var/lib/cassandra/ \
 && mkdir -p ${CASSANDRA_HOME}/logs \
 && chown -R cassandra:cassandra /var/lib/cassandra/ \
 && chown -R cassandra:cassandra ${CASSANDRA_HOME}/logs/ \
 && chmod 777 /var/lib/cassandra \
 && chmod 774 /docker-entrypoint.sh \
 && chmod 774 /create_keyspace.py

EXPOSE 7000 7001 7199 9042 9160

RUN pip3 install -U pip \
 && pip install -r /tmp/requirements.txt \
 && rm -f /tmp/requirements.txt

USER cassandra

ENV PATH=/home/cassandra/.local/bin:${PATH}

ENV CASSANDRA_HOME="${CASSANDRA_HOME}"
VOLUME /var/lib/cassandra

ENTRYPOINT [ "/docker-entrypoint.sh" ]
