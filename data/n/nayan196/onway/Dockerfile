FROM java:8-jdk-alpine

COPY ./target/onway-0.0.1-SNAPSHOT.jar /usr/app/

WORKDIR /usr/app

RUN sh -c 'touch onway-0.0.1-SNAPSHOT.jar'

ENTRYPOINT ["java","-jar","onway-0.0.1-SNAPSHOT.jar"]