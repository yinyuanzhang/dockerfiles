# Start with a base image containing Java runtime
FROM arm32v7/openjdk

# Database persitency mount point
WORKDIR /db
WORKDIR /

# Make port 8080 available to the world outside this container
EXPOSE 8080

# The application's jar file
ARG JAR_FILE=target/shopping-list-0.0.1-SNAPSHOT.jar

# Add the application's jar to the container
ADD ${JAR_FILE} shopping-list.jar

# Run the jar file 
ENTRYPOINT ["java","-jar","/shopping-list.jar"]