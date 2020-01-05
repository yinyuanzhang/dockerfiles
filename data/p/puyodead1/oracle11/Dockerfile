#
# Oracle Java 8 Dockerfile
#
# https://github.com/dockerfile/java
# https://github.com/dockerfile/java/tree/master/oracle-java8
#

# Pull base image.
FROM puyodead1/ubuntu

# Install Java.
RUN \
  apt-get update && \
  apt-get upgrade && \
  apt-get install -y python-software-properties debconf-utils && \
  add-apt-repository ppa:linuxuprising/java && \
  apt-get update && \
  echo debconf shared/accepted-oracle-license-v1-2 select true | debconf-set-selections && \
  echo debconf shared/accepted-oracle-license-v1-2 seen true | debconf-set-selections && \
  apt-get install -y oracle-java11-installer

# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-11-oracle

# Define default command.
CMD ["bash"]
