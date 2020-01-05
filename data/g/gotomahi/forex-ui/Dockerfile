FROM node:10-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json  /app/
RUN cd /app && npm install
COPY .  /app
RUN npm build
RUN cd /app && npm run build

FROM httpd:2.4
RUN rm -rf /usr/local/apache2/htdocs/*
COPY httpd.conf /usr/local/apache2/conf/httpd.conf
COPY --from=builder /app/dist /usr/local/apache2/htdocs
EXPOSE 0.0.0.0:81:81
