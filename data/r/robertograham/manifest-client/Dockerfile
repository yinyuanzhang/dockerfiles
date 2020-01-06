ARG BUILD_DIR=/usr/src/app

FROM node:10.13.0-alpine AS build
ARG BUILD_DIR
WORKDIR $BUILD_DIR
COPY package.json .
RUN npm install
COPY src src
COPY public public
RUN npm run build

FROM httpd:2.4.37-alpine
ARG BUILD_DIR
ARG VERSION
ARG TITLE
ARG DESCRIPTION
ARG REVISION
ARG CREATED
ENV SERVER_CONTAINER_NAME=manifest-server
WORKDIR /usr/local/apache2
COPY --from=build $BUILD_DIR/build htdocs
RUN sed -i 's,#\(LoadModule rewrite_module modules/mod_rewrite.so\),\1,g' conf/httpd.conf \
  && sed -i -e '/<Directory "\/usr\/local\/apache2\/htdocs">/,/<\/Directory>/{s/AllowOverride None/AllowOverride All/}' conf/httpd.conf \
  && sed -i 's,#\(LoadModule proxy_module modules/mod_proxy.so\),\1,g' conf/httpd.conf \
  && sed -i 's,#\(LoadModule proxy_wstunnel_module modules/mod_proxy_wstunnel.so\),\1,g' conf/httpd.conf \
  && echo 'ProxyRequests off' >> conf/httpd.conf \
  && echo 'ProxyPass /ws ws://${SERVER_CONTAINER_NAME}:8080/ws interpolate' >> conf/httpd.conf
LABEL org.opencontainers.image.version=$VERSION
LABEL org.opencontainers.image.title=$TITLE
LABEL org.opencontainers.image.description=$DESCRIPTION
LABEL org.opencontainers.image.revision=$REVISION
LABEL org.opencontainers.image.created=$CREATED
LABEL org.opencontainers.image.authors="Roberto Graham"
LABEL org.opencontainers.image.source="https://bitbucket.org/robertograham/manifest-client"