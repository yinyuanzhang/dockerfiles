FROM jupyter/datascience-notebook:1386e2046833
RUN  pip install nbgitpuller && \ 
     jupyter serverextension enable nbgitpuller --sys-prefix && \
     pip install symbulate
USER $NB_USER
