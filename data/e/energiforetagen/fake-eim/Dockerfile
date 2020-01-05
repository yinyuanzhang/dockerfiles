ARG VERSION=8u222-jdk
ARG GRADLE=5.5.1-jdk

FROM gradle:$GRADLE as builder

ENV GRADLE_USER_HOME=/build
WORKDIR $GRADLE_USER_HOME
USER root

COPY gradle.* ./
COPY *.gradle ./
COPY src src

RUN gradle --no-daemon installDist

FROM openjdk:$VERSION as main

ENV BIN_NAME=fakeEIM

WORKDIR /app

COPY --from=builder /build/build/install/*/bin ./bin
COPY --from=builder /build/build/install/*/lib ./lib

COPY src/main/resources/defaults.properties src/main/resources/
COPY src/main/resources/templates src/main/resources/templates

CMD bin/$BIN_NAME
