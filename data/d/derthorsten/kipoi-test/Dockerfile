FROM nvidia/cuda:9.0-base-ubuntu16.04
# based on https://github.com/Paperspace/fastai-docker/tree/master/fastai-v3
ENV LANG C.UTF-8
LABEL com.nvidia.volumes.needed="nvidia_driver"

RUN apt-get update && apt-get install -y --no-install-recommends \
         git \
         curl \
         bzip2 \
         zlib1g-dev
    #&&\
    #rm -rf /var/lib/apt/lists/*

ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64
ENV PYTHON_VERSION=3.6

RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
    /opt/conda/bin/conda install conda-build

ENV PATH=$PATH:/opt/conda/bin/

# Create Enviroment
COPY enviroment.yaml /enviroment.yaml
RUN conda env create -f enviroment.yaml
RUN echo "source activate kipoi-dev" > ~/.bash
ENV PATH /opt/conda/envs/kipoi-dev/bin:$PATH

# for strange reasons mmsplice installation process tries 
# to build c
RUN pip install mmsplice --no-deps 

# hotfixes
RUN git clone https://github.com/DerThorsten/kipoi -b    docker kipoi
RUN cd kipoi && pip install --force-reinstall --no-deps -e . && cd 