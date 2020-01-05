FROM tensorflow/tensorflow:nightly-gpu-py3-jupyter
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
RUN mkdir /working_dir

# NAS
RUN mkdir /mnt/nas