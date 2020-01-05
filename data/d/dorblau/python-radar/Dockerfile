FROM continuumio/miniconda3
MAINTAINER Aaron Anderson

RUN groupadd -r pyart && useradd --no-log-init -ms /bin/bash -r -g pyart pyart
RUN apt-get update && apt-get install -y gcc git libgl1-mesa-glx && apt-get clean

RUN conda config --add channels conda-forge &&\
    #conda config --append channels http://conda.anaconda.org/jjhelmus && \
    conda install --yes gdal ncurses siphon metpy boto numpy scipy xarray jupyter matplotlib netcdf4 pyproj basemap nose pillow owslib pyepsg cartopy \
    trmm_rsl wradlib arm_pyart && pip install nexradaws && pip install runipy && conda clean --all 


EXPOSE 8888
RUN chmod -R a+X /opt/conda/
RUN mkdir /opt/notebooks /opt/radar /opt/source && chown pyart:pyart /opt/notebooks && chown pyart:pyart /opt/radar && chown pyart:pyart /opt/source
VOLUME /opt/notebooks /opt/radar /opt/source
USER pyart
#CMD ["python"]

ADD make_tifs.py work/
WORKDIR work/
VOLUME ["work/"]
ENTRYPOINT ["python", "make_tifs.py"]
