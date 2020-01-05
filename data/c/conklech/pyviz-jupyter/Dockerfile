FROM jupyter/minimal-notebook:4cdbc9cdb7d1 
RUN conda install -c pyviz holoviews bokeh scipy datashader ipywidgets seaborn selenium phantomjs pillow netcdf4 --yes && \
    conda remove --quiet --yes --force qt pyqt && \
    conda clean -tipsy && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38.1 && \
    jupyter labextension install @pyviz/jupyterlab_pyviz && \
    jupyter labextension install jupyterlab_bokeh@0.6.3 && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER
   
USER $NB_UID
