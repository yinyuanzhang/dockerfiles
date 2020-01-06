FROM openjdk:13-jdk-alpine3.9 AS java
FROM elixir:1.8.2-alpine

MAINTAINER Skyler Nesheim

COPY sbt-project /sbt-project
COPY ruby /ruby
COPY --from=java /opt/openjdk-13 /opt/openjdk-13

ENV JAVA_HOME=/opt/openjdk-13 \
    SBT_VERSION=1.2.8 \
    SBT_HOME=/usr/local/sbt

ENV PATH=${JAVA_HOME}/bin:${SBT_HOME}/bin:${PATH}

RUN apk add --update \
    curl \
    bash \
    ruby \
    ruby-dev \
    python \
    libffi-dev \
    build-base \
    make \
    libc-dev && \
    curl -sL "https://github.com/sbt/sbt/releases/download/v1.2.8/sbt-1.2.8.tgz" -o /tmp/sbt-1.2.8.tgz && \
    tar xzf /tmp/sbt-1.2.8.tgz -C /usr/local && \
    gem install --no-ri --no-doc bundler && \
    cd /sbt-project && \
    sbt compile && \
    cd ../ruby && \
    bundle install
