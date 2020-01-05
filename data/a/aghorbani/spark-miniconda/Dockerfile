FROM aghorbani/spark:2.1.0
MAINTAINER Asghar Ghorbani [https://de.linkedin.com/in/aghorbani]


# The installation of the miniconda is followed from:
# https://hub.docker.com/r/gurvin/spark-worker-base/
# https://github.com/UNINETT/kubernetes-apps
# The vesions might not match.

# Configure environment
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

# Install conda
RUN cd /tmp && \
    mkdir -p $CONDA_DIR && \
    curl -s https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh -o miniconda.sh && \
    /bin/bash miniconda.sh -f -b -p $CONDA_DIR && \
    rm miniconda.sh && \
    $CONDA_DIR/bin/conda install --quiet --yes conda==4.2.12 && \
    $CONDA_DIR/bin/conda install --quiet --yes 'conda-build=2.0*' && \
    $CONDA_DIR/bin/conda config --system --add channels conda-forge && \
    $CONDA_DIR/bin/conda config --system --set auto_update_conda false && \
    conda clean -tipsy

# Install Python 3 packages
RUN conda install --yes \
    'notebook=4.2*' 'ipywidgets=5.2*' 'pandas=0.18*'       'numexpr=2.6*'       'matplotlib=1.5*' \
    'scipy=0.18*'   'seaborn=0.7*'    'scikit-learn=0.17*' 'scikit-image=0.12*' 'sympy=1.0*'      \
    'cython=0.24*'  'patsy=0.4*'      'statsmodels=0.6*'   'cloudpickle=0.2*'   'dill=0.2*'       \
    'numba=0.28*'   'bokeh=0.12*'     'sqlalchemy=1.0*'    'hdf5=1.8.17'        'h5py=2.6*'       \
    'jsonschema'    'pillow'          'pip'                'jpeg=8d'            'pyzmq'           \
     terminado     && \
    conda clean -tipsy

# Install Python 2 packages
RUN conda create --yes -p $CONDA_DIR/envs/python2 python=2.7 \
    'notebook=4.2*' 'ipywidgets=5.2*' 'pandas=0.18*'       'numexpr=2.6*'       'matplotlib=1.5*' \
    'scipy=0.18*'   'seaborn=0.7*'    'scikit-learn=0.17*' 'scikit-image=0.12*' 'sympy=1.0*'      \
    'cython=0.24*'  'patsy=0.4*'      'statsmodels=0.6*'   'cloudpickle=0.2*'   'dill=0.2*'       \
    'numba=0.28*'   'bokeh=0.12*'     'sqlalchemy=1.0*'    'hdf5=1.8.17'        'h5py=2.6*'       \
    'jsonschema'    'pillow'          'pip'                'jpeg=8d'            'pyzmq'           \
    terminado     && \
    conda clean -tipsy

# Install Python 2 kernel spec into the Python 3 conda environment which
# runs the notebook server
# Also add any pip package needs to be installed in Python 2
RUN bash -c '. activate python2 && \
    python -m ipykernel.kernelspec --prefix=$CONDA_DIR && \
    pip install thunder-python && \
    conda clean -tipsy && \
    . deactivate'

# R packages
RUN conda config --add channels r
RUN conda install --yes \
    'r-base=3.3.1 1'      'r-irkernel=0.6*'     'r-plyr=1.8*'    'r-devtools=1.11*' \
    'r-dplyr=0.4*'        'r-ggplot2=2.1*'      'r-tidyr=0.5*'   'r-shiny=0.13*'    \
    'r-rmarkdown=0.9*'    'r-forecast=7.1*'     'r-stringr=1.0*' 'r-rsqlite=1.0*'   \
    'r-reshape2=1.4*'     'r-nycflights13=0.2*' 'r-caret=6.0*'   'r-rcurl=1.95*'    \
    'r-randomforest=4.6*' 'r-crayon=1.3*' && \
    conda clean -tipsy

#Environment vaiables for Spark to use Anaconda Python and iPython notebook
ENV PYSPARK_PYTHON $CONDA_DIR/bin/python3
#ENV PYSPARK_DRIVER_PYTHON $CONDA_DIR/bin/ipython3
ENV PYSPARK_DRIVER_PYTHON $CONDA_DIR/bin/jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS "notebook --no-browser --port=8888 --ip='*'"

#iPython port
EXPOSE 8888

