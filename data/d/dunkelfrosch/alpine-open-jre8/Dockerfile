#
# BUILD    : DF/[CORE][ALPINE][OPENJDK/JRE]
# OS/CORE  : alpine:3.7
# SERVICES : ...
#
# VERSION 1.0.1
#

FROM dunkelfrosch/alpine:3.7

LABEL maintainer="Patrick Paechnatz <patrick.paechnatz@gmail.com>" \
      com.container.vendor="dunkelfrosch impersonate" \
      com.container.service="core/alpine/jdk8" \
      com.container.priority="1" \
      com.container.project="alpine/jdk8" \
      img.version="1.0.1" \
      img.description="alpine base image container for JRE/JDK 8"

# build parameters
ARG JAVA_DISTRIBUTION=jdk
ARG JAVA_MAJOR_VERSION=8
ARG JAVA_UPDATE_VERSION=192
ARG JAVA_BUILD_NUMBER=12
ARG JAVA_HASH=750e1c8617c5452694857ad95c3ee230
ARG GLIBC_VERSION=2.27-r0

#https://download.oracle.com/otn-pub/java/jdk/8u192-b12/750e1c8617c5452694857ad95c3ee230/jre-8u192-linux-x64.tar.gz
ENV TERM="xterm" \
    TIMEZONE="Europe/Berlin" \
    LANG="en_US.UTF-8" \
    JAVA_VERSION=${JAVA_MAJOR_VERSION}.${JAVA_UPDATE_VERSION}.${JAVA_BUILD_NUMBER} \
    JAVA_PACKAGE_POSTFIX_VERSION="-jre" \
    JAVA_HOME="/usr/lib/jvm/default-jvm" \
    JAVA_HASH_EXTENTION=${JAVA_HASH} \
    JAVA_TARBALL=${JAVA_DISTRIBUTION}-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz \
    JAVA_URL=http://download.oracle.com/otn-pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/${JAVA_HASH} \
    PATH=$PATH:$JAVA_HOME/bin

# prepare base sytem JRE8
RUN mkdir -p /opt/java && \
    apk add --update curl wget ca-certificates unzip tini; cd /opt && \
    wget --quiet --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" ${JAVA_URL}/${JAVA_TARBALL} && \
    tar zxf ${JAVA_DISTRIBUTION}-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz  && \
    ln -s /opt/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION} /opt/jdk && \
    ln -s /opt/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}/bin/* /usr/bin && \
    wget --quiet --directory-prefix=/tmp https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \
    wget --quiet --directory-prefix=/tmp https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk && \
    wget --quiet --directory-prefix=/tmp https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk && \
    apk add --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk && \
    apk add --allow-untrusted /tmp/glibc-bin-${GLIBC_VERSION}.apk && \
    apk add --allow-untrusted /tmp/glibc-i18n-${GLIBC_VERSION}.apk && \
    /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8

RUN apk del ca-certificates wget curl && \
    rm -rf ${JAVA_DISTRIBUTION}-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz \
            /opt/jdk/*src.zip \
            /opt/jdk/lib/missioncontrol \
            /opt/jdk/lib/visualvm \
            /opt/jdk/lib/*javafx* \
            /opt/jdk/jre/lib/plugin.jar \
            /opt/jdk/jre/lib/ext/jfxrt.jar \
            /opt/jdk/jre/bin/javaws \
            /opt/jdk/jre/lib/javaws.jar \
            /opt/jdk/jre/lib/desktop \
            /opt/jdk/jre/plugin \
            /opt/jdk/jre/lib/deploy* \
            /opt/jdk/jre/lib/*javafx* \
            /opt/jdk/jre/lib/*jfx* \
            /opt/jdk/jre/lib/amd64/libdecora_sse.so \
            /opt/jdk/jre/lib/amd64/libprism_*.so \
            /opt/jdk/jre/lib/amd64/libfxplugins.so \
            /opt/jdk/jre/lib/amd64/libglass.so \
            /opt/jdk/jre/lib/amd64/libgstreamer-lite.so \
            /opt/jdk/jre/lib/amd64/libjavafx*.so \
            /opt/jdk/jre/lib/amd64/libjfx*.so \
            /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*
