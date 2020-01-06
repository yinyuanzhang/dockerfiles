FROM node:8-alpine

ENV SONAR_SCANNER_VERSION=3.2.0.1227 \
    SONAR_SCANNER_HOME="/opt/sonar-scanner" \
    TOOLS_HOME="/opt/tools"

WORKDIR /root

# Install dependencies
RUN apk add --no-cache zip lftp curl jq bash openjdk8-jre git

# Install build dependencies
RUN apk add --no-cache --virtual=.build-dependencies ca-certificates wget unzip

# Update npm
RUN npm i -g npm@6

# set up bower and gulp
RUN npm install -g bower gulp && \
    echo '{ "allow_root": true }' > /root/.bowerrc

# Install pipeline tools
COPY ./pipeline/shared/tools ${TOOLS_HOME}
RUN chmod +x ${TOOLS_HOME}/*
COPY ./pipeline/shared/webdeploy ${TOOLS_HOME}/webdeploy
RUN ln -s ${TOOLS_HOME}/* /usr/local/bin/

# Install Sonar.
RUN wget -O sonar.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    unzip sonar.zip && \
    mkdir -p ${SONAR_SCANNER_HOME} && \
    mv sonar-scanner-*/* ${SONAR_SCANNER_HOME} && \
    chmod +x ${SONAR_SCANNER_HOME}/bin/sonar-scanner && \
    ln -s ${SONAR_SCANNER_HOME}/bin/sonar-scanner /usr/local/bin/sonar-scanner && \
    rm sonar.zip && rm sonar-scanner-* -r

COPY ./pipeline/shared/sonarqube/sonar-scanner.properties ${SONAR_SCANNER_HOME}/conf/

RUN mkdir /application
WORKDIR /application