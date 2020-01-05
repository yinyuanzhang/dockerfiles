FROM ubuntu:16.04
MAINTAINER Serfim TIC

# Base NPM
RUN apt update && apt install -y \
  locales \
  build-essential \
  gcc-4.8 \
  g++-4.8 \
  git \
  rpm \
  openjdk-8-jdk \
  curl \
  wget \
  jq \
  python \
  unzip
  
ENV SONAR_SCANNER_VERSION 3.0.3.778

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && apt install -y nodejs

RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} && \
    cd /usr/bin && \
    ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner sonar-scanner && \
    ln -s /usr/bin/sonar-scanner-run.sh /bin/gitlab-sonar-scanner
    
COPY sonar-scanner-run.sh /usr/bin
