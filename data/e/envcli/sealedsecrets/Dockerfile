############################################################
# Dockerfile
############################################################

# Set the base image
FROM alpine:3.8

############################################################
# Configuration
############################################################
ENV VERSION "0.7.0"

############################################################
# Entrypoint
############################################################
COPY docker-entrypoint.sh /usr/local/bin/

############################################################
# Installation
############################################################
RUN apk add --no-cache curl bash ca-certificates &&\
    curl -L -o /usr/local/bin/kubeseal https://github.com/bitnami-labs/sealed-secrets/releases/download/v${VERSION}/kubeseal-linux-amd64 &&\
    chmod 755 /usr/local/bin/kubeseal &&\
    chmod +x /usr/local/bin/docker-entrypoint.sh &&\
    apk del curl

############################################################
# Execution
############################################################
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["kubeseal", "help"]
