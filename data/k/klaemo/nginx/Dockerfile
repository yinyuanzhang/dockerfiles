FROM ubuntu:13.10

RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:nginx/development && apt-get update
RUN apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# Attach volumes.
VOLUME /etc/nginx/sites-enabled
VOLUME /var/log/nginx

# Set working directory.
WORKDIR /etc/nginx

# Expose ports.
EXPOSE 80

# Define default command.
ENTRYPOINT ["nginx"]
