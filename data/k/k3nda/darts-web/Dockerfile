FROM node:8-alpine as builder

RUN mkdir /web
ADD . /web
WORKDIR /web
RUN yarn && yarn build

FROM nginx:1.17-alpine

MAINTAINER Lukáš Medelský <medel8159@gmail.com>

# Environmental variable for set up back-end url
ENV BE_URL=http://localhost:8080

# Copy static content and nginx config
COPY --from=builder /web/dist/ /usr/share/nginx/html/
COPY nginx_template.conf /etc/nginx/nginx_template.conf

# Expose port 80 for nginx
EXPOSE 80

# substitute variables in NGINX config template with real values, run and keep NGINX alive
ENTRYPOINT envsubst '$${BE_URL}' < /etc/nginx/nginx_template.conf > /etc/nginx/nginx.conf && \
            nginx -g 'daemon off;'
