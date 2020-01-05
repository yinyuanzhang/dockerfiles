FROM fastgenomics/jupyter-base:0.1.7

# bugfix for error during slingshot install:
# "libGL.so.1: cannot open shared object file: No such file or directory"
USER root
RUN apt-get update && apt-get install -y libgl1-mesa-glx
USER jovyan

COPY requirements_conda.txt requirements_pip.txt /tmp/

# Add channels in such order that the highest priority comes last

RUN conda config --append channels bioconda

RUN conda install -yq --file /tmp/requirements_conda.txt && \
	conda clean -afy

RUN pip install --upgrade pip && \
	pip install -r /tmp/requirements_pip.txt

# set flags for rgl-DLL used by Slingshot (see manual in Luecken & Theis, git repo)
RUN echo '#!/bin/sh\
CFLAGS_OLD=$CFLAGS\
export CFLAGS_OLD\
export CFLAGS="`gsl-config --cflags` ${CFLAGS_OLD}"\
LDFLAGS_OLD=$LDFLAGS\
export LDFLAGS_OLD\
export LDFLAGS="`gsl-config --libs` ${LDFLAGS_OLD}"' \
> /opt/conda/etc/conda/activate.d/env_vars.sh
RUN echo '#!/bin/sh\
CFLAGS=$CFLAGS_OLD\
export CFLAGS\
unset CFLAGS_OLD\
LDFLAGS=$LDFLAGS_OLD\
export LDFLAGS\
unset LDFLAGS_OLD' \
> /opt/conda/etc/conda/deactivate.d/env_vars.sh

# because R is R
ENV R_GZIPCMD=/bin/gzip
USER root
RUN ln -s /bin/tar /bin/gtar
USER jovyan

COPY install.R /tmp/install.R
RUN bash && Rscript /tmp/install.R

# install JupyterLab Extension
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

# run jupyter lab build just to make sure everything is up-to-date after package install
RUN jupyter lab build
