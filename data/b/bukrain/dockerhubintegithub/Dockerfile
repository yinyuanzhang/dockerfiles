FROM ubuntu:latest
LABEL maintainer="rafal.sieczka@pollub.edu.pl"
RUN apt-get update && apt-get -y install apache2

EXPOSE 80

CMD apachectl -D FOREGROUND
