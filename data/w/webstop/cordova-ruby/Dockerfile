# This image adds latest version of ruby to LTS version of 
# node in order to facilitate running `cordova prepare`
# hooks written in ruby.  Also, the other `cordova` commands
# except build or run are supported for managing platform
# and such.

FROM node:10.15.3
MAINTAINER Dan Lynn <docker@danlynn.org>

WORKDIR /myapp

# install bower
RUN \
	npm install -g bower@1.8.8

RUN \
	npm install -g cordova@9.0.0

# Disable cordova telemetry prompt
RUN \
	cordova telemetry off

# Install ruby
RUN \ 
	apt-get update -y &&\
	apt-get install -y ruby &&\
	apt-get install -y git

# set container bash prompt color to green in order to
# differentiate container terminal sessions from host 
# terminal sessions
RUN \
	echo 'PS1="\\[\\e[0;92m\\]\\W\\[\\e[0;36m\\]\\\\$\\[\\e[m\\] "' >> ~/.bashrc
