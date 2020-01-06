FROM openjdk:8

# Setup Grails path.
ENV GRAILS_HOME /usr/lib/jvm/grails
ENV GRADLE_USER_HOME /gradle
ENV PATH $GRAILS_HOME/bin:$PATH

# Create App Directory
RUN mkdir /app

EXPOSE 8080

# Set Workdir
WORKDIR /app
