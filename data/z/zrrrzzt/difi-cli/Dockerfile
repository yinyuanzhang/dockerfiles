# Setting the base to nodejs 8.11.1
FROM node:8.16.0-alpine@sha256:396b157f138a837de34fc48dc0ca8e37bf04d2fefc568e962acf429418950948

#### Begin setup ####

# Installs git
RUN apk add --update git && rm -rf /var/cache/apk/*

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Startup
ENTRYPOINT node cli.js --dataset=$DATASET --query=$QUERY --format=$FORMAT