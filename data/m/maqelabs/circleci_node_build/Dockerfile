FROM node:10.15.3-stretch-slim

RUN apt-get update -y && \
        apt-get install -y \
        libgtk2.0-0 libnotify-dev libgconf-2-4 \
        libnss3 libxss1 libasound2 xvfb \
        curl jq git python3-pip groff

RUN apt-get install python3-pip

# pre-install Cypress
RUN npm install -g --unsafe-perm=true cypress@3.5

RUN pip3 --no-cache-dir install awscli

# Install git-ftp
RUN curl https://raw.githubusercontent.com/git-ftp/git-ftp/master/git-ftp > /bin/git-ftp && \
		chmod 755 /bin/git-ftp

RUN mkdir /workspace
WORKDIR /workspace
