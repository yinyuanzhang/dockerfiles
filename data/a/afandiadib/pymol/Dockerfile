FROM ubuntu

MAINTAINER "Adib Afandi bin Abdullah <fendy90.oscura@gmail.com>" 

ENV PATH /opt/conda/bin:$PATH

RUN apt-get update && \
    apt-get -y install --no-install-recommends git ca-certificates wget bzip2 && \
    apt-get -y install build-essential libglew-dev freeglut3-dev libpng-dev libfreetype6-dev libxml2-dev libmsgpack-dev libglm-dev && \
    wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    chmod +x Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    conda install -y -c conda-forge pmw && \
    conda install -y -c anaconda pyqt numpy && \
    git clone https://github.com/schrodinger/pymol-open-source.git && \
    cd pymol-open-source && \
    python setup.py install --prefix=/opt/conda && \
    apt-get -y purge git wget && \
    apt-get -y autoremove && apt-get -y clean && rm -rf /var/lib/apt/lists/* && \
    conda update -y --all && conda clean -p -y && \
    rm -rf /pymol-open-source && \
    chmod -R 777 /opt

CMD /opt/conda/bin/pymol
