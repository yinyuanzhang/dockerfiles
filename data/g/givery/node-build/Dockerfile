FROM node:10.15.3-alpine

WORKDIR /tmp/workspace

# Install dependencies for following tools
# - bcrypt to build with node-gyp
# - node-prune to slim node_modules
RUN apk --no-cache add --virtual builds-deps build-base python curl git \
  && curl -sSfL https://install.goreleaser.com/github.com/tj/node-prune.sh | sh -s -- -b /usr/local/bin
