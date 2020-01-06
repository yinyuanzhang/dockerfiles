#from python:3-alpine
from google/cloud-sdk:alpine

WORKDIR /data/

COPY bashrc /root/.bashrc
COPY . .

RUN apk add zip \
    terraform \
    ansible
    # aws-cli \   dependency problems
    #pip3 install --no-cache-dir boto3


