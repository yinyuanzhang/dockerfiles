# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/pyspark-notebook

LABEL maintainer="Ernesto Espinosa <eespinosa@ucsb.edu>"

USER $NB_UID

RUN conda install --quiet -y 'nltk' && \
    conda install --quiet -y 'pyarrow' && \
    conda install --quiet -y 'tensorflow=1.7.0' && \
    conda install --quiet -y 'tensorboard' && \
    conda install --quiet -y 'requests' && \
    conda install --quiet -y 'h5py' && \
    conda install --quiet -y 'keras=2.1.5' && \
    conda install --quiet -y 'six' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
