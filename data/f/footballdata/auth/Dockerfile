FROM gradle:jdk8-alpine as gradle

MAINTAINER vasko.gal@gmail.com

WORKDIR /app
ADD . /app

USER root

RUN ["gradle", "generate", "build", "-i", "--stacktrace"]

FROM openjdk:8-jre-alpine

COPY --from=gradle /app/build/libs/app.jar /app/app.jar
RUN mkdir /app/config
WORKDIR /app

EXPOSE 8082
ENTRYPOINT ["java", "-jar", "app.jar"]
CMD []