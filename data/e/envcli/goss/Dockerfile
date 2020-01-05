############################################################
# Dockerfile
############################################################

# Set the base image
FROM docker:stable

############################################################
# Configuration
############################################################
ENV VERSION "0.3.5"

############################################################
# Installation
############################################################

ADD egoss /usr/local/bin/egoss

RUN apk add --no-cache bash curl > /dev/null &&\
    curl -L -o /usr/local/bin/goss https://github.com/aelsabbahy/goss/releases/download/v${VERSION}/goss-linux-amd64 &&\
    curl -L -o /usr/local/bin/dgoss https://raw.githubusercontent.com/aelsabbahy/goss/v${VERSION}/extras/dgoss/dgoss &&\
    chmod +x /usr/local/bin/goss &&\
    chmod +x /usr/local/bin/dgoss &&\
    chmod +x /usr/local/bin/egoss &&\
	apk del --no-cache curl > /dev/null

############################################################
# Execution
############################################################
CMD ["goss", "--help"]
