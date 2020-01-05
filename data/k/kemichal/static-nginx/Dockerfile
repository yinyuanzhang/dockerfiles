FROM nginx:1.13.6-alpine

RUN apk --no-cache add openssl

VOLUME /var/www/html
VOLUME /etc/nginx/conf.d

COPY conf/static.conf /conf/static.conf

COPY scripts/add_user.sh /scripts/add_user.sh
COPY scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod -R +x /scripts

ENTRYPOINT ["/bin/sh", "/scripts/entrypoint.sh"]

# Redefine CMD, see https://github.com/moby/moby/issues/19611#issuecomment-174244260
CMD ["nginx", "-g", "daemon off;"]
