FROM ubuntu:14.04
MAINTAINER Jason Wilder jwilder@litl.com

# Install Nginx.
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" > /etc/apt/sources.list.d/nginx-stable-trusty.list
RUN echo "deb-src http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >> /etc/apt/sources.list.d/nginx-stable-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C
RUN apt-get update
RUN apt-get install -y  wget nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

#fix for long server names
RUN sed -i 's/# server_names_hash_bucket/server_names_hash_bucket/g' /etc/nginx/nginx.conf

ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego /usr/local/bin/forego
RUN chmod u+x /usr/local/bin/forego

# Generate dummy SSL certificates
RUN mkdir /ssl
RUN openssl req -new -x509 -days 365 -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.org" -nodes -out /ssl/nginx.pem -keyout /ssl/nginx.key

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN wget https://github.com/jwilder/docker-gen/releases/download/0.7.3/docker-gen-linux-amd64-0.7.3.tar.gz
RUN tar xvzf docker-gen-linux-amd64-0.7.3.tar.gz

EXPOSE 80
EXPOSE 443
ENV DOCKER_HOST unix:///tmp/docker.sock

CMD ["forego", "start", "-r"]
