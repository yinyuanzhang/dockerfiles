FROM jupyter/scipy-notebook

MAINTAINER GoAbout <tech@goabout.com>

# Install Jupyter Lab, extensions, and supporting packages
RUN pip install arrow ipyleaflet jupyterlab requests && \
    jupyter serverextension enable --py jupyterlab && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    jupyter labextension install jupyter-leaflet
