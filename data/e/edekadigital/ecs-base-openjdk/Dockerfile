FROM openjdk:11.0-jre

MAINTAINER EDEKA DIGITAL GmbH <dpp@edeka.de>

# Relocate the timezone file
RUN echo UTC | tee /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# Define the application version for the subsequent application images
ENV VERSION=1.0.0

# Define the spring boot configuration directory
ENV CONFIG_DIR=/opt/edeka/configuration

# Define the spring boot application name
ENV APP_NAME edekadigitalapp

# Define the spring boot application port
ENV APP_PORT 8000

# Define the java options
ENV JAVA_OPTS="-XX:+ExitOnOutOfMemoryError -XX:MinRAMPercentage=90 -XX:MaxRAMPercentage=90"

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:$APP_PORT/health || exit 1

# Ports
EXPOSE $APP_PORT

# Run it
ENTRYPOINT exec java $JAVA_OPTS -jar /app.jar
