FROM nginx

# Add special configuration for nginx
ADD ./deployment/nginx/nginx.conf /etc/nginx/nginx.conf

# Add the application itself
ADD ./app/ /var/www/kibana

# Define working directory.
WORKDIR /etc/nginx

# Expose ports
EXPOSE 80
EXPOSE 443