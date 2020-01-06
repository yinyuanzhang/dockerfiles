FROM nvidia/cuda:10.0-devel-ubuntu16.04

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get -y install \
        git make cmake build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
        libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils \
        libffi-dev liblzma-dev

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

ENV HOME  /
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get -y install libblas-dev libturbojpeg liblapack-dev \
    libpq-dev libreadline-dev libsqlite3-dev \ 
    libssl-dev libxml2-dev libxslt1-dev ffmpeg

RUN pyenv install 3.6.6
RUN pyenv global 3.6.6

RUN pip install -U pip
RUN pip install Cython
RUN pip install numpy scipy pandas torch torchvision opencv-python-headless scikit-image scikit-video
RUN pip install flake8 coverage pytest pytest-cov

# install dlib 
RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.15' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS
