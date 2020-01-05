FROM openjdk:11
LABEL maintainer="Pablo Bastidas V. - pablobastidasv.co" description="OpenLiberty Java EE 8 w. Microprofile 1.3 dev"

ENV RELEASE 2019-04-19_0642
ENV VERSION 19.0.0.4

env INSTALL_DIR /opt
ENV WLP_HOME ${INSTALL_DIR}/wlp
ENV CONFIG ${WLP_HOME}/usr/servers/defaultServer/

RUN curl -O https://public.dhe.ibm.com/ibmdl/export/pub/software/openliberty/runtime/release/${RELEASE}/openliberty-${VERSION}.zip \
    && unzip openliberty-${VERSION}.zip -d ${INSTALL_DIR} \
    && rm openliberty-${VERSION}.zip

ENV DEPLOYMENT_DIR=${CONFIG}/dropins/
ENV APPS_DIR=${CONFIG}/apps/
ENV SHARED=${WLP_HOME}/usr/shared
ENV RESOURCES=${SHARED}/resources
ENV CUSTOM_CONFIG=${CONFIG}/configDropins/defaults
ENV FEATURES=${CUSTOM_CONFIG}/features.xml 
ENV CONFIG_FILES_DIR ${CONFIG}/configDropins/defaults

ENV AUTO_EXPAND=true

COPY ./jvm.options /tmp
COPY ./startup.sh /opt
COPY server.xml ${CONFIG}

COPY features.xml $FEATURES

EXPOSE 9080 9443 9090

CMD ["/opt/startup.sh"]
