FROM beevelop/nodejs:v8.12.0
MAINTAINER Gerben Bas <gerben.bas@widgetbrain.com>

# Install Python.
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python python-dev python-pip python-virtualenv python3.6 python3.6-dev && rm -rf /var/lib/apt/lists/*

# Install Pip.
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.6 get-pip.py

# Install the Azure CLI.
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

RUN npm install -g mocha
RUN pip install boto3==1.3.0
RUN apt-get update
RUN apt-get install -y zip
RUN apt-get install -y git
RUN npm install -g npx
RUN npm install -g npm-login-cmd
RUN npm install -g npm-cli-login
RUN npm config set registry https://npm.widgetbrain.io
