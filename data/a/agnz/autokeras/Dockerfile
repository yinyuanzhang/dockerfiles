FROM nvidia/cuda:10.0-runtime-ubuntu18.04

RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3 python3-dev python3-pip python3-setuptools libgomp1 git graphviz && \
    apt-get purge --autoremove -y curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir tf-nightly-gpu
RUN pip3 install --no-cache-dir https://download.pytorch.org/whl/cu100/torch-1.0.0-cp36-cp36m-linux_x86_64.whl
RUN git clone https://github.com/jhfjhfj1/autokeras.git
RUN cd autokeras && \
    sed '/tensorflow/ d' -i setup.py && \
    python3 setup.py install && \
    cd .. && \
    rm -rf autokeras
RUN pip3 install --no-cache-dir jupyter graphviz
