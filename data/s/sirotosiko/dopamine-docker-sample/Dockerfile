FROM ubuntu
SHELL ["/bin/bash", "-c"]
RUN apt-get update && apt-get install -y \
    python \
    python-pip \
    git \
    libgtk2.0-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y \
    cmake \
    zlib1g-dev \
    g++ \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN pip install \
    absl-py \
    atari-py \
    gin-config \
    gym \
    opencv-python \
    tensorflow
RUN git clone https://github.com/google/dopamine.git
WORKDIR dopamine
ENV PYTHONPATH /usr/bin/python:.
CMD ["python","tests/atari_init_test.py"]
