FROM maven:3.6.0-jdk-8-slim

WORKDIR /var/partner-api-mare/

ADD . /var/partner-api-mare/

RUN sed -i 's/localhost/partner-api-db/' /var/partner-api-mare/src/main/resources/hibernate.cfg.xml

RUN mvn clean package -DskipTests -Ddir="/var/partner-api-mare/"

RUN cp /var/partner-api-mare/target/partner-api-0.0.1-SNAPSHOT.jar /partner-api.jar

RUN rm -rf /var/partner-api-mare/

EXPOSE 8080

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-Djava.awt.headless=true","-jar","/partner-api.jar"]
