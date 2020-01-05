#
# Maven with OpenJDK-8 running on Alpine Linux image
#

FROM java:openjdk-8-jdk-alpine
MAINTAINER IFlavours's Docker Team <docker@iflavours.nl>

ENV MAVEN_VERSION 3.3.9
ENV MAVEN_ARCHIVE http://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz

RUN apk --update add --no-cache bash wget curl tar git && \
    wget ${MAVEN_ARCHIVE} && \
    tar -xf apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /usr/local && \
    mv /usr/local/apache-maven-${MAVEN_VERSION} /usr/local/maven && \
    rm apache-maven-${MAVEN_VERSION}-bin.tar.gz

ENV MAVEN_HOME /usr/local/maven
ENV PATH=${PATH}:${MAVEN_HOME}/bin

VOLUME [ "/code" ]
WORKDIR /code
