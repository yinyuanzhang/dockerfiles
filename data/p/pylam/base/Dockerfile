#https://github.com/mksec/docker-debian-systemd/blob/master/Dockerfile
ARG TAG=debian
FROM pylam/base:${TAG} 

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install ruby git vim
RUN apt-get -y install ruby2.3-dev libffi-dev automake autoconf libtool make 
RUN gem install travis
RUN apt-get -y remove ruby2.3-dev libffi-dev automake autoconf libtool make \
    && apt-get -y autoremove \
    && apt-get clean

CMD ["/bin/bash"]
