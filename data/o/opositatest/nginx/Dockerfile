FROM nginx:1.16

ADD configuration /etc/nginx/configuration
ADD entrypoint.sh /entrypoint.sh
ADD nginx.conf /etc/nginx/nginx.conf

RUN rm /etc/nginx/conf.d/default.conf && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
