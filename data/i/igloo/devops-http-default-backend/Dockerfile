FROM node:10.16.0-alpine
ENV NPM_CONFIG_LOGLEVEL warn
WORKDIR /app
COPY ./package.json ./package-lock.json ./gatsby-config.js ./
RUN npm ci
COPY ./gatsby-*.js ./
COPY ./src ./src/
RUN npm run build:prefix

FROM nginx:1.17.0-alpine
ENV NGINX_PORT=8080
COPY ./nginx-server.conf /etc/nginx/conf.d/default.conf.tpl
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
COPY --from=0 /app/public /public

CMD ["/docker-entrypoint.sh"]
