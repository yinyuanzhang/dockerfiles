# Start with a base image containing Java runtime
FROM maven

# Add Maintainer Info
LABEL maintainer="aforoughipour@gmail.com"
COPY src /home/app/src
COPY pom.xml /home/app
WORKDIR /home/app
#building the project
RUN mvn clean
RUN  mvn install
# Make port 8080 available to the world outside this container
EXPOSE 8090

# Run the jar file
ENTRYPOINT ["java","-jar","/home/app/target/electionportal-1.0-SNAPSHOT.jar"]
