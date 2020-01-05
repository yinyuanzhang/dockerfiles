FROM ubuntu:16.04

LABEL maintainer Mario Werner <mario.werner@iaik.tugraz.at>

# Install commonly used packages for python3 development.
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip && \
  pip3 install pycodestyle \
    pytest pytest-console-scripts pytest-cov pytest-mock pytest-runner pytest-xdist \
    sphinx sphinx-autodoc-typehints \
    twine \
    typeguard 
