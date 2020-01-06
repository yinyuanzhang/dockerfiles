FROM maven:3-jdk-8-alpine as BUILD

ARG SPRING_CLOUD_CONFIG_VERSION="2.0.1.RELEASE"
ARG SPRING_BOOT_VERSION="2.0.4.RELEASE"

WORKDIR /opt

COPY pom.xml pom.xml

RUN mvn package \
 -Dspring.cloud.config.version=${SPRING_CLOUD_CONFIG_VERSION} \
 -Dspring.boot.version=${SPRING_BOOT_VERSION}

FROM openjdk:8-jre-alpine as RUN

ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1"

COPY --from=BUILD /opt/target/app-1.jar /opt/app.jar

WORKDIR /opt

EXPOSE 8888

HEALTHCHECK --interval=2s --start-period=15s \
 CMD wget --quiet --tries=1 --spider http://localhost:8888/actuator/health || exit 1

ENTRYPOINT ["sh", "-c", "java ${JAVA_OPTS} -jar app.jar"]
