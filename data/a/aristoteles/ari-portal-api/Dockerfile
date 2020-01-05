FROM openjdk:8-jdk-alpine

RUN mkdir /workspace

COPY ./ /workspace

#VOLUME /tmp

ENV CONFIG_SERVER_PORT 7000

ENV EJB_URL http-remoting://aristotelles:8080

EXPOSE ${CONFIG_SERVER_PORT}

WORKDIR /workspace

#ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom", "-XX:MaxMetaspaceSize=512m", "-Xmx1024m" , "-jar","/workspace/target/ari-portal-api-1.0.0.jar" , "--spring.profiles.active=dev,fast"]

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom", "-jar","/workspace/target/ari-portal-api-1.0.0.jar" ]
