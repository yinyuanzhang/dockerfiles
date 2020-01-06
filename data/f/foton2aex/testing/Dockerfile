#######################################
#                                     #
#             Build part              #
#                                     #
#######################################
FROM maven:3.5-jdk-8 AS build  
COPY src /usr/src/app/src  
COPY pom.xml /usr/src/app  
RUN mvn -f /usr/src/app/pom.xml clean package -DskipTests

#######################################
#                                     #
#             Image part              #
#                                     #
#######################################
FROM openjdk:8-jre-alpine3.9
COPY --from=build /usr/src/app/target/service-test-1.0.0-SNAPSHOT.jar /usr/app/service-test-1.0.0-SNAPSHOT.jar
EXPOSE 8081
ENTRYPOINT ["java","-jar","-XX:+UnlockExperimentalVMOptions","-XX:+UseCGroupMemoryLimitForHeap","/usr/app/service-test-1.0.0-SNAPSHOT.jar"]


