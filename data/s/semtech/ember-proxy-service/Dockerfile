FROM nginx:1.15.3

LABEL maintainer="erika.pauwels@gmail.com"

ENV STATIC_FOLDERS_REGEX "^/(assets|font)/"

RUN rm /etc/nginx/conf.d/default.conf \
    && ln -s /usr/share/nginx/html /app
COPY nginx.conf /etc/nginx/conf.d/app.conf
COPY ember-proxy-service.sh /

EXPOSE 80

CMD ["/bin/bash", "/ember-proxy-service.sh"]
