FROM alpine/git AS git
WORKDIR /app
RUN git clone --single-branch --branch aws2c9 https://github.com/secobau/4399

FROM nginx:stable-alpine AS utils
RUN apk add apache2-utils
RUN htpasswd -b -c htpasswd user password

FROM nginx:stable-alpine
WORKDIR /etc/nginx/conf.d/
RUN rm -f *
COPY --from=git /app/4399/aws2c9.conf .
COPY --from=utils htpasswd .
