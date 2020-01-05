FROM adoptopenjdk/openjdk8-openj9:alpine-slim

LABEL de.kdac.crowd.maintainer = "Claus Böhmer" \
      de.kdac.crowd.authors = "eso@bistum-eichstaett.de" \
      de.kdac.crowd.url = "https://hub.docker.com/r/kidac/crowd" \
      de.kdac.crowd.documentation = "https://hub.docker.com/r/kidac/crowd" \
      de.kdac.crowd.source = "https://github.com/kidac/crowd" \
      de.kdac.crowd.version = "3.7.0" \
      de.kdac.crowd.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.crowd.licenses = "https://www.atlassian.com/legal/software-license-agreement, https://www.atlassian.com/legal/privacy-policy" \
      de.kdac.crowd.title = "Atlassian Crowd (KDAC Version)" \
      de.kdac.crowd.description = "Adapted Atlassians Crowd Dockerfile used by https://ews.kdac.de"

ENV RUN_USER=daemon \
    RUN_GROUP=daemon \
    CROWD_HOME=/var/atlassian/application-data/crowd \
    CROWD_INSTALL_DIR=/opt/atlassian/crowd \
    LD_LIBRARY_PATH=/usr/lib

VOLUME ["${CROWD_HOME}"]

EXPOSE 8095

WORKDIR $CROWD_HOME

CMD ["/entrypoint.sh", "-fg"]
ENTRYPOINT ["/sbin/tini", "--"]

RUN apk --no-cache upgrade \
 && apk add --no-cache bash curl ghostscript motif ttf-dejavu tini \
 && fc-cache -f

COPY entrypoint.sh /entrypoint.sh

ARG CROWD_VERSION=3.7.0
ARG DOWNLOAD_URL=https://www.atlassian.com/software/crowd/downloads/binary/atlassian-crowd-${CROWD_VERSION}.tar.gz

RUN mkdir -p ${CROWD_INSTALL_DIR} \
 && curl -jkSL ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C "$CROWD_INSTALL_DIR" \
 && chown -R ${RUN_USER}:${RUN_GROUP} ${CROWD_INSTALL_DIR}/ \
 && sed -i -e 's/port="8095"/port="8095" secure="${catalinaConnectorSecure}" scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}" proxyPort="${catalinaConnectorProxyPort}"/' ${CROWD_INSTALL_DIR}/apache-tomcat/conf/server.xml \
 && sed -i -e 's/<\/Engine>/<Context path=\"\${catalinaContextPath}\" docBase=\"..\/..\/crowd-webapp\" debug=\"0\"><Manager pathname=\"\" \/><\/Context><\/Host><\/Engine>/g' ${CROWD_INSTALL_DIR}/apache-tomcat/conf/server.xml \
 && ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so \
 && ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 \
 && ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1 \
 && sed -i -e 's/unpackWARs="true"\/>/unpackWARs="true">/g' ${CROWD_INSTALL_DIR}/apache-tomcat/conf/server.xml \
 && sed -i -e 's/-Xms\([0-9]\+[kmg]\) -Xmx\([0-9]\+[kmg]\)/-Xms\${JVM_MINIMUM_MEMORY:=\1} -Xmx\${JVM_MAXIMUM_MEMORY:=\2} \${JVM_SUPPORT_RECOMMENDED_ARGS} -Dcrowd.home=\${CROWD_HOME}/g' ${CROWD_INSTALL_DIR}/apache-tomcat/bin/setenv.sh \
 && rm -rf /opt/atlassian/crowd/*openid* \
 && rm -rf /opt/atlassian/crowd/apache-tomcat/conf/Catalina/localhost/openid*
