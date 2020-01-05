FROM ubuntu:18.04
MAINTAINER Philipp Goellner, philipp.goellner@xaltbc.de

# setup useful environment variables
ENV BACKUP_HOST                 false
ENV BACKUP_PATH                 false
ENV BACKUP_USER                 false
ENV BACKUP_KEY_FILE             /tmp/id_rsa

ENV DEBIAN_FRONTEND             noninteractive
ENV JAVA_HOME                   /opt/jdk

ENV JIRA_VERSION                8.5.1
ENV JIRA_HOME                   /var/atlassian/jira
ENV JIRA_HOME_SHARED            /var/atlassian/jira-shared
ENV JIRA_INSTALL                /opt/atlassian/jira
# set JIRA_NODE_ID to a number to activate this container as JIRA Datacenter Node
ENV JIRA_NODE_ID                false
ENV JIRA_REMOTE_DEBUG           false
ENV JIRA_URL                    https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-${JIRA_VERSION}.tar.gz

ENV HTTPS                       false
ENV IMPORTCERT                  false
ENV IMPORTPATH                  /var/certificates
ENV INSTALL_PLUGINS             false
ENV INSTALL_PLUGINS_URLS_V1     false
ENV INSTALL_PLUGINS_URLS_V2     false
ENV PROXY_NAME                  false
ENV RAM_MIN                     512m
ENV RAM_MAX                     2048m
ENV SESSION_TIMEOUT             43200
ENV DB_MAX_POOL_SIZE            30

ENV MYSQL_DRIVER_VERSION        5.1.36
ENV MYSQL_DRIVER_URL            http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz

ENV LIQUIBASE                   false
ENV LIQUIBASE_VERSION           3.6.2
ENV LIQUIBASE_INSTALL           /opt/liquibase
ENV LIQUIBASE_URL               https://github.com/liquibase/liquibase/releases/download/liquibase-parent-${LIQUIBASE_VERSION}/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz

ENV NEWRELIC_VERSION            current
ENV NEWRELIC_APP_NAME           jira-docker
ENV NEWRELIC_LICENSE            false
ENV NEWRELIC_URL                https://download.newrelic.com/newrelic/java-agent/newrelic-agent/${NEWRELIC_VERSION}/newrelic-java.zip

ENV RUN_USER                    daemon

ENV TIME_ZONE                   false

ENV WAIT                        false
ENV WAIT_COMMAND                none
ENV WAIT_SLEEP                  2
ENV WAIT_LOOPS                  10

RUN apt-get update -qq \
 && apt-get install --no-install-recommends -qq -y gnupg2 \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 \
 && apt-get update -qq \
 && apt-get install --no-install-recommends -qq -y curl \
                                                   libtcnative-1 \
                                                   rsync \
                                                   openssh-client \
                                                   sed \
                                                   tzdata \
                                                   unzip \
                                                   wget \
                                                   xmlstarlet \
 && rm -rf                                         /var/lib/apt/lists/* \
 && mkdir -p                                       "${JIRA_HOME}" \
 && mkdir -p                                       "${JIRA_INSTALL}" \
 && curl -Lsk                                      "${JIRA_URL}" | tar -xz --directory         "${JIRA_INSTALL}" --strip-components=1 \
 && curl -Lsk                                      "${MYSQL_DRIVER_URL}" | tar -xz --directory "${JIRA_INSTALL}/lib" --strip-components=1 --no-same-owner "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar" \
 && mkdir -p                                       "${LIQUIBASE_INSTALL}" \
 && curl -Lsk                                      "${LIQUIBASE_URL}"    | tar -xz --directory "${LIQUIBASE_INSTALL}" \
 && cp "${LIQUIBASE_INSTALL}/sdk/lib-sdk/slf4j-api-1.7.25.jar" "${LIQUIBASE_INSTALL}/lib/" \
 && curl -Lsk                                      "${NEWRELIC_URL}" -o                        /tmp/newrelic-java.zip \
 && unzip /tmp/newrelic-java.zip -d                "${JIRA_INSTALL}" \
 && rm -f /tmp/newrelic-java.zip \
 && echo "jira.home = ${JIRA_HOME}" > ${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-application.properties \
 && mkdir                                          "${IMPORTPATH}" \
 && chown -R ${RUN_USER}:                          "${IMPORTPATH}" \
                                                   "${JIRA_INSTALL}"

COPY changelogs ${LIQUIBASE_INSTALL}/changelogs/
COPY liquibase.properties ${LIQUIBASE_INSTALL}/
COPY setenv.sh ${JIRA_INSTALL}/bin/
COPY configure-and-start-root.sh ${JIRA_INSTALL}/bin/
COPY configure-and-start.sh ${JIRA_INSTALL}/bin/
COPY jdk-8u212-linux-x64.tar.gz                     /tmp
RUN mkdir -p /opt/jdk \
 && tar -xvf /tmp/jdk-8u212-linux-x64.tar.gz -C    "${JAVA_HOME}" --strip-components=1 \
 && rm -f /tmp/jdk-8u212-linux-x64.tar.gz \
 && update-alternatives --install /usr/bin/java  java  "${JAVA_HOME}/bin/java"  100 \
 && update-alternatives --install /usr/bin/javac javac "${JAVA_HOME}/bin/javac" 100 \
 && update-alternatives --display java \
 && update-alternatives --display javac \
 && chmod 500                                       ${JIRA_INSTALL}/bin/configure-and-start*.sh \
 && chown -R ${RUN_USER}:                          "${JIRA_INSTALL}/bin/configure-and-start.sh" \
                                                   "${LIQUIBASE_INSTALL}" \
                                                   "${JAVA_HOME}"

# Remote Debug Port, HTTP Port, Data Center Ehcache Port
EXPOSE 5005 8080 40001

# set volume mount points for home directories
# to have persinstant data after docker container rebuild
VOLUME "${JIRA_HOME}" \
       "${JIRA_HOME_SHARED}"

# Set the default working directory as the installation directory.
WORKDIR ${JIRA_INSTALL}

# Run Atlassian JIRA as a foreground process by default.
ENTRYPOINT ["bin/configure-and-start-root.sh", "-fg"]
