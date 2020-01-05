FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip groff build-essential && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install awscli --upgrade && \
    pip3 install --upgrade setuptools

COPY ./scripts/aws-account-profile-add.sh /usr/local/bin/aws-account-profile-add
COPY ./scripts/aws-role-profile-add.sh /usr/local/bin/aws-role-profile-add

WORKDIR /code
