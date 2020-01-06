FROM maven:3.5.4-jdk-8-alpine AS MAVEN_TOOL_CHAIN

COPY pom.xml /tmp/
COPY src /tmp/src/
WORKDIR /tmp/
RUN mvn package -Drolemaster-final-jar-name=app

FROM openjdk:8-jdk-alpine
MAINTAINER A. Filip Wojenko <aleksander@wojenko.de>

ENV ROLEMASTER_ENV=docker

EXPOSE 8081

WORKDIR /tmp
COPY --from=MAVEN_TOOL_CHAIN /tmp/target/app.jar /app.jar
ENTRYPOINT ["/usr/bin/java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app.jar"]
