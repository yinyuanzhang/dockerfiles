FROM ubuntu-upstart:latest

# Install dependencies
RUN apt-get update \
    && apt-get install -y curl git gnupg

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install vue-cli
RUN npm install -g vue-cli

# Install react
RUN npm install -g create-react-app

RUN mkdir -p /home/projects

# Other settings
VOLUME /home/projects

WORKDIR /home/projects