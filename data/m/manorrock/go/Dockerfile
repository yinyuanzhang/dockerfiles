FROM manorrock/debian
ENV GO_VERSION=1.13.5
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://dl.google.com/go/go$GO_VERSION.linux-amd64.tar.gz && \
    tar xvf go$GO_VERSION.linux-amd64.tar.gz && \
    mv go /usr/local && \
    rm go$GO_VERSION.linux-amd64.tar.gz && \
    rm -rf /var/lib/apt/lists/*
ENV PATH=$PATH:/usr/local/go/bin
WORKDIR /mnt
