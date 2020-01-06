# ---- Base Node ----
FROM node:10.16.0-alpine AS base
WORKDIR /app
RUN apk add --no-cache tini curl

#
# ---- Dependencies ----
FROM node:10.16.0-alpine AS dependencies
WORKDIR /app
RUN apk add --no-cache python make g++
RUN apk add --no-cache g++
COPY package.json .
RUN yarn install --prod
RUN cp -R node_modules prod_node_modules

# # install ALL node_modules, including 'devDependencies'
# RUN yarn install
#RUN npm install

#
# ---- Test ----
# run linters, setup and tests
#FROM dependencies AS test
#COPY . .
#RUN  npm run lint && npm run setup && npm run test

#
# ---- Release ----
FROM base AS release
WORKDIR /app
#ENV NODE_ICU_DATA=node_modules/full-icu
CMD tini node src/index.js
# copy production node_modules
COPY --from=dependencies /app/prod_node_modules ./node_modules
# copy app sources
COPY src src

HEALTHCHECK CMD curl -f http://localhost/health || exit 1
EXPOSE 80

