FROM eugenmayer/java:server-jre8

ARG CONFLUENCE_VERSION=6.5.1
# permissions
ARG CONTAINER_UID=1000
ARG CONTAINER_GID=1000
ARG LANG_LANGUAGE=en
ARG LANG_COUNTRY=US

# Setup useful environment variables
ENV CONF_HOME=/var/atlassian/confluence \
    CONF_INSTALL=/opt/atlassian/confluence \
    CONFLUENCE_DB_HOST=db \
    CONFLUENCE_DB_PORT=3306 \
    MYSQL_DRIVER_VERSION=5.1.44 \
    POSTGRESQL_DRIVER_VERSION=9.4.1212

COPY bin/custom_scripts.sh /usr/local/bin/custom_scripts.sh
COPY bin/wait-for-it.sh /usr/local/bin/wait-for-it
# Install Atlassian Confluence
RUN export CONTAINER_USER=confluence                &&  \
    export CONTAINER_GROUP=confluence               &&  \
    addgroup -g $CONTAINER_GID $CONTAINER_GROUP     &&  \
    adduser -u $CONTAINER_UID                           \
            -G $CONTAINER_GROUP                         \
            -h /home/$CONTAINER_USER                    \
            -s /bin/bash                                \
            -S $CONTAINER_USER                      &&  \

    apk add --update                                    \
      ca-certificates                                   \
      gzip                                              \
      curl                                              \
      tar                                               \
      msttcorefonts-installer                           \
      ttf-dejavu					                    \
      fontconfig                                        \
      motif						                        \
      ghostscript                                       \
      graphviz                                          \
      xmlstarlet                                        \
      wget                                          &&  \
    # Install xmlstarlet
    update-ms-fonts                                 && \
    fc-cache -f                                     && \
    /usr/glibc-compat/bin/localedef -i ${LANG_LANGUAGE}_${LANG_COUNTRY} -f UTF-8 ${LANG_LANGUAGE}_${LANG_COUNTRY}.UTF-8 && \
    mkdir -p ${CONF_HOME} \    
    && chown -R confluence:confluence ${CONF_HOME} \
    && mkdir -p ${CONF_INSTALL}/conf \
    && wget -O /tmp/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz http://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz && \
    tar xzf /tmp/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz --strip-components=1 -C ${CONF_INSTALL} && \
    echo "confluence.home=${CONF_HOME}" > ${CONF_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties && \
    # Install database drivers
    rm -f                                               \
      ${CONF_INSTALL}/lib/mysql-connector-java*.jar &&  \
    wget -O /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz                                              \
      http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz && \
    tar xzf /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz                                              \
      -C /tmp && \
    cp /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar     \
      ${CONF_INSTALL}/lib/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar                                &&  \
    rm -f ${CONF_INSTALL}/lib/postgresql-*.jar                                                                &&  \
    wget -O ${CONF_INSTALL}/lib/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar                                        \
      https://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar                          && \
    chown -R confluence:confluence ${CONF_INSTALL} && \
    # Adding letsencrypt-ca to truststore
    export KEYSTORE=$JRE_HOME/lib/security/cacerts && \
    wget -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx1.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx2.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias isrgrootx1 -file /tmp/letsencryptauthorityx1.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias isrgrootx2 -file /tmp/letsencryptauthorityx2.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx1 -file /tmp/lets-encrypt-x1-cross-signed.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx2 -file /tmp/lets-encrypt-x2-cross-signed.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx3 -file /tmp/lets-encrypt-x3-cross-signed.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx4 -file /tmp/lets-encrypt-x4-cross-signed.der && \
    # Install atlassian ssl tool
    wget -O /home/${CONTAINER_USER}/SSLPoke.class https://confluence.atlassian.com/kb/files/779355358/779355357/1/1441897666313/SSLPoke.class && \
    chown -R confluence:confluence /home/${CONTAINER_USER} && \
    # Install Tini Zombie Reaper And Signal Forwarder
    export TINI_VERSION=0.9.0 && \
    curl -fsSL https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static -o /bin/tini && \
    chmod +x /bin/tini && \
    # Remove obsolete packages and cleanup
    apk del wget && \
    # Clean caches and tmps
    rm -rf /var/cache/apk/*                         &&  \
    rm -rf /tmp/*                                   &&  \
    rm -rf /var/log/* && \
    mkdir -p /docker-entrypoint.d && \
    chmod +x /usr/local/bin/custom_scripts.sh && \
    chmod +x /usr/local/bin/wait-for-it

# Expose default HTTP connector port.
EXPOSE 8090 8091

USER confluence
COPY confluence.cfg.xml.tpl ${CONF_HOME}/confluence.cfg.xml
VOLUME ["/var/atlassian/confluence"]
# Set the default working directory as the Confluence home directory.
WORKDIR ${CONF_HOME}
COPY bin/docker-entrypoint.sh /home/confluence/docker-entrypoint.sh

ENTRYPOINT ["/bin/tini","--","/home/confluence/docker-entrypoint.sh"]
CMD ["confluence"]
