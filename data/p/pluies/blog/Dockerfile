FROM cibuilds/hugo as builder

RUN mkdir -p /var/www/blog
COPY . /var/www/blog
WORKDIR /var/www/blog
RUN hugo

FROM nginx:1-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /var/www/blog/public/ /usr/share/nginx/html
