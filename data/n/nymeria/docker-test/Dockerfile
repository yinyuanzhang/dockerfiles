 FROM ubuntu:latest

 MAINTAINER Muratcan İtap <mitap45@gmail.com>

 RUN apt-get update && apt-get install -y iputils-ping

 RUN apt-get install -y nginx

 RUN apt-get install -y git

 RUN apt-get install nano

 # Clone our private GitHub Repository
 RUN git clone https://github.com/mitap45/docker-test.git /docker-test/
 RUN cp -R /docker-test/* /var/www/html/


 #ADD ["./index.html", "/var/www/html/"]

 EXPOSE 80

 ENTRYPOINT nginx -g 'daemon off;'
 