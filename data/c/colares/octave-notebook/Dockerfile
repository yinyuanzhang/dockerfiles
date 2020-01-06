# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/base-notebook
FROM $BASE_CONTAINER


LABEL maintainer="Thiago Colares <thicolares@gmail.com>"


USER root


# Install GNU Octave and GNU Plot (a portable command-line driven graphing utility)
RUN apt-get update && \
    apt-get install -y gnuplot octave && \
    apt-get clean


USER $NB_UID


# Install octave_kernell as jovyan.
# Set the OCTAVE_EXECUTABLE environment variable
# so the octave_kernel knows which Octave program to run.
RUN pip install octave_kernel && \
    export OCTAVE_EXECUTABLE=$(which octave)
