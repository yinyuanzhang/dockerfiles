# Pull base image.
FROM node:alpine

# Maintainer
MAINTAINER Andre Marcelo-Tanner <andre@enthropia.com>

# Install Bower & Gulp
RUN npm install -g bower

# Install Git
RUN apk update && apk upgrade \
	&& apk add --no-cache \
    	bash \
    	git \
    	openssh

# Define working directory.
WORKDIR /data

# Define default command.
ENTRYPOINT ["bower", "--allow-root", "--config.interactive=false"]

# Default param
CMD ["install"]