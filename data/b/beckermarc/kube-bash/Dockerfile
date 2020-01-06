FROM beckermarc/git-bash:latest

# install utilities
RUN apk add --no-cache  openssl \
                        curl

# install docker (for CLI)
# the /docker-init.sh file can be used to set the DOCKER_HOST environment variable
RUN apk add --no-cache docker && \
    echo "if [ -e /docker-init.sh ]; then source /docker-init.sh; fi" >> ~/.profile && \
    docker --version

# install kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.10.3/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl && \
    kubectl version --client

# install knctl
RUN curl -LO https://github.com/cppforlife/knctl/releases/download/v0.0.9/knctl-linux-amd64 && \
    chmod +x ./knctl-linux-amd64 && \
    mv ./knctl-linux-amd64 /usr/local/bin/knctl && \
    knctl version

# load environment during container startup
CMD ["su", "-"]
