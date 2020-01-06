# using latest version as of 11-12-2019
FROM jupyter/datascience-notebook:45f07a14b422

USER root

USER jovyan

RUN conda install obspy basemap 
RUN pip install telewavesim && \
    pip install obspyh5 toeplitz rf && \
    pip install git+https://git.pyrocko.org/pyrocko/pyrocko.git
