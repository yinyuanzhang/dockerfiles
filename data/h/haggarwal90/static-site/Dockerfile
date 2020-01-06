FROM nginx:latest
# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /data/www
COPY index.html /data/www/index.html
COPY 404.html /data/www/404.html
COPY . /data/www
