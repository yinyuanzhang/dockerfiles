FROM frolvlad/alpine-miniconda3:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# alpine

RUN apk update
RUN apk --no-cache add bash build-base npm nodejs libgcc git tar bzip2 ca-certificates
RUN update-ca-certificates
RUN apk upgrade

#conda

RUN conda update conda && conda config --append channels conda-forge
RUN conda install -y numpy pandas geopandas gdal rasterio ipython jupyterlab ipywidgets beakerx tk qgrid
RUN conda update --all && conda clean --all -f -y


