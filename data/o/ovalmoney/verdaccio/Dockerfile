FROM node:10-alpine as builder

WORKDIR /opt/verdaccio-gitlab-build

ARG PLUGIN_GITLAB=933cba3b7acb0c1ce6fd3df8944c4996664a23e6
ENV NODE_ENV=production \
    VERDACCIO_BUILD_REGISTRY=https://registry.npmjs.org/

RUN apk add --no-cache \
    curl \
    zip

RUN curl -S -L -O \
    https://github.com/bufferoverflow/verdaccio-gitlab/archive/${PLUGIN_GITLAB}.tar.gz && \
    tar -xvf ${PLUGIN_GITLAB}.tar.gz --strip 1 && \
    rm -R ${PLUGIN_GITLAB}.tar.gz

RUN yarn config set registry $VERDACCIO_BUILD_REGISTRY && \
    yarn install --production=false && \
    yarn code:docker-build && \
    yarn cache clean && \
    yarn install --production=true --pure-lockfile

FROM verdaccio/verdaccio:4.3

# Go back to root to be able to install the plugin
USER root

COPY --from=builder /opt/verdaccio-gitlab-build/build /opt/verdaccio-gitlab/build
COPY --from=builder /opt/verdaccio-gitlab-build/package.json /opt/verdaccio-gitlab/package.json
COPY --from=builder /opt/verdaccio-gitlab-build/node_modules /opt/verdaccio-gitlab/node_modules

# Inherited from parent image
WORKDIR $VERDACCIO_APPDIR
RUN ln -s /opt/verdaccio-gitlab/build /verdaccio/plugins/verdaccio-gitlab

# Inherited from parent image
USER $VERDACCIO_USER_UID
