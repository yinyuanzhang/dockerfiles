FROM node:lts AS build
COPY . /app
WORKDIR /app
RUN npm install

FROM node:lts-alpine
COPY --from=build /app /app
WORKDIR /app
ENV PORT=80
CMD ["node", "server.js"]
