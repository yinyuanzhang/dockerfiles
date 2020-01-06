FROM datmo/keras-tensorflow:gpu-py35-notebook
LABEL maintainer="Samuel Bernardo <samuelbernardo.mail@gmail.com>"

WORKDIR /root/
# Install addittional features
RUN apt-get update && \
    apt-get --assume-yes install \
      wget \
      pkg-config \
      python \
      python-dev \
      python-pip \
      python-numpy \
      python-scipy \
      python-matplotlib \
      python-h5py \
      python-astropy \
      glue-sprite \
      python-six \
      libblas-dev \
      liblapack-dev \
      libssl-dev \
      gfortran && \
    pip --no-cache-dir install glue && \
    pip --no-cache-dir install -U scikit-learn && \
    pip install --user gwpy && \
    mkdir -p /notebooks

CMD ["/run_jupyter.sh", "--allow-root", "--notebook-dir=/notebooks"]
