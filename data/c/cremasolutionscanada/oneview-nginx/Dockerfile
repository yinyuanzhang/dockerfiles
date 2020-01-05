# Set nginx base image
FROM nginx

# File Author / Maintainer
MAINTAINER Kishore Chandra

# Copy custom configuration file from the current directory
RUN rm -v /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/default.conf