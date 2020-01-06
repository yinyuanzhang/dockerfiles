FROM floydhub/pytorch:0.3.0-gpu.cuda9cudnn7-py3.22
MAINTAINER deif79@gmail.com

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.3.27-Linux-x86_64.sh -O ~/miniconda.sh
RUN /bin/bash ~/miniconda.sh -b -p /opt/conda && rm ~/miniconda.sh
RUN /opt/conda/bin/conda install hdfs3 -y
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:/opt/conda/lib/
RUN pip install hdfs3
RUN pip install torch==0.4.0
