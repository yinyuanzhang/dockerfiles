FROM java:openjdk-8-jre
MAINTAINER Atlassian Jira

# Setup useful environment variables
ENV JIRA_HOME    /var/atlassian/application-data/jira
ENV JIRA_INSTALL /opt/atlassian/jira
ENV JIRA_VERSION 8.4.3

LABEL Description="This image is used to start Atlassian Jira" Vendor="Atlassian" Version="${JIRA_VERSION}"

ENV JIRA_DOWNLOAD_URL https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-${JIRA_VERSION}.tar.gz
ENV MYSQL_VERSION 5.1.47
ENV MYSQL_DRIVER_DOWNLOAD_URL http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_VERSION}.tar.gz

# Use the default unprivileged account. This could be considered bad practice
# on systems where multiple processes end up being executed by 'daemon' but
# here we only ever run one process anyway.
ENV RUN_USER            daemon
ENV RUN_GROUP           daemon

ADD sources.list /etc/apt/sources.list
RUN rm -rf /etc/apt/sources.list.d/jessie-backports.list

# Install Atlassian Jira and helper tools and setup initial home
# directory structure.
RUN set -x \
    && apt-get update --quiet \
    && apt-get install --quiet --yes --no-install-recommends libtcnative-1 xmlstarlet \
    && apt-get clean \
    && mkdir -p                           "${JIRA_HOME}" \
    && chmod -R 700                       "${JIRA_HOME}" \
    && chown ${RUN_USER}:${RUN_GROUP}     "${JIRA_HOME}" \
    && mkdir -p                           "${JIRA_INSTALL}/conf" \
    && mkdir -p                           "${JIRA_INSTALL}/jira/WEB-INF/lib" \
    && curl -Ls                           "${JIRA_DOWNLOAD_URL}" | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 --no-same-owner \
    && curl -Ls                           "${MYSQL_DRIVER_DOWNLOAD_URL}" | tar -xz --directory "${JIRA_INSTALL}/atlassian-jira/WEB-INF/lib" --strip-components=1 --no-same-owner "mysql-connector-java-${MYSQL_VERSION}/mysql-connector-java-${MYSQL_VERSION}.jar" \
    && chmod -R 700                       "${JIRA_INSTALL}/conf" \
    && chmod -R 700                       "${JIRA_INSTALL}/temp" \
    && chmod -R 700                       "${JIRA_INSTALL}/logs" \
    && chmod -R 700                       "${JIRA_INSTALL}/work" \
    && chown -R ${RUN_USER}:${RUN_GROUP}  "${JIRA_INSTALL}/conf" \
    && chown -R ${RUN_USER}:${RUN_GROUP}  "${JIRA_INSTALL}/temp" \
    && chown -R ${RUN_USER}:${RUN_GROUP}  "${JIRA_INSTALL}/logs" \
    && chown -R ${RUN_USER}:${RUN_GROUP}  "${JIRA_INSTALL}/work" \
    && echo -e                            "\njira.home=${JIRA_HOME}" >> "${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-init.properties"

# Use the default unprivileged account. This could be considered bad practice
# on systems where multiple processes end up being executed by 'daemon' but
# here we only ever run one process anyway.
USER ${RUN_USER}:${RUN_GROUP}

# Expose default HTTP connector port.
EXPOSE 8080

# Set volume mount points for installation and home directory. Changes to the
# home directory needs to be persisted as well as parts of the installation
# directory due to eg. logs.
VOLUME ["${JIRA_INSTALL}", "${JIRA_HOME}"]

# Set the default working directory as the Jira installation directory.
WORKDIR ${JIRA_INSTALL}

# Run Atlassian Jira as a foreground process by default.
CMD ["./bin/catalina.sh", "run"]
