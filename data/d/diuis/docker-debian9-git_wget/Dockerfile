FROM diuis/docker-debian9-git:v1.0.5

RUN apt-get update && apt-get install --no-install-recommends -y wget gnupg2 ca-certificates && \
    apt-get autoremove && apt-get clean
