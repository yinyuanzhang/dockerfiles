FROM anapsix/alpine-java:8u201b09_jdk

MAINTAINER draca <info@draca.be>

ARG JIRA_VERSION=3.14.2
ARG JIRA_DOWNLOAD=https://www.atlassian.com/software/jira/downloads/binary/atlassian-servicedesk-3.14.2.tar.gz

ENV JIRA_HOME=/opt/atlassian/jira/data
ENV JIRA_INSTALL=/opt/atlassian/jira/install
ENV JIRA_CERTS=/opt/atlassian/jira/certs

ENV RUN_USER=jira
ENV RUN_GROUP=jira

EXPOSE 8080

WORKDIR $JIRA_HOME

RUN apk add --no-cache curl tar shadow tzdata \
    && groupadd -r ${RUN_GROUP} \
    && useradd -d "${JIRA_HOME}" -r -g ${RUN_GROUP} ${RUN_USER} \
    && mkdir -p "${JIRA_HOME}" "${JIRA_INSTALL}" "${JIRA_CERTS}" \
    && curl -Ls ${JIRA_DOWNLOAD} | tar -xz --directory "${JIRA_INSTALL}" --strip-components=1 --no-same-owner \
    && echo -e "\njira.home=${JIRA_HOME}" >> "${JIRA_INSTALL}/atlassian-jira/WEB-INF/classes/jira-application.properties" \
    && apk del curl tar shadow \
    && chown -R ${RUN_USER}:${RUN_GROUP} "${JIRA_HOME}" "${JIRA_INSTALL}" "${JIRA_CERTS}"


COPY "entrypoint.sh" "/"
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/opt/atlassian/jira/install/bin/start-jira.sh", "-fg"]