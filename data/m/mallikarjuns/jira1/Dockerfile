FROM openjdk:8
# Configuration variables.
ENV JIRA_HOME /var/atlassian/jira
ENV JIRA_INSTALL /opt/atlassian/jira
ENV JIRA_VERSION 7.3.6
# Install Atlassian JIRA and helper tools and setup initial home
# directory structure.
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
RUN apt-get update --quiet
RUN apt-get install --quiet --yes --no-install-recommends xmlstarlet
RUN apt-get install --quiet --yes --no-install-recommends -t jessie-backports libtcnative-1
RUN apt-get clean
RUN mkdir -p "${JIRA_HOME}"
RUN mkdir -p "${JIRA_HOME}/caches/indexes"
RUN chmod -R 700 "${JIRA_HOME}"
RUN mkdir -p "${JIRA_INSTALL}/conf/Catalina"
RUN curl -Ls "https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-core-${JIRA_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 --no-same-owner
RUN curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.38.tar.gz" | tar -xz --directory "${JIRA_INSTALL}/lib" --strip-components=1 --no-same-owner "mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar"
RUN sed --in-place "s/java version/openjdk version/g" "${JIRA_INSTALL}/bin/check-java.sh"
RUN touch -d "@0" "${JIRA_INSTALL}/conf/server.xml"

VOLUME ["/var/atlassian/jira", "/opt/atlassian/jira/logs"]
WORKDIR /var/atlassian/jira
ADD build/server.xml /opt/atlassian/jira/conf
COPY "docker-entrypoint.sh" "/"
#ENTRYPOINT ["/docker-entrypoint.sh"]
RUN chmod +x /docker-entrypoint.sh
EXPOSE 8082
#CMD ["/opt/atlassian/jira/bin/catalina.sh", "run"]
CMD bash
