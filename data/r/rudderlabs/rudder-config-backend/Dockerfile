FROM node:10.16.0-alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN npm install
RUN npm run build-ts
CMD npm run typeorm migration:run && npm start