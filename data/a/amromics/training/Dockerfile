FROM jupyter/minimal-notebook:177037d09156
LABEL   maintainer="Hoang Anh Nguyen <hoangnguyen177@amromics.org>"

ARG     KRAKEN_DB_URL=https://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_4GB.tgz
ARG     CENTRIFUGE_DB_URL=ftp://ftp.ccb.jhu.edu/pub/infphilo/centrifuge/data/p_compressed+h+v.tar.gz
ENV     KRAKEN_DB_PATH=/databases/minikraken
ENV     CENTRIFUGE_DB_PATH=/databases/centrifuge-db

ENV     KRAKEN_DEFAULT_DB=$KRAKEN_DB_PATH/minikraken_20171013_4GB
ENV     CENTRIFUGE_DEFAULT_DB=$CENTRIFUGE_DB_PATH/p_compressed+h+v


USER root
RUN apt-get -y update && \
    apt-get -y install curl procps build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p $KRAKEN_DB_PATH && \
    curl -fsSL $KRAKEN_DB_URL --output minikraken_20171019_4GB.tgz && \
    tar -C $KRAKEN_DB_PATH -xzvf minikraken_20171019_4GB.tgz && \
    rm -f minikraken_20171019_4GB.tgz

RUN mkdir -p $CENTRIFUGE_DB_PATH && \
    curl $CENTRIFUGE_DB_URL --output p_compressed+h+v.tar.gz && \
    tar -C $CENTRIFUGE_DB_PATH -xvzf p_compressed+h+v.tar.gz && \
    rm -f p_compressed+h+v.tar.gz

RUN conda install -y -c bioconda -c conda-forge nullarbor

# samtools openssl fix - this step can be removed once this problem is properly fixed in future package versions
RUN conda install -y -c bioconda samtools=1.9 bcftools --force
RUN conda install -y openssl=1.1 nbgitpuller=0.8.0
RUN conda install -y perl --force
# ensure samtools and bcftools run without libcrypto error
RUN samtools --version
RUN bcftools --version

# kraken2 seems to clobber the /opt/conda/libexec/classify binary from kraken,
# so we force install kraken again to ensure classify is the correct version
RUN conda install -y -c bioconda kraken --force

# sanity check
RUN nullarbor.pl --check

USER $NB_UID

# ENTRYPOINT ["nullarbor.pl"]
