FROM continuumio/miniconda3

# To fix the issue with locale language. 
ENV LANG C.UTF-8
ENV PYTHONIOENCODING=utf-8

# To fix issue with picture production.
ENV DISPLAY :0

LABEL maintainer="Belcour A."
LABEL Version="0.1.9"
LABEL Description="Pathmodel dockerfile with Clingo (Python3.6.5) and rdkit."


RUN apt-get update; \
    apt-get install -y gcc tmux libxrender1

RUN conda update -y -n base conda

RUN conda install -c rdkit rdkit;\
    conda install -c anaconda pygraphviz;\
    conda install -c potassco clingo;\
    echo 'export LANG="C.UTF-8"' >> ~/.bashrc

RUN pip install pathmodel==0.1.9
