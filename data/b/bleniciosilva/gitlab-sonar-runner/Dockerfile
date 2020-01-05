FROM java:8-jdk-alpine
MAINTAINER Ruben Blenicio Tavares Silva

ENV SONAR_RUNNER_VERSION 2.4
ENV SONAR_RUNNER_HOME /opt/sonar-runner-${SONAR_RUNNER_VERSION}
ENV SONAR_RUNNER_PACKAGE sonar-runner-dist-${SONAR_RUNNER_VERSION}.zip
ENV HOME ${SONAR_RUNNER_HOME}

RUN apk update
RUN apk fetch nodejs
RUN apk add --no-cache nodejs

RUN apk fetch wget && apk fetch unzip
RUN apk add --no-cache wget && apk add --no-cache unzip

WORKDIR /opt

RUN wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/${SONAR_RUNNER_VERSION}/${SONAR_RUNNER_PACKAGE} \
 && unzip sonar-runner-dist-${SONAR_RUNNER_VERSION}.zip \
 && rm ${SONAR_RUNNER_PACKAGE}

WORKDIR /data
VOLUME /data

COPY gitlab-entrypoint.sh /gitlab-entrypoint.sh
RUN chmod +x /gitlab-entrypoint.sh
ENTRYPOINT ["/gitlab-entrypoint.sh"]
CMD ${SONAR_RUNNER_HOME}/bin/sonar-runner
