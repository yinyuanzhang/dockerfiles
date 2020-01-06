FROM circleci/openjdk:8-jdk

# Install AWS CLI
RUN sudo apt install -y python-pip coreutils
RUN sudo pip install awscli

USER root
# Install Node.js 6 and npm 5
RUN apt-get update
RUN apt-get -qq update
RUN apt-get install -y build-essential
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash
RUN apt-get install -y nodejs
# Create the maven directory
RUN mkdir ~/.m2
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container
ADD . /app
# Install any needed packages specified in requirements.txt
RUN npm install

#Install GULP
RUN npm install -g gulp
RUN gulp -v

# TODO could install other stuff here to speed up deploys, e.g. Terraform.
# Having it already available on the image is faster than downloading it from a cache.
