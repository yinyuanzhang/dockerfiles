FROM ubuntu:16.04
Maintainer Seamaster1103
Label pupose="HandsonLAB"
run apt-get update
RUN apt-get install apache2 -y
#ADD test.html /var/www/html
workdir /var/www/html
RUN ["/bin/bash", "-c", "echo Welcome to docker Automated!!! >> test2.html"]
Expose 80
CMD ["apachectl", "-DFOREGROUND"]