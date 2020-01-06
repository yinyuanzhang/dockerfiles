ARG NODE_VERSION=11.15

FROM node:${NODE_VERSION}-alpine AS builder

WORKDIR /app

COPY package.json .
RUN npm install
COPY . /app
RUN npm run build:ssr

EXPOSE 4000

ENTRYPOINT ["npm"]
CMD ["run", "serve:ssr"]
