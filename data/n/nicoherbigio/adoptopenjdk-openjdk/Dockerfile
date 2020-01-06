FROM nicoherbigio/debian:stretch

LABEL maintainer="Nico Herbig <nico@nicoherbig.io>"


# Install Adopt Open Java Development Kit (AdoptOpenJDK)

ARG JAVA_DOWNLOAD_URL=https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u232-b09/OpenJDK8U-jdk_x64_linux_hotspot_8u232b09.tar.gz

ARG JAVA_INSTALL_DIR=/opt/java/openjdk

RUN set -euxo \
    && apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates fontconfig \
    && mkdir -p ${JAVA_INSTALL_DIR} \
    && curl -fSL ${JAVA_DOWNLOAD_URL} | tar -xz --no-same-owner --strip-components=1 -C ${JAVA_INSTALL_DIR} \
    && apt-get remove -y curl ca-certificates \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=${JAVA_INSTALL_DIR}
ENV PATH="${JAVA_INSTALL_DIR}/bin:${PATH}"
ENV JAVA_TOOL_OPTIONS="-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap"
