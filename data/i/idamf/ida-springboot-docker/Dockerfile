FROM openjdk:8-jdk-alpine

WORKDIR /app

COPY ./ /app

RUN ./mvnw install

ENV JAVA_OPTS=""

ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app/target/aurora-0.0.1-SNAPSHOT.jar