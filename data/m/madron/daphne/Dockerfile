FROM alpine:3.8

# Packages and requirements
COPY docker/requirements.txt /docker/requirements.txt
RUN apk add --no-cache python3==3.6.6-r0 su-exec==0.2-r0 nginx==1.14.0-r1 \
    # Install build packages
    python3-dev musl-dev gcc \
    \
    # Install requirements
    && pip3 install -r /docker/requirements.txt \
    \
    # Remove build packages
    && apk del python3-dev musl-dev gcc \
    \
    # Nginx: forward request and error logs to docker log collector
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


COPY nginx.conf /etc/nginx/nginx.conf
COPY docker /docker/


ENTRYPOINT ["/docker/entrypoint.sh"]
CMD ["nginx"]
