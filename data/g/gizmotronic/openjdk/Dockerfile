#
# OpenJDK 8 Dockerfile
#

# Pull base image.
FROM ubuntu:18.04

ARG version=8u191-b12-2ubuntu0.18.04.1

# Install Java.
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk-headless=${version} && \
  rm -rf /var/lib/apt/lists/*


# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Define default command.
CMD ["bash"]
