FROM node:11.1.0-alpine

WORKDIR /usr/src/api

RUN echo "unsafe-perm = true" >> ~/.npmrc

RUN npm install -g strapi@3.0.0-alpha.25

COPY strapi.sh ./
RUN chmod +x ./strapi.sh

EXPOSE 1337

COPY healthcheck.js ./
HEALTHCHECK --interval=15s --timeout=10s --start-period=60s \
      CMD node /usr/src/api/healthcheck.js
COPY ./strapi-app ./strapi-app
RUN npm install --prefix ./strapi-app
ENV NODE_ENV=staging
CMD ["./strapi.sh"]
