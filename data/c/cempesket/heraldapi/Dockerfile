FROM maven:3.3-jdk-8-onbuild
FROM java:8
EXPOSE 8080
COPY --from=0 /usr/src/app/target/heraldapi-0.0.1-SNAPSHOT.jar /opt/heraldapi.jar
CMD ["java","-jar","/opt/heraldapi.jar"]

