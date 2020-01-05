FROM ubuntu:14.04
MAINTAINER Nicolai Kochtov
EXPOSE 8888
VOLUME /notebooks
WORKDIR /notebooks
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python2.7 python2.7-dev python-pip python-zmq libzmq-dev
RUN pip2 install ipython[all]
CMD ipython notebook
