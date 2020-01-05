FROM nginx:latest

RUN apt-get update && apt-get install -y vim mc net-tools
COPY default.conf /etc/nginx/conf.d/default.conf

WORKDIR /etc/nginx

EXPOSE 80