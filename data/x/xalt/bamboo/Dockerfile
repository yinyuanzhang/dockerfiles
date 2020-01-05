FROM ubuntu:18.04
MAINTAINER Philipp Goellner, philipp.goellner@xaltbc.de

# setup useful environment variables
ENV BACKUP_HOST                                    false
ENV BACKUP_KEY_FILE                                /tmp/id_rsa
ENV BACKUP_PATH                                    false
ENV BACKUP_USER                                    false

ENV BAMBOO_VERSION                                 6.5.0
ENV BAMBOO_HOME                                    /var/atlassian/bamboo
ENV BAMBOO_INSTALL                                 /opt/atlassian/bamboo
ENV BAMBOO_REMOTE_DEBUG                            false
ENV BAMBOO_URL                                     https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-${BAMBOO_VERSION}.tar.gz

ENV DEBIAN_FRONTEND                                noninteractive
ENV JAVA_HOME                                      /opt/jdk

ENV DEBUG_PORT                                     5005
ENV HTTPS                                          false
ENV IMPORTCERT                                     false
ENV IMPORTPATH                                     /var/certificates
ENV PROXY_NAME                                     false
ENV RAM_MIN                                        1024
ENV RAM_MAX                                        2048
ENV SESSION_TIMEOUT                                43200

ENV LIQUIBASE                                      false
ENV LIQUIBASE_VERSION                              3.6.2
ENV LIQUIBASE_INSTALL                              /opt/liquibase
ENV LIQUIBASE_URL                                  https://github.com/liquibase/liquibase/releases/download/liquibase-parent-${LIQUIBASE_VERSION}/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz

ENV MYSQL_DRIVER_VERSION                           5.1.36
ENV MYSQL_DRIVER_URL                               http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz

ENV NEWRELIC_VERSION                               current
ENV NEWRELIC_APP_NAME                              bamboo-docker
ENV NEWRELIC_LICENSE                               false
ENV NEWRELIC_URL                                   https://download.newrelic.com/newrelic/java-agent/newrelic-agent/${NEWRELIC_VERSION}/newrelic-java.zip

ENV RUN_USER                                       daemon
ENV RUN_GROUP                                      daemon

ENV TIME_ZONE                                      false

ENV WAIT                                           false
ENV WAIT_COMMAND                                   none
ENV WAIT_SLEEP                                     2
ENV WAIT_LOOPS                                     10

# Install Java, git, other dependencies, download and extract Bamboo and create the required directory layout.
RUN apt-get update -qq \
 && apt-get install --no-install-recommends -qq -y gnupg2 \
                                                   lsb-release \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 \
 && apt-get update -qq \
 && apt-get install --no-install-recommends -qq -y curl \
                                                   git \
                                                   openssh-client \
                                                   rsync \
                                                   sed \
                                                   tzdata \
                                                   unzip \
                                                   xmlstarlet \
 && rm -rf                                         /var/lib/apt/lists/* \
 && mkdir -p                                       "${BAMBOO_INSTALL}" \
 && curl -Lsk                                      "${BAMBOO_URL}"       | tar -xz --directory "${BAMBOO_INSTALL}"     --strip-components=1 \
 && curl -Lsk                                      "${MYSQL_DRIVER_URL}" | tar -xz --directory "${BAMBOO_INSTALL}/lib" --strip-components=1 --no-same-owner "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar" \
 && mkdir -p                                       "${LIQUIBASE_INSTALL}" \
 && curl -Lsk                                      "${LIQUIBASE_URL}"    | tar -xz --directory "${LIQUIBASE_INSTALL}" \
 && cp "${LIQUIBASE_INSTALL}/sdk/lib-sdk/slf4j-api-1.7.25.jar" "${LIQUIBASE_INSTALL}/lib/" \
 && curl -Lsk                                      "${NEWRELIC_URL}" -o                        /tmp/newrelic-java.zip \
 && unzip /tmp/newrelic-java.zip -d                "${BAMBOO_INSTALL}" \
 && rm -f /tmp/newrelic-java.zip \
 && mkdir                                          "${IMPORTPATH}" \
 && chown -R ${RUN_USER}:${RUN_GROUP}              "${IMPORTPATH}" \
                                                   "${BAMBOO_INSTALL}"

COPY changelogs                                    "${LIQUIBASE_INSTALL}/changelogs/"
COPY liquibase.properties                          "${LIQUIBASE_INSTALL}/"
COPY configure-and-start-root.sh                   "${BAMBOO_INSTALL}/bin/"
COPY configure-and-start.sh                        "${BAMBOO_INSTALL}/bin/"
COPY jdk-8u212-linux-x64.tar.gz                     /tmp
RUN mkdir -p /opt/jdk \
 && tar -xvf /tmp/jdk-8u212-linux-x64.tar.gz -C    "${JAVA_HOME}" --strip-components=1 \
 && rm -f /tmp/jdk-8u212-linux-x64.tar.gz \
 && update-alternatives --install /usr/bin/java  java  "${JAVA_HOME}/bin/java"  100 \
 && update-alternatives --install /usr/bin/javac javac "${JAVA_HOME}/bin/javac" 100 \
 && update-alternatives --display java \
 && update-alternatives --display javac \
 && chmod 500                                       ${BAMBOO_INSTALL}/bin/configure-and-start*.sh \
 && chown -R ${RUN_USER}:${RUN_GROUP}              "${BAMBOO_INSTALL}/bin/configure-and-start.sh" \
                                                   "${LIQUIBASE_INSTALL}" \
                                                   "${JAVA_HOME}"

# HTTP Port, Bamboo Agent Port
EXPOSE 8085 54663

VOLUME ["${BAMBOO_HOME}"]

WORKDIR ${BAMBOO_INSTALL}

# Run in foreground
ENTRYPOINT ["./bin/configure-and-start-root.sh"]
