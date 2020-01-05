FROM nginx:1.15.10-alpine

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./entrypoint.sh /entrypoint.sh

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["/bin/sh", "/entrypoint.sh"]
