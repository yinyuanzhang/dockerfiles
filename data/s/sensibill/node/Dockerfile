# Since there is no offical image for node v4.8, we must use the ubuntu 14.04 image as a base. Once node has been
# upgraded, we should consider changing the base image.

FROM    ubuntu:14.04

RUN     apt-get update && \
        apt-get install -y \
        git mercurial wget build-essential jq \
        poppler-utils shellcheck rlwrap curl && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* # clean up caches to make the image smaller.

# Install NodeJS v4.8.6
WORKDIR /tmp
RUN     curl -sLO https://deb.nodesource.com/node_4.x/pool/main/n/nodejs/nodejs_4.8.6-1nodesource1_amd64.deb && \
        dpkg -i nodejs_4.8.6-1nodesource1_amd64.deb && \
        rm nodejs_4.8.6-1nodesource1_amd64.deb

RUN groupadd --gid 1000 sensibill \
    && useradd --uid 1000 --gid sensibill --shell /bin/bash --create-home sensibill
