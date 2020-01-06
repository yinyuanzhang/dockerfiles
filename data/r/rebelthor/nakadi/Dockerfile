# Build phase
FROM openjdk:latest as builder
ADD ./ /usr/src/
WORKDIR /usr/src
RUN ./gradlew build -x test


# Image phase
FROM registry.opensource.zalan.do/stups/openjdk:8-54

MAINTAINER Team Aruha, team-aruha@zalando.de

WORKDIR /
COPY --from=builder /usr/src/build/libs/nakadi.jar nakadi.jar
ADD api/nakadi-event-bus-api.yaml nakadi-event-bus-api.yaml

EXPOSE 8080

ENTRYPOINT exec java -Djava.security.egd=file:/dev/./urandom -jar nakadi.jar
