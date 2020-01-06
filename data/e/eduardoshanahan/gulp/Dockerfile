FROM eduardoshanahan/node:6.10.3.1

LABEL maintainer 'Eduardo Shanahan <contact@eduardoshanahan.com>'

RUN apk add --virtual .install_dependencies \
    build-base \
    python \
&&  npm install -g gulp \
&&  apk del .install_dependencies

CMD ["/bin/sh"]
