FROM tensorflow/tensorflow:latest-gpu-py3
LABEL maintainer="noshita"

# Packages
RUN apt-get update && apt-get install -y \
	aptitude \
	cifs-utils \
	emacs \
	git \
	iputils-ping \
	net-tools

# NN
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
RUN mkdir /working_dir && cd /working_dir && \
	git clone https://github.com/jackyko1991/vnet-tensorflow.git && \
	git clone https://github.com/matterport/Mask_RCNN.git && \
	git clone https://github.com/affinelayer/pix2pix-tensorflow.git

# NAS
RUN mkdir /mnt/nas