FROM jupyter/all-spark-notebook
LABEL maintainer="Abhinav A V<abhai2k@gmail.com>"

USER $NB_UID
RUN pip install --upgrade pip \
      jupyterlab \
      prompt_toolkit \
      ipyparallel
# Add Changed below this
# Install SQL Driver
USER root
RUN apt-get update && apt-get install -my wget gnupg
# RUN wget -O - https://deb.nodesource.com/setup_12.x | bash
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update --allow-unauthenticated
RUN ACCEPT_EULA=Y apt-get install msodbcsql17 -y
RUN ACCEPT_EULA=Y apt-get install mssql-tools -y
ENV PATH="/opt/mssql-tools/bin:${PATH}"
RUN apt-get install --no-install-recommends  -y \
            unixodbc-dev \
            fonts-dejavu \
            r-cran-rodbc \
            gfortran \
            gcc

# Fix for devtools https://github.com/conda-forge/r-devtools-feedstock/issues/4
RUN ln -s /bin/tar /bin/gtar

USER $NB_UID
RUN npm install -g ijavascript
RUN ijsinstall
RUN npm install -g itypescript mongodb

USER root
RUN its --install=global
RUN ipcluster nbextension enable
RUN jupyter nbextension install --sys-prefix --py ipyparallel
RUN jupyter nbextension enable --sys-prefix --py ipyparallel
RUN jupyter serverextension enable --sys-prefix --py ipyparallel

USER $NB_UID
# iMongo Kernel - Does not work
# RUN pip install git+https://github.com/boun/imongo.git
# RUN pip install git+https://github.com/gusutabopb/imongo.git
RUN pip install --upgrade \
          pyodbc \
          ipython-sql \
          pymongo \
          tensorrec \
          psycopg2-binary \
          dist-keras \
          scikit-multilearn \
          rpy2 \
          strsim \
          fuzzywuzzy \
          python-levenshtein \
          dedupe \
          matlab_kernel \
          redis_kernel

# R-Kernel
RUN conda install --quiet --yes \
    'r-base=3.5.1' \
    'r-rodbc=1.3*' \
    'unixodbc=2.3.*' \
    'r-irkernel=0.8*' \
    'r-plyr=1.8*' \
    'r-devtools=2.0*' \
    'r-tidyverse=1.2*' \
    'r-shiny=1.2*' \
    'r-rmarkdown=1.11*' \
    'r-forecast=8.2*' \
    'r-rsqlite=2.1*' \
    'r-reshape2=1.4*' \
    'r-nycflights13=1.0*' \
    'r-caret=6.0*' \
    'r-rcurl=1.95*' \
    'r-crayon=1.3*' \
    'r-randomforest=4.6*' \
    'r-htmltools=0.3*' \
    'r-sparklyr=0.9*' \
    'r-htmlwidgets=1.2*' \
    'r-hexbin=1.27*' && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR

# Extensions
RUN jupyter labextension install \
      @jupyterlab/hub-extension \
      jupyterlab_bokeh \
      @jupyter-widgets/jupyterlab-manager \
      @jupyterlab/git \
      qgrid \
      @ryantam626/jupyterlab_code_formatter \
      @krassowski/jupyterlab_go_to_definition \
      jupyterlab-spreadsheet \
      @jupyterlab/celltags \
      @enlznep/runall-extension \
      jupyterlab-topbar-extension \
      jupyterlab-system-monitor

# Git
RUN pip install jupyterlab-git && \
    jupyter serverextension enable --py jupyterlab_git

# SQL
RUN pip install jupyterlab_sql && \
      jupyter serverextension enable jupyterlab_sql --py --sys-prefix && \
      jupyter lab build

# Code Formatter
RUN pip install jupyterlab_code_formatter && \
    jupyter serverextension enable --py jupyterlab_code_formatter && \ 
    pip install black

# Auto Version
RUN pip install jupyterlab_autoversion && \
      jupyter labextension install jupyterlab_autoversion && \
      jupyter serverextension enable --py jupyterlab_autoversion

# Spark Tab UI
# RUN pip install jupyterlab-spark-ui-tab && \
#       jupyter labextension install @liorbaber/jupyterlab-spark-ui-tab && \
#       jupyter serverextension enable --py spark-ui-tab

# SparkMagic
RUN pip install sparkmagic
# RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension  
USER root
RUN jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/sparkkernel
RUN jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/pysparkkernel
RUN jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/pyspark3kernel
RUN jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/sparkrkernel
USER $NB_UID
RUN jupyter serverextension enable --py sparkmagic

# Do not change below this
USER root
RUN npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER &&\
    apt-get autoremove -y && \
    apt-get clean -y
  
USER $NB_UID