FROM debian:stretch
MAINTAINER LWB

# Signavio
ENV VERSION=11.5.1
ENV CONNECTOR_VERSION=5.1.47
ENV CONNECTOR_FILE=mysql-connector-java-${CONNECTOR_VERSION}-bin.jar
ENV WEBAPPS_PATH=/opt/tomcat/webapps
ENV CONF_PATH=/opt/tomcat/conf.bak
ENV LIB_PATH=/opt/tomcat/lib.bak
ENV HOST=HOST
ENV DB_URL=DB
ENV DB_USERNAME=ADMIN
ENV DB_PASSWORD=ADMIN
ENV SMTP_HOST_NAME=HOST
ENV SMTP_EMAIL=EMAIL
ENV SMTP_PORT=25
ENV SUPPORT_EMAIL=EMAIL
ENV SOLR_URL=http://localhost:8080/solr

ENV FILE_IMPORT_USER=ADMIN
ENV FILE_IMPORT_PASSWORD=ADMIN
ENV FILE_IMPORT_PATH=/

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --force-yes --no-install-recommends cifs-utils unzip wget ca-certificates && \
    rm -rf /var/lib/apt/lists && \
    mkdir -p ${WEBAPPS_PATH} && \
    mkdir -p ${CONF_PATH} && \
    mkdir -p ${LIB_PATH}

VOLUME ${WEBAPPS_PATH}
VOLUME ${CONF_PATH}
VOLUME ${LIB_PATH}

RUN wget -O /tmp/connector.zip https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${CONNECTOR_VERSION}.zip && \
	unzip -o /tmp/connector.zip -d /tmp/ && \
	mv -v /tmp/mysql-connector-java-${CONNECTOR_VERSION}/${CONNECTOR_FILE} /tmp/ && \
	rm -vrf /tmp/mysql-connector-java-${CONNECTOR_VERSION} && \
	rm -vf /tmp/connector.zip

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
