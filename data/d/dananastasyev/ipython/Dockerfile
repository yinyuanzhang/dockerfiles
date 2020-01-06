FROM ubuntu:14.04
MAINTAINER Daniil Anastasyev 

EXPOSE 8888

VOLUME /notebooks
WORKDIR /notebooks

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python2.7 python2.7-dev python-pip python-zmq libzmq-dev
#RUN apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
RUN pip2 install ipython[all]

CMD ipython notebook
