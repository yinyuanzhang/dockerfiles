FROM maven:3.6.1-jdk-8-slim AS build

WORKDIR /build

COPY . . 

RUN mvn package -Pprod

FROM openjdk:8-jdk-alpine

ENV TZ=Europe/Oslo \
    SPRING_OUTPUT_ANSI_ENABLED=ALWAYS \
    SLEEP_TIME=0 \
    JAVA_OPTS=""

COPY --from=0 /build/management-ui/target/management-ui.war .

EXPOSE 8080

ENTRYPOINT ["java","-jar","management-ui.war"]  
