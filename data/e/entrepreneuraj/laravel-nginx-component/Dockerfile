FROM nginx:alpine

MAINTAINER Aiden Andrews-McDermott <aj@peoplerange.com>

ADD nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /run/nginx

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
