FROM node:10.3-slim

WORKDIR /app

ADD . /app

EXPOSE 1337

RUN \
  npm install && \
  npx strapi install content-manager || true && \
  npx strapi install content-type-builder || true && \
  npx strapi install settings-manager || true && \
  npx strapi install upload || true

RUN mkdir ./plugins/users-permissions && cp -r ./node_modules/strapi-plugin-users-permissions/* ./plugins/users-permissions/ && true
COPY ./to_overwrite/User.settings.json ./plugins/users-permissions/models/

CMD ["npm", "start"]