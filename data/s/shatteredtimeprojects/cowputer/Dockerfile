# our base build image
FROM maven:3.6.1-jdk-13 as maven

# copy the project pom
COPY ./pom.xml ./pom.xml

# build all dependencies
RUN mvn dependency:go-offline -B

# copy other files
COPY ./src ./src

# build for release
RUN mvn package

# our final base image
FROM openjdk:13-jdk-alpine3.9

# set deployment directory
WORKDIR /cowputerbackend

# copy over the built artifact from the maven image
COPY --from=maven target/cowputerbackend-0.5.0-BETA.jar ./

# set the startup commands to run your binary
EXPOSE 8080
RUN chmod +rwx cowputerbackend-0.5.0-BETA.jar
ENTRYPOINT /bin/sh -c 'java -jar cowputerbackend-0.5.0-BETA.jar'