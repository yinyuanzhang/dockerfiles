FROM maven:3.5-jdk-8 AS build  
COPY src /usr/src/app/src  
COPY pom.xml /usr/src/app  
RUN mvn -f /usr/src/app/pom.xml clean package

FROM gcr.io/distroless/java 
COPY --from=build /usr/src/app/target/ht-1.0-SNAPSHOT-jar-with-dependencies.jar /usr/app/ht-1.0-SNAPSHOT-jar-with-dependencies.jar  
EXPOSE 4567  
ENTRYPOINT ["java","-jar","/usr/app/ht-1.0-SNAPSHOT-jar-with-dependencies.jar"] 
