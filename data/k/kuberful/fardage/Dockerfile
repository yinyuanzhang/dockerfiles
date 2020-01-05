FROM maven:3.6.2-jdk-11-slim as maven

COPY ./pom.xml ./pom.xml

RUN mvn dependency:go-offline -B

COPY ./src ./src

RUN mvn package

FROM openjdk:11.0-jre-slim

WORKDIR /usr/src/app
COPY --from=maven target/*.jar .

CMD java -jar ${JAVA_OPTS} *.jar
