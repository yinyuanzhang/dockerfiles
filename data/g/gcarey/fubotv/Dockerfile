FROM circleci/node:10-browsers

USER root

# install python-dev & sendmail
RUN apt-get update && apt-get install -y \
    python-dev \
    sendmail \
    sendmail-bin \
 && rm -rf /var/lib/apt/lists/*

# install pip & awscli
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py && \
    pip install awscli pydash

# install static-server for deployments
RUN yarn global add static-server

USER circleci