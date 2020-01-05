FROM openjdk:12-jdk-alpine
MAINTAINER Bola Taylor
EXPOSE 8080
ADD /target/capDistroApp-1.0-SNAPSHOT.jar capDistroApp-1.0-SNAPSHOT.jar
CMD java -jar capDistroApp-1.0-SNAPSHOT.jar
ENTRYPOINT ["java", "-jar", "capDistroApp-1.0-SNAPSHOT.jar"]