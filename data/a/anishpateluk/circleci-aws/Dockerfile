FROM circleci/buildpack-deps

ENV AWSCLI_VERSION=1.15.72

USER root

RUN apt-get update && \
    apt-get install -y python-pip python-dev && \
    pip install --upgrade awscli==$AWSCLI_VERSION

USER circleci
