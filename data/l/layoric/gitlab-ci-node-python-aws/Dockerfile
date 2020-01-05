FROM node:6.9.3
ARG DEBIAN_FRONTEND=noninteractive
ADD https://www.npmjs.com/install.sh ./install.sh
RUN sh install.sh
RUN ["apt-get", "update", "-qq"]
RUN ["apt-get", "install", "-y", "--no-install-recommends", "build-essential", "g++", "python2.7", "python2.7-dev", "unzip", "curl", "gettext", "jq"]
RUN ["rm", "-rf", "/var/lib/apt/lists/*"]
RUN ["curl", "-O", "https://bootstrap.pypa.io/get-pip.py"]
RUN ["python", "get-pip.py"]
RUN ["pip", "install", "awscli"]
