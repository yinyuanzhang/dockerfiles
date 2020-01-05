FROM adoptopenjdk/openjdk8
MAINTAINER Christoph Eßer <christoph@cehser.de>

ENV RUN_USER            					daemon
ENV RUN_GROUP           					daemon

# https://confluence.atlassian.com/doc/confluence-home-and-other-important-directories-590259707.html
ENV CONFLUENCE_HOME          				/var/atlassian/application-data/confluence
ENV CONFLUENCE_INSTALL_DIR   				/opt/atlassian/confluence

VOLUME ["${CONFLUENCE_HOME}"]
WORKDIR $CONFLUENCE_HOME

# Expose HTTP and Synchrony ports
EXPOSE 8090
EXPOSE 8091

CMD ["/entrypoint.sh", "-fg"]
ENTRYPOINT ["/sbin/tini", "--"]

RUN apt-get update \
	&& apt-get install -y --no-install-recommends fontconfig \
	&& apt-get clean autoclean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

ARG TINI_VERSION=v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /sbin/tini
RUN chmod +x /sbin/tini

COPY entrypoint.sh              			/entrypoint.sh

ARG CONFLUENCE_VERSION=6.15.9
ARG DOWNLOAD_URL=https://product-downloads.atlassian.com/software/confluence/downloads/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz

RUN mkdir -p                             	${CONFLUENCE_INSTALL_DIR} \
    && curl -L --silent                  	${DOWNLOAD_URL} | tar -xz --strip-components=1 -C "${CONFLUENCE_INSTALL_DIR}" \
    && chown -R ${RUN_USER}:${RUN_GROUP} 	${CONFLUENCE_INSTALL_DIR}/ \
    && sed -i -e 's/-Xms\([0-9]\+[kmg]\) -Xmx\([0-9]\+[kmg]\)/-Xms\${JVM_MINIMUM_MEMORY:=\1} -Xmx\${JVM_MAXIMUM_MEMORY:=\2} \${JVM_SUPPORT_RECOMMENDED_ARGS} -Dconfluence.home=\${CONFLUENCE_HOME}/g' ${CONFLUENCE_INSTALL_DIR}/bin/setenv.sh \
    && sed -i -e 's/port="8090"/port="8090" secure="${catalinaConnectorSecure}" scheme="${catalinaConnectorScheme}" proxyName="${catalinaConnectorProxyName}" proxyPort="${catalinaConnectorProxyPort}"/' ${CONFLUENCE_INSTALL_DIR}/conf/server.xml \
    && sed -i -e 's/Context path=""/Context path="${catalinaContextPath}"/' ${CONFLUENCE_INSTALL_DIR}/conf/server.xml

# Add MySQL Connector
ARG CONNECTOR_VERSION=5.1.47
ADD https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${CONNECTOR_VERSION}.tar.gz /tmp/
RUN cd /tmp &&\
  tar zxvf mysql-connector-java-${CONNECTOR_VERSION}.tar.gz &&\
  cd mysql-connector-java-${CONNECTOR_VERSION} &&\
  cp mysql-connector-java-${CONNECTOR_VERSION}.jar /opt/atlassian/confluence/confluence/WEB-INF/lib/ &&\
  cd /tmp &&\
  rm -rf /tmp/mysql-connector-java-${CONNECTOR_VERSION} mysql-connector-java-${CONNECTOR_VERSION}.tar.gz
