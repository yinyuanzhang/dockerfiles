FROM node:erbium as builder

WORKDIR /dist
COPY ./ /dist/

RUN npm install && npm run build

FROM nginx:alpine
COPY --from=builder /dist/build/. /usr/share/nginx/html

RUN echo 'server { location / {\
    root   /usr/share/nginx/html; \
    index  index.html index.htm; \
    add_header "Set-Cookie" "base_url=${REACT_APP_BASE_URL}"; \
    }}' > '/etc/nginx/conf.d/nginx_api.conf.template'

RUN rm /etc/nginx/conf.d/default.conf

CMD ["sh", "-c", "envsubst < /etc/nginx/conf.d/nginx_api.conf.template > /etc/nginx/conf.d/nginx_api.conf && nginx -g 'daemon off;'"]