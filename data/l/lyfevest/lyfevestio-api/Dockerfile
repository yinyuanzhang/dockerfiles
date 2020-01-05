FROM node:10

WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install

COPY . .
RUN npm run build

FROM node:10

WORKDIR /usr/src/app

COPY --from=0 /usr/src/app/*.json ./
COPY --from=0 /usr/src/app/.env ./
COPY --from=0 usr/src/app/dist dist
RUN npm install
ENV KEYCLOAK_CONFIG=keycloak-prod.json

EXPOSE 3000
CMD [ "node", "-r", "tsconfig-paths/register", "dist/server.js"]