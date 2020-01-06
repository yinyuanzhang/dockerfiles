FROM openjdk:8-jre

WORKDIR usr/app/shinyproxy

COPY shinyproxy-1.0.2.jar ./

COPY logo.png ./
COPY application.yml ./

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "shinyproxy-1.0.2.jar"]
