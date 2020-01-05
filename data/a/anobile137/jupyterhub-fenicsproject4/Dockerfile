# Public Domain
# github project: jupyterhub-fenicsproject with necessary packages
# install mshr, scipy, matplotlib and bokeh (for interactive graphics) for use in fenics environment
# version: 0.1
FROM jupyter/minimal-notebook

LABEL maintainer="Art Nobile <anobile137@gmail.com>"

USER root

USER $NB_UID

# Install mshr Python Package
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN conda install mshr && \
    conda install scipy && \
    conda install matplotlib && \
    conda install bokeh && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
USER $NB_UID
