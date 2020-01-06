FROM ubuntu:16.04
MAINTAINER Serfim TIC

# Base MVN / NPM
RUN apt update && apt install -y \
  locales \
  build-essential \
  git \
  openjdk-8-jdk \
  maven \
  curl 

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
  && apt install -y nodejs

CMD /bin/bash 

# Get Chrome sources
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Install Chrome
RUN apt update && apt install -y \
    google-chrome-stable \
    --no-install-recommends

# Install Ruby
RUN apt install -y ruby ruby-dev

# Install Compass
RUN gem install compass

# Install Bower
RUN npm install -g bower

# Install Grunt CLI
RUN npm install -g grunt-cli

# Install Python/ Pip
RUN apt install -y python-pip

# Install AWS CLI
RUN pip install awscli --ignore-installed six

# Install SSHPASS
RUN apt install sshpass

# Set language
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8
