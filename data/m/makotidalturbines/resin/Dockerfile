FROM circleci/buildpack-deps:latest

# install gcloud
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl -sS https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && \
    sudo apt-get update -y -qq && \
    sudo apt-get install google-cloud-sdk -y && \
    sudo rm -rf /var/lib/apt/lists/*

# install resin-cli
ENV RESINCLI_VERSION 7.9.2
RUN sudo wget -q -O tmp.zip https://github.com/resin-io/resin-cli/releases/download/v${RESINCLI_VERSION}/resin-cli-v${RESINCLI_VERSION}-linux-x64.zip && \
    sudo unzip tmp.zip -d /usr/local/bin && \
    sudo rm -rf tmp.zip
ENV PATH="/usr/local/bin/resin-cli:${PATH}"

# install dart 2 and webdev tool
RUN sudo apt-get update -y -qq && \
    sudo apt-get install apt-transport-https -y && \
    sudo sh -c 'curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -' && \
    sudo sh -c 'curl https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list' && \
    sudo apt-get update -y -qq && \
    sudo apt-get install dart && \
    sudo rm -rf /var/lib/apt/lists/* && \
    dart --version
ENV PATH="/usr/lib/dart/bin:${PATH}:/home/circleci/.pub-cache/bin"
RUN pub global activate webdev
