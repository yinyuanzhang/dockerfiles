FROM openjdk:12-alpine

# Download Awtrix Server jar
RUN apk add --no-cache wget
RUN wget -O /opt/awtrix.jar https://blueforcer.de/awtrix/beta/awtrix.jar

# Web Ui Server Port
EXPOSE 7000
# Matrix Port
EXPOSE 7001

WORKDIR /opt

# Start Server
CMD ["java","-jar","/opt/awtrix.jar"]
