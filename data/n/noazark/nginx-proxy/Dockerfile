FROM ubuntu:14.04
MAINTAINER Jason Wilder jwilder@litl.com

# Install Nginx.
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" > /etc/apt/sources.list.d/nginx-stable-trusty.list
RUN echo "deb-src http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >> /etc/apt/sources.list.d/nginx-stable-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C
RUN apt-get update
RUN apt-get install -y nginx

RUN mkdir /app
WORKDIR /app

ADD https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-amd64/forego /usr/local/bin/forego
RUN chmod u+x /usr/local/bin/forego

ADD https://github.com/jwilder/docker-gen/releases/download/0.3.2/docker-gen-linux-amd64-0.3.2.tar.gz /app/docker-gen-linux-amd64-0.3.2.tar.gz
RUN tar xvzf docker-gen-linux-amd64-0.3.2.tar.gz
RUN rm docker-gen-linux-amd64-0.3.2.tar.gz

EXPOSE 80
EXPOSE 443
ENV DOCKER_HOST unix:///tmp/docker.sock

ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./nginx.tmpl /app/nginx.tmpl
ADD ./Procfile /app/Procfile

CMD ["forego", "start", "-r"]
