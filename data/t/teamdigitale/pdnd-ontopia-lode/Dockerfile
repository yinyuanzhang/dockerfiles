FROM openjdk:8

RUN apt-get update && apt-get -y install maven git

RUN git clone https://github.com/essepuntato/LODE.git lode

# Override Jetty configuration to enable HTTPS
COPY pom.xml lode/pom.xml

WORKDIR /lode

# Follow HTTP(s) schema while downloading CSS and JS files
RUN sed -i 's/"http:\/\/"/"\/\/"/g' src/main/java/it/essepuntato/lode/LodeServlet.java

EXPOSE 8080 8443

ENTRYPOINT ["mvn", "jetty:run"]
