FROM circleci/buildpack-deps:latest

# install latest stable gcloud SDK
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl -sS https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && \
    sudo apt-get update -y -qq && \
    sudo apt-get install google-cloud-sdk -y && \
    sudo rm -rf /var/lib/apt/lists/*

# install balena-CLI
ENV BALENACLI_VERSION 9.6.0
RUN sudo wget -q -O tmp.zip https://github.com/balena-io/balena-cli/releases/download/v${BALENACLI_VERSION}/balena-cli-v${BALENACLI_VERSION}-linux-x64.zip && \
    sudo unzip tmp.zip -d /usr/local/bin && \
    sudo rm -rf tmp.zip
ENV PATH="/usr/local/bin/balena-cli:${PATH}"

# install the latest stable dart SDK and webdev tool
RUN sudo apt-get update -y -qq && \
    sudo apt-get install apt-transport-https -y && \
    sudo sh -c 'curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -' && \
    sudo sh -c 'curl https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list' && \
    sudo apt-get update -y -qq && \
    sudo apt-get install dart && \
    sudo rm -rf /var/lib/apt/lists/*
ENV PATH="/usr/lib/dart/bin:${PATH}:/home/circleci/.pub-cache/bin"
RUN pub global activate webdev

# summarise bindary versions
RUN echo "\ngcloud:" && gcloud version && \
    echo "\nbalena:" && balena version && \
    echo "\ndart:" && dart --version && \
    echo "\npub:" && pub --version && \
    echo "\nwebdev:" && webdev --version
