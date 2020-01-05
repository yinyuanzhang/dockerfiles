FROM openjdk:11-jre-slim

VOLUME /tmp
ADD build/libs/bank_api-0.0.1.jar app.jar
RUN bash -c 'touch /app.jar'
ENTRYPOINT ["java","-jar","/app.jar"]