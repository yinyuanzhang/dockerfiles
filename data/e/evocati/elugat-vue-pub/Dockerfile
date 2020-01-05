# build stage
FROM node:lts-alpine as build-stage
WORKDIR /elugat
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
# copy custom configuration
COPY ./k8s/conf/nginx.conf /etc/nginx/
COPY --from=build-stage /elugat/dist /etc/nginx/html
CMD ["nginx", "-g", "daemon off;"]
