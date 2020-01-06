FROM anapsix/alpine-java:jdk8

MAINTAINER Liu Yiding<odinushuaia@gmail.com>

RUN apk update && apk add ca-certificates openssl && apk add git

RUN wget https://dl.bintray.com/sbt/native-packages/sbt/0.13.11/sbt-0.13.11.tgz && \
tar -xvf sbt-0.13.11.tgz && \
mv sbt /opt/ && rm -rf sbt-0.13.11.tgz

RUN /opt/sbt/bin/sbt sbt-version
ENV SBT_HOME=/opt/sbt
ENV PATH=$SBT_HOME/bin:$PATH
