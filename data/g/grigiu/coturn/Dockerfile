FROM debian:stretch-slim

MAINTAINER Gri Giu <grigiua@gmail.com>

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

EXPOSE 3478

RUN apt-get update && apt-get install -y \
    dnsutils \
    coturn \
  && rm -rf /var/lib/apt/lists/*
  
COPY ./turnserver.conf /etc/turnserver.conf

ENTRYPOINT ["bash", "deploy-turnserver.sh"]    
