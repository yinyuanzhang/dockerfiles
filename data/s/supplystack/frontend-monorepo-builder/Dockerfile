FROM ubuntu:18.04
RUN apt-get update && \
    apt-get --yes upgrade && \
    apt-get --yes install curl software-properties-common && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get --yes install jq python3-pip dh-autoreconf git nodejs openjdk-8-jdk apt-transport-https ca-certificates gnupg-agent docker-ce docker-ce-cli containerd.io && \
    pip3 install awscli && \
    useradd drone -g 999 -d /drone/src -u 999 && \
    rm -rf /var/lib/apt/lists/*
