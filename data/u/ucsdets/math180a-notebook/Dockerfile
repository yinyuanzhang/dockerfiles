ARG BASE_CONTAINER=ucsdets/datascience-notebook:2019.4.7
FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

USER root

RUN pip install prob140 datascience matplotlib scipy ipywidgets ipython 

USER $NB_UID
