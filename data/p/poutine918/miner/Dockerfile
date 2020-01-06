# Based on https://nodejs.org/en/docs/guides/nodejs-docker-webapp/

FROM arm32v7/node:lts-slim
# Create app directory
WORKDIR /app

COPY qemu-arm-static /usr/bin

# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json /app/

# Install OS & npm dependencies
RUN apt-get -y update && apt-get -y install git python make g++ curl bash sudo && npm ci --only=production

# Bundle app source
COPY . /app

# Install Parity
RUN /bin/bash scripts/install_parity.sh

EXPOSE 3006

CMD ["npm", "run", "start:all:prod"]
