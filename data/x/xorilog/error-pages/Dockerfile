FROM nginx:alpine
ADD src/ buildit.sh /usr/share/nginx/html/
RUN apk add --no-cache --virtual .build-deps \
    bash \
    && cd /usr/share/nginx/html/ \
    && ./buildit.sh \
    && rm ./buildit.sh \
    && apk del .build-deps
