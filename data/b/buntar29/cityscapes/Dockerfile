#COPY /folderlocation/sysctl.conf /etc/sysctl.conf
FROM tensorflow/tensorflow:latest-devel-gpu-py3
RUN pip install -q PyYAML
RUN pip install scikit-image
RUN pip install tensorflow==1.10.0
RUN pip install keras==2.2.4
RUN pip install h5py==2.8.0
RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN pip install opencv-python
RUN pip install -I torch==1.0.0
RUN pip install torchvision==0.2.1
