FROM noenv/node

LABEL maintainer "NoEnv"
LABEL version "1.3.0"
LABEL description "SonarQube Scanner in NodeJS environment for scanning typescript and javascript projects"

ENV SONAR_SCANNER_VERSION 4.2.0.1873
ENV JAVA_HOME /usr/lib/jvm/default-jvm
ENV PATH $PATH:/sonar-scanner/bin

ADD "https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip" /

RUN set -x \
	&& apk add --no-cache unzip openjdk11 --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community \
  && unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
	&& ln -s /sonar-scanner-${SONAR_SCANNER_VERSION} /sonar-scanner \
  && rm -f sonar-scanner-cli-*.zip \
  && mkdir -p /data

VOLUME /data
WORKDIR /data
