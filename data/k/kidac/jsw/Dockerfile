FROM adoptopenjdk/openjdk8:alpine-slim

LABEL de.kdac.jsw.maintainer = "Claus Böhmer" \
      de.kdac.jsw.authors = "eso@bistum-eichstaett.de" \
      de.kdac.jsw.url = "https://hub.docker.com/r/kidac/jsw" \
      de.kdac.jsw.documentation = "https://hub.docker.com/r/kidac/jsw" \
      de.kdac.jsw.source = "https://github.com/kidac/jsw" \
      de.kdac.jsw.version = "8.5.1" \
      de.kdac.jsw.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.jsw.licenses = "https://www.atlassian.com/legal/software-license-agreement, https://www.atlassian.com/legal/privacy-policy" \
      de.kdac.jsw.title = "Atlassian Jira Software (KDAC Version)" \
      de.kdac.jsw.description = "Adapted Atlassians Jira Software Dockerfile used by https://ews.kdac.de"

ENV RUN_USER=daemon \
    RUN_GROUP=daemon \
    JIRA_HOME=/var/atlassian/application-data/jira \
    JIRA_INSTALL_DIR=/opt/atlassian/jira \
    LD_LIBRARY_PATH=/usr/lib

VOLUME ["${JIRA_HOME}"]

EXPOSE 8080 8081

WORKDIR $JIRA_HOME

CMD ["/entrypoint.sh", "-fg"]
ENTRYPOINT ["/sbin/tini", "--"]

RUN apk --no-cache upgrade \
 && apk add --no-cache bash curl ghostscript motif ttf-dejavu tini \
 && fc-cache -f

COPY entrypoint.sh /entrypoint.sh

ARG JIRA_VERSION=8.5.1
ARG DOWNLOAD_URL=https://product-downloads.atlassian.com/software/jira/downloads/atlassian-jira-software-${JIRA_VERSION}.tar.gz

RUN mkdir -p ${JIRA_INSTALL_DIR} \
 && curl -jkSL ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C "$JIRA_INSTALL_DIR" \
 && chown -R ${RUN_USER}:${RUN_GROUP} ${JIRA_INSTALL_DIR}/ \
 && sed -i -e 's/port="8080"/port="8080" secure="${catalinaConnectorSecure}" scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}" proxyPort="${catalinaConnectorProxyPort}"/' ${JIRA_INSTALL_DIR}/conf/server.xml \
 && sed -i -e 's/Context path=""/Context path="${catalinaContextPath}"/' ${JIRA_INSTALL_DIR}/conf/server.xml \
 && ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so \
 && ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 \
 && ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1 \
 && sed -i -e 's/^JVM_SUPPORT_RECOMMENDED_ARGS=""$/: \${JVM_SUPPORT_RECOMMENDED_ARGS:=""}/g' ${JIRA_INSTALL_DIR}/bin/setenv.sh \
 && sed -i -e 's/^JVM_\(.*\)_MEMORY="\(.*\)"$/: \${JVM_\1_MEMORY:=\2}/g' ${JIRA_INSTALL_DIR}/bin/setenv.sh \
 && sed -i -e 's/grep "java version"/grep -E "(openjdk|java) version"/g' ${JIRA_INSTALL_DIR}/bin/check-java.sh
