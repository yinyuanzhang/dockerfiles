FROM nginx:1.12.1

EXPOSE 80 443

RUN rm /etc/nginx/conf.d/default.conf

COPY ./config/*.conf /etc/nginx/conf.d/

RUN service nginx restart

ENTRYPOINT  nginx -g 'daemon off;'
