# using latest version as of 11-12-2019
FROM jupyter/datascience-notebook:45f07a14b422

USER root

RUN pip install nbzip && \
    jupyter nbextension install --py nbzip
USER jovyan

RUN jupyter serverextension enable --py nbzip --sys-prefix && \
    jupyter nbextension enable --py nbzip
