# This a docker file with multi-stage builds.

# Stage number one building the code with maven.
FROM maven as build
WORKDIR /service
COPY pom.xml .
COPY src/ src/
RUN mvn install

# Stage number two running the jar file from stage one. 
FROM openjdk:8
WORKDIR /service
COPY --from=build /service/target/authserver-2.jar /service
EXPOSE 8080
CMD ["java","-Dspring.profiles.active=prod","-jar","authserver-2.jar"]
