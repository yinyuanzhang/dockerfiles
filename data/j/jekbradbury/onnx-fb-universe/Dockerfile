FROM jekbradbury/ofu-deps

RUN mkdir -p /programs && \
    git clone --recursive https://github.com/onnxbot/onnx-fb-universe.git /programs

RUN cd /programs && ./install-develop.sh

WORKDIR /programs
