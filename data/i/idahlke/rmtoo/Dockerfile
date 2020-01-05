FROM ubuntu:latest
LABEL maintainer="ian.dahlke@mdaus.com"

#latex is a large package, so it's nice to have it in an isolated command
RUN apt-get update &&\
    apt-get -y install texlive-font-utils texlive-latex-extra texlive-latex-recommended

RUN apt-get update &&\
    apt-get -y install less make man nano gnuplot graphviz python3-pip virtualenv

RUN pip3 install --upgrade pip setuptools wheel

RUN /bin/bash -c 'mkdir /rmtoo &&\
    cd /rmtoo'

RUN pip3 install --only-binary=numpy,scipy numpy scipy &&\
    pip3 install rmtoo

RUN sed -i.bak 's/import distutils/import distutils.sysconfig/'\
    /usr/local/lib/python3.5/dist-packages/rmtoo/lib/configuration/CmdLineParams.py

RUN sed -i.bak 's/RMTOO_CONTRIB_DIR ?=.*/RMTOO_CONTRIB_DIR ?= \/usr\/local\/rmtoo/'\
    /usr/local/rmtoo/contrib/template_project/Makefile

RUN cp -r /usr/local/rmtoo/contrib/template_project/* /rmtoo

COPY newproj /usr/bin/
WORKDIR /rmtoo

CMD make 2>&1 | tee make.log