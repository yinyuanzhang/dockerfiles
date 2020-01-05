FROM python:3.7.2-stretch

RUN apt-get update -y

WORKDIR /usr/src
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip install awscli --upgrade

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs zip
RUN npm install -g newman

RUN wget https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_linux_amd64.zip
RUN unzip terraform_0.11.11_linux_amd64.zip -d /usr/local/bin

RUN rm -rf /usr/src/*

WORKDIR /
ENTRYPOINT ["/bin/bash", "-c"]
