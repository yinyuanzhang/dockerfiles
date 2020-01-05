FROM tensorflow/tensorflow:1.3.0-gpu-py3

RUN apt-get update && apt-get install -y \
        libsm6 \
        libxrender1 \
        libfontconfig1 \
        libxtst6 \
        p7zip-full \
        && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt

#RUN pip install cxflow-tensorflow==0.2.1 --no-deps
RUN pip install -r /requirements.txt

RUN \
    touch /usr/local/lib/python3.5/dist-packages/testpath-0.3.1.dist-info/top_level.txt \
    touch /usr/local/lib/python3.5/dist-packages/ptyprocess-0.5.2.dist-info/top_level.txt \
    touch /usr/local/lib/python3.5/dist-packages/entrypoints-0.2.3.dist-info/top_level.txt
