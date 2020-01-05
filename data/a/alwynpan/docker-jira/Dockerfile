FROM adoptopenjdk/openjdk8:alpine

ENV JIRA_HOME /var/atlassian/jira
ENV JIRA_INSTALL /opt/atlassian/jira
ENV JIRA_VERSION 8.0.0

ADD assets/ /

RUN set -x \
	&& apk update && apk --no-cache add bash curl fontconfig ttf-dejavu xmlstarlet \
	&& mkdir -p                "${JIRA_HOME}" \
	&& mkdir -p                "${JIRA_HOME}/caches/indexes" \
	&& chmod -R 700            "${JIRA_HOME}" \
	&& chown -R daemon:daemon  "${JIRA_HOME}" \
	&& mkdir -p                "${JIRA_INSTALL}/conf/Catalina" \
	&& curl -Ls                "https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-8.0.0.tar.gz" | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 --no-same-owner \
	&& curl -Ls                "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.38.tar.gz" | tar -xz --directory "${JIRA_INSTALL}/lib" --strip-components=1 --no-same-owner "mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar" \
	&& rm -f                   "${JIRA_INSTALL}/lib/postgresql-9.1-903.jdbc4-atlassian-hosted.jar" \
	&& curl -Ls                "https://jdbc.postgresql.org/download/postgresql-42.2.1.jar" -o "${JIRA_INSTALL}/lib/postgresql-42.2.1.jar" \
	&& chmod -R 700            "${JIRA_INSTALL}/conf" \
	&& chmod -R 700            "${JIRA_INSTALL}/logs" \
	&& chmod -R 700            "${JIRA_INSTALL}/temp" \
	&& chmod -R 700            "${JIRA_INSTALL}/work" \
	&& chown -R daemon:daemon  "${JIRA_INSTALL}/conf" \
	&& chown -R daemon:daemon  "${JIRA_INSTALL}/logs" \
	&& chown -R daemon:daemon  "${JIRA_INSTALL}/temp" \
	&& chown -R daemon:daemon  "${JIRA_INSTALL}/work" \
	&& sed --in-place          "s/java version/openjdk version/g" "${JIRA_INSTALL}/bin/check-java.sh" \
	&& echo -e                 "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-application.properties" \
	&& touch -d "@0"           "${JIRA_INSTALL}/conf/server.xml" \
	&& chmod +x /entrypoint.sh

USER daemon:daemon

EXPOSE 8080

VOLUME ["${JIRA_HOME}", "${JIRA_INSTALL}"]

WORKDIR ${JIRA_HOME}

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/opt/atlassian/jira/bin/start-jira.sh", "-fg"]
