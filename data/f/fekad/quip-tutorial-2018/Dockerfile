FROM jupyter/minimal-notebook

LABEL maintainer="Adam Fekete <adam.fekete@kcl.ac.uk>"

USER root

RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
        gfortran \
        openmpi-bin \
        libopenmpi-dev \
        liblapack-dev \
        libblas-dev \
        libnetcdf-dev \
        netcdf-bin \
        libxpm-dev \
        libgsl-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN conda install --quiet --yes \
    'conda-forge::blas=*=openblas' \
    'ipywidgets=7.2*' \
    'matplotlib=2.2*' \
    'scipy=1.1*' \
    'scikit-learn=0.19*' \
    'cython=0.28*' \
    'numba=0.38*' \
    'bokeh=0.13*' \
    'hdf5=1.10*' \
    'h5py=2.7*' \
    ase \
    asap3 \
    scikit-learn \
    nglview \
 && conda remove --quiet --yes --force qt pyqt \
 && conda clean -tipsy \
 # Activate ipywidgets extension in the environment that runs the notebook server
 && jupyter nbextension enable --py widgetsnbextension --sys-prefix \
 && npm cache clean --force \
 && rm -rf $CONDA_DIR/share/jupyter/lab/staging \
 && rm -rf /home/$NB_USER/.cache/yarn \
 && rm -rf /home/$NB_USER/.node-gyp \
 && fix-permissions $CONDA_DIR \
 && fix-permissions /home/$NB_USER


# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME=/home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" \
 && fix-permissions /home/$NB_USER


# ================================================================================
# Python 2.x environment
# ================================================================================


# Create a Python 2.x environment using conda including at least the ipython kernel
# and the kernda utility. Add any additional packages you want available for use
# in a Python 2 notebook to the first line here (e.g., pandas, matplotlib, etc.)
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \
    ipython \
    ipykernel \
    kernda \
    numpy \
    scipy \
    scikit-learn \
    matplotlib \
    ase \
    nglview \
 && conda remove -n python2 --quiet --yes --force qt pyqt \
 && conda clean -tipsy \
 && npm cache clean --force \
 && rm -rf $CONDA_DIR/share/jupyter/lab/staging \
 && rm -rf /home/$NB_USER/.cache/yarn \
 && rm -rf /home/$NB_USER/.node-gyp \
 && fix-permissions $CONDA_DIR \
 && fix-permissions /home/$NB_USER


USER root
# Create a global kernelspec in the image and modify it so that it properly activates
# the python2 conda environment.
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install \
 && $CONDA_DIR/envs/python2/bin/kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json

USER $NB_USER


# ================================================================================
#  QUIP + GAP + quippy
# ================================================================================

# All the QUIPs go here; added to path in the end.
ENV QUIP_ROOT=/opt/quip \
    QUIP_ARCH=linux_x86_64_gfortran_openmp

ADD QUIP $QUIP_ROOT
ADD Makefile.inc $QUIP_ROOT/build/$QUIP_ARCH/Makefile.inc

USER root
RUN chown -R $NB_USER:$NB_GID $QUIP_ROOT
USER $NB_USER

## QUIP for general use is the OpenMP version.
## Installs with no suffix, e.g. quip
## Installs quippy using pytho2 environment

RUN cd $QUIP_ROOT  \
 && make > /dev/null 2>&1 \
 && QUIP_INSTALLDIR=$QUIP_ROOT/bin make install \
 && /bin/bash -c "source activate python2; make install-quippy > /dev/null 2>&1" \
 && fix-permissions $QUIP_ROOT

ENV PATH=$QUIP_ROOT/bin:$PATH


# ================================================================================

ENV SKETCHMAP_ROOT=/opt/sketchmap

ADD sketchmap $SKETCHMAP_ROOT

USER root
RUN chown -R $NB_USER:$NB_GID $SKETCHMAP_ROOT
USER $NB_USER

RUN cd $SKETCHMAP_ROOT  \
 && make \
 && fix-permissions $SKETCHMAP_ROOT

ENV PATH=$SKETCHMAP_ROOT/bin:$SKETCHMAP_ROOT/utils:$PATH


# ================================================================================

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID