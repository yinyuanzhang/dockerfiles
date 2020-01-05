FROM alpine:latest

# install requirements
RUN apk --no-cache add curl 

# install kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

# install rancher cli version 2.0.0 to bin/
RUN curl -L https://github.com/rancher/cli/releases/download/v2.0.5/rancher-linux-amd64-v2.0.5.tar.gz -o tmp/rancher.tar.gz && \
    tar -zxf tmp/rancher.tar.gz && \
    rm tmp/rancher.tar.gz && \
    find . -name "rancher" -exec mv {} ../bin +