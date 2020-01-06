# Setup base node image (LTS)
ARG NODE_VERSION=10.15.3

FROM ubuntu:bionic
# Environment...
ENV NODE_ENV production
ENV TZ Australia/Sydney
ENV PKG docker-ce-cli_18.09.3~3-0~ubuntu-bionic_amd64.deb
ENV URL https://download.docker.com/linux/ubuntu/dists/bionic/pool/stable/amd64/${PKG}
# Install docker cli... (xz for tar decompress)
RUN apt-get update && apt-get install --assume-yes --no-install-recommends curl xz-utils ca-certificates && rm -rf /var/lib/apt/lists/*
RUN curl -OL ${URL} && dpkg -i ${PKG} && rm ${PKG}
RUN docker --version
# Install node...
ENV NODE_VERSION 10.15.3
RUN curl -s -N https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz | tar -xJ --directory /usr/local --strip-components 1
RUN node -v
# Install dumb init...
RUN curl -L https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 -o /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init
# Copy project...
COPY . .

RUN ln -sf /dev/stdout /root/stdout.log && ln -sf /dev/stderr /root/stderr.log
ENTRYPOINT dumb-init node index.js
EXPOSE 3000
