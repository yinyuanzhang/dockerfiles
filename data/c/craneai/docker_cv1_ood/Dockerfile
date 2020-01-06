FROM tensorflow/tensorflow:1.6.0-py3

# The code below is all based off the repos made by https://github.com/janza/
# He makes great dockerfiles for opencv, I just used a different base as I need
# tensorflow on a gpu.

RUN apt-get update

# Core linux dependencies. 
RUN apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libjasper-dev \
        libavformat-dev \
        libhdf5-dev \
        libpq-dev \
		libsm6 \
		libxext6 \
		libxrender-dev

# Python dependencies
RUN pip3 --no-cache-dir install \
    numpy \
    hdf5storage \
    h5py \
    scipy \
    py3nvml


RUN pip3 install --upgrade tensorflow

RUN pip3 install imutils flask requests opencv-python

#RUN pip3 install imutils requests

RUN mkdir root && \
	cd root && mkdir models 


RUN apt-get update && \
		apt-get install protobuf-compiler python-pil python-lxml -y

	RUN git clone https://github.com/tensorflow/models.git /root/models


RUN cd /root/models/research/object_detection && ls
	RUN curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip
	RUN unzip protoc-3.2.0-linux-x86_64.zip -d protoc3 && \
		mv protoc3/bin/* /usr/local/bin/ && \
		mv protoc3/include/* /usr/local/include/ && \
		export PATH=$PATH:~/protobuf/bin


RUN cd /root/models/research && protoc object_detection/protos/*.proto --python_out=.

RUN ls

COPY object_detection /root/models/research/object_detection

RUN head /root/models/research/object_detection/rest_api/api.py

COPY object_detection/data /root/models/research/object_detection/rest_api/data

COPY object_detection/ui_output_inference_graph_week5/frozen_inference_graph.pb /root/models/research/object_detection/rest_api
COPY object_detection/data/ui_label_map_new.pbtxt /root/models/research/object_detection/rest_api


COPY object_detection/ui_output_inference_graph_week5/frozen_inference_graph.pb /root/models/research/object_detection/ui_output_inference_graph_week5
COPY object_detection/icon_output_inference_graph_week5/frozen_inference_graph.pb /root/models/research/object_detection/icon_output_inference_graph_week5



  WORKDIR "/root/models/research/object_detection/rest_api"


	EXPOSE 8080


	ENTRYPOINT [ "python3" ]

	CMD [ "-u","api.py" ]