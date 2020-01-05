FROM patdiscvrd/ubuntu-cuda

MAINTAINER Patrick Wenzel

# Docker container for theano/pylearn2 with GPU support

# Get latest ubuntu packages
RUN apt-get update -y

# Get dependencies
RUN apt-get install -y build-essential gfortran g++ libopenblas-dev git curl nano

# Install Python
RUN apt-get install -y python python-numpy python-scipy python-dev python-pip python-nose python-yaml python-imaging python-matplotlib

# Install IPython notebook
RUN pip install "ipython[notebook]"

# Install Theano
RUN cd /opt && git clone git://github.com/Theano/Theano.git
RUN cd /opt/Theano && python setup.py develop

# Install pylearn2
RUN cd /opt && git clone git://github.com/lisa-lab/pylearn2.git
RUN cd /opt/pylearn2 && python setup.py develop

# Set pylearn2 data path
RUN bash -c 'echo "export PYLEARN2_DATA_PATH=/opt/data" >> ~/.bashrc'

# Set scripts path
RUN bash -c 'echo "export PATH=/opt/pylearn2/pylearn2/scripts:$PATH" >> ~/.bashrc'

# Enable GPU in Theano
RUN cd ~ && echo "[global]\ndevice=gpu0\nfloatX=float32\n\n[cuda]\nroot=/usr/local/cuda" > .theanorc
