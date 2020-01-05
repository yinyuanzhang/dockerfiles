FROM openjdk:9

MAINTAINER Scott Markwell <scott@blurryworks.com>

RUN mkdir -p /opt/youtrack && \
curl -o /opt/youtrack/youtrack.jar -L https://download.jetbrains.com/charisma/youtrack-2018.3.47247.jar

EXPOSE 80/tcp
VOLUME [ "/data" ]
CMD java -Djava.awt.headless=true -Ddatabase.location=/data -Djetbrains.youtrack.baseUrl=${SERVER_URL} -jar /opt/youtrack/youtrack.jar --J-Xmx1g --J-XX:MaxMetaspaceSize=250m 80

