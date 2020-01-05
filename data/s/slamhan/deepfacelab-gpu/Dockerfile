FROM tensorflow/tensorflow:1.12.0-gpu-py3

RUN apt-get update -qq -y \
 && apt-get install -y libsm6 libxrender1 libxext-dev

# Install Python3.6
RUN add-apt-repository ppa:deadsnakes/ppa -y \
 && apt-get update \
 && apt -y install python3-pip python3.6 python3.6-dev

# Install DeepFaceLab Dependencies
RUN apt -y install ffmpeg cmake build-essential git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install DeepFaceLab Python Dependencies
COPY requirements-cuda.txt /opt/
RUN python3 -m  pip install --upgrade pip
RUN python3.6 -m pip install -r /opt/requirements-cuda.txt && rm /opt/requirements-cuda.txt

RUN python3.6 -m pip install dlib
RUN python3.6 -m pip install jupyter matplotlib
RUN python3.6 -m pip install jupyter_http_over_ws
RUN jupyter serverextension enable --py jupyter_http_over_ws
# patch for tensorflow:latest-gpu-py3 image
RUN cd /usr/local/cuda/lib64 \
 && mv stubs/libcuda.so ./ \
 && ln -s libcuda.so libcuda.so.1 \
 && ldconfig

WORKDIR "/notebooks"
CMD ["jupyter-notebook", "--allow-root" ,"--port=8888" ,"--no-browser" ,"--ip=0.0.0.0"]
