FROM circleci/node:10.16.1-buster
USER root
RUN apt-get update && sudo apt-get -y -qq install python-dev \
 && curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o awscli-bundle.zip \
 && unzip awscli-bundle.zip \
 && awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \
 && rm awscli-bundle.zip \
 && rm -rf awscli-bundle \
 && apt-get remove python-dev \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && npm install -g npm@6.10.2 \
 && usermod -u 1003 circleci \
 && groupmod -g 1003 circleci
USER circleci