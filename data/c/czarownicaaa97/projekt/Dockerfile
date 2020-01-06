FROM ubuntu
LABEL maintainer ="Iga Wilk"
RUN apt-get upgrade
RUN apt-get update -y
RUN apt-get install apache2 -y
EXPOSE 80
CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]

