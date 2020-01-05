FROM ubuntu:latest
LABEL author="Tokarzewski"
RUN apt-get update && apt-get install -y apache2
COPY ./ports.conf /etc/apache2/
CMD ["/bin/bash","service apache2 restart"]
EXPOSE 8080
CMD ["apachectl", "-D", "FOREGROUND"]
