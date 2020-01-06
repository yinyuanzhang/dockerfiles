FROM ubuntu:latest
MAINTAINER Servicio de Administracion Electrónica
EXPOSE 22 5901
ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
#RUN apt-get -y upgrade 
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install mc apt-utils sudo apt-utils dialog
RUN apt-get -y install openssh-server
RUN apt-get -y install tzdata 
#RUN apt-get -y install lxde
RUN apt-get install -y openbox obconf obmenu xterm
RUN apt-get -y install tigervnc-standalone-server

COPY addUserWithPassword /usr/bin/addUserWithPassword
RUN chmod 777 -R /usr/bin/addUserWithPassword
COPY runcontainer_vncserver /usr/bin/runcontainer_vncserver
RUN chmod 777 -R /usr/bin/runcontainer_vncserver
COPY containervncserver-setup.sh /usr/bin/containervncserver-setup.sh
RUN chmod 777 -R /usr/bin/containervncserver-setup.sh

ENTRYPOINT ["/bin/bash", "-c", "/usr/bin/runcontainer_vncserver"]