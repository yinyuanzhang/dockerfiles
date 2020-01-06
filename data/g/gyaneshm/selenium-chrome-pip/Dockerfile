FROM selenium/standalone-chrome

# Add maintainer information
LABEL maintainer="Gyanesh Mishra <gyanesh.mishra10@gmail.com>"

# Install pip
USER root
RUN apt-get update -y
RUN apt-get install -y python3-pip

# Install selenium
RUN pip3 install selenium