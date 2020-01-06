FROM java:openjdk-7-jdk

# Install maven
RUN apt-get update  
RUN apt-get install -y maven

WORKDIR /code

ADD pom.xml /code/pom.xml
RUN ["mvn", "dependency:resolve"]  

ADD src /code/src  
RUN ["mvn", "package"]

EXPOSE 8080

CMD ["java", "-jar", "target/hello-0.1.0.jar"]
