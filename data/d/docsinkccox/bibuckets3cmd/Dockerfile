#Download base image ubuntu 18.04
FROM ubuntu:18.04

# Update Software repository
RUN apt-get update

# Get s3cmd
RUN apt-get install s3cmd -y

# Get Zip
RUN apt-get install zip -y

# Get npm
RUN apt-get install npm -y

# Get npm
RUN apt-get install npm -y

# Get Gulp
RUN npm install --global gulp-cli

RUN apt-get install python3.7 -y
RUN apt-get install python-pip -y

RUN pip install --upgrade pip

# Get boto3
RUN pip install awscli --upgrade --user
WORKDIR /opt/app
RUN pip install boto3==1.3.0
