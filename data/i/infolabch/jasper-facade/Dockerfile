FROM zenika/alpine-maven:3-jdk8 as builder

WORKDIR /build

COPY src /build/src/
COPY pom.xml /build/

RUN mvn package

FROM openjdk:8-jdk-alpine

RUN apk update
RUN apk add ttf-dejavu

VOLUME /tmp

ARG DEPENDENCY=/build/target/dependency

COPY --from=builder ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY --from=builder ${DEPENDENCY}/META-INF /app/META-INF
COPY --from=builder ${DEPENDENCY}/BOOT-INF/classes /app

ENTRYPOINT ["java","-cp","app:app/lib/*","ch.infolab.infocentre.reporting.Application"]
