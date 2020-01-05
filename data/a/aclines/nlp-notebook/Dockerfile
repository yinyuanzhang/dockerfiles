FROM jupyter/minimal-notebook

LABEL maintainer="Alexander Clines <me@alexanderclines.com"

# Install Python 3 packages
RUN conda install --quiet --yes \
    'nltk=3.3*' && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
