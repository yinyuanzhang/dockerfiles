# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=ucsdets/scipy-ml-notebook:5005dae
FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

USER root

###########################
RUN apt-get update && apt-get -qq install -y \
	libgeos-3.6.2 libgeos-c1v5 libgeos-dev

# nbgrader
RUN conda install nbgrader && conda clean -tipsy && \
	jupyter nbextension install --symlink --sys-prefix --py nbgrader && \
	jupyter nbextension enable --sys-prefix --py nbgrader && \
	jupyter serverextension enable --sys-prefix --py nbgrader && \
	jupyter nbextension disable --sys-prefix formgrader/main --section=tree && \
	jupyter serverextension disable --sys-prefix nbgrader.server_extensions.formgrader && \
	jupyter nbextension disable --sys-prefix create_assignment/main && \
	pip install ipywidgets && \
	jupyter nbextension enable --sys-prefix --py widgetsnbextension

# hacked local version of nbresuse to show GPU activity
RUN pip install --no-cache-dir git+https://github.com/agt-ucsd/nbresuse.git && \
	jupyter serverextension enable --sys-prefix --py nbresuse && \
	jupyter nbextension install --sys-prefix --py nbresuse && \
	jupyter nbextension enable --sys-prefix --py nbresuse && \
	pip install google-cloud-bigquery

RUN conda install --yes basemap && \
	fix-permissions $CONDA_DIR

ENV PROJ_LIB /opt/conda/share/proj

USER $NB_UID

#COPY pip-requirements.txt /tmp
#RUN pip install --no-cache-dir -r /tmp/pip-requirements.txt  && \
	#fix-permissions $CONDA_DIR
