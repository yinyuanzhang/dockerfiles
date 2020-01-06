FROM jenkins:latest
MAINTAINER demetrius.nunes@izzui.com

USER root 

RUN wget -qO- https://get.docker.com/ | sh

RUN usermod -aG docker jenkins

RUN apt-get install -yq python-pip 

RUN pip install -U docker-compose
