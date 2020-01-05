# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Roberto Di Remigio <roberto.diremigio@gmail.com>"

USER root

# ffmpeg for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN conda install --quiet --yes \
    'conda-forge::blas=*=mkl' \
    'ipywidgets=7.2*' \
    'pandas=0.23*' \
    'numexpr=2.6*' \
    'matplotlib=2.2*' \
    'scipy=1.1*' \
    'seaborn=0.9*' \
    'sympy=1.1*' \
    'cloudpickle=0.5*' \
    'dill=0.2*' \
    'bokeh=0.13*' \
    'hdf5=1.10*' \
    'h5py=2.7*' \
    'vincent=0.4.*' \
    'beautifulsoup4=4.6.*' \
    'xlrd' \
    'psi4=*=py36*' \
    'psi4-rt=*=py36*' \
    -c psi4 && \
    # Test that Psi4 works
    psi4 --test && \
    conda remove --quiet --yes --force qt pyqt && \
    conda clean -tipsy && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    # Also activate ipywidgets extension for JupyterLab
    # Check this URL for most recent compatibilities
    # https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@^0.38.1 && \
    jupyter labextension install jupyterlab_bokeh@0.6.3 && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER && \
    mkdir -p /home/$NB_USER/scratch

# Configure Emacs
COPY .spacemacs /home/$NB_USER
RUN git clone --single-branch -b develop https://github.com/syl20bnr/spacemacs /home/$NB_USER/.emacs.d \
      && emacs --batch -l /home/$NB_USER/.emacs.d/init.el --eval="(configuration-layer/update-packages t)"

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER
ENV PSI_SCRATCH /home/$NB_USER/scratch

USER $NB_UID
