# Use Ubuntu 18.04
FROM ubuntu:18.04

# Install NodeJS and NPM
RUN apt-get update
RUN apt-get -y install nginx git nodejs npm
RUN apt-get -y clean

# Create directories that will be required
RUN mkdir -p /var/log/nginx
RUN mkdir -p /var/www/html

# Copy the respective nginx configuration files
COPY nginx_config/nginx.conf /etc/nginx/nginx.conf
COPY nginx_config/default.conf /etc/nginx/conf.d/default.conf

# Set the directory we want to run the next commands for
WORKDIR /var/www/html

# Copy our source code into the container
COPY . .

# Navigate to the web directory and install npm packages and build using webpack
RUN npm install && npm run build

# Make all files belong to the www-data user
RUN chown www-data:www-data /var/www/html

# Make ports 80 and 443 available to the world outside this container
EXPOSE 80
EXPOSE 443

# Start nginx and keep the process from backgrounding and the container from quitting
CMD ["nginx", "-g", "daemon off;"]
