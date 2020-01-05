FROM jupyter/scipy-notebook

LABEL maintainer="Lee Nookx <leenookx@purplemonkeys.co.uk>"

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=jovyan \
    NB_UID=1000 \
    NB_GID=100 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER

USER $NB_USER

# Install Python 3 packages
RUN conda install --quiet --yes -c conda-forge \
    'lxml' \
    'psycopg2' \
    'nltk' \
    'spacy'

RUN pip install textacy

RUN conda install --quiet --yes -c conda-forge \
    'wordcloud' \
    'nltk_data' \
    'python-louvain' \
    'keras' \
    'tensorflow' \
    'plotly' \
    'cufflinks-py' \
    'jsonlines' \
    'python-Levenshtein' \
    'genson' \
    'geopandas' \
    'plotly_express' \
    'folium' \
    'pandas-profiling' \
    'papermill'

# Needed to install wordcloud this way due to some kind of issue with using
# Python 3.6. See:
# https://github.com/amueller/word_cloud/issues/246
RUN conda install --quiet --yes -c https://conda.anaconda.org/amueller wordcloud

# For now we are only choosing to support English.
RUN python -m spacy download en

RUN conda clean -tipsy && \
    fix-permissions $CONDA_DIR

RUN mkdir /home/$NB_USER/data && \
    fix-permissions /home/$NB_USER

USER $NB_USER
