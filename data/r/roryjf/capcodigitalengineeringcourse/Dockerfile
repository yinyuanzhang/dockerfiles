FROM openjdk:8-jdk-alpine
RUN mkdir -p /app
ARG JAR_FILE=build/libs/capcodigitalengineeringcourse-0.1.0.jar
ADD ${JAR_FILE} /app/app.jar
ENTRYPOINT ["/usr/bin/java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app/app.jar"]