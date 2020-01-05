FROM jupyter/base-notebook
ARG JUPYTERHUB_VERSION=1.0.0
RUN conda config --set ssl_verify false
RUN conda config --add channels conda-forge
RUN conda config --add channels pyviz
RUN conda install --quiet --yes \
          xarray \
          dask \
          distributed \
          dask-jobqueue \
          graphviz \
          netCDF4 \
          bottleneck \
          nc-time-axis \
          ipywidgets \
          'tornado < 6' \
          cartopy \
          holoviews \
          geoviews \
          bokeh && \
    conda clean -tipsy
