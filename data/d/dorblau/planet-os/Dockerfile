FROM continuumio/miniconda3
MAINTAINER Aaron Anderson

RUN groupadd -r pyart && useradd --no-log-init -ms /bin/bash -r -g pyart pyart
RUN apt-get update && apt-get install -y gcc git libgl1-mesa-glx  && apt-get clean

RUN conda config --add channels conda-forge &&\
    conda install --yes gdal ncurses siphon metpy boto numpy scipy xarray jupyter netcdf4 pyproj basemap nose pillow owslib pyepsg cartopy \
    trmm_rsl wradlib arm_pyart && pip install nexradaws && pip install runipy && conda clean --all 

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install pkg-config

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

RUN python -m pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install --upgrade jupyter

EXPOSE 8888

RUN mkdir /notebooks
CMD jupyter notebook --no-browser --ip 0.0.0.0 --port 8888 --allow-root

