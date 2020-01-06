# Set the base image to use to Ubuntu
FROM python:3

# Set the file maintainer (your name - the file's author)
MAINTAINER Daniel Valenzuela

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKER_SRC=fbcleaner
# Directory in container for all project files
ENV DOCKER_APPHOME=/app
# Directory in container for project source files
ENV DOCKER_APPPROJ=/app/fbcleaner

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python-pip

# Create application subdirectories
WORKDIR $DOCKER_APPHOME
RUN mkdir media static logs
VOLUME ["$DOCKER_APPHOME/media/", "$DOCKER_APPHOME/logs/"]

# Copy application source code to SRCDIR
COPY $DOCKER_SRC $DOCKER_APPPROJ

# Install Python dependencies
RUN pip install -r $DOCKER_APPPROJ/requirements.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $DOCKER_APPPROJ
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]