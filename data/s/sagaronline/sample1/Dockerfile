FROM openjdk:8-jdk-alpine
RUN mkdir app
COPY target/helloworld.jar app/app.jar
ENTRYPOINT ["java","-jar","app/app.jar", "com.baeldung.application.Application"]