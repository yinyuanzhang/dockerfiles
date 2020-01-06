############################################################
# Dockerfile
############################################################

# Set the base image
FROM alpine:3.8

############################################################
# Configuration
############################################################

ENV VERSION 0.7.0

############################################################
# Installation
############################################################

RUN apk add --no-cache bash git curl &&\
    curl -L https://github.com/coreos/container-linux-config-transpiler/releases/download/v${VERSION}/ct-v${VERSION}-x86_64-unknown-linux-gnu -o /usr/local/bin/ct &&\
    chmod +x /usr/local/bin/ct

############################################################
# Execution
############################################################

CMD [ "/usr/local/bin/ct" ]
