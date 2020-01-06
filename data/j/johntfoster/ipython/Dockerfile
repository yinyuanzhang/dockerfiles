FROM debian:wheezy

MAINTAINER John Foster <johntfosterjr@gmail.com>

ENV HOME /root

RUN apt-get update
RUN apt-get -yq install gcc g++ gfortran build-essential
RUN apt-get -yq install pandoc python supervisor wget python-pip
RUN apt-get -yq install python-dev
RUN apt-get -yq install libblas-dev
RUN apt-get -yq install liblapack-dev
RUN apt-get -yq install libfreetype6-dev
RUN apt-get -yq install libpng12-dev
RUN apt-get -yq install openssl
RUN pip install pip --upgrade
RUN pip install numpy
RUN pip install scipy
RUN pip install distribute --upgrade
RUN pip install matplotlib
RUN pip install ipython[notebook]

RUN ipython profile create
RUN echo "c.FileNotebookManager.notebook_dir = u'/ipy'" >> /root/.ipython/profile_default/ipython_notebook_config.py

RUN mkdir /ipy
VOLUME ["/ipy"]
