# Base image:
FROM reddotpay/docker-go-sql-api:latest
LABEL maintainer="daryl.n.w.k@gmail.com"

# Install golint
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py --user
RUN ~/.local/bin/pip install awscli --upgrade --user

RUN apt-get update
RUN apt-get install jq zip -y

ENV PATH $PATH:~/.local/bin