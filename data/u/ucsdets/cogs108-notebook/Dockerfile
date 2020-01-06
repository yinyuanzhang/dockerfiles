ARG BASE_CONTAINER=ucsdets/datascience-notebook:2019.4.7
FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

USER root

RUN conda install -y pandas==0.25.2
RUN pip install nltk

USER $NB_UID
