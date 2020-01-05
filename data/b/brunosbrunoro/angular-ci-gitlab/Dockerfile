FROM node:10-slim
LABEL authors="Bruno Scrok Brunoro"
LABEL email="bruno.sbrunoro@gmail.com"

RUN npm install -g @angular/cli@6.0.0
RUN npm install -g firebase-tools
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update && apt-get install -y google-cloud-sdk
RUN apt-get update && apt-get install -y git