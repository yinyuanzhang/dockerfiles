#
# SBT image based on Oracle JRE 8
#

FROM 1science/java:oracle-jre-8
MAINTAINER 1science Devops Team <devops@1science.org>

ENV SBT_VERSION 1.1.0
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

# Install sbt
RUN curl -sL "https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz" | gunzip | tar -x -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built

# Download binaries
RUN sbt sbtVersion

WORKDIR /app
