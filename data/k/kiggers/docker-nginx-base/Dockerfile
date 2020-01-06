FROM nginx:1.13.3-alpine

ADD . /usr/share/nginx/html/.

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]