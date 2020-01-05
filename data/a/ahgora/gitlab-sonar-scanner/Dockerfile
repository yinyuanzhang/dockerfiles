FROM openjdk:8-jdk-alpine
## Based on this example http://stackoverflow.com/a/40612088/865222
ENV SONAR_SCANNER_VERSION 3.2.0.1227-linux

RUN apk add --no-cache wget && \
    wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} && \
    rm sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    rm -Rf /sonar-scanner-${SONAR_SCANNER_VERSION}/jre && \
    sed -i 's/use_embedded_jre=true/use_embedded_jre=false/' /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner && \
    cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner sonar-scanner && \
    apk del wget && \
    ln -s /usr/bin/sonar-scanner-run.sh /bin/gitlab-sonar-scanner

COPY sonar-scanner-run.sh /usr/bin
