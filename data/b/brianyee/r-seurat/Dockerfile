################## BASE IMAGE ######################

FROM brianyee/r-jupyter

################## METADATA ######################

LABEL base_image="continuumio/miniconda:latest"
LABEL version="1"
LABEL software="R"
LABEL software.version="3.5.1"
LABEL about.summary="R-Seurat + jupyter irkernel"
LABEL about.home="https://github.com/byee4/docker"
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
RUN Rscript -e 'devtools::install_github(repo = "satijalab/seurat", ref = "48b6ba0e15983cfadef6228b86a0ab95e0cb0c1e")'
RUN Rscript -e 'remove.packages(c("curl","httr"))' # https://github.com/Microsoft/microsoft-r-open/issues/63
RUN Rscript -e 'IRkernel::installspec(name = "R-Seurat", displayname = "R-Seurat", user = FALSE)'
RUN Rscript -e 'install.packages("reticulate")'
RUN pip install umap-learn
RUN Rscript -e 'library("reticulate");py_install("umap-learn", pip = T, pip_ignore_installed = T)'
RUN Rscript -e 'install.packages("umap")'
# RUN conda install -y -c bioconda umap-learn;
# RUN Rscript -e 'install.packages("https://cran.r-project.org/src/contrib/umap_0.2.0.0.tar.gz",repos=NULL)'
RUN apt-get remove -y libc6-dev # https://github.com/riscv/riscv-gnu-toolchain/issues/105 (the solution that sucks, but curl wont ins$
RUN Rscript -e 'install.packages(c("curl","httr"))' # https://github.com/Microsoft/microsoft-r-open/issues/63
RUN apt-get install -y libc6-dev
