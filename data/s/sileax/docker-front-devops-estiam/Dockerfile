FROM httpd:latest

ENV FRONT_DEVOPS_VERSION 0.0.1

RUN apt update
RUN apt install git-all -y
RUN git clone https://github.com/Sileax/docker-front-devops-estiam.git
RUN cp -R /usr/local/apache2/docker-front-devops-estiam/* /usr/local/apache2/htdocs
RUN kill -USR1 1
