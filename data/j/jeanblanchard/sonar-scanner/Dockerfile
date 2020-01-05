FROM openjdk:8-slim
MAINTAINER Jean Blanchard <jean@blanchard.io>

ENV VERSION 3.2.0.1227

RUN apt-get update && apt-get install -y curl
RUN curl -Lo sonar-scanner.zip https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${VERSION}-linux.zip
RUN mkdir -p /opt && unzip sonar-scanner.zip -d /opt && mv /opt/sonar-scanner-$VERSION-linux /opt/sonar-scanner
RUN ln -s /opt/sonar-scanner/bin/sonar-scanner /usr/bin/sonar-scanner

ENTRYPOINT ["sonar-scanner"]
