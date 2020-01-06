FROM nginx:alpine

LABEL mantainer="Juan Jaramillo <juan.jaramillo@koombea.com>"

ADD default.conf /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD redirect.template /redirect.template
ADD entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]

CMD ["nginx", "-g", "daemon off;"]
