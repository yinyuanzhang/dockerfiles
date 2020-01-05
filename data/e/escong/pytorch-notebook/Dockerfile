# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/scipy-notebook

MAINTAINER escong <suhong.seo@gmail.com>

USER root

# Torch7 installation scripts - http://torch.ch/docs/getting-started.html
#RUN git clone https://github.com/torch/distro.git torch --recursive && \
#    cd torch && \
#    bash install-deps && \
#    ./install.sh && \
#    cp install/bin/* /usr/local/bin && \
#    cd .. && \
#    rm -rf torch

USER $NB_USER
# Install Python 3.6 pytorch without cuda
RUN conda install --quiet --yes  pytorch-cpu torchvision-cpu -c pytorch

# Install Python 2 pytorch 
# python 2 environment  deprecated in scipy-notebook container
#RUN conda install --quiet --yes -n python2 conda install pytorch-cpu torchvision-cpu -c pytorch

