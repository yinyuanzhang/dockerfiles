FROM python:3.8-rc

ARG GOLANG=https://dl.google.com/go/go1.12.4.linux-amd64.tar.gz
WORKDIR /root

RUN apt-get update && \
    apt-get install -y wget git curl && \
    rm -rf /var/lib/apt/lists/*

# Install Golang
RUN wget $GOLANG -O golang-binary.tar.gz -nv && \
    tar -C /usr/local -xzf golang-binary.tar.gz
ENV PATH="/root/go/bin:/usr/local/go/bin/:${PATH}"

# Setup DCOS

# Environment variables
ENV CLUSTER_URL http://mesos.blueci.io:8080
ENV GH_USERNAME BlueCIO
ENV GH_PASSWORD CEDBsF&57i3CVFAfFjyyOUoJ#

# Install the DCOS login tool to generate a valid JWT API token
RUN go get -u github.com/blueci-io/dcos-login/cmd/dcos-login

# Install the DCOS CLI
COPY scripts/* scripts/
RUN scripts/dcos-cli-install.sh

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Cleanup

RUN apt-get purge -y wget git curl && \
    apt-get autoremove -y          && \
    rm -rf golang-binary.tar.gz    && \
    apt-get clean -y
