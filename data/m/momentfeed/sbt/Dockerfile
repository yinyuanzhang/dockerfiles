FROM openjdk:8

ARG SBT_VERSION
ENV SBT_VERSION ${SBT_VERSION:-1.3.2}

RUN set -ex; \
  curl -sLO https://piccolo.link/sbt-${SBT_VERSION}.tgz; \
  tar xf sbt-${SBT_VERSION}.tgz -C /usr/local/; \
  rm sbt-${SBT_VERSION}.tgz; \
  useradd -m -s /bin/bash sbtuser; \
  mkdir /app; \
  chown sbtuser:sbtuser /app

USER sbtuser
WORKDIR /app

ENV PATH /usr/local/sbt/bin:${PATH}
