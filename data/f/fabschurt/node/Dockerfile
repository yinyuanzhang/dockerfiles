FROM node:8
LABEL maintainer='Fabien Schurter <fabien@fabschurt.com>'

# Build args and env vars
ONBUILD ARG NODE_ENV=production
ONBUILD ENV NODE_ENV="$ENVIRONMENT"
ONBUILD ARG LOCAL_APP_ROOT=.
ONBUILD ARG IMAGE_APP_ROOT=/usr/src/app
ONBUILD ARG RUNTIME_USER_NAME=node
ONBUILD ARG RUNTIME_USER_UID=1000
ONBUILD ARG RUNTIME_USER="${RUNTIME_USER_UID}:${RUNTIME_USER_UID}"
ONBUILD ENV PATH="${PATH}:${IMAGE_APP_ROOT}/node_modules/.bin"

# Ship the code!
ONBUILD COPY "$LOCAL_APP_ROOT" "$IMAGE_APP_ROOT"
ONBUILD RUN chown -R "$RUNTIME_USER" "$IMAGE_APP_ROOT"

# Set the default runtime user and CWD
ONBUILD WORKDIR "$IMAGE_APP_ROOT"
ONBUILD USER "$RUNTIME_USER"

# Upgrade packages
RUN \
  apt-get update && \
  apt-get upgrade -y && \
  rm -r /var/lib/apt/lists/*
