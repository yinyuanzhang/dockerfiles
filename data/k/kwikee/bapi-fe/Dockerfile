FROM node:slim as builder
WORKDIR /
COPY src/ /src/
COPY scripts /scripts/
COPY config /config/
COPY public/ /public/
COPY package.json /
RUN npm install
RUN npm run build

FROM nginx:alpine
COPY --from=builder build/ /app_local/build/
COPY defaults/ /defaults/
COPY server_start.sh /app_local/
COPY nginx_conf/* /etc/nginx/conf.d/
RUN rm -f /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/log/nginx/
RUN chmod +x  /app_local/server_start.sh
RUN ln -sf /app_local /app
WORKDIR /app
EXPOSE 80
