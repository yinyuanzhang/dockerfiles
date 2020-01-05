
FROM balenalib/raspberry-pi-debian-node:9.11.2-stretch-build-20181207

RUN [ "cross-build-start" ]

# Create node user
RUN groupadd -g 1000 node \
  && useradd -u 1000 -g node -ms /bin/bash node

# Create app directory
WORKDIR /usr/src/app
RUN chown node:node /usr/src/app

# Create node_modules symlink target directory
RUN mkdir /node_modules
RUN chown -R node:node /node_modules

COPY --chown=node app/package*.json app/*yarn* ./


RUN mv yarn.arm32v6.lock yarn.lock
RUN su - node -c 'cd /usr/src/app/ && yarn install --frozen-lockfile'

RUN [ "cross-build-end" ]

COPY --chown=node app .

USER node
