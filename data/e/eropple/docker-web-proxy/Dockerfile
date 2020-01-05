FROM ubuntu:14.04
MAINTAINER Ed Ropple ed+dockerwebproxy@edropple.com

RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" > /etc/apt/sources.list.d/nginx-stable-trusty.list
RUN echo "deb-src http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >> /etc/apt/sources.list.d/nginx-stable-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C
RUN apt-get update
RUN apt-get install -y  wget nginx ruby bundler

RUN update-rc.d -f nginx disable

#fix for long server names (h/t Jason Wilder, https://github.com/jwilder/nginx-proxy)
RUN sed -i 's/# server_names_hash_bucket/server_names_hash_bucket/g' /etc/nginx/nginx.conf

ADD ./app /opt/proxy
WORKDIR /opt/proxy
RUN bundle install

ENV DOCKER_URL unix:///var/run/docker.sock
EXPOSE 80
EXPOSE 443

CMD ["./bin/approxinate_server.rb"]