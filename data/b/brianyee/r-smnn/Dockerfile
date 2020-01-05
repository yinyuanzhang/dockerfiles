################## BASE IMAGE ######################

FROM brianyee/r-jupyter:43471383db04

################## METADATA ######################

LABEL base_image="continuumio/miniconda:latest"
LABEL version="1"
LABEL software="R"
LABEL software.version="3.5.1"
LABEL about.summary="R-SMNN + jupyter irkernel"
LABEL about.home=""
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags="Genomics"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>
RUN apt-get remove -y libc6-dev # https://github.com/riscv/riscv-gnu-toolchain/issues/105 (the solution that sucks, but curl wont install with it)
RUN Rscript -e 'install.packages(c("curl","httr"))' # https://github.com/Microsoft/microsoft-r-open/issues/63
RUN apt-get update && apt-get install -y libc6-dev 
RUN apt-get install -y libhdf5-dev && Rscript -e 'install.packages("hdf5r")'
# RUN Rscript -e 'install.packages("sctransform", type = "binary")'
RUN Rscript -e 'devtools::install_github(repo = "ChristophH/sctransform")'
RUN Rscript -e 'install.packages("BiocManager");BiocManager::install(c("ape", "BH", "bibtex", "bindr", "bindrcpp", "bitops", "caTools", "cowplot", "crosstalk", "data.table", "dplyr", "fitdistrplus", "gbRd", "gdata", "ggrepel", "ggridges", "gplots", "gtools", "hexbin", "htmlwidgets", "httpuv", "ica", "igraph", "irlba", "later", "lmtest", "metap", "pbapply", "pkgconfig", "plogr", "plotly", "promises", "purrr", "R.methodsS3", "R.oo", "R.utils", "RANN", "RcppAnnoy", "RcppProgress", "Rdpack", "reticulate", "ROCR", "rsvd", "Rtsne", "SDMTools", "shiny", "sourcetools", "tidyr", "tidyselect", "tsne", "xtable", "yaml", "zoo"))'
RUN Rscript -e 'BiocManager::install("leiden")'
RUN Rscript -e 'BiocManager::install("uwot")'
RUN Rscript -e 'devtools::install_github(repo = "satijalab/seurat", ref = "develop")'
#RUN Rscript -e 'remove.packages(c("curl","httr"))' # https://github.com/Microsoft/microsoft-r-open/issues/63
#RUN Rscript -e 'IRkernel::installspec(name = "R-Seurat-develop", displayname = "R-Seurat-develop", user = FALSE)'
RUN Rscript -e 'install.packages("reticulate")'
RUN pip install umap-learn
#RUN Rscript -e 'library("reticulate");py_install("umap-learn", pip = T, pip_ignore_installed = T)'
RUN Rscript -e 'install.packages("umap")'
RUN Rscript -e 'install.packages("reshape")'
RUN Rscript -e 'install.packages("BiocManager");BiocManager::install("S4Vectors")'
RUN pip install numba==0.43.1
RUN cd /opt && \
  git clone https://github.com/chriscainx/mnnpy.git && \
  cd mnnpy && \
  pip install .
RUN cd /opt && \
  wget https://yunliweb.its.unc.edu/SMNN/software/SMNN-0.99.0-master.zip && \
  unzip /opt/SMNN-0.99.0-master.zip && \
  Rscript -e 'install.packages("/opt/SMNN-master/", repos = NULL, type = "sources")'
RUN Rscript -e 'remove.packages(c("curl","httr"))' # https://github.com/Microsoft/microsoft-r-open/issues/63
RUN Rscript -e 'IRkernel::installspec(name = "R-Seurat-develop_SMNN-0.99.0", displayname = "R-Seurat-develop + SMNN-0.99.0", user = FALSE)'
RUN apt-get remove -y libc6-dev # https://github.com/riscv/riscv-gnu-toolchain/issues/105 (the solution that sucks, but curl wont install)
RUN Rscript -e 'install.packages(c("curl","httr"))' # https://github.com/Microsoft/microsoft-r-open/issues/63
RUN apt-get install -y libc6-dev
