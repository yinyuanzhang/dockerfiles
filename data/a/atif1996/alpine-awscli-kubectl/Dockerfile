# Slim alpine container to interact with AWS and EKS
#
# Contains python3, awscli, kubectl as well as make, curl and git.  Just the
# basics without all the fat.
#

FROM alpine:3.10.3
LABEL maintainer="Atif Mahmood <atif.1996@gmail.com>"

RUN apk add --no-cache make curl git coreutils && \
    rm -rf /tmp/* 

# Install kubectl
RUN curl -sLO https://storage.googleapis.com/kubernetes-release/release/$(\
    curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

# Install AWS CLI and python3
RUN apk add --no-cache  python3 && \
    pip3 install --upgrade pip && \
    pip3 install awscli && \
    rm -rf /tmp/* && \
    rm -rf /root/.cache

# Install postgres client
RUN apk add --no-cache postgresql-client && \
    rm -rf /tmp/* && \
    rm -rf /root/.cache

