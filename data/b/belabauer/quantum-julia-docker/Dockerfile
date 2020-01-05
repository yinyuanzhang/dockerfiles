# Use an official Python runtime as a parent image
FROM julia:0.6.4-stretch

COPY getaztools.sh /install/
COPY microsoft.key /install/
RUN /install/getaztools.sh

COPY packages.jl /install/
COPY preload.jl /install/

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    gfortran \
    hdf5-tools \
    make \
    git \
    cmake \
    libopenmpi-dev

RUN julia /install/packages.jl && julia /install/preload.jl && chmod -R 777 /root

WORKDIR APP

