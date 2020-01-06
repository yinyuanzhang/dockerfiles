FROM circleci/node:latest

RUN sudo apt-get update && \
  sudo apt-get install -y python python-pip python-dev && \
  sudo pip install awscli && \
  sudo pip install awsebcli && \
  sudo apt-get clean
