FROM bezyxel/legacy-gemini-build-u1804:latest

MAINTAINER maik.dybek@zyxel.eu

# Set environment variables.
# define home directory
USER root

# Update apt list
RUN apt-get update

RUN apt-get install -y libmicrohttpd-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y libpcre3-dev

# Clean up apt to save space
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install script to check for installed components
#COPY run_docker_tests.sh /work
#RUN chmod a+rx /work/run_docker_tests.sh

# define the default user when starting the container
# give user with docker run -u
USER heinzm
