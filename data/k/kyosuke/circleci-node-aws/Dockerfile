FROM circleci/node:10

# Install aws-cli
RUN sudo apt-get update && sudo apt-get install -y \
  python-dev \
  && curl https://bootstrap.pypa.io/get-pip.py | sudo python \
  && sudo pip install awscli
