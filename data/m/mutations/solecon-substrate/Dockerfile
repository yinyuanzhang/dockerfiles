# Main docker image
FROM ruby:2.6.1-alpine3.9

# Metadata
LABEL maintainer="Mutations Limited" \
      name="mutations/solecon-substrate" \
      version="1.0"

# ARG APP_USER=app
# RUN addgroup -S "$APP_USER" && adduser -S -g "$APP_USER" "$APP_USER"

ARG APP_DIR=/app
WORKDIR "$APP_DIR"

# GEM_HOME set in ruby image
ENV RUBY_GEM_HOME /usr/local/bundle

# Build-time Packages:
# ------------
ARG BUILD_PACKAGES="\
    libstdc++ \
    libxml2-dev \
    libxslt-dev \
    openssl \
"

# Run-time Packages:
# ------------
# less: needed for color output of binding.pry
# postgresql-client: required for dumping db structure when migrating
#
ARG RUNTIME_PACKAGES="\
    autoconf \
    automake \
    bash \
    build-base \
    curl \
    git \
    less \
    libtool \
    nasm \
    nodejs \
    postgresql-client \
    postgresql-dev \
    tzdata \
    util-linux \
    yarn \
"

# Heroku deployment-related Packages:
# ------------
# List provided by Heroku support team
ARG HEROKU_PACKAGES="\
    bash \
    ca-certificates \
    py-pip \
    python \
"

# Ensure directories exist
RUN mkdir -p "$APP_DIR"

# Install packages
RUN apk update && \
    apk upgrade && \
    apk add --no-cache $BUILD_PACKAGES && \
    apk add --no-cache $RUNTIME_PACKAGES

# Commands from Heroku support
RUN apk add --no-cache $HEROKU_PACKAGES && \
    curl https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub > /etc/apk/keys/sgerrand.rsa.pub && \
    curl -L https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk > /tmp/glibc.apk && \
    apk add /tmp/glibc.apk

# Make private gems local to bundler
ENV BUNDLE_DISABLE_SHARED_GEMS false
ENV BUNDLE_DISABLE_LOCAL_BRANCH_CHECK true

COPY Gemfile "$APP_DIR/Gemfile"
COPY Gemfile.lock "$APP_DIR/Gemfile.lock"
RUN bundle install --jobs 20 --retry 3

# Where Node lib files are installed
ENV NODE_MODULES_FOLDER "$APP_DIR/frontend/node_modules"
ENV NODE_BIN_FOLDER "$NODE_MODULES_FOLDER/.bin"

# Ensure the directories exist
RUN mkdir -p "$NODE_MODULES_FOLDER"

# Copy the application dependency files
COPY frontend/package.json "$APP_DIR/frontend/"
COPY frontend/yarn.lock "$APP_DIR/frontend/"

# Run `yarn` to install dependencies
RUN cd "$APP_DIR/frontend" && yarn install --ignore-optional --modules-folder "$NODE_MODULES_FOLDER"

# Install Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh

# Cleanup Build-time packages to save space
RUN apk del $BUILD_PACKAGES

# Add the application
# COPY . "$APP_DIR"

# Build the static frontend
# ENV NODE_PATH src
# ENV SKIP_PREFLIGHT_CHECK true
# RUN cd frontend && yarn build && yarn deploy

# Ensure directories are writable by `APP_USER`
# RUN chown -R "$APP_USER":"$APP_USER" \
#     "$APP_DIR" \
#     "$RUBY_GEM_HOME" \
#     "$NODE_MODULES_FOLDER"

# Run as an unprivileged user
# USER "$APP_USER"

# Add node binaries to path
# ENV PATH "$PATH:$NODE_BIN_FOLDER"

ENV SHELL /bin/bash

# Expose the React frontend port
# EXPOSE 3000

# Expose the Rails backend port
# EXPOSE 3001

# Run the Rails server
# CMD ["bundle", "exec", "iodine"]
