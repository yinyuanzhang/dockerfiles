from openjdk:jre-slim
ENV SONAR_SCANNER_VERSION 3.0.3.778
RUN apt update && apt install -y wget
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip\
&& unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip\
&& rm sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip\
&& mv /sonar-scanner-${SONAR_SCANNER_VERSION}-linux /sonar-scanner
RUN mkdir /code
VOLUME /code
WORKDIR /code
ENTRYPOINT ["/sonar-scanner/bin/sonar-scanner"]
