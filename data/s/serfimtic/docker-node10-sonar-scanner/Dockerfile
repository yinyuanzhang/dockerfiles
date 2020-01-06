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

ENV SONAR_SCANNER_VERSION 4.2.0.1873

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt install -y nodejs

RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip && \
    unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip && \
    cd /usr/bin && \
    ln -s /sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux/bin/sonar-scanner sonar-scanner && \
    ln -s /usr/bin/sonar-scanner-run.sh /bin/gitlab-sonar-scanner

RUN rm /sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip


COPY sonar-scanner-run.sh /usr/bin
