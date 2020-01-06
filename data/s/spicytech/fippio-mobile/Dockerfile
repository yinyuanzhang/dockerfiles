# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
# RUN npm install -g yarn
COPY . .
RUN apk add --no-cache git
RUN yarn install --non-interactive
RUN yarn run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]