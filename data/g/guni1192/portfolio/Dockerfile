FROM golang:1.12-alpine as hugo
RUN apk add --update --no-cache git && \
    go get -v github.com/spf13/hugo && \
    apk del --purge git

WORKDIR /app
COPY . /app
RUN hugo

FROM nginx:1.15-alpine as nginx
COPY --from=hugo /app/public /usr/share/nginx/html
