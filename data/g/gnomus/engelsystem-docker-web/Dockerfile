FROM nginx:alpine

MAINTAINER Felix Favre <gnomus@gnomus.de>

COPY vhost.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
