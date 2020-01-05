FROM adoptopenjdk:8u212-b03-jdk-hotspot
LABEL maintainer="sysadmin@flowable.com"

# Setup useful environment variables
ENV JIRA_HOME     /var/atlassian/application-data/jira
ENV JIRA_INSTALL  /opt/atlassian/jira
ENV JIRA_VERSION  7.13.5
ENV JIRA_DOWNLOAD_URL https://product-downloads.atlassian.com/software/jira/downloads/atlassian-jira-core-${JIRA_VERSION}.tar.gz
LABEL Description="This image is used to start Atlassian JIRA" Vendor="Atlassian" Version="${JIRA_VERSION}"

# Use the default unprivileged account. This could be considered bad practice
# on systems where multiple processes end up being executed by 'daemon' but
# here we only ever run one process anyway.
ENV RUN_USER            daemon
ENV RUN_GROUP           daemon

# User configurable environment variables
ENV CHECK_LOCK_FILE=true
ENV CATALINA_CONNECTOR_PROXYNAME=
ENV CATALINA_CONNECTOR_PROXYPORT=
ENV CATALINA_CONNECTOR_SCHEME=

# download requirements
RUN apt-get update -y && \
    apt-get install -y xmlstarlet fontconfig && \
    rm -rf /var/lib/apt/lists/*

# download jira
RUN mkdir -p "${JIRA_HOME}" && \
    chmod -R 700 "${JIRA_HOME}" &&\
    chown ${RUN_USER}:${RUN_GROUP} "${JIRA_HOME}" && \

    mkdir -p "${JIRA_INSTALL}" && \
    curl -Ls "${JIRA_DOWNLOAD_URL}" | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 --no-same-owner && \

    echo -e "\njira.home=${JIRA_HOME}" > "${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-application.properties" && \
    mv "${JIRA_INSTALL}/conf/server.xml" "${JIRA_INSTALL}/conf/server.xml.orig"

# fix permissions on jira install folder
RUN chmod -R 700 "${JIRA_INSTALL}" && \
    chown -R ${RUN_USER}:${RUN_GROUP} "${JIRA_INSTALL}"



# Use the default unprivileged account. This could be considered bad practice
# on systems where multiple processes end up being executed by 'daemon' but
# here we only ever run one process anyway.
#USER ${RUN_USER}:${RUN_GROUP}

# Expose default HTTP connector port.
EXPOSE 8080

# Set the default working directory as the JIRA installation directory.
WORKDIR ${JIRA_INSTALL}

# install the entrypoint
COPY entrypoint /entrypoint
RUN chmod 755 /entrypoint

# start
ENTRYPOINT ["/entrypoint"]
