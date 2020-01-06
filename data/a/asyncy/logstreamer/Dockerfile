FROM        openjdk:12.0.1-jdk-oracle

RUN         mkdir /app
WORKDIR     /app
ADD         .mvn .mvn
ADD         mvnw .

RUN         ./mvnw -v

ADD         pom.xml .
ADD         src src

RUN         ls  /app/
RUN         ./mvnw compile assembly:single

ENTRYPOINT  java -jar /app/target/log-streamer-1.0-SNAPSHOT-jar-with-dependencies.jar