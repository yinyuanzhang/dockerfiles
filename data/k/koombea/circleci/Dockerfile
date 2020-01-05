FROM ubuntu:16.04

ENV YARN_VERSION="1.1.0"

RUN apt update && \
    apt install -y curl git unzip python python-pip  && \
    pip install awscli && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt install -y nodejs  && \
    curl -L https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz -o ${YARN_VERSION}.tar.gz && \
    tar -xzf ${YARN_VERSION}.tar.gz && \
    rm ${YARN_VERSION}.tar.gz && \
    ln -s /yarn-v${YARN_VERSION}/bin/yarn /usr/local/bin/yarn
