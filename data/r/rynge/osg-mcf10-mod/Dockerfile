FROM opensciencegrid/osgvo-el7

MAINTAINER Mats Rynge <rynge@isi.edu>

ADD conda.yml /tmp/

RUN cd /tmp && \
    wget -nv -O ~/conda-setup.sh https://repo.continuum.io/miniconda/Miniconda2-4.6.14-Linux-x86_64.sh && \
    bash ~/conda-setup.sh -b -f -p /opt/conda && \
    . /opt/conda/bin/activate && \
    conda env update -f conda.yml

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

