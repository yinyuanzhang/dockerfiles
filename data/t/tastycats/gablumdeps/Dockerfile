FROM maven:3.6.0-jdk-12

COPY / /deps

WORKDIR /deps

RUN mvn dependency:go-offline
