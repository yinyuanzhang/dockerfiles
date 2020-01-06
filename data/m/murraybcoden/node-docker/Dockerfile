FROM ubuntu:18.04

RUN echo "Upgrading Node"

# install dependencies
RUN apt-get update && \
     apt-get install -yq --no-install-recommends \
     gconf-service libasound2 libatk1.0-0 libatk-bridge2.0-0 \
     libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 \
     libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 \
     libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 \
     libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates \
     fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils curl gnupg wget software-properties-common


# set up gpg keys
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# grab library
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

# install nodejs
RUN apt-get install -y nodejs

# install nvm
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

# set up nvm env variables
RUN export NVM_DIR="$HOME/.nvm"

# get docker repository
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update

# install docker
RUN apt-get -y install docker-ce docker-ce-cli containerd.io

# install docker compose
RUN echo "Installing Docker Compose"
RUN apt install -y docker-compose

# verify versions
#RUN nvm ls
#
## switch version
#RUN nvm use v8.*

# verify version
# RUN node --version


# verify that its running
CMD service docker restart && \
    docker --version