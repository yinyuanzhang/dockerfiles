#####################################################
# Dockerfile to customeize NGINX for local HTTPs
# development, based on the official NGINX
#####################################################

# Set the base image
FROM        nginx:alpine

# File Author / Maintainer
LABEL       maintainer=info@adiwit.co.th

# Environmental Variables
ARG         DEBIAN_FRONTEND=noninteractive

# Change System TimeZone to Asia/Bangkok
RUN         ln -sf /usr/share/zoneinfo/Asia/Bangkok /etc/localtime

# Update Repositories
RUN         apk update \
            && apk add -U openssl \
            && openssl req -new -newkey rsa:1024 -nodes -x509 -subj '/C=TH/ST=localhost/L=localhost/O=localhost/CN=localhost' -keyout /etc/ssl/localhost.key -out /etc/ssl/localhost.crt \
            && openssl dhparam -out /etc/ssl/dhparam.pem 512

# Configurations
COPY        nginx.conf /etc/nginx/nginx.conf
