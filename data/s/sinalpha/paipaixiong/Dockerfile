# build stage
FROM node:lts-alpine as build-front
ARG front
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build && \
    rm -rf build/static/css/*.map \
    rm -rf build/static/js/*.map 

FROM nginx:alpine
COPY nginx.conf /etc/nginx/
COPY --from=build-front /app/build /usr/share/nginx/html