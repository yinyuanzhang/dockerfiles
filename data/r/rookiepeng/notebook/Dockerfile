ARG BASE_CONTAINER=rookiepeng/notebook-core
FROM $BASE_CONTAINER

LABEL maintainer="rookiepeng <zpeng.me@gmail.com>"

USER $NB_UID
RUN conda install --quiet --yes \
    'numpy' \
    'matplotlib' \
    'pandas' \
    'scipy' \
    'seaborn' \
    'xlrd' \
    'plotly' \
    'autopep8' \
    'pandoc' \
    'ipywidgets' \
    'h5py' \
    'cython' \
    'conda-forge::jupyter_contrib_nbextensions' \
    && \
    conda clean --all -f -y && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    jupyter nbextension enable code_prettify/autopep8 && \
    jupyter nbextension enable collapsible_headings/main && \
    jupyter nbextension enable hide_header/main && \
    # Also activate ipywidgets extension for JupyterLab
    # Check this URL for most recent compatibilities
    # https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@^1.0.1 --no-build && \
    # jupyter labextension install jupyterlab_bokeh@1.0.0 --no-build && \
    jupyter lab build --dev-build=False && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER

# Switch back to notebook to avoid accidental container runs as root
USER $NB_UID
