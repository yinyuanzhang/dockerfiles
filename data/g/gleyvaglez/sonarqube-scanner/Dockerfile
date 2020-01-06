FROM java:8-jre-alpine

RUN apk update && apk add --no-cache curl git python3
# RUN pip3 install --upgrade pip
# RUN pip3 install --upgrade pylint setuptools

WORKDIR /root

ARG LATEST

RUN env && \
curl --insecure -OL 'https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/'$LATEST && \
mkdir sonar_scanner && unzip -d sonar_scanner $LATEST && mv sonar_scanner/* sonar_home && rm -rf sonar_scanner $LATEST

ENV SONAR_RUNNER_HOME=/root/sonar_home
ENV PATH ${SONAR_RUNNER_HOME}/bin:$PATH

CMD sonar-scanner -Dsonar.projectBaseDir=./src
