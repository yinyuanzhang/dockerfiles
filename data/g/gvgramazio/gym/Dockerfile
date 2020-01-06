FROM giangiangian/eclipse_che_gpu_dockerfile_base:9.0-cudnn7-devel-ubuntu16.04

RUN sudo apt-get update

RUN sudo apt-get install -y python3 python3-pip

RUN python3 -m pip install \
  h5py \
  jupyter \
  keras \
  matplotlib \
  numpy \
  pandas \
  scipy \
  sklearn \
  tensorflow==1.10.1

RUN sudo apt-get install -y \
  python3-dev \
  zlib1g-dev \
  libjpeg-dev \
  cmake \
  swig \
  python-pyglet \
  python3-opengl \
  libboost-all-dev \
  libsdl2-dev \
  libosmesa6-dev \
  patchelf \
  ffmpeg \
  xvfb

# MuJoCo has a proprietary dependency we can't set up for you. Follow the
# instructions in the `mujoco-py` package for help.
# RUN python3 -m pip install 'gym[all]'
RUN python3 -m pip install gym

# Expose port for TensorBoard
EXPOSE 6006

# Expose port for jupyter notebook
EXPOSE 8888

# You can launch jupyter with `jupyter notebook --allow-root --ip=0.0.0.0`.
# Remember that if you want to be able to reach it the host browser, you need
# to run the container with `-p 8888:8888` option, e.g `docker run -it -p
# 8888:8888 gym`.
