FROM node:alpine as build

WORKDIR /app

ADD package.json /app/package.json

RUN npm install

COPY . /app

RUN npm run build

RUN mkdir /app/dist/stubs && cp -r /app/src/stubs/* /app/dist/stubs


FROM node:alpine 
COPY --from=build /app/dist /app
COPY --from=build /app/node_modules /app/node_modules
CMD node /app/main
