# Updated as of Aug 16, 2017
# FROM specified which image i want to download
# Needs to be provided before any other section of code.
FROM tomcat:8.5

# Author of the Docker File
# MAINTAINER has been deprecated for LABEL, 
# LABEL is a key value pair 
LABEL maintainer="Gabriele Del Monte"

# In order to have a correct function in this case we have to launch a 'mvn clean package' to generate the .war file
# before building the image from this Dockerfile
# Copy the WAR file into the 'webapps' Tomcat folder inside the container
#COPY docker-spring-mvc/target/docker-spring-mvc.war /usr/local/tomcat/webapps/docker-spring-mvc.war
COPY docker-spring-mvc.war /usr/local/tomcat/webapps/docker-spring-mvc.war