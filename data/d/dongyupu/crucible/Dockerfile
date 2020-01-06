FROM openjdk:8

USER root

ARG CRUCIBLE_VERSION=4.7.2

ENV FISHEYE_INST=/var/atlassian/crucible \
    CRUCIBLE_INSTALL=/opt/atlassian/crucible

RUN export POSTGRESQL_DRIVER_VERSION=9.4.1207 && \
    wget -O /tmp/crucible.zip https://www.atlassian.com/software/crucible/downloads/binary/crucible-${CRUCIBLE_VERSION}.zip && \
    unzip /tmp/crucible.zip -d /tmp && \
    mv /tmp/fecru-${CRUCIBLE_VERSION} /tmp/crucible && \
    mkdir -p /var/atlassian/crucible && \
    mkdir -p /opt/atlassian && \
    mv /tmp/crucible /opt/atlassian/crucible && \
    # Install database drivers
    wget -O ${CRUCIBLE_INSTALL}/lib/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar                                       \
      https://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar && \
    # Clean caches and tmps
    rm -rf /tmp/*

WORKDIR /var/atlassian/crucible
VOLUME ["/var/atlassian/crucible"]
EXPOSE 8060

CMD ["/opt/atlassian/crucible/bin/run.sh", "-fg"]
