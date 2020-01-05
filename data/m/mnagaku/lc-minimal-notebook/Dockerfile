FROM jupyter/base-notebook
MAINTAINER mnagaku

USER root
# Install tools and fonts
RUN apt-get update && apt-get upgrade -y && apt-get install -yq --no-install-recommends \
    git \
    vim \
    unzip \
    curl \
    iproute2 \
    fonts-ipafont-gothic fonts-ipafont-mincho \
### Utilities
    zip iputils-ping \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
### ansible
    pip --no-cache-dir install requests paramiko ansible \
### Utilities
    papermill \
    pandas matplotlib pytz numpy seaborn scipy scikit-learn dill bokeh \
#### Visualization
    folium \
### extensions for jupyter
    jupyter_nbextensions_configurator six \
    https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master \
    https://github.com/NII-cloud-operation/Jupyter-LC_nblineage/tarball/master \
    https://github.com/NII-cloud-operation/Jupyter-LC_run_through/tarball/master \
    https://github.com/NII-cloud-operation/Jupyter-LC_wrapper/tarball/master \
    git+https://github.com/NII-cloud-operation/Jupyter-multi_outputs \
    git+https://github.com/NII-cloud-operation/Jupyter-LC_index.git \
    git+https://github.com/NII-cloud-operation/Jupyter-LC_notebook_diff.git

# Copy config files
ADD conf /tmp/
RUN mkdir -p $CONDA_DIR/etc/jupyter && \
    cp -f /tmp/jupyter_notebook_config.py \
       $CONDA_DIR/etc/jupyter/jupyter_notebook_config.py

SHELL ["/bin/bash", "-c"]

### Add files
RUN mkdir -p /etc/ansible && cp /tmp/ansible.cfg /etc/ansible/ansible.cfg

RUN jupyter contrib nbextension install --sys-prefix && \
    jupyter nblineage quick-setup --sys-prefix && \
    jupyter nbextension install --py lc_run_through --sys-prefix && \
    jupyter nbextension enable --py lc_run_through --sys-prefix && \
    jupyter nbextension install --py lc_multi_outputs --sys-prefix && \
    jupyter nbextension enable --py lc_multi_outputs --sys-prefix && \
    jupyter nbextension install --py notebook_index --sys-prefix && \
    jupyter nbextension enable --py notebook_index --sys-prefix && \
    jupyter nbextension install --py lc_wrapper --sys-prefix && \
    jupyter nbextension enable --py lc_wrapper --sys-prefix && \
    jupyter nbextension install --py lc_notebook_diff --sys-prefix && \
    jupyter nbextension enable nbextensions_configurator/config_menu/main --sys-prefix && \
    jupyter nbextension enable contrib_nbextensions_help_item/main --sys-prefix && \
    jupyter nbextension enable collapsible_headings/main --sys-prefix && \
    jupyter nbextension enable toc2/main --sys-prefix && \
    jupyter nbextension enable dragdrop/main --sys-prefix && \
    jupyter kernelspec install /tmp/kernels/python3-wrapper --sys-prefix && \
    fix-permissions /home/$NB_USER

### nbconfig
RUN mkdir -p $CONDA_DIR/etc/jupyter/nbconfig/notebook.d && \
    cp /tmp/nbextension-config.json $CONDA_DIR/etc/jupyter/nbconfig/notebook.d/nbextension-config.json

### notebooks dir
ADD sample-notebooks /home/$NB_USER
RUN fix-permissions /home/$NB_USER

### Bash Strict Mode
RUN cp /tmp/bash_env /etc/bash_env

### Theme for jupyter
RUN CUSTOM_DIR=$(python -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib())')/notebook/static/custom && \
    cat /tmp/custom.css >> $CUSTOM_DIR/custom.css && \
    cp /tmp/logo.png $CUSTOM_DIR/logo.png && \
    mkdir -p $CUSTOM_DIR/codemirror/addon/merge/ && \
    curl -fL https://raw.githubusercontent.com/cytoscape/cytoscape.js/master/dist/cytoscape.min.js > $CUSTOM_DIR/cytoscape.min.js && \
    curl -fL https://raw.githubusercontent.com/iVis-at-Bilkent/cytoscape.js-view-utilities/master/cytoscape-view-utilities.js > $CUSTOM_DIR/cytoscape-view-utilities.js && \
    curl -fL https://raw.githubusercontent.com/NII-cloud-operation/Jupyter-LC_notebook_diff/master/html/jupyter-notebook-diff.js > $CUSTOM_DIR/jupyter-notebook-diff.js && \
    curl -fL https://raw.githubusercontent.com/NII-cloud-operation/Jupyter-LC_notebook_diff/master/html/jupyter-notebook-diff.css > $CUSTOM_DIR/jupyter-notebook-diff.css && \
    curl -fL https://cdnjs.cloudflare.com/ajax/libs/diff_match_patch/20121119/diff_match_patch.js > $CUSTOM_DIR/diff_match_patch.js && \
    curl -fL https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.35.0/addon/merge/merge.js > $CUSTOM_DIR/codemirror/addon/merge/merge.js && \
    curl -fL https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.35.0/addon/merge/merge.min.css > $CUSTOM_DIR/merge.min.css

### Custom get_ipython().system() to control error propagation of shell commands
RUN mkdir -p $CONDA_DIR/etc/ipython/startup/ && \
    cp /tmp/ipython_config.py $CONDA_DIR/etc/ipython/ && \
    cp /tmp/10-custom-get_ipython_system.py $CONDA_DIR/etc/ipython/startup/

USER $NB_USER
