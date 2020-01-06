FROM ubuntu
LABEL MAINTAINER = "Adrian Siembida bida94@gmail.com"
RUN apt-get update -y
RUN apt-get install apache2 -y
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
