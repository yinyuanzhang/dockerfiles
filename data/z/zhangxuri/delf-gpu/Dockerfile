FROM tensorflow/tensorflow:1.13.1-gpu-py3
RUN apt-get update && apt-get install -y \
    wget \
    zip \
    git
RUN mkdir /home/delf \
    && cd /home/delf \
    && mkdir proto \
    && cd proto \
    && wget https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip \
    && unzip protoc-3.3.0-linux-x86_64.zip 
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib \
    numpy \
    scikit-image \
    scipy
RUN cd /home/delf && git clone https://github.com/tensorflow/models
RUN cd /home/delf/proto \
    && PATH_TO_PROTOC=`pwd` \
    && cd .. \
    && cd models/research/slim/ \
    && pip install -e . \
    && cd .. \
    && export PYTHONPATH=$PYTHONPATH:`pwd` \
    && cd delf/ \
    && ${PATH_TO_PROTOC?}/bin/protoc delf/protos/*.proto --python_out=. \
    && pip install -e . 
ENV PYTHONPATH  /home/delf/models/research
RUN cd /home/delf/models/research/delf/delf/python/examples \
    && mkdir parameters && cd parameters \
    && wget http://download.tensorflow.org/models/delf_v1_20171026.tar.gz \
    && tar -xvzf delf_v1_20171026.tar.gz
