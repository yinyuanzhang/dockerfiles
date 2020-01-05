# ************************
# building java artifact #
# ************************

FROM maven:3.6.1-jdk-8-slim as builder
WORKDIR /building
ADD . .

RUN mvn -T 4 clean install -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn
RUN mv target/$(ls ./target | grep \.jar | grep -v original | grep -v javadoc | grep -v sources) ./application.jar

# **********************************
# packing jar file to docker image #
# **********************************

FROM anapsix/alpine-java:8

WORKDIR /app

COPY --from=builder /building/application.jar .

ENTRYPOINT java -Xms128m -Xmx256m -jar application.jar