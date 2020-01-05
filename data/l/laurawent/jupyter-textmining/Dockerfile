ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Marc <marc@went.io>"

# Install Packages
RUN conda install --quiet --yes \
    'numpy=1.16*' \
    'nltk=3.4*' \
    'spacy=2.0*' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
