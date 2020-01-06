FROM nvidia/cuda:9.2-cudnn7-devel-ubuntu18.04
#FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04


#RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python-pip python-tk wget curl git vim libsm6 libxext6 libxrender-dev && pip install --upgrade pip
#RUN pip install torch==1.2.0+cu92 torchvision==0.4.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
#RUN pip install numpy opencv-python matplotlib pillow

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3-dev python3-pip python3-tk wget curl git vim libsm6 libxext6 libxrender-dev screen nodejs npm
RUN ln -sf /usr/bin/python3 /usr/bin/python && python -V && which python
RUN ln -sf /usr/bin/pip3 /usr/bin/pip && pip -V && which pip
RUN pip3 install -U pip six numpy wheel setuptools mock future>=0.17.1 opencv-python matplotlib pillow jupyterlab
#RUN pip3 install tensorflow-gpu
#RUN pip3 install keras
RUN pip3 install torch==1.2.0+cu92 torchvision==0.4.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install https://github.com/inoryy/tensorflow-optimized-wheels/releases/download/v1.10.0/tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl keras==2.2.5
#RUN wget https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.13.1-cp36-cp36m-linux_x86_64.whl
#RUN python -m pip install tensorflow_gpu-1.13.1-cp36-cp36m-linux_x86_64.whl && pip3 install keras

RUN mkdir /jupyter
WORKDIR /jupyter
ADD entrypoint.sh /jupyter
RUN mkdir /jupyter/settings
ADD ./src /jupyter/settings

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
