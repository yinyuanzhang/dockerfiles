ARG BASE_IMAGE_PREFIX
FROM ${BASE_IMAGE_PREFIX}node:8-alpine

ARG ARCH
COPY qemu-${ARCH}-static /usr/bin

WORKDIR /app

COPY package.json /app
RUN npm install
COPY . /app

CMD ["npm", "start"]