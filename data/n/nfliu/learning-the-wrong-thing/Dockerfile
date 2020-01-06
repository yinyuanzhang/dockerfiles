# Copied in part from the codalab default Dockerfile and from the AllenNLP Dockerfile.
FROM nvidia/cuda:9.0-cudnn7-runtime
MAINTAINER Nelson F. Liu "nfliu@cs.stanford.edu"

############################################################
# Common steps (must be the same in the CPU and GPU images)
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y \
        wget \
        bzip2 \
        ca-certificates \
        curl \
        gcc \
        git \
        libc-dev \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        libevent-dev \
        tree \
        jq \
        build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

### Without this Python thinks we're ASCII and unicode chars fail
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

### Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Compile EVALB that comes with AllenNLP, since it's used in the parser
RUN python -c "from allennlp.training.metrics import EvalbBracketingScorer; EvalbBracketingScorer.compile_evalb()"

# Set up spacy
RUN python -m spacy download en
