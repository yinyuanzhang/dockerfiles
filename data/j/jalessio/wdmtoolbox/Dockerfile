FROM continuumio/anaconda

WORKDIR WDM

RUN apt-get update && apt-get install -y \
      gfortran \
      less \
      unzip \
      wget

RUN pip install wdmtoolbox

COPY README.md README.md
