# To use GPU instead of CPU add: --build-arg GPU_SUFFIX=-gpu
ARG GPU_SUFFIX=
FROM tensorflow/tensorflow:1.14.0${GPU_SUFFIX}-py3 AS nun

WORKDIR /root

# tensorflow/models installation
RUN apt-get update && \
    apt-get install -y git protobuf-compiler
RUN git clone --depth 1 -b v1.13.0 https://github.com/tensorflow/models.git tensorflow/models
ENV PYTHONPATH "${PYTHONPATH}:/root/tensorflow/models/research/:/root/tensorflow/models/research/slim/"
RUN cd tensorflow/models/research/ && \
    protoc object_detection/protos/*.proto --python_out=.

# Essential tools
RUN apt-get update && \
    apt-get install -y vim tmux htop wget

COPY requirements.txt ./nun/
RUN pip install -r ./nun/requirements.txt

COPY . ./nun/
RUN pip install --no-cache-dir -e ./nun


CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter lab --notebook-dir=/root --ip 0.0.0.0 --no-browser --allow-root --LabApp.token=''"]
