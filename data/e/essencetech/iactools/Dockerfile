FROM python:3-alpine

RUN apk update 
RUN apk add bash unzip curl
RUN curl https://releases.hashicorp.com/terraform/0.12.8/terraform_0.12.8_linux_amd64.zip | funzip > /usr/local/bin/terraform \
    && chmod +x /usr/local/bin/terraform
COPY requirements.txt /
RUN pip install -r /requirements.txt
