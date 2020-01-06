FROM jupyter/datascience-notebook:5ed91e8e3249 
RUN jupyter labextension install @jupyterlab/git && \
  pip install jupyterlab-git && \
  jupyter serverextension enable --py jupyterlab_git && \
  pip install nbgitpuller && \
  jupyter serverextension enable --py nbgitpuller --sys-prefix

