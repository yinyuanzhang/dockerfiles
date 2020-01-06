FROM continuumio/miniconda3
MAINTAINER wuyang@vt.edu

ENV PY_VER=3.7
ENV TRINITY_VER=2.8.5
ENV SRA_VER=2.10.0

WORKDIR /opt

RUN conda config --add channels bioconda && \
    conda config --add channels conda-forge && \
    # Trinity and sratoolkit:
    conda install -yq trinity=$TRINITY_VER sra-tools=$SRA_VER numpy && \
    # sratoolkit:
    # wget -O /opt/sratoolkit.tar.gz -q https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/${SRA_VER}/sratoolkit.${SRA_VER}-ubuntu64.tar.gz && \
    # tar -zxvf /opt/sratoolkit.tar.gz -C /opt/ && \
    # ln -sf /opt/sratoolkit.${SRA_VER}-ubuntu64/bin/* /usr/bin/ && \
    # HF:
    git clone https://github.com/yangwu91/HF.git && \
    cd HF && \
    pip install -q . && \
    # Clean:
    conda clean -ayq

ENTRYPOINT ["/opt/conda/bin/HF"]