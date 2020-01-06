FROM maven:3.5-jdk-8-slim

COPY mvn-init.sh /usr/bin/mvn-init
COPY mvn-setversion.sh /usr/bin/mvn-setversion
COPY mvn-mule-deploy.sh /usr/bin/mvn-mule-deploy
RUN chmod +x /usr/bin/mvn-init /usr/bin/mvn-setversion /usr/bin/mvn-mule-deploy
