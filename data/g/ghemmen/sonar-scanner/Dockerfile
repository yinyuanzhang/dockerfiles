FROM debian:stretch

LABEL maintainer="guillaume@van-hemmen.com"

RUN apt-get update && \
    apt-get -y install wget unzip && \
    cd /root/ && \
    wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492-linux.zip && \
    unzip sonar-scanner-cli-3.3.0.1492-linux.zip && \
    ln -sf /root/sonar-scanner-3.3.0.1492-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner
