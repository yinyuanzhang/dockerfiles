# Specify the official docker image for the latest long term support (LTS) release. 
# Use a specific version, rather than node:latest, so avoid risking an accidental upgrades
FROM node:6.11.1-alpine

# Add git for private npms
RUN apk add --no-cache git

#Build Arguments & defaults
ARG PORT=5000
ARG SERVICE_NAME=default

#Environment vars
ENV STARTUP=lib/server.js

# Replace this with your application's default port
EXPOSE $PORT

# Create an unprivileged user,called dls, to run the app inside the container. If you don’t do this, then the container will run as
# root, security principles. 
# Install a more recent version of NPM, get npm has improvement a lot recently. Again, specify an exact version to avoid 
#accidental upgrades.
RUN adduser -D -u 1001 comprodls

# Setup $HOME
ENV HOME=/home/comprodls

WORKDIR $HOME/$SERVICE_NAME
RUN chown -R comprodls:comprodls $HOME/*

# Change user and working directory
USER comprodls

# Copy application packaging files on the host into $HOME/auth.
# We could COPY the whole application folder, but save some time on our docker builds by only copying in what we need
# at this point, and copying in the rest after we run npm install. This takes better advantage of docker build’s layer caching.
COPY package*.json $HOME/$SERVICE_NAME

# Run npm install. This will install the dependencies in WORKDIR/node_modules 
RUN npm install --silent --progress=false && npm cache clean --force

# Finally install the app, by copying in the remaining source files, 
COPY . $HOME/$SERVICE_NAME

# Bypass the package.json's start command and bake it directly into the image itself. This reduces the number of processes
# running inside of your container
# Secondly it causes exit signals such as SIGTERM and SIGINT to be received by the Node.js process instead of npm swallowing them.
CMD ["sh", "-c", "node lib/server.js"]
