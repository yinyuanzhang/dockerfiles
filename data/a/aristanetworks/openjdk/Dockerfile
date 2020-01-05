# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

FROM aristanetworks/base:2.3
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

RUN apk add openjdk8=8.191.12-r0

ENV JMXP_VERSION 0.10
# Install jmx prometheus exporter
RUN wget -nv -O /usr/lib/jvm/default-jvm/jre/lib/jmx_prometheus_javaagent-${JMXP_VERSION}.jar \
    https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/${JMXP_VERSION}/jmx_prometheus_javaagent-${JMXP_VERSION}.jar \
  && echo "b4cbd620adc89baabf7752ab74ee2ed8b7aecdcd  /usr/lib/jvm/default-jvm/jre/lib/jmx_prometheus_javaagent-${JMXP_VERSION}.jar" | sha1sum -c -
