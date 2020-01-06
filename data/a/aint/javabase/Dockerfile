FROM adoptopenjdk/openjdk11:latest AS builder

LABEL maintainer="olexandr.tyshkovets@gmail.com"

RUN jlink \
      --compress=2 \
      --add-modules java.base,java.logging,java.xml,java.sql,java.desktop,java.naming,java.security.jgss,java.management,java.instrument,jdk.unsupported \
      --no-header-files \
      --no-man-pages \
      --strip-debug \
      --output /opt/jre

FROM debian:9-slim

COPY --from=builder /opt/jre /opt/jre

ENV JAVA_HOME=/opt/jre

ENV PATH="$PATH:$JAVA_HOME/bin"
