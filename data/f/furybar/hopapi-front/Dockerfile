FROM nginx:alpine

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/ssl/fullchain.pem /etc/letsencrypt/live/hopapi.com/fullchain.pem
COPY nginx/ssl/privkey.pem /etc/letsencrypt/live/hopapi.com/privkey.pem

WORKDIR /usr/share/nginx/html
COPY dist/ .