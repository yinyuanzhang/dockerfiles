FROM  jupyterhub/jupyterhub

COPY jupyterhub_config.py .

RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0

RUN apt-get update
RUN apt install -y tzdata font-manager

RUN conda config --add channels bioconda
RUN conda config --add channels conda-forge

RUN conda install -c anaconda curl 
RUN conda install vim
RUN conda install emacs ncurses=6
RUN pip install jupyterhub-dummyauthenticator
RUN pip install jupyterhub-firstuseauthenticator

RUN conda install  --quiet --yes -c r r-irkernel
RUN conda install -c r r-devtools 
RUN conda install -c bioconda bioconductor-elmer

RUN conda install -c conda-forge tar 
RUN ln -s /bin/tar /bin/gtar

RUN pip install notebook
RUN conda install jupyterlab
RUN pip install oauthenticator
RUN conda install unzip 
RUN conda install -c conda-forge r-vegan
RUN conda install -c bioconda bioconductor-karyoploter 
RUN conda install -c bioconda bioconductor-txdb.hsapiens.ucsc.hg38.knowngene 
RUN conda install -c bioconda bioconductor-org.hs.eg.db 


RUN R -e 'options(unzip = "internal");source("https://bioconductor.org/biocLite.R");biocLite("BiocInstaller");devtools::install_github(c("tiagochst/ELMER.data", "BioinformaticsFMRP/TCGAbiolinks","tiagochst/ELMER","jokergoo/ComplexHeatmap","bernatgel/karyoploteR"))'
