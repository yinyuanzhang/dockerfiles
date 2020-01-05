# This image is for running tests via test.sh
FROM ubuntu:latest

# Install packages
RUN apt-get update && apt-get install -y curl git unzip wget xvfb

# Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Node.js
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt install -y nodejs
