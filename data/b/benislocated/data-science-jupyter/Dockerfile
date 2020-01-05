# https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook

# docker build -t datasci .

# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html#run-jupyterlab
# docker run -it -e JUPYTER_ENABLE_LAB=yes -p 8888:8888 --net=dockernet  -v "$PWD":/home/jovyan datasci start.sh jupyter lab --LabApp.token=''

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#core-stacks
# https://raw.githubusercontent.com/jupyter/docker-stacks/master/datascience-notebook/Dockerfile

ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root

# R pre-requisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    tzdata \
    graphviz \
    gfortran \
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Julia dependencies
# install Julia packages in /opt/julia instead of $HOME
ENV JULIA_DEPOT_PATH=/opt/julia
ENV JULIA_PKGDIR=/opt/julia
ENV JULIA_VERSION=1.0.0

RUN mkdir /opt/julia-${JULIA_VERSION} && \
    cd /tmp && \
    wget -q https://julialang-s3.julialang.org/bin/linux/x64/`echo ${JULIA_VERSION} | cut -d. -f 1,2`/julia-${JULIA_VERSION}-linux-x86_64.tar.gz && \
    echo "bea4570d7358016d8ed29d2c15787dbefaea3e746c570763e7ad6040f17831f3 *julia-${JULIA_VERSION}-linux-x86_64.tar.gz" | sha256sum -c - && \
    tar xzf julia-${JULIA_VERSION}-linux-x86_64.tar.gz -C /opt/julia-${JULIA_VERSION} --strip-components=1 && \
    rm /tmp/julia-${JULIA_VERSION}-linux-x86_64.tar.gz
RUN ln -fs /opt/julia-*/bin/julia /usr/local/bin/julia

# Show Julia where conda libraries are \
RUN mkdir /etc/julia && \
    echo "push!(Libdl.DL_LOAD_PATH, \"$CONDA_DIR/lib\")" >> /etc/julia/juliarc.jl && \
    # Create JULIA_PKGDIR \
    mkdir $JULIA_PKGDIR && \
    chown $NB_USER $JULIA_PKGDIR && \
    fix-permissions $JULIA_PKGDIR

USER $NB_UID

# R packages including IRKernel which gets installed globally.
RUN conda install --quiet --yes \
    'rpy2=2.8*' \
    'r-base=3.4.1' \
    'r-irkernel=0.8*' \
    'r-plyr=1.8*' \
    'r-devtools=1.13*' \
    'r-tidyverse=1.1*' \
    'r-shiny=1.0*' \
    'r-rmarkdown=1.8*' \
    'r-forecast=8.2*' \
    'r-rsqlite=2.0*' \
    'r-reshape2=1.4*' \
    'r-nycflights13=0.2*' \
    'r-caret=6.0*' \
    'r-rcurl=1.95*' \
    'r-crayon=1.3*' \
    'r-randomforest=4.6*' \
    'r-htmltools=0.3*' \
    'r-sparklyr=0.7*' \
    'r-htmlwidgets=1.0*' \
    'r-hexbin=1.27*' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Add Julia packages. Only add HDF5 if this is not a test-only build since
# it takes roughly half the entire build time of all of the images on Travis
# to add this one package and often causes Travis to timeout.
#
# Install IJulia as jovyan and then move the kernelspec out
# to the system share location. Avoids problems with runtime UID change not
# taking effect properly on the .local folder in the jovyan home dir.
RUN julia -e 'import Pkg; Pkg.update()' && \
    (test $TEST_ONLY_BUILD || julia -e 'import Pkg; Pkg.add("HDF5")') && \
    julia -e 'import Pkg; Pkg.add("Gadfly")' && \
    julia -e 'import Pkg; Pkg.add("RDatasets")' && \
    julia -e 'import Pkg; Pkg.add("IJulia")' && \
    # Precompile Julia packages \
    julia -e 'using IJulia' && \
    # move kernelspec out of home \
    mv $HOME/.local/share/jupyter/kernels/julia* $CONDA_DIR/share/jupyter/kernels/ && \
    chmod -R go+rx $CONDA_DIR/share/jupyter && \
    rm -rf $HOME/.local && \
    fix-permissions $JULIA_PKGDIR $CONDA_DIR/share/jupyter

# based on
# https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile

USER root
RUN conda config --append channels auto
RUN conda config --append channels conda-forge
RUN conda config --append channels jlmenut
RUN conda config --append channels qinves
RUN conda config --append channels trung
RUN conda install --quiet --yes \
    'dicttoxml' \
#https://github.com/quandyfactory/dicttoxml
#    'dict2xml' \
    'google-api-python-client' \
#https://anaconda.org/conda-forge/google-api-python-client
    'httplib2' \
#https://github.com/httplib2/httplib2
    'lxml' \
#https://github.com/lxml/lxml
    'missingno' \
#https://github.com/ResidentMario/missingno
    'oauth2client' \
#https://anaconda.org/conda-forge/oauth2client
    'python-pdfkit' \
#https://anaconda.org/conda-forge/python-pdfkit
#    'pycallgraph' \
#https://anaconda.org/qinves/pycallgraph
    'pydot' \
#https://anaconda.org/anaconda/pydot
    'selenium' \
#https://anaconda.org/conda-forge/selenium
#    'json2xml' \
#https://anaconda.org/auto/json2xml
    'tzlocal' \
#https://anaconda.org/conda-forge/tzlocal
#    'weasyprint' \
#https://anaconda.org/jlmenut/weasyprint
    'wkhtmltopdf' \
#https://anaconda.org/bioconda/wkhtmltopdf
    'xhtml2pdf' \
#https://anaconda.org/SasView/xhtml2pdf
    'xlsxwriter' \
#https://anaconda.org/anaconda/xlsxwriter
    'xmltodict' \
#https://anaconda.org/conda-forge/xmltodict
    'pypdf2' \
#http://mstamy2.github.io/PyPDF2/
    'faker' \
#https://faker.readthedocs.io/en/master/
    'graphviz' \
    'python-graphviz' \
    'line_profiler' \
#https://anaconda.org/anaconda/line_profiler
    'py2neo' \
    'openpyxl' && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER


USER $NB_UID
