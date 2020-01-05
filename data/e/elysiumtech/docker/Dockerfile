FROM ubuntu

LABEL maintainer="it@elysium.tech" 
RUN apt-get clean && \
    apt-get update && \
    apt-get install -y sudo git curl python-pip zip && \
    curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - && \
    apt-get install -y nodejs && \
    pip install --upgrade pip && \
    pip install awscli --upgrade --user 

ENV PATH "$PATH:/root/.local/bin"