FROM bioconductor/release_core2:R3.6.0_Bioc3.9

RUN apt-get update -qq && apt-get -y install libssl-dev libssh2-1-dev libcurl4-openssl-dev libxml2-dev texlive pandoc

RUN Rscript -e "\
    install.packages(c(\
        'boot', \
        'dendextend', \
        'devtools', \
        'GGally', \
        'ggfortify', \
        'ggrepel', \
        'ggpubr', \
        'gplots', \
        'kableExtra', \
        'knitr', \
        'openxlsx', \
        'RColorBrewer', \
        'rmarkdown', \
        'roxygen2', \
        'stringr', \
        'testthat', \
        'tidyverse', \
        'statmod', \
        'pheatmap')); \
    BiocManager::install(c(\
        'annotatr', \
        'DMRcate', \
        'ENmix', \
        'FlowSorted.Blood.EPIC', \
        'FlowSorted.CordBlood.450k', \
        'GenomicRanges', \
        'IlluminaHumanMethylationEPICanno.ilm10b2.hg19', \
        'IlluminaHumanMethylationEPICanno.ilm10b4.hg19', \
        'limma', \
        'minfi', \
        'org.Hs.eg.db'), \
        ask = FALSE, update = TRUE);"
