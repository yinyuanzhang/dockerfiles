FROM bradrydzewski/base
MAINTAINER nel215

WORKDIR /home/ubuntu
USER ubuntu
ADD nodejs.sh /etc/drone.d/

RUN /bin/bash -c ". /home/ubuntu/nvm/nvm.sh && nvm install v4.2.2"
