FROM openjdk:8-jre-alpine

ENV SONAR_SCANNER_VERSION 3.0.3.778

RUN mkdir -p /data
VOLUME /data

COPY ./sonar-wrapper /usr/bin
COPY ./common/sonar-await-results /usr/bin/

RUN apk add --no-cache jq curl bash nodejs nodejs-npm git
RUN npm install -g typescript

ENV NODE_PATH="/usr/lib/node_modules/"

ADD "https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip" /

RUN unzip "sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip"

ENV PATH "/sonar-scanner-${SONAR_SCANNER_VERSION}/bin:${PATH}"

ENTRYPOINT ["sonar-wrapper"]

WORKDIR /data
