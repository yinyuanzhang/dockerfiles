######################################################################################
# Dockerfile
#
# Software Version:  augustus3.3
# Description:      AUGUSTUS is a gene prediction program for eukaryotes written by Mario Stanke and Oliver Keller.
# Code:             http://bioinf.uni-greifswald.de/augustus/
# Base Image:       conda/miniconda3
# Build Cmd:        sudo docker build -t cgwyx:augustus .
# Pull Cmd:         docker pull cgwyx/augustus
# Run Cmd:          sudo docker run -it --rm -v /home:/home --name=canu cgwyx/augustus:latest /bin/bash
# File Author / Maintainer: cheng gong <512543469@qq.com>
######################################################################################

FROM conda/miniconda3

RUN conda update --all -y &&\
    conda config --add channels conda-forge &&\
    conda config --add channels r &&\
    conda config --add channels bioconda &&\
    conda config --set show_channel_urls yes &&\
    conda install -y -c bioconda augustus
    
CMD ["/bin/bash"]


