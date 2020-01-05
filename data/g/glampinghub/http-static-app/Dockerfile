FROM nginx:1.17.5-alpine

LABEL \
    version="1.0" \
    maintainer="Juan Ramón Guerrero Sánchez <juanramonguerrero@glampinghub.com>"

RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing awscli

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]