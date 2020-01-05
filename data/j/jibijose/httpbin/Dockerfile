FROM openjdk:8u232-jdk-slim
LABEL maintainer="jibijose@yahoo.com"
EXPOSE 8080

RUN apt-get update -qq

RUN apt-get install wget -y -qq
RUN wget http://apachemirror.wuchna.com/maven/maven-3/3.6.2/binaries/apache-maven-3.6.2-bin.tar.gz --quiet -O /opt/apache-maven-3.6.2-bin.tar.gz
RUN tar -xvzf /opt/apache-maven-3.6.2-bin.tar.gz -C /opt
RUN rm -rf /opt/apache-maven-3.6.2-bin.tar.gz
RUN mv /opt/apache-maven-3.6.2 /opt/maven

COPY src /tmp/app/src/
COPY templates /tmp/app/templates/
COPY pom.xml /tmp/app/
RUN /opt/maven/bin/mvn -f /tmp/app/pom.xml clean package -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn

RUN mkdir /service
RUN cp /tmp/app/target/httpbin-*.*.*.jar /service/app.jar

RUN rm -rf /tmp/app
RUN rm -rf ~/.m2
RUN rm -rf /opt/maven

ENTRYPOINT ["java", "-jar", "/service/app.jar"]
