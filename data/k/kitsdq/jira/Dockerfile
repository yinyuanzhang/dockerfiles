# Use AdoptOpenJDK because it is officially supported by Atlassian
FROM adoptopenjdk/openjdk11:alpine-jre

# Install dependencies
RUN apk add --no-cache gzip bash fontconfig ttf-dejavu

# Add JIRA user
RUN adduser -D -u 1432 jira

# Define JIRA home
ENV JIRA_INSTALL=/opt/jira
ENV JIRA_HOME=/var/jira

# Install JIRA including MySQL connector according to
# https://confluence.atlassian.com/adminjiraserver/installing-jira-applications-on-linux-from-archive-file-938846844.html
RUN VERSION=8.6.0 && \
    MYSQL_CONNECTOR_VERSION=5.1.47 && \
    mkdir $JIRA_INSTALL $JIRA_HOME && \
    wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-$VERSION.tar.gz -O /tmp/jira.tar.gz && \
    tar -xzf /tmp/jira.tar.gz -C $JIRA_INSTALL --strip 1 && \
    rm /tmp/jira.tar.gz && \
    wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-$MYSQL_CONNECTOR_VERSION.tar.gz -O /tmp/mysql-connector.tar.gz && \
    tar -zxf /tmp/mysql-connector.tar.gz -C $JIRA_INSTALL/lib --strip 1 "mysql-connector-java-$MYSQL_CONNECTOR_VERSION/mysql-connector-java-$MYSQL_CONNECTOR_VERSION-bin.jar" && \
    rm /tmp/mysql-connector.tar.gz && \
    sed -i "s#jira.home[[:space:]]*=[[:space:]]*#jira.home=$JIRA_HOME#g" $JIRA_INSTALL/atlassian-jira/WEB-INF/classes/jira-application.properties && \
    chown -R jira $JIRA_INSTALL/conf $JIRA_INSTALL/logs $JIRA_INSTALL/temp $JIRA_INSTALL/work && \
    chmod -R u=rwx,go-rwx $JIRA_INSTALL/conf $JIRA_INSTALL/logs $JIRA_INSTALL/temp $JIRA_INSTALL/work && \
    chown -R jira $JIRA_HOME && \
    chmod -R u=rwx,go-rwx $JIRA_HOME && \
    VERSION=

# Set executing user to jira
USER jira

# Set working dir to installation dir
WORKDIR "$JIRA_INSTALL"

# Define volume for home dir
VOLUME ["$JIRA_HOME"]

# Expose default port
EXPOSE 8080

# Set start command to launch JIRA in foreground
CMD ["bin/start-jira.sh", "-fg"]
