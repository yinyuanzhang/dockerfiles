FROM ubuntu:trusty

# An external atlas dir will bind here
RUN mkdir -p /opt/atlas

RUN apt-get update && \
    apt-get install -y wget zip && \
    wget -q -P /opt/ https://www.dropbox.com/s/xa04fa7k57w94zu/ashs-fastashs-20170915.zip && \
    unzip -q /opt/ashs-fastashs-20170915.zip -d /opt/ && \
    rm /opt/ashs-fastashs-20170915.zip

# Libraries needed by ml_affine
RUN apt-get update && apt-get install -y libxt6 libgl1-mesa-glx

# Replace files that we modified
COPY ashs_extractstats_qsub.sh /opt/ashs-1.0.0/bin/ashs_extractstats_qsub.sh

# Install packages required by dax
RUN apt-get update && apt-get install -y \
    python-pip libfreetype6-dev pkg-config libxml2-dev libxslt1-dev \
    python-dev zlib1g-dev python-numpy python-scipy python-requests \ 
    python-urllib3 python-pandas

RUN pip install matplotlib --upgrade
RUN pip install pandas --upgrade
RUN pip install pydicom==0.9.9

# Install dax
RUN pip install https://github.com/VUIIS/dax/archive/v0.7.1.zip

# Install src
COPY src /opt/src/
RUN chmod +x /opt/src/dcm2nii

# Make directories for I/O to bind
RUN mkdir /INPUTS /OUTPUTS

# Get the spider code
COPY spider.py /opt/spider.py
ENTRYPOINT ["python", "/opt/spider.py"]
