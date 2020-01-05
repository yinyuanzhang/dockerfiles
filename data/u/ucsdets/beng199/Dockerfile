ARG BASE_CONTAINER=ucsdets/datascience-notebook:2019.4-stable
FROM $BASE_CONTAINER

USER root

# install imbalanced for beng199
RUN pip install -U imbalanced-learn

RUN conda install --quiet --yes pykalman

RUN conda clean -tipsy

RUN apt-get update && apt-get -qq install -y \
	zip unzip

RUN pip install cvxpy
