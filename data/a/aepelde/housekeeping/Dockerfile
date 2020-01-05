FROM maven:3.6.3-jdk-8-slim as build

WORKDIR /housekeeping

COPY ./pom.xml /housekeeping/pom.xml

RUN mvn dependency:go-offline

COPY ./src /housekeeping/src

RUN mvn package

FROM openjdk:8-jdk-alpine

COPY --from=build /housekeeping/target/housekeeping.jar housekeeping.jar

EXPOSE 8080

CMD ["java", "-jar", "/housekeeping.jar"]