
###########################################################
## step 1: loader
## GOTCHA: use debian because of the limitations of unzip in busybox/alpine,
##         which cannot unzip symlinks
FROM debian:buster as loader

ARG SONAR_SCANNER_VERSION=4.0.0.1744-linux

RUN apt-get update \
  && apt-get install -y unzip wget \
  && rm -rf /var/lib/apt/lists/*

RUN cd / \
  && wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
  && unzip -q sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
  && rm sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
  && mv sonar-scanner-${SONAR_SCANNER_VERSION} sonar-scanner \
  && rm -rf sonar-scanner/jre

###########################################################
## step 2: run image
FROM openjdk:8-jre-slim

LABEL maintainer="Vincent Pfister <vincent.pfister@raisepartner.com>"

# copy sonar-scanner from loader
RUN mkdir -p /var/lib/sonar-scanner
COPY --from=loader /sonar-scanner/. /var/local/sonar-scanner

# remove reference to embedded JRE, link command to path
RUN sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g' /var/local/sonar-scanner/bin/sonar-scanner
RUN ln -s /var/local/sonar-scanner/bin/sonar-scanner /usr/bin/sonar-scanner \
  && ln -s /var/local/sonar-scanner/bin/sonar-scanner-debug /usr/bin/sonar-scanner-debug

RUN apt-get update \
  && apt-get install -y curl wget git \
  && rm -rf /var/lib/apt/lists/*

CMD /usr/bin/sonar-scanner
