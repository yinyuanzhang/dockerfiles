FROM jupyter/base-notebook

USER $NB_UID

RUN pip install --no-cache-dir \
    'numpy==1.16.4' \
    'plotly==3.10.0' \
    'matplotlib==3.1.0' \
    'mne==0.18.1' \
    'ipywidgets==7.4.2' && \
    conda clean --all -f -y && \
    export NODE_OPTIONS=--max-old-space-size=4096 && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38 --no-build && \
    jupyter labextension install plotlywidget@0.11.0 --no-build && \
    jupyter labextension install @jupyterlab/plotly-extension@0.18.2 --no-build && \
    jupyter labextension install @mohirio/jupyterlab-horizon-theme@0.1.4 --no-build && \
    jupyter lab build && \
    npm cache clean --force && \
    unset NODE_OPTIONS && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

ENV JUPYTER_ENABLE_LAB=yes
USER $NB_UID