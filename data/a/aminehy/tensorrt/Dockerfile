FROM nvcr.io/nvidia/tensorrt:19.05-py2

LABEL maintainer "Amine Hadj-Youcef  <hadjyoucef.amine@gmail.com> "

# install python samples for tensorrt
# RUN /opt/tensorrt/python/python_setup.sh


# install prerequisites
RUN apt-get update && apt-get install -y --no-install-recommends \
    protobuf-compiler \
    geany \
    libprotoc-dev \
    python-tk \
    eog \
    gedit
    
        
# install necessary python packages
RUN pip install numpy==1.16.4 \
	onnx==1.1.1 \
	pycuda==2018.1.1 \
	Pillow==6.0.0 \
	wget==3.2 \
	matplotlib==2.2.4

# set the working directory
WORKDIR /workspace

