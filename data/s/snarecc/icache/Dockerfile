FROM node:13-alpine AS build

WORKDIR /usr/src/app
COPY . .
RUN yarn
RUN yarn testOnce
RUN yarn build

FROM node:13-alpine AS release
WORKDIR /usr/dist/app
COPY --from=build /usr/src/app/build/ .
COPY --from=build /usr/src/app/node_modules/ ./node_modules
EXPOSE 8080
CMD ["node", "index.js"]