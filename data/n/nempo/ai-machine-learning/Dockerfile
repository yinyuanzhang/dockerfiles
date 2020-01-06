ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL MAINTAINER L. Van Acker

USER $NB_UID

RUN conda install --quiet --yes \
    'nltk'

RUN pip install -e git://github.com/YannDubs/scikit-optimize.git#egg=scikit-optimize
