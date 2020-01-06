FROM jupyter/scipy-notebook:latest
USER root

RUN conda update -y --all

# Install xelatex and latex extension
RUN apt-get update && apt-get -yq dist-upgrade \
  && apt-get install -yq --no-install-recommends \
  texlive-xetex \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* && \
  pip install jupyterlab_latex && \
  jupyter labextension install @jupyterlab/latex

RUN jupyter labextension install jupyterlab-drawio

RUN jupyter lab clean && \
  jupyter lab build

RUN fix-permissions $CONDA_DIR && \ 
  fix-permissions /home/$NB_USER

USER $NB_UID