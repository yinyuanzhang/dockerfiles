FROM thredup/node:12.12.0

RUN apk add --no-cache \
    autoconf \
    automake \
    g++ \
    gcc \
    git \
    make \
    nasm \
    python \
    zlib-dev

ONBUILD ARG AWS_KEY
ONBUILD ENV AWS_KEY=${AWS_KEY}
ONBUILD ARG AWS_SECRET
ONBUILD ENV AWS_SECRET=${AWS_SECRET}

ONBUILD ARG DATADOG_API_KEY
ONBUILD ENV DATADOG_API_KEY=${DATADOG_API_KEY}

ONBUILD ARG NPM_TOKEN

ONBUILD ARG NODE_ENV=production
ONBUILD ENV NODE_ENV=${NODE_ENV}

ONBUILD ARG NPM_LOG_LEVEL=error
ONBUILD ENV npm_config_loglevel=${NPM_LOG_LEVEL}

ONBUILD ARG PUBLISH_ASSETS=false
ONBUILD ENV PUBLISH_ASSETS=${PUBLISH_ASSETS}
ONBUILD ARG PUBLISH_BUILD_STATS=false
ONBUILD ENV PUBLISH_BUILD_STATS=${PUBLISH_BUILD_STATS}

ONBUILD ARG REVISION
ONBUILD ENV REVISION=${REVISION}

ONBUILD COPY package.json package-lock.json ./
ONBUILD RUN echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" >> ~/.npmrc \
  && npm config set unsafe-perm true \
  && npm install \
  && rm ~/.npmrc
ONBUILD COPY . ./
ONBUILD RUN if [ -f ./scripts/build.sh ]; then ./scripts/build.sh; fi
