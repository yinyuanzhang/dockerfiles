FROM ubuntu:18.04
MAINTAINER Philipp Goellner <philipp.goellner@xaltbc.de>

# setup useful environment variables
ENV BACKUP_HOST                                    false
ENV BACKUP_PATH=false
ENV BACKUP_USER=false
ENV BACKUP_KEY_FILE=/tmp/id_rsa

ENV CROWD_VERSION                                  3.2.3
ENV CROWD_CONTEXT                                  ROOT
ENV CROWD_HOME                                     /var/atlassian/crowd
ENV CROWD_INSTALL                                  /opt/atlassian/crowd
ENV CROWD_REMOTE_DEBUG                             false
ENV CROWD_URL                                      https://www.atlassian.com/software/crowd/downloads/binary/atlassian-crowd-${CROWD_VERSION}.tar.gz

ENV CROWDDB_URL                                    mysql://dbuser:dbpass@dbhost:dbport/dbname
ENV CROWDID_CONTEXT                                ""

ENV DEMO_CONTEXT                                   demo
ENV RAM_MIN                                        768
ENV RAM_MAX                                        2048
ENV DEBUG_PORT                                     5005
ENV HTTPS                                          false
ENV IMPORTCERT                                     false
ENV IMPORTPATH                                     /var/certificates
ENV PROXY_NAME                                     false

ENV DEBIAN_FRONTEND                                noninteractive

ENV LIQUIBASE                                      false
ENV LIQUIBASE_VERSION                              3.6.2
ENV LIQUIBASE_INSTALL                              /opt/liquibase
ENV LIQUIBASE_URL                                  https://github.com/liquibase/liquibase/releases/download/liquibase-parent-${LIQUIBASE_VERSION}/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz

ENV MYSQL_DRIVER_VERSION                           5.1.36
ENV MYSQL_DRIVER_URL                               http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz

ENV NEWRELIC_VERSION=current
ENV NEWRELIC_APP_NAME=crowd-docker
ENV NEWRELIC_LICENSE=false
ENV NEWRELIC_URL=https://download.newrelic.com/newrelic/java-agent/newrelic-agent/${NEWRELIC_VERSION}/newrelic-java.zip

ENV RUN_USER=daemon

ENV TIME_ZONE=false

ENV WAIT=false
ENV WAIT_COMMAND=none
ENV WAIT_SLEEP=2
ENV WAIT_LOOPS=10

RUN apt-get update -qq \
 && apt-get install --no-install-recommends -qq -y gnupg2 \
                                                   lsb-release \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 \
 && echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu/ $(lsb_release -s -c) main" > /etc/apt/sources.list.d/java.list \
 && echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections \
 && echo "debconf shared/accepted-oracle-license-v1-1 seen true"   | debconf-set-selections \
 && apt-get update -qq \
 && apt-get install --no-install-recommends -qq -y curl \
                                                   openssh-client \
                                                   oracle-java8-installer \
                                                   python3-pip \
                                                   rsync \
                                                   sed \
                                                   tzdata \
                                                   unzip \
                                                   xmlstarlet \
 && rm -rf                                         /var/lib/apt/lists/* \
 && pip3 install                                   passlib \
 && mkdir -p                                       "${CROWD_INSTALL}" \
 && curl -Lsk                                      "${CROWD_URL}"        | tar -xz --directory "${CROWD_INSTALL}"                   --strip-components=1 \
 && curl -Lsk                                      "${MYSQL_DRIVER_URL}" | tar -xz --directory "${CROWD_INSTALL}/apache-tomcat/lib" --strip-components=1 --no-same-owner "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar" \
 && mkdir -p                                       "${LIQUIBASE_INSTALL}" \
 && curl -Lsk                                      "${LIQUIBASE_URL}"    | tar -xz --directory "${LIQUIBASE_INSTALL}" \
 && cp "${LIQUIBASE_INSTALL}/sdk/lib-sdk/slf4j-api-1.7.25.jar" "${LIQUIBASE_INSTALL}/lib/" \
 && curl -Lsk                                      "${NEWRELIC_URL}" -o                        /tmp/newrelic-java.zip \
 && unzip /tmp/newrelic-java.zip -d                "${CROWD_INSTALL}" \
 && rm -f /tmp/newrelic-java.zip \
 && echo "\ncrowd.home=${CROWD_HOME}" >>           "${CROWD_INSTALL}/crowd-webapp/WEB-INF/classes/crowd-init.properties" \
 && sed -i               's|exec "$PRGDIR"\/"$EXECUTABLE" start "$@"|exec "$PRGDIR"/"$EXECUTABLE" run "$@"|g' ${CROWD_INSTALL}/apache-tomcat/bin/startup.sh \
 && mv ${CROWD_INSTALL}/apache-tomcat/webapps/ROOT ${CROWD_INSTALL}/splash-webapp \
 && mv ${CROWD_INSTALL}/apache-tomcat/conf/Catalina/localhost ${CROWD_INSTALL}/webapps \
 && mkdir ${CROWD_INSTALL}/apache-tomcat/conf/Catalina/localhost \
 && mkdir                                          "${IMPORTPATH}" \
 && chown -R ${RUN_USER}:${RUN_GROUP}              "${IMPORTPATH}" \
                                                   "${CROWD_INSTALL}" \
                                                   /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts

#TODO
#    && xmlstarlet           ed --inplace \
#        --delete            "Server/@debug" \
#        --delete            "Server/Service/Connector/@debug" \
#        --delete            "Server/Service/Connector/@minProcessors" \
#        --delete            "Server/Service/Connector/@maxProcessors" \
#        --delete            "Server/Service/Connector/@useURIValidationHack" \
#        --delete            "Server/Service/Engine/@debug" \
#        --delete            "Server/Service/Engine/Host/@debug" \
#        --delete            "Server/Service/Engine/Host/Context/@debug" \
#		            "${CROWD_INSTALL}/conf/server.xml" \
#TODO
#    && sed -ri "s/-Xms1024m -Xmx1024m//" ${CROWD_INSTALL}/bin/setenv.sh \ 
#    && sed -ri 's~export CATALINA_OPTS~. ${CROWD_INSTALL}/bin/set-remote-debug.sh\nexport CATALINA_OPTS~' ${CROWD_INSTALL}/bin/setenv.sh \
#    && chown -R ${RUN_USER}: "${CROWD_INSTALL}"

COPY splash-context.xml                            "${CROWD_INSTALL}/webapps/splash.xml"
COPY common.bash                                   "${CROWD_INSTALL}/"
COPY changelogs                                    "${LIQUIBASE_INSTALL}/changelogs/"
COPY liquibase.properties                          "${LIQUIBASE_INSTALL}/"
COPY configure-and-start-root.sh                   "${CROWD_INSTALL}/bin/"
COPY configure-and-start.sh                        "${CROWD_INSTALL}/bin/"
RUN chmod 500                                       ${CROWD_INSTALL}/bin/configure-and-start*.sh \
 && chown -R ${RUN_USER}:${RUN_GROUP}              "${CROWD_INSTALL}/bin/configure-and-start.sh" \
                                                   "${LIQUIBASE_INSTALL}"

# expose default Remote Debug port & HTTP port
EXPOSE 5005 8095

# set volume mount points for installation and home directory
VOLUME ["${CROWD_HOME}"]

# Set the default working directory as the installation directory.
WORKDIR ${CROWD_INSTALL}

# Run Atlassian Crowd as a foreground process by default.
ENTRYPOINT ["./bin/configure-and-start-root.sh"]
