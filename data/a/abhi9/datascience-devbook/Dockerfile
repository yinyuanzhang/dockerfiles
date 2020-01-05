FROM jupyter/all-spark-notebook
LABEL maintainer="Abhinav A V<abhai2k@gmail.com>"

USER $NB_UID
RUN pip install --upgrade pip
# BeakerX
# RUN conda install -y -c conda-forge beakerx
# RUN jupyter labextension install beakerx-jupyterlab
RUN pip install beakerx
RUN beakerx install
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager
RUN jupyter labextension install beakerx-jupyterlab

# Install SQLServer driver
USER root
RUN apt-get update && apt-get install -my wget gnupg
RUN wget -O - https://deb.nodesource.com/setup_10.x | bash
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update --allow-unauthenticated
RUN ACCEPT_EULA=Y apt-get install msodbcsql17 -y
RUN ACCEPT_EULA=Y apt-get install mssql-tools -y
ENV PATH="/opt/mssql-tools/bin:${PATH}"
RUN apt-get install unixodbc-dev nodejs -y

USER $NB_UID
RUN pip install --upgrade jupyterlab \
                pyodbc \
                ipyparallel \
                ipython-sql \
                pymongo \
                prompt_toolkit

RUN npm install -g ijavascript
RUN ijsinstall
RUN npm install -g itypescript mongodb

USER root
RUN ipcluster nbextension enable
RUN its --install=global

USER $NB_UID
RUN pip install --upgrade imongo-kernel \
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

# GIT
RUN jupyter labextension install @jupyterlab/git
RUN pip install jupyterlab-git
RUN jupyter serverextension enable --py jupyterlab_git
# QGrid
# RUN jupyter labextension install qgrid
# SQL
# RUN pip install jupyterlab_sql
# RUN jupyter serverextension enable jupyterlab_sql --py --sys-prefix
# RUN jupyter lab build
# Code Formatter
RUN jupyter labextension install @ryantam626/jupyterlab_code_formatter
RUN pip install jupyterlab_code_formatter
RUN jupyter serverextension enable --py jupyterlab_code_formatter
RUN pip install black
# GoTo Defn
RUN jupyter labextension install @krassowski/jupyterlab_go_to_definition
# Spreadsheet
# RUN jupyter labextension install jupyterlab-spreadsheet
# Autoversion
RUN pip install jupyterlab_autoversion
RUN jupyter labextension install jupyterlab_autoversion
RUN jupyter serverextension enable --py jupyterlab_autoversion
# Bonobo
RUN pip install bonobo
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension
RUN jupyter nbextension enable --py --sys-prefix bonobo.contrib.jupyter
# Resource Monitor
RUN pip install nbresuse
RUN jupyter serverextension enable --py nbresuse
RUN jupyter labextension install jupyterlab-topbar-extension
RUN jupyter labextension install jupyterlab-system-monitor
# Cell Tags
RUN jupyter labextension install @jupyterlab/celltags
# Shortcut UI https://github.com/jupyterlab/jupyterlab-shortcutui
#RUN jupyter labextension install @jupyterlab/shortcutui # Disabled due to lab ver > extension
# Run All extension
RUN jupyter labextension install @enlznep/runall-extension
# Material Dark Theme
RUN jupyter labextension install @oriolmirosa/jupyterlab_materialdarker
# #Jupyter Widgets JupyterLab Extension
# RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager
# Spark UI
# RUN pip install jupyterlab-spark-ui-tab
# RUN jupyter labextension install @liorbaber/spark-ui-tab
# RUN jupyter serverextension install --py spark-ui-tab
# # Hub Extension
# RUN jupyter labextension install @jupyterlab/hub-extension
# Spark Magic
RUN pip install sparkmagic
# RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension  
USER root
RUN jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/sparkkernel
RUN jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/pysparkkernel
RUN jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/pyspark3kernel
RUN jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/sparkrkernel
USER $NB_UID
RUN jupyter serverextension enable --py sparkmagic

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




