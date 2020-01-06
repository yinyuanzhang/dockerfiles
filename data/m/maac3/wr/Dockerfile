
ARG MVN_PROFILE=docker

FROM maven:3.6-jdk-8 AS maven

ARG MVN_PROFILE

COPY ./docker/files/lib/mvn /build/lib
COPY ./pom.xml /build/pom.xml
COPY ./src /build/src

WORKDIR /build/lib
RUN \
  mvn install:install-file -Dfile=coffee-common-cipher-1.0.jar -DpomFile=coffee-common-cipher-1.0.pom && \
  mvn install:install-file -Dfile=coffee-common-core-1.0.jar -DpomFile=coffee-common-core-1.0.pom && \
  mvn install:install-file -Dfile=coffee-server-core-1.0.jar -DpomFile=coffee-server-core-1.0.pom && \
  mvn install:install-file -Dfile=coffee-server-webcore-1.0.jar -DpomFile=coffee-server-webcore-1.0.pom && \
  mvn install:install-file -Dfile=hcis-utils-1.9.12.jar -DpomFile=hcis-utils-1.9.12.pom && \
  mvn install:install-file -Dfile=bootstrap-1.0.9.jar -DpomFile=bootstrap-1.0.9.pom

WORKDIR /build
RUN \
  mvn -Dproject.build.sourceEncoding=UTF-8 \
    package -P ${MVN_PROFILE} && \
  cp target/*.war target/wr.war

FROM payara/micro

ARG MVN_PROFILE

# setup configuration
USER root

ENV PAYARA_PATH /opt/payara
ENV LIB_DIR $PAYARA_PATH/ext
ENV FOP_CONF_DIR $PAYARA_PATH/fop/conf
ENV FOP_CONF $FOP_CONF_DIR/fop.xconf
ENV APP_DIR /opt/WR

# installing libs needed for POI (sun.awt.fontconfiguration.getversion NPE)
RUN \
  set -xe && \
  apk --no-cache add ttf-dejavu fontconfig

RUN \
  umask 0002 && \
  mkdir -p $LIB_DIR && \
  mkdir -p $FOP_CONF_DIR && \
  mkdir -p $APP_DIR

# copy external libs
COPY ./docker/files/lib/ext $LIB_DIR

# copy fop conf files
COPY ./docker/files/lib/fop/conf $FOP_CONF_DIR

# copy app dir
#COPY ./docker/app/$MVN_PROFILE $APP_DIR

# copy war to deploy dir
COPY --from=maven build/target/wr.war $DEPLOY_DIR

# entry point
COPY ./docker/files/entrypoint.sh $PAYARA_PATH/entrypoint.sh

RUN \
  chown payara:payara $PAYARA_PATH/entrypoint.sh && \
  chmod +x $PAYARA_PATH/entrypoint.sh

USER payara
WORKDIR $PAYARA_PATH

ENTRYPOINT ["sh", "./entrypoint.sh"]
