FROM openjdk:8u141-jre
VOLUME /tmp
ADD target/gs-spring-boot-docker-0.1.0.jar app.jar
ENTRYPOINT exec java -jar app.jar