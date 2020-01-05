FROM ubuntu:18.04
MAINTAINER Sylvestre Wa.
RUN apt-get update
RUN apt-get install -y maven
COPY pom.xml /usr/local/service/pom.xml
COPY docker.sh /usr/local/service/docker.sh
COPY src /usr/local/service/src
WORKDIR /usr/local/service
RUN mvn package
ENTRYPOINT ["./docker.sh"]
