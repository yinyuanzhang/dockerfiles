FROM        openjdk:8-jdk-alpine

RUN         apk update
RUN         apk add maven

RUN         mkdir /app
WORKDIR     /app
ADD         pom.xml .
RUN         mvn dependency:go-offline
ADD         src src

RUN         mvn clean package

RUN         apk del maven

ENTRYPOINT  ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "target/hub-release.jar"]
