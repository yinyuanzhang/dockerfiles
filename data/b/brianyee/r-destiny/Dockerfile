################## BASE IMAGE ######################

FROM brianyee/r-jupyter

################## METADATA ######################

LABEL base_image="continuumio/miniconda:latest"
LABEL version="1"
LABEL software="destiny"
LABEL software.version="2.14.0"
LABEL about.summary="R-destiny + jupyter irkernel"
LABEL about.home="https://github.com/theislab/destiny"
LABEL about.documentation="https://github.com/theislab/destiny/tree/master/vignettes"
LABEL about.license_file=""
LABEL about.license="Artistic-2.0"
LABEL about.tags="Genomics"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>
RUN apt-get update
RUN apt-get remove -y libc6-dev # https://github.com/riscv/riscv-gnu-toolchain/issues/105 (the solution that sucks)
RUN Rscript -e 'install.packages(c("curl","httr"))' # https://github.com/Microsoft/microsoft-r-open/issues/63
RUN apt-get install -y libc6-dev
RUN apt-get install -y libhdf5-dev && Rscript -e 'install.packages("hdf5r")'
RUN Rscript -e 'withr::with_makevars(c(PKG_LIBS="-liconv"), install.packages(c("readxl","haven")), assignment="+=")'
RUN Rscript -e 'install.packages("BiocManager");BiocManager::install("destiny")'
# RUN conda install -y -c bioconda/label/gcc7 bioconductor-destiny
RUN Rscript -e 'remove.packages(c("curl","httr"))' # https://github.com/Microsoft/microsoft-r-open/issues/63
RUN Rscript -e 'IRkernel::installspec(name = "R-destiny-2.14.0", displayname = "R-destiny-2.14.0", user = FALSE)'
