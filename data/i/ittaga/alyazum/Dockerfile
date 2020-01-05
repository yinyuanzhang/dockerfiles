FROM gradle:jdk8-alpine as builder

COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle build --no-daemon

FROM openjdk:8-jdk-alpine

EXPOSE 8080

COPY --from=builder /home/gradle/src/build/libs/*.jar /app.jar

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
