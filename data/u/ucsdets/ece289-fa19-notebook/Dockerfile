ARG BASE_CONTAINER=ucsdets/scipy-ml-notebook:2019.4.5
FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

USER root

RUN pip install networkx rpy2==3.1.0 python-igraph powerlaw numpy scipy python-louvain

RUN apt-get update && apt-get -qq install -y \
	libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential pkg-config \
	&& apt-get clean

RUN pip install pycairo

USER $NB_UID
