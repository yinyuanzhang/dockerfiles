FROM nginx:1.15-alpine

COPY download-static-resource.sh /root/
COPY mysite.template /etc/nginx/conf.d/mysite.template
COPY index.html.template /usr/share/nginx/html/index.html.template

ARG CACHE_TAG
RUN apk update && apk add curl
RUN /root/download-static-resource.sh /usr/share/nginx/html
RUN sed -e "s/%VERSION%/$CACHE_TAG/g" /usr/share/nginx/html/index.html.template > /usr/share/nginx/html/index.html

