# DESCRIPTION:  Create the EPF Composer in a container
# AUTHOR:       Diego Casas <diego@acurable.com>
# COMMENTS:
#	  This file describes how to build the EPF Composer
#	  in a container with all dependencies installed.
#
# USAGE:
#	  # Download  Dockerfile
#	  wget https://raw.githubusercontent.com/jessfraz/dockerfiles/master/atom/Dockerfile
#
#	  # Build atom image
#	  docker build -t atom .
#
#	  docker run -v /tmp/.X11-unix:/tmp/.X11-unix \
#		           -e DISPLAY=unix$DISPLAY atom
#

# Base docker image
FROM nginx:alpine
MAINTAINER "Diego Casas <diego@acurable.com>"

WORKDIR /usr/share/nginx/html
COPY ./site .
