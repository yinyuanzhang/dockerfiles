FROM node:10.15-alpine

# Set up build environment.
ENV NODE_ENV=prod

# Set the build directory.
WORKDIR /opt/app

# warm up npm cache
COPY package.json .
COPY yarn.lock .
RUN yarn install --frozen-lockfile --production
