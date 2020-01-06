# Docker Asciidoctor - Dockerfile

# Mario Ban, 2019-08, based on https://hub.docker.com/r/asciidoctor/docker-asciidoctor

FROM asciidoctor/docker-asciidoctor

LABEL version="1.0.0"
LABEL maintainer="Mario Ban <mario.ban@bluewin.ch>"

# Set user to use
USER root

# Install additional packages
RUN apk add --no-cache \
      joe \
      vim

# Set timezone CET (UTC+1)
# (see https://serverfault.com/questions/683605)
RUN cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime

# Add user and group
RUN addgroup -g 1000 -S docker && adduser -u 1000 -S docker -G docker

# Set user to use
USER docker:docker

# Aliases
RUN echo "alias ll='ls -l'" >> /home/docker/.bashrc

# Create and set working directory
WORKDIR /data

# Create mount point /data to hold an externally mounted volume
VOLUME ["/data"]

# Set the default command to run when starting the container
ENTRYPOINT ["/bin/bash"]
