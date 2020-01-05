FROM openjdk:11.0.3

ARG liquibase_version=3.6.3
ARG liquibase_download_url=https://github.com/liquibase/liquibase/releases/download/liquibase-parent-${liquibase_version}
ARG tarfile=liquibase-${liquibase_version}-bin.tar.gz

WORKDIR /workspace

ENV DERBY_PORT=${DERBY_PORT:-1527}\
    LIQUIBASE_CLASSPATH=${LIQUIBASE_CLASSPATH:-/opt/jdbc-driver/derbytools.jar}\
    LIQUIBASE_CHANGELOGFILE=${LIQUIBASE_CHANGELOGFILE:-changelog.xml}\
    DERBY_PORT=${DERBY_PORT:-1527}\
    DERBY_HOST=${DERBY_HOST:-localhost}\
    DERBY_DB=${DERBY_DB:-dbtest}\
    LIQUIBASE_DEFAULTSCHEMA=${LIQUIBASE_DEFAULTSCHEMA:-app}

ADD ${liquibase_download_url}/${tarfile} /tmp/${tarfile}
ADD http://mirrors.ae-online.de/apache//db/derby/db-derby-10.15.1.3/db-derby-10.15.1.3-bin.tar.gz /tmp/db-derby-10.15.1.3-bin.tar.gz
ADD run.sh /run.sh

RUN mkdir -p /opt/liquibase && \
    chmod +x /run.sh && \
    tar -xzf /tmp/${tarfile} -C /opt/liquibase/ && \
    tar -xzf /tmp/db-derby-10.15.1.3-bin.tar.gz -C /tmp/  && \
    mkdir /opt/jdbc-driver/ -p && \
    cp /tmp/db-derby-10.15.1.3-bin/lib/derby* /opt/jdbc-driver/ && \
    rm /opt/jdbc-driver/derbyLocale_* && \
    chmod +x /opt/liquibase/liquibase && \
    rm /tmp/${tarfile} /tmp/db-derby-10.15.1.3-bin.tar.gz /tmp/db-derby-10.15.1.3-bin -Rf && \
    ln -s /opt/liquibase/liquibase /usr/local/bin/liquibase

ENTRYPOINT [ "/run.sh" ]
