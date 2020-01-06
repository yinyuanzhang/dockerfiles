FROM python:3.5.5-jessie
MAINTAINER fraoustin@gmail.com


# install ablog
RUN pip install docutils==0.14
RUN pip install sphinx==1.7.1
RUN pip install ablog==0.9.2 
RUN pip install sphinx_fontawesome
RUN pip install alabastermobile
COPY ./src/sphinxcontrib-master /tmp/sphinxcontrib-master
RUN cd /tmp/sphinxcontrib-master && \
	python setup.py install 

RUN mkdir /in

WORKDIR /in
VOLUME /in

ENTRYPOINT ["ablog"]
