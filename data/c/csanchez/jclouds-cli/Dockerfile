FROM openjdk:8-jre-alpine

ARG JCLOUDS_VERSION=2.1.0
ENV JCLOUDS_VERSION=${JCLOUDS_VERSION}

RUN apk add --no-cache curl bash

RUN wget http://search.maven.org/remotecontent?filepath=org/apache/jclouds/cli/jclouds-cli-assembly/${JCLOUDS_VERSION}/jclouds-cli-assembly-${JCLOUDS_VERSION}.tar.gz -O - | tar -xz

ENV PATH=${PATH}:/jclouds-cli-${JCLOUDS_VERSION}/bin
CMD /jclouds-cli-${JCLOUDS_VERSION}/bin/jclouds-cli
