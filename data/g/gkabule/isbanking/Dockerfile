# stage 1
FROM node:12.2.0 as node
WORKDIR /app

ARG NPM_TOKEN

COPY . .
COPY .npmrc .npmrc
RUN npm config set "@fortawesome:registry" https://npm.fontawesome.com/
RUN npm config set "//npm.fontawesome.com/:_authToken" 9E95255B-E59E-40A5-A137-7DA775AE77F4

RUN npm install
RUN npm install --save @fortawesome/fontawesome-pro

RUN npm run build --prod

RUN rm -f .npmrc

# stage 2
FROM nginx:alpine
COPY --from=node /app/dist /usr/share/nginx/html
