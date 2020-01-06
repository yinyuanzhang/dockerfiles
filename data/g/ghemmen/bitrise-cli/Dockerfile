FROM debian:latest

RUN apt update && \
    apt -y upgrade && \
    apt -y install curl && \
    curl -fL https://github.com/bitrise-io/bitrise/releases/download/1.27.1/bitrise-$(uname -s)-$(uname -m) > /usr/local/bin/bitrise && \
    chmod +x /usr/local/bin/bitrise
