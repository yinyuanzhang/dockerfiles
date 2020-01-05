FROM debian:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 libxft-dev libfreetype6 libfreetype6-dev \
    git vim

# install miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    conda update conda -y && \
    conda install python==3.6.9 && \
    conda install -c conda-forge pip && \
    conda install -c conda-forge ocw && \
    conda install pandas -y && \
    conda install dask distributed -c conda-forge && \
    pip install geojsoncontour && \
    conda update basemap -y && \
    conda install -c conda-forge netcdftime -y && \
    conda clean -y --all

# install OCW from Git repository
RUN cd /usr/local  && \
    git clone https://github.com/apache/climate.git
#ENV PYTHONPATH /usr/local/climate:/usr/local/climate/ocw
ENV PYTHONPATH="/usr/local/climate:/usr/local/climate/ocw" \
    PROJ_LIB="/opt/conda/share/proj"

# additional pyyaml dependency
#RUN pip install pyyaml

# execute python script in this directory
WORKDIR /usr/local/climate/RCMES/CORDEX

#ENTRYPOINT [ "python", "cordex.py" ] # I commented this lline to enable data analysts to choose their own analytical programs