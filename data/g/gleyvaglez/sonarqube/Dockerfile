FROM openjdk:8-alpine

ENV SONAR_VERSION=7.3 \
    SONAR_DOWNLOAD_URL=https://binaries.sonarsource.com/Distribution/sonarqube \
    SONARQUBE_HOME=/opt/sonarqube \
    # Database configuration
    # Defaults to using H2
    SONARQUBE_JDBC_USERNAME= \
    SONARQUBE_JDBC_PASSWORD= \
    SONARQUBE_JDBC_URL=

# Http port
EXPOSE 9000

RUN addgroup -S sonarqube && adduser -S -G sonarqube sonarqube

ADD $SONAR_DOWNLOAD_URL/sonarqube-$SONAR_VERSION.zip /opt/sonarqube.zip
# COPY sonarqube-$SONAR_VERSION.zip.asc /opt/sonarqube.zip.asc

RUN set -x \
    # && export HTTP_PROXY="http://proxy:port" \
	# && export HTTPS_PROXY="http://proxy:port" \
    && apk add --no-cache gnupg unzip \
    && apk add --no-cache libressl wget \
    && apk add --no-cache su-exec \
    && apk add --no-cache bash \
    # pub   2048R/D26468DE 2015-05-25
    #       Key fingerprint = F118 2E81 C792 9289 21DB  CAB4 CFCA 4A29 D264 68DE
    # uid                  sonarsource_deployer (Sonarsource Deployer) <infra@sonarsource.com>
    # sub   2048R/06855C1D 2015-05-25
    && cd /opt \
    && unzip sonarqube.zip \
    && mv sonarqube-$SONAR_VERSION sonarqube \
    && chown -R sonarqube:sonarqube sonarqube \
    && rm sonarqube.zip* \
    && rm -rf $SONARQUBE_HOME/bin/*

VOLUME "$SONARQUBE_HOME/data"

WORKDIR $SONARQUBE_HOME

COPY run.sh $SONARQUBE_HOME/bin/

RUN cd /opt && chown -R sonarqube:sonarqube sonarqube

ENTRYPOINT ["./bin/run.sh"]
