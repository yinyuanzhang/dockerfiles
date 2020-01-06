FROM openjdk:8-jre-alpine


ENV JAVA_OPTS="" \
    PORT="8081"

CMD java ${JAVA_OPTS} -jar /opt/app.jar -p ${PORT}

ADD ./JrebelBrainsLicenseServer.jar /opt/app.jar