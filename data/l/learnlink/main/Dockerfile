FROM node:8.11.1

RUN npm install -g firebase-tools@6.4.0 --unsafe
RUN npm install -g quasar-cli@0.6.5
RUN npm install -g @sentry/cli@1.36.4 --unsafe-perm

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

EXPOSE 8081
