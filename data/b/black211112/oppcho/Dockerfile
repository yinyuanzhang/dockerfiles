FROM ubuntu
LABEL maintainer="Ochalski Piotr piotr.ochalski@pollub.edu.pl"
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install apache2 -y
CMD apachectl -D FOREGROUND
EXPOSE 80
