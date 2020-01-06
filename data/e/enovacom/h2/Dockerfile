FROM debian:stable-20181112 as builder

RUN apt-get update \
 && apt-get install -y curl=7.52.1-5+deb9u8

ARG VERSION=1.4.197

RUN curl "http://central.maven.org/maven2/com/h2database/h2/${VERSION}/h2-${VERSION}.jar" -o /opt/h2.jar

FROM openjdk:8u181-jdk-alpine3.8

LABEL maintainer="Sylvain Brocard sbrocard@enovacom.fr"

RUN addgroup -S h2 && adduser -S -G h2 h2

USER h2

RUN mkdir /home/h2/data

COPY --from=builder --chown=h2:h2 /opt/h2.jar /home/h2/h2.jar

EXPOSE 9092

VOLUME ["/home/h2/data"]

ENV JAVA_TOOL_OPTIONS="-Xms16m -Xmx128m"

HEALTHCHECK --interval=10s --start-period=60s --timeout=3s \
  CMD nc -z localhost 9092 || exit 1

# Use JAVA_TOOL_OPTIONS to add custom JVM parameters
ENTRYPOINT ["java", "-server", "-XX:+UnlockExperimentalVMOptions", "-XX:+UseCGroupMemoryLimitForHeap", "-cp", "/home/h2/h2.jar", "org.h2.tools.Server"]
CMD ["-tcp", "-tcpAllowOthers", "-tcpPort", "9092", "-baseDir", "/home/h2/data"]