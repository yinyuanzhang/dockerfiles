FROM openjdk:11-jre-slim

COPY ./target/aristotle-0.0.0-DEVEL.jar /usr/app/

WORKDIR /usr/app

RUN sh -c 'touch aristotle-0.0.0-DEVEL.jar'

ENTRYPOINT ["java","-jar","aristotle-0.0.0-DEVEL.jar"]