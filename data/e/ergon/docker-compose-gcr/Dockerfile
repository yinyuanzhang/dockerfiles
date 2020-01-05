FROM docker/compose:1.25.0-rc1-alpine

ENV DOCKER_CREDENTIAL_GCR_VERSION 1.5.0

RUN wget -O - "https://github.com/GoogleCloudPlatform/docker-credential-gcr/releases/download/v${DOCKER_CREDENTIAL_GCR_VERSION}/docker-credential-gcr_linux_amd64-${DOCKER_CREDENTIAL_GCR_VERSION}.tar.gz" \
  | tar xz --to-stdout ./docker-credential-gcr > /usr/local/bin/docker-credential-gcr && chmod +x /usr/local/bin/docker-credential-gcr

# Provide a home where docker-credential-gcr can store the configuration for the docker credential helper.
RUN mkdir -p /home/compose
ENV HOME="/home/compose"

COPY ./docker-compose-gcr-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["sh","/usr/local/bin/docker-compose-gcr-entrypoint.sh"]