FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

RUN apt-get update && apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev protobuf-compiler libhdf5-10 libhdf5-serial-dev libhdf5-dev libhdf5-cpp-11 
RUN apt-get install -y --no-install-recommends libboost-all-dev
RUN apt-get install -y libatlas-base-dev libopenblas-dev python-dev libgflags-dev libgoogle-glog-dev liblmdb-dev git python-numpy wget curl libssl-dev python-pip awscli 

RUN pip install --upgrade pip
RUN python -V && which python && pip -V
RUN apt-get install -y python-tk
RUN pip install --no-cache-dir werkzeug flask tornado numpy pandas pillow pyyaml opencv-python scikit-image matplotlib

#RUN wget https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz && tar xfz Python-2.7.15.tgz 
#RUN cd Python-2.7.15/ && ./configure --prefix /usr/local/lib/python2.7.15 --enable-ipv6 --enable-optimizations && sudo make && sudo make install
#RUN cd Python-2.7.15/ && sudo ./configure --enable-optimizations --prefix /usr/local/lib/python2.7.15 && sudo make && sudo make install
#RUN ln -sf /usr/bin/python2.7 /usr/bin/python && python -V && python2.7 -V && which python
#RUN ln -sf /usr/local/lib/python2.7.15/bin/python /usr/bin/python && python -V && which python

#RUN sudo apt-get install -y python-pip
#RUN sudo pip install --upgrade pip
#RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py
#RUN pip
#RUN sudo apt-get install --reinstall python-pkg-resources
#RUN sudo pip install --no-warn-script-location --upgrade pip
#RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && pip

RUN mkdir /workspace
RUN mkdir /workspace/tt100k
ADD ./src /workspace/
WORKDIR /workspace/tt100k

RUN git clone https://jooblue:tkdthr0803@bitbucket.org/jooblue/tt100k.git
RUN cd /workspace/cuda && cp lib64/* /usr/local/cuda/lib64 && cp include/cudnn.h /usr/local/cuda/include
#RUN git clone https://jooblue:tkdthr0803@bitbucket.org/jooblue/tt100k.git 
RUN cd tt100k/caffe && export PYTHONPATH=/workspace/tt100k/tt100k/model/python_layers:$PYTHONPATH && make clean && make -j8 && make pycaffe

