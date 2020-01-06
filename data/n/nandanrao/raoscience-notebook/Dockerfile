FROM jupyter/datascience-notebook

USER $NB_USER

# Python 3
RUN conda install --quiet --yes \
    'xgboost' \
    'boto3'

RUN pip install fancyimpute

RUN /bin/bash -c "source activate python2" && pip install fancyimpute

# Python 2
RUN conda install --name python2 --quiet --yes \
    'xgboost' \
    'boto3'
