

FROM ubuntu:18.04
MAINTAINER "A test production"
RUN apt-get update && apt-get install apache2 -y && service apache2 start
ADD https://github.com/irajibbiswas/rbgithubrepository/blob/master/index.html /var/www/html


#####################
#FROM ubuntu:18.04
#FROM httpd
#RUN apt-get update
#RUN  apt-get install apache2 -y
#RUN service apache2 start
#WORKDIR /var/www/html/