FROM openjdk:8-jre-alpine

RUN mkdir -p /opt/shinyproxy/
RUN wget https://www.shinyproxy.io/downloads/shinyproxy-2.3.0.jar -O /opt/shinyproxy/shinyproxy.jar

WORKDIR /opt/shinyproxy/

CMD ["java", "-jar", "/opt/shinyproxy/shinyproxy.jar"]
