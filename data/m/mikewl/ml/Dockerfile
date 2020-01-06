FROM mikewl/ml:base

MAINTAINER Michael Wallace Louwrens <michael@louwrens.me>

# Clone MXNet repo 
RUN cd /root && git clone --recursive https://github.com/dmlc/mxnet

#move into the repo, setup config.mk and make
RUN cd /root/mxnet && \
# Copy config.mk and enable CUDA. NVRTC and MKL cause compilation to fail
  cp make/config.mk config.mk && \
# Set OpenBLAS
  sed -i 's/USE_BLAS = atlas/USE_BLAS = openblas/g' config.mk && \
# Set CUDA flag
  sed -i 's/USE_CUDA = 0/USE_CUDA = 1/g' config.mk && \
  sed -i 's/USE_CUDA_PATH = NONE/USE_CUDA_PATH = \/usr\/local\/cuda/g' config.mk && \
# Set cuDNN flag
  sed -i 's/USE_CUDNN = 0/USE_CUDNN = 1/g' config.mk && \
# Set MKL 2017 flags
  #sed -i 's/USE_MKL2017 = 0/USE_MKL2017 = 1/g' config.mk && \
  #sed -i 's/USE_MKL2017_EXPERIMENTAL = 0/USE_MKL2017_EXPERIMENTAL = 1/g' config.mk && \
# Set NVRTC
  #sed -i 's/USE_NVRTC = 0/USE_NVRTC = 1/g' config.mk && \
# Make 
  make -j"$(nproc)"

#add MXNet home variable
RUN echo 'export MXNET_HOME=/root/mxnet/' >> ~/.bashrc 
#install Python package
RUN cd /root/mxnet/python && python3 setup.py install

#install Julia package
RUN export MXNET_HOME=/root/mxnet/ && julia -e 'Pkg.add("MXNet")'
