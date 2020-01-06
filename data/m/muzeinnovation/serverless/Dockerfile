FROM node:8.10
RUN apt-get update && \
  apt-get install -y awscli && \
  apt-get autoremove -y
RUN yarn global add serverless@1.27.2
