FROM maven:3.6.0-jdk-11-slim AS builder
COPY src /home/app/src
COPY pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package

FROM openjdk:8-jre-alpine
WORKDIR /user/app
COPY --from=builder  /home/app/target/*.jar ./
CMD ["java","-Dspring.profiles.active=container", "-jar", "./spend-boot-0.0.1-SNAPSHOT.jar"]
EXPOSE 8080
