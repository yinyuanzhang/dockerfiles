FROM nginx:alpine

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx"]

COPY rootfs/ /

