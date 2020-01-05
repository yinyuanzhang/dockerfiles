FROM node:11.1.0-alpine

WORKDIR /usr/src/api

RUN echo "unsafe-perm = true" >> ~/.npmrc

# COPY package.json package-lock.json ./
RUN cd /usr/src/api

COPY package.json /usr/src/api/

RUN yarn

COPY . .

RUN npm run build

ENV HOST 0.0.0.0

ENV PORT 80

COPY healthcheck.js ./

HEALTHCHECK --interval=15s --timeout=5s --start-period=30s \
    CMD node /usr/src/api/healthcheck.js


EXPOSE 80

CMD ["npm", "start"]