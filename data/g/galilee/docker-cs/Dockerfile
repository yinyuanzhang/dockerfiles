FROM maven:3.5-jdk-8-alpine
MAINTAINER Gabriel Malet <gmalet@galilee.fr>

ENV SONAR_SCANNER_VERSION="3.2.0.1227"

RUN apk add --no-cache \
        bash \
        wget \
        curl \
        git \
        openssh-client \
        nodejs \
        nodejs-npm \
        yarn

RUN curl -sL "https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SONAR_SCANNER_VERSION.zip" -o /tmp/setup.zip \
	&& unzip -d /root /tmp/setup.zip \
	&& ln -s "/root/sonar-scanner-$SONAR_SCANNER_VERSION/bin/sonar-scanner" /usr/local/bin/ \
	&& ln -s "/root/sonar-scanner-$SONAR_SCANNER_VERSION/bin/sonar-scanner-debug" /usr/local/bin/ \
	&& rm -f /tmp/setup.zip

RUN node -v \
    && yarn -v \
    && mvn -v \
    && sonar-scanner -v

COPY resources/.npmrc /root/.npmrc
COPY resources/ssh_config /root/.ssh/config
COPY resources/entrypoint.sh /entrypoint.sh
COPY resources/maven.settings.xml /root/.m2/settings.xml

ENTRYPOINT ["/entrypoint.sh"]
