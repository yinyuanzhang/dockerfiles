FROM alpine:3.7

MAINTAINER Arun Allamsetty <arun.allamsetty@gmail.com>

ENV USER docker
ENV USERNAME "Docker User"

# Install 'bash' as many installations require that to run. 'shadow' provides user modification
# functions which we use.
RUN apk add --no-cache --update \
      bash \
      shadow && \
    rm -rf /var/cache/apk/*

# Create a 'docker' user because we might not want to run everything as 'root'. Use 9999 as the ID
# to keep it specific and away from the IDs in the host system. Also, lock the user to avoid 
# unwanted logins into a Docker container using the 'docker' user as a security measure.
RUN addgroup -g 9999 $USER && \
    adduser -u 9999 -G $USER -g "$USERNAME" -s /bin/bash -D $USER && \
    usermod -L $USER

# Create a 'app' directory to house application specific code when this image or one of its'
# children are being used as a base image for running applications/tests.
ENV APP_DIR /usr/src/app
RUN mkdir -p $APP_DIR && \
    chown -R $USER:$USER $APP_DIR

# Switch to the user 'docker'.
USER $USER
