FROM node:11 as builder
WORKDIR /app
COPY . /app
RUN apt-get update
RUN npm i
RUN npm run build

FROM nginx
RUN apt-get install gettext-base
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/dist/sweetsale /usr/share/nginx/html
EXPOSE 80 443
CMD sed "s/{{NGINX_HOST}}/$NGINX_HOST/g" /etc/nginx/conf.d/mysite.template > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'