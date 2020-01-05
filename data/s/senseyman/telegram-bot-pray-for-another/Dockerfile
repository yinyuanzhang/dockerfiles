FROM maven:3.6.2-jdk-11-slim as builder
WORKDIR /building
RUN mkdir /output
ADD . .
RUN mkdir -p ~/.m2/repository/
RUN mv libs/gui ~/.m2/repository/

RUN mvn -T 4 clean install  -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn
RUN mv target/$(ls ./target | grep \.jar | grep -v original | grep -v javadoc | grep -v sources) /output/application.jar
RUN rm -rf ~/.m2/
RUN rm -rf /building

# **********************************
# packing jar file to docker image #
# **********************************

FROM openjdk:11-oracle

#RUN apt update && apt install libfreetype6 -y

WORKDIR /app

COPY --from=builder /output/application.jar .

ENTRYPOINT java -Xms128m -Xmx256m -jar application.jar