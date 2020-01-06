FROM centos:latest
LABEL maintainer="loind89@gmail.com"

USER root
# Install packages necessary
RUN yum update -y \
    && yum -y install unzip wget curl telnet \
    && yum clean all

# Create a user and group used to launch processes
# The user ID 1000 is the default for the first "regular" user on Fedora/RHEL,
# so there is a high chance that this ID will be equal to the current user
# making it easier to use volumes (no permission issues)

# Set the working directory to jboss' user home directory
WORKDIR /app

# Specify the user which should be used to execute all commands below
#USER bootapp