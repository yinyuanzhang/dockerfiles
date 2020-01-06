FROM ubuntu:latest as apache
RUN apt update
RUN apt -y install apache2
COPY ./script.sh .
EXPOSE 80
CMD ["/bin/bash", "./script.sh"]
