# Tag: nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04
# FROM mcr.microsoft.com/azureml/base-gpu:latest
FROM mcr.microsoft.com/azureml/base-gpu:intelmpi2018.3-cuda9.0-cudnn7-ubuntu16.04
ENV STAGE_DIR=/root/gpu/install 
RUN mkdir -p $STAGE_DIR


# Install basic dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        --allow-change-held-packages \
        build-essential \
        cmake \
        wget \
        vim \
        tmux \
        htop \
        git \
        unzip \
        libnccl2 \
        libnccl-dev \
        ca-certificates \
        libjpeg-dev

# Install lib for video
# RUN apt-get update && apt-get install -y software-properties-common
# RUN add-apt-repository -y ppa:jonathonf/ffmpeg-3
# RUN apt update && apt-get install -y libavformat-dev libavcodec-dev libswscale-dev libavutil-dev libswresample-dev
# RUN apt-get install -y ffmpeg
RUN export LIBRARY_PATH=/usr/local/lib:$LIBRARY_PATH

# Set timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# Get Conda-ified Python.
#RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
#    wget --quiet https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh -O ~/anaconda.sh && \
#    sh ~/anaconda.sh -b -p /opt/conda && \
#    rm ~/anaconda.sh

ENV PATH /opt/miniconda/bin:$PATH
# Install general libraries
RUN conda update -n base -c defaults conda
RUN conda install -y python=3.6 numpy pyyaml scipy ipython mkl scikit-learn pandas setuptools Cython cython h5py graphviz nltk spacy jpeg
RUN conda clean -ya
RUN conda install -y mkl-include cmake typing cython
RUN conda install -y -c mingfeima mkldnn
RUN pip install boto3 addict regex pyyaml opencv-python
RUN pip install scikit-image lmdb gensim pyemd


# Set CUDA_ROOT
RUN export CUDA_HOME="/usr/local/cuda"

# Install pytorch
RUN conda install pytorch cudatoolkit=9.0 -c pytorch
RUN pip install git+git://github.com/pytorch/vision.git@24577864e92b72f7066e1ed16e978e873e19d13d


# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME


# Install allennlp 0.8.0
# RUN pip install -r allennlp-requirements.txt
# https://github.com/rowanz/r2c/blob/master/allennlp-requirements.txt
RUN pip install overrides boto3 unidecode ftfy editdistance pytest flaky jupyter 
RUN pip install pytest-cov coverage codecov aiohttp sphinx-autobuild sphinx_rtd_theme pypandoc
RUN pip install "jsonnet==0.10.0" "msgpack>=0.5.6,<0.6.0" "spacy>=2.0,<2.1" "numpydoc==0.8.0" "tensorboardX==1.2" "cffi==1.11.5" "awscli>=1.11.91"
RUN pip install "flask==1.0.2" "flask-cors==3.0.7" "gevent==1.3.6" "parsimonious==0.8.0" "sqlparse==0.2.4" "pytorch-pretrained-bert==0.3.0"
RUN pip install "matplotlib==2.2.3" "requests>=2.18" "tqdm>=4.19" "pytz==2017.3" "conllu==0.11" "responses>=0.7" "moto==1.3.4" "pylint==1.8.1"
RUN pip install "ipykernel<5.0.0" "mypy==0.521" "sphinx==1.5.3" "twine==1.11.0"

RUN pip install --no-deps allennlp==0.8.0
RUN python -m spacy download en_core_web_sm
