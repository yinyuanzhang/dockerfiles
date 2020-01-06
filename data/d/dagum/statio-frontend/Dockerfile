FROM nginx:alpine
COPY config/nginx.conf /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/
RUN chmod -R 0755 /usr/share/nginx/html/*
EXPOSE 8080
