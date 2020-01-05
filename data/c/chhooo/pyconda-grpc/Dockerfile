FROM python:3.6
#FROM debian:jessie

#RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
#    libglib2.0-0 libxext6 libsm6 libxrender1 \
#    git mercurial subversion python-dev pandoc python-pip
    
#RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
#    wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh && \
#    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
#    rm ~/anaconda.sh
RUN apt-get update
RUN apt-get install -y pandoc vim

#RUN pip install pymysql
#RUN pip install sqlalchemy 
#RUN pip install python-dotenv
#RUN pip install grpcio
#RUN pip install grpcio-tools
#RUN pip install kazoo
#RUN pip install aliyun-log-python-sdk
#RUN pip install psutil
#RUN pip install pandas
#RUN pip install schedule
#RUN pip install mpld3
#RUN pip install matplotlib
#RUN pip install jinja2
#include requirements
RUN pip install git+https://github.com/chrisho/grpcpy.git#egg=grpcpy
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
