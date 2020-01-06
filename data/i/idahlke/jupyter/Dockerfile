#This runs Jupyter datascience-notebook with extra packages installed
ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Ian Dahlke <ian.dahlke@gmail.com>"

USER root

# set up brew package manager
RUN apt-get -yq update && apt-get install -yq \
    build-essential \
    curl \
    file \
    git \
    python-setuptools \
    && apt-get clean

RUN mkdir ~/.linuxbrew  \
    && git clone https://github.com/Linuxbrew/brew.git ~/.linuxbrew 
ENV PATH="$HOME/.linuxbrew/bin:${PATH}" 
ENV MANPATH="$(brew --prefix)/share/man:${MANPATH}" 
ENV INFOPATH="$(brew --prefix)/share/info:${INFOPATH}"

# Install desired packages from scipy-notebook
RUN pip install --upgrade pip
RUN pip install \
    pandas \
    matplotlib \
    scipy \
    seaborn \
    scikit-learn \
    scikit-image \
    sympy \
    bokeh

# Install Conda Packages
RUN conda install -yc conda-forge nodejs

########################################
# Setup Jupyter Notebook Extensions
########################################
# Install Extension Configurator and extensions
RUN conda install -yc conda-forge \
    jupyter_nbextensions_configurator \
	jupyter_contrib_nbextensions

# Add live slideshows with RISE
RUN pip install RISE && \
    jupyter-nbextension install rise --py --sys-prefix && \
    jupyter-nbextension enable rise --py --sys-prefix

# Add ipyleaflet plugin for Jupyter
RUN pip install ipyleaflet && \
    jupyter nbextension install --py --sys-prefix ipyleaflet && \
    jupyter nbextension enable --py --sys-prefix ipyleaflet

########################################
# Setup Jupyter Lab Extensions
########################################
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build && \
	jupyter labextension install jupyterlab-plotly@1.3.0 --no-build && \
	jupyter labextension install plotlywidget@1.3.0 --no-build && \
	jupyter lab build

# Add Octave and Octave kernel
RUN apt-get -yq update && apt-get -yq install octave && apt-get clean
RUN pip install octave_kernel

# Add bash kernel
RUN pip install bash_kernel && \
    python -m bash_kernel.install

# Install Humor-Sans.ttf for xkcd plots
RUN apt-get update -yq && apt-get install -yq fonts-humor-sans && apt-get clean

# set auth token to null string. i.e. disable auth.
RUN mkdir -p ~/.jupyter && \
    echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID