FROM adoptopenjdk/openjdk8-openj9:alpine-slim

LABEL de.kdac.confluence.maintainer = "Claus Böhmer" \
      de.kdac.confluence.authors = "eso@bistum-eichstaett.de" \
      de.kdac.confluence.url = "https://hub.docker.com/r/kidac/confluence" \
      de.kdac.confluence.documentation = "https://hub.docker.com/r/kidac/confluence" \
      de.kdac.confluence.source = "https://github.com/kidac/confluence" \
      de.kdac.confluence.version = "6.13.9" \
      de.kdac.confluence.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.confluence.licenses = "https://www.atlassian.com/legal/software-license-agreement, https://www.atlassian.com/legal/privacy-policy" \
      de.kdac.confluence.title = "Atlassian Confluence (KDAC Version)" \
      de.kdac.confluence.description = "Adapted Atlassians Confluence Dockerfile used by https://ews.kdac.de"

ENV RUN_USER=daemon \ 
    RUN_GROUP=daemon \
    CONFLUENCE_HOME=/var/atlassian/application-data/confluence \ 
    CONFLUENCE_INSTALL_DIR=/opt/atlassian/confluence \
    LD_LIBRARY_PATH=/usr/lib

VOLUME ["${CONFLUENCE_HOME}"]

EXPOSE 8090 8091

WORKDIR $CONFLUENCE_HOME

CMD ["/entrypoint.sh", "-fg"]
ENTRYPOINT ["/sbin/tini", "--"]

RUN apk --no-cache upgrade \
 && apk add --no-cache bash curl ghostscript motif ttf-dejavu tini \
 && fc-cache -f

COPY entrypoint.sh /entrypoint.sh

ARG CONFLUENCE_VERSION=6.13.9
ARG DOWNLOAD_URL=http://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz

RUN mkdir -p ${CONFLUENCE_INSTALL_DIR} \
 && curl -jkSL ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C "$CONFLUENCE_INSTALL_DIR" \
 && chown -R ${RUN_USER}:${RUN_GROUP} ${CONFLUENCE_INSTALL_DIR}/ \
 && sed -i -e 's/port="8090"/port="8090" secure="${catalinaConnectorSecure}" scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}" proxyPort="${catalinaConnectorProxyPort}"/' ${CONFLUENCE_INSTALL_DIR}/conf/server.xml \
 && sed -i -e 's/Context path=""/Context path="${catalinaContextPath}"/' ${CONFLUENCE_INSTALL_DIR}/conf/server.xml \
 && ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so \
 && ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 \
 && ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1 \
 && sed -i -e 's/-Xms\([0-9]\+[kmg]\) -Xmx\([0-9]\+[kmg]\)/-Xms\${JVM_MINIMUM_MEMORY:=\1} -Xmx\${JVM_MAXIMUM_MEMORY:=\2} \${JVM_SUPPORT_RECOMMENDED_ARGS} -Dconfluence.home=\${CONFLUENCE_HOME}/g' ${CONFLUENCE_INSTALL_DIR}/bin/setenv.sh 
