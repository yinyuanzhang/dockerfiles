FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install --no-install-recommends -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get upgrade --no-install-recommends -y -qq && \
    apt-get install -y ansible
