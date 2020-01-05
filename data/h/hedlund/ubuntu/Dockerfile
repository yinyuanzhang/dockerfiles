FROM ubuntu:xenial
MAINTAINER henrik@hedlund.im

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set the timezone
RUN echo "Europe/Oslo" > /etc/timezone

# Install curl
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y curl

# Set xterm so we can use nano and other editors
ENV TERM xterm
