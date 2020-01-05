#FROM phusion/baseimage:0.9.17

FROM ubuntu

MAINTAINER Marcin Mejran "marcin@teachingmachines.io"

# Update aptitude with new repo
# Install other software
RUN apt-get -y update && apt-get install -y \
	graphviz \
	default-jdk \
	maven \
	git

# Clone the graphviz-server github repo
RUN git clone https://github.com/teachingmachines/graphviz-server.git /opt/graphviz-server

# Expose port 8080 to the host
EXPOSE 80

# Set the current work directory
WORKDIR /opt/graphviz-server

# If you want to run maven to package the jar with dependencies yourself
#RUN mvn package

# Run graphviz-server
ENTRYPOINT ["java", "-jar", "/opt/graphviz-server/dist/DotGraphics.jar","80"]
