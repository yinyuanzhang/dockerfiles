FROM ubuntu:latest
LABEL maintainer="Philipp Goellner <philipp.goellner@xaltbc.de>"

ENV RESET                   false

ENV BACKUP_HOST             false
ENV BACKUP_PATH             false
ENV BACKUP_USER             false
ENV BACKUP_KEY_FILE         /tmp/id_rsa

ENV DEBIAN_FRONTEND         noninteractive
ENV JAVA_HOME               /opt/jdk

ENV CONF_VERSION            6.15.10
ENV CONF_HOME               /var/atlassian/confluence
ENV CONF_HOME_SHARED        /var/atlassian/confluence-shared
ENV CONF_INSTALL            /opt/atlassian/confluence
ENV CONF_URL                http://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-${CONF_VERSION}.tar.gz

#####
# Confluence Plugin support
#####
ENV VIEWPORT                false

ENV MYSQL_DRIVER_VERSION    5.1.38
ENV MYSQL_DRIVER_URL        http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz

ENV OVERWRITE_DB_URL        false
ENV OVERWRITE_DB_USER       false
ENV OVERWRITE_DB_PASSWORD   false

ENV CONF_REMOTE_DEBUG       false
ENV DATA_CENTER_CONFIG      false
ENV DATA_CENTER_DNS_SUFFIX  false
ENV DATA_CENTER_IP_LIST     false
ENV DATA_CENTER_IPS         false
ENV DATA_CENTER             false

ENV DEBUG_PORT              5005
ENV HTTPS                   false
ENV IMPORTCERT              false
ENV IMPORTPATH              /var/certificates
ENV PROXY_NAME              false
ENV RAM_MIN                 1024
ENV RAM_MAX                 2048
ENV SESSION_TIMEOUT         43200

ENV LIQUIBASE               false
ENV LIQUIBASE_VERSION       3.6.2
ENV LIQUIBASE_INSTALL       /opt/liquibase
ENV LIQUIBASE_URL           https://github.com/liquibase/liquibase/releases/download/liquibase-parent-${LIQUIBASE_VERSION}/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz

ENV NEWRELIC_VERSION        4.12.1
ENV NEWRELIC_APP_NAME       confluence-docker
ENV NEWRELIC_LICENSE        false
ENV NEWRELIC_URL            https://download.newrelic.com/newrelic/java-agent/newrelic-agent/${NEWRELIC_VERSION}/newrelic-java.zip

ENV RUN_USER                daemon

ENV TIME_ZONE               false

ENV WAIT                    false
ENV WAIT_COMMAND            none
ENV WAIT_SLEEP              3
ENV WAIT_LOOPS              10

RUN apt-get update --quiet \
 && apt-get install --quiet --no-install-recommends -y \
        gnupg2 \
        lsb-release \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 \
 && apt-get update --quiet \
 && apt-get install --quiet --no-install-recommends -y \
        curl \
        libtcnative-1 \
        openssh-client \
        rsync \
        sed \
        tzdata \
        unzip \
        wget \
        xmlstarlet \
        postgresql-client \
        cron \
 && rm -rf                                   /var/lib/apt/lists/* \
 && mkdir -p                                 "${CONF_HOME}" \
 && chown -R ${RUN_USER}:${RUN_GROUP}        "${CONF_HOME}" \
 && mkdir -p                                 "${CONF_INSTALL}" \
 && curl -Lsk                                "${CONF_URL}" | tar -xz --directory "${CONF_INSTALL}" --strip-components=1 \
 && curl -Lsk                                "${MYSQL_DRIVER_URL}" | tar -xz --directory "${CONF_INSTALL}/confluence/WEB-INF/lib" --strip-components=1 --no-same-owner "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar" \
 && mkdir -p                                 "${LIQUIBASE_INSTALL}" \
 && curl -Lsk                                "${LIQUIBASE_URL}"    | tar -xz --directory "${LIQUIBASE_INSTALL}" \
 && cp "${LIQUIBASE_INSTALL}/sdk/lib-sdk/slf4j-api-1.7.25.jar" "${LIQUIBASE_INSTALL}/lib/" \
 && curl -Lsk                                "${NEWRELIC_URL}" -o /tmp/newrelic-java.zip \
 && unzip /tmp/newrelic-java.zip -d          "${CONF_INSTALL}" \
 && rm -f /tmp/newrelic-java.zip \
 && echo -e                                  "\nconfluence.home=${CONF_HOME}" >> "${CONF_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties" \
 && xmlstarlet                               ed --inplace \
        --delete                             "Server/@debug" \
        --delete                             "Server/Service/Connector/@debug" \
        --delete                             "Server/Service/Connector/@minProcessors" \
        --delete                             "Server/Service/Connector/@maxProcessors" \
        --delete                             "Server/Service/Connector/@useURIValidationHack" \
        --delete                             "Server/Service/Engine/@debug" \
        --delete                             "Server/Service/Engine/Host/@debug" \
        --delete                             "Server/Service/Engine/Host/Context/@debug" \
                                             "${CONF_INSTALL}/conf/server.xml" \
 && sed -ri "s/-Xms1024m -Xmx1024m//"        "${CONF_INSTALL}/bin/setenv.sh" \
 && mkdir -p                                 "${CONF_INSTALL}/conf/Standalone" \
 && chmod -R 777                             "${CONF_INSTALL}" \
 && chown -R ${RUN_USER}:                    "${CONF_INSTALL}" \
 && mkdir                                    "${IMPORTPATH}"

COPY changelogs_mysql                        "${LIQUIBASE_INSTALL}/changelogs_mysql/"
COPY changelogs_postgres                     "${LIQUIBASE_INSTALL}/changelogs_postgres/"
COPY liquibase.properties                    "${LIQUIBASE_INSTALL}/"
COPY check-status.sh                         "${CONF_INSTALL}/bin/"
COPY configure-and-start-root.sh             "${CONF_INSTALL}/bin/"
COPY configure-and-start.sh                  "${CONF_INSTALL}/bin/"
COPY scripts/online-backup.sh                "${CONF_INSTALL}/bin/"
COPY scripts/restore.sh                      "${CONF_INSTALL}/bin/" 
COPY jdk-8u212-linux-x64.tar.gz               /tmp
RUN mkdir -p /opt/jdk \
 && tar -xvf /tmp/jdk-8u212-linux-x64.tar.gz -C        "${JAVA_HOME}" --strip-components=1 \
 && rm -f /tmp/jdk-8u212-linux-x64.tar.gz \
 && update-alternatives --install /usr/bin/java  java  "${JAVA_HOME}/bin/java"  100 \
 && update-alternatives --install /usr/bin/javac javac "${JAVA_HOME}/bin/javac" 100 \
 && update-alternatives --display java \
 && update-alternatives --display javac \
 && chmod 500                                 ${CONF_INSTALL}/bin/configure-and-start*.sh \
 && chown -R ${RUN_USER}:                    "${CONF_INSTALL}/bin/configure-and-start.sh" \
                                             "${LIQUIBASE_INSTALL}"

# expose default ``Atlassian Confluence`` Remote Debug Target port
EXPOSE 5005

# expose default ``Atlassian Confluence Data Center`` Hazelcast port
EXPOSE 5801

# expose default ``Atlassian Confluence`` HTTP port
EXPOSE 8090

# expose default ``Atlassian Confluence`` Synchrony port
EXPOSE 8091

# set volume mount points for installation and home directory
VOLUME ["${CONF_HOME}"]

# Set the default working directory as the installation directory.
WORKDIR ${CONF_INSTALL}

# Run Atlassian Confluence as a foreground process by default.
ENTRYPOINT ["bin/configure-and-start-root.sh"]
