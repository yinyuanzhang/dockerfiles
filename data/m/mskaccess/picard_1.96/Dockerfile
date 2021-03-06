################## BASE IMAGE ######################

FROM openjdk:8 

################## ARGUMENTS/Environments ##########

ARG BUILD_DATE
ARG BUILD_VERSION
ARG JAVA_VERSION=8
ARG LICENSE="Apache-2.0"
ARG PICARD_VERSION=1.96
ARG R_VERSION="Latest"

################## METADATA ########################
LABEL org.opencontainers.image.vendor="MSKCC"
LABEL org.opencontainers.image.authors="Ronak H Shah (shahr2@mskcc.org)" 

LABEL org.opencontainers.image.created=${BUILD_DATE} \ 
      org.opencontainers.image.version=${BUILD_VERSION} \
      org.opencontainers.image.licenses=${LICENSE} \
      org.opencontainers.image.version.picard=${PICARD_VERSION} \
      org.opencontainers.image.version.R=${R_VERSION} \
      org.opencontainers.image.version.java=${JAVA_VERSION} \
      org.opencontainers.image.source.picard="https://sourceforge.net/projects/picard/files/picard-tools/${PICARD_VERSION}/picard-tools-${PICARD_VERSION}.zip" \
      org.opencontainers.image.source.R="r-base"

LABEL org.opencontainers.image.description="This container uses openjdk ${JAVA_VERSION} as the base image to build \
      picard version ${PICARD_VERSION}, \
      R version ${R_VERSION}"

# Install ant, git for building
RUN apt-get update && \
      apt-get --no-install-recommends install -y \
      git \
      unzip \
      wget \
      r-base && \
      apt-get clean autoclean && \
      apt-get autoremove -y

WORKDIR /usr/src

RUN wget "https://sourceforge.net/projects/picard/files/picard-tools/${PICARD_VERSION}/picard-tools-${PICARD_VERSION}.zip" && \
      unzip picard-tools-${PICARD_VERSION}.zip && \
      cp -s /usr/src/picard-tools-${PICARD_VERSION}/* /usr/local/bin/
