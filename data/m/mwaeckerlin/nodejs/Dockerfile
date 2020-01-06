FROM mwaeckerlin/base
MAINTAINER mwaeckerlin

ENV CONTAINERNAME    "node.js"
ENV NODE_ENV         "production"
ENV PATH             "node_modules/.bin:/app/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
RUN mkdir /app \
 && chown -R "${RUN_USER}" /app \
 && $PKG_INSTALL nodejs npm
USER "${RUN_USER}"
WORKDIR /app
