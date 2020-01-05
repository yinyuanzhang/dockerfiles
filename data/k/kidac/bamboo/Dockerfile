FROM adoptopenjdk/openjdk8-openj9:alpine-slim

LABEL de.kdac.bamboo.maintainer = "Claus Böhmer" \
      de.kdac.bamboo.authors = "eso@bistum-eichstaett.de" \
      de.kdac.bamboo.url = "https://hub.docker.com/r/kidac/bamboo" \
      de.kdac.bamboo.documentation = "https://hub.docker.com/r/kidac/bamboo" \
      de.kdac.bamboo.source = "https://github.com/kidac/bamboo" \
      de.kdac.bamboo.version = "6.10.3" \
      de.kdac.bamboo.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.bamboo.licenses = "https://www.atlassian.com/legal/software-license-agreement, https://www.atlassian.com/legal/privacy-policy" \
      de.kdac.bamboo.title = "Atlassian Bamboo (KDAC Version)" \
      de.kdac.bamboo.description = "Adapted Atlassians Bamboo Dockerfile used by https://ews.kdac.de"

ENV RUN_USER=daemon \
    RUN_GROUP=daemon \
    BAMBOO_HOME=/var/atlassian/application-data/bamboo \
    BAMBOO_INSTALL_DIR=/opt/atlassian/bamboo \
    LD_LIBRARY_PATH=/usr/lib

VOLUME ["${BAMBOO_HOME}"]

EXPOSE 8085 54663

WORKDIR $BAMBOO_HOME

CMD ["/entrypoint.sh", "-fg"]
ENTRYPOINT ["/sbin/tini", "--"]

RUN apk --no-cache upgrade \
 && apk add --no-cache bash curl ghostscript motif ttf-dejavu tini \
 && fc-cache -f

COPY entrypoint.sh /entrypoint.sh

ARG BAMBOO_VERSION=6.10.3
ARG DOWNLOAD_URL=https://product-downloads.atlassian.com/software/bamboo/downloads/atlassian-bamboo-${BAMBOO_VERSION}.tar.gz

RUN mkdir -p ${BAMBOO_INSTALL_DIR} \
 && curl -jkSL ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C "$BAMBOO_INSTALL_DIR" \
 && chown -R ${RUN_USER}:${RUN_GROUP} ${BAMBOO_INSTALL_DIR}/ \
 && sed -i -e 's/port="8085"/port="8085" secure="${catalinaConnectorSecure}" scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}" proxyPort="${catalinaConnectorProxyPort}"/' ${BAMBOO_INSTALL_DIR}/conf/server.xml \
 && sed -i -e 's/Context path=""/Context path="${catalinaContextPath}"/' ${BAMBOO_INSTALL_DIR}/conf/server.xml \
 && ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so \
 && ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 \
 && ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1 \
 && sed -i -e 's/^JVM_SUPPORT_RECOMMENDED_ARGS=""$/: \${JVM_SUPPORT_RECOMMENDED_ARGS:=""}/g' ${BAMBOO_INSTALL_DIR}/bin/setenv.sh \
 && sed -i -e 's/^JVM_\(.*\)_MEMORY="\(.*\)"$/: \${JVM_\1_MEMORY:=\2}/g' ${BAMBOO_INSTALL_DIR}/bin/setenv.sh \
 && sed -i -e 's/^JAVA_OPTS="/JAVA_OPTS="${JAVA_OPTS} /g' ${BAMBOO_INSTALL_DIR}/bin/setenv.sh

#RUN apk add --no-cache git git-lfs maven
