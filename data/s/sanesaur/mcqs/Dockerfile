#Checking pipeline
FROM openjdk:8u111-jdk-alpine

EXPOSE 8080

RUN mkdir apps

ADD ./target/questions-0.0.1-SNAPSHOT.jar ./apps/

RUN chmod 777 -R ./apps

ENTRYPOINT [ "java", "-jar", "./apps/questions-0.0.1-SNAPSHOT.jar" ]