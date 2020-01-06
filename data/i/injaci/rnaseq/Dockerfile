# Dockerfile to build tools for RNAseq
#4th october 2018

FROM ubuntu:14.04

LABEL ubuntu.version = "14.04"

USER root

RUN apt-get update -y && apt-get install -y python-dev python-pip wget unzip tar && \

pip install --upgrade cutadapt && \

export PATH="$PATH:$HOME/.local/bin"

RUN wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.7.zip

RUN unzip fastqc_v0.11.7.zip && \

rm fastqc_v0.11.7.zip && \

mv FastQC /opt/ && \

ln -s /opt/FastQC/fastqc /usr/bin/fastqc

RUN wget https://github.com/pachterlab/kallisto/releases/download/v0.44.0/kallisto_linux-v0.44.0.tar.gz && \

tar -zxf kallisto_linux-v0.44.0.tar.gz && \

rm kallisto_linux-v0.44.0.tar.gz && \

mv kallisto_linux-v0.44.0 /opt/ && \

ln -s /opt/kallisto_linux-v0.44.0/kallisto /usr/bin/kallisto

RUN wget http://ccb.jhu.edu/software/stringtie/dl/stringtie-1.3.4d.tar.gz && \

tar -zxf stringtie-1.3.4d.tar.gz && \

rm stringtie-1.3.4d.tar.gz && \

mv stringtie-1.3.4d /opt/ && \

ln -s /opt/stringtie-1.3.3d/stringtie /usr/bin/stringtie

# to mount a drive for you to access the data
# docker run -it -v "$(pwd)":/home rnaseq 
#where -v is the volume "$(pwd)" is the folder containing the data and /home is the folder name in container
# and rnaseq is the image name
