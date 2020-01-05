FROM debian:sid-slim

SHELL ["/bin/bash", "-c"]

WORKDIR /home/nodec/

# installs dependencies required for provisioning and node packer
RUN apt-get update && apt-get install -y --no-install-recommends curl git squashfs-tools python gcc g++ make xz-utils \
 && rm -rf /var/lib/apt/lists/*

# installs upx
RUN curl -sSLko- https://github.com/upx/upx/releases/download/v3.95/upx-3.95-amd64_linux.tar.xz | tar xJf - \
  && mv upx-3.95-amd64_linux/upx /usr/local/bin/ && chmod a+x /usr/local/bin/upx && rm -rf upx-3.95-amd64_linux

# installs node v8.11.4 and npm v6.4.1
RUN curl -sSLko- https://nodejs.org/dist/v8.11.4/node-v8.11.4-linux-x64.tar.gz | tar xfz - \
  && cp -R node-v8.11.4-linux-x64/lib/node_modules /usr/local/lib/ \
  && ln -s /usr/local/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx \
  && ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
  && cp node-v8.11.4-linux-x64/bin/node /usr/local/bin \
  && rm -rf node-v8.11.4-linux-x64 \
  && chmod a+x /usr/local/bin/npx \
  && chmod a+x /usr/local/bin/npm \
  && chmod a+x /usr/local/bin/node \
  && npm install -g npm@6.4.1

# adds node packer and precompiled node sources
ADD nodec /usr/local/bin/nodec
ADD nodec-node-8.11.4-1.6.0-precompiled.tar.gz /

# removes dependencies only required for provisioning. note: only works with --squash
RUN apt-get remove --purge -y curl xz-utils && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/bash"]