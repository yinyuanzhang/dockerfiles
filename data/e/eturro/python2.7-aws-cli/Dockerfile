FROM circleci/python:2.7

SHELL ["/bin/bash", "-c"]

RUN sudo apt-get update -qq && \
  sudo curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
  sudo unzip awscli-bundle.zip && \
  sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
  sudo rm -rf ./awscli-bundle awscli-bundle.zip