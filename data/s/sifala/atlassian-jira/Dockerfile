#FROM openjdk:8-alpine
FROM adoptopenjdk/openjdk8:alpine-jre

# Configuration variables.
ENV JIRA_HOME     /var/atlassian/jira
ENV JIRA_INSTALL  /opt/atlassian/jira
ENV JAVA_HOME     /opt/java/adoptopenjdk
ENV JIRA_VERSION  8.4.2

# Install Atlassian JIRA and helper tools and setup initial home
# directory structure.
RUN set -x \
    && apk                     update \
    && apk add --no-cache curl xmlstarlet bash ttf-dejavu tomcat-native \
    && addgroup -S             jira \
    && adduser -u 5472 -S      jira -G jira \
    && mkdir -p                "${JAVA_HOME}" \
    && mkdir -p                "${JIRA_HOME}" \
    && chmod -R 700            "${JIRA_HOME}" \
    && mkdir -p                "${JIRA_INSTALL}/logs" \
    && chmod -R 700            "${JIRA_INSTALL}/logs" \
    && chown -R daemon:daemon  "${JIRA_INSTALL}/logs" \
    && curl -Ls                "https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u222-b10/OpenJDK8U-jdk_x64_linux_hotspot_8u222b10.tar.gz" | tar -xz --directory "${JAVA_HOME}" --strip-components=1 \
    && curl -Ls                "https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-${JIRA_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 \
    && curl -Ls                "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.45.tar.gz" | tar -xz --directory "${JIRA_INSTALL}/lib" --strip-components=1 --no-same-owner "mysql-connector-java-5.1.45/mysql-connector-java-5.1.45-bin.jar" \
    && rm -f                   "${JIRA_INSTALL}/lib/postgresql-9.1-903.jdbc4-atlassian-hosted.jar" \
    && curl -Ls                "https://jdbc.postgresql.org/download/postgresql-42.2.1.jar" -o "${JIRA_INSTALL}/lib/postgresql-42.2.1.jar" \
    && echo -e                 "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-application.properties" \
    && echo -e                 "\nexport PATH="${JAVA_HOME}/bin:$PATH"" >> "/home/jira/.bashrc" \
    && touch -d "@0"           "${JIRA_INSTALL}/conf/server.xml" \
    && chown -R jira:jira      "${JAVA_HOME}" \
    && chown -R jira:jira      "${JIRA_INSTALL}" \
    && chown -R jira:jira      "${JIRA_HOME}"


COPY "dbconfig.xml" "/"

RUN chown jira:jira "/dbconfig.xml"

# Use jira unprivileged account. 
USER jira:jira

VOLUME ["/var/atlassian/jira", "/opt/atlassian/jira/logs"]

# Set the default working directory as the installation directory.
WORKDIR /var/atlassian/jira

COPY "docker-entrypoint.sh" "/"
ENTRYPOINT ["/docker-entrypoint.sh"]

# Run Atlassian JIRA as a foreground process by default.
CMD ["/opt/atlassian/jira/bin/start-jira.sh", "-fg"]
