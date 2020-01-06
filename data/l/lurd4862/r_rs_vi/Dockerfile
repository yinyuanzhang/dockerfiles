FROM rocker/tidyverse

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update
RUN apt-get install -y software-properties-common

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install htop

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

RUN R -e 'install.packages("RPostgres")'
RUN R -e 'install.packages("caret")'

RUN apt-get update
RUN apt-get install -y --no-install-recommends software-properties-common

USER root
RUN mkdir -p /usr/share/man/man1 && \
    apt-get update -y && \
    apt-get install -y openjdk-8-jdk

RUN R -e 'install.packages("h2o")'
RUN R -e 'devtools::install_github("MI2DataLab/modelDown")'

RUN apt-get install -y libudunits2-dev
RUN apt install -y libgdal-dev
RUN R -e 'install.packages("pdp")'
RUN R -e 'install.packages("pdp")'
RUN R -e 'install.packages("units")'
RUN R -e 'install.packages("sf")'
RUN R -e 'install.packages("spdep")'
RUN R -e 'install.packages("agricolae")'
RUN R -e 'install.packages("factorMerger")'
RUN R -e 'install.packages("reticulate")'
RUN R -e 'install.packages("glue")'
RUN R -e 'install.packages("yaml")'
RUN R -e 'install.packages("optparse")'

RUN pip install tsfresh
