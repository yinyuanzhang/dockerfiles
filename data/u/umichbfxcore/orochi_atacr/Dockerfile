FROM bioconductor/release_core2:R3.6.0_Bioc3.9

RUN apt-get update -qq && apt-get -y install libssl-dev libssh2-1-dev libcurl4-openssl-dev libxml2-dev texlive pandoc

RUN Rscript -e "\
    install.packages(c(\
        'devtools', \
        'optparse', \
        'rmarkdown', \
        'roxygen2', \
        'testthat', \
        'kableExtra', \
        'knitr', \
        'boot', \
        'gplots', \
        'GGally', \
        'ggfortify', \
        'ggrepel', \
        'ggpubr', \
        'tidyverse', \
        'openxlsx', \
        'statmod', \
        'pheatmap')); \
    BiocManager::install(c(\
        'BiocCheck', \
        'BiocStyle', \
        'annotatr', \
        'chipenrich', \
        'DelayedArray', \
        'edgeR', \
        'GO.db', \
        'BSgenome.Hsapiens.UCSC.hg38', \
        'BSgenome.Hsapiens.UCSC.hg19', \
        'BSgenome.Mmusculus.UCSC.mm10', \
        'org.Dm.eg.db', \
        'org.Dr.eg.db', \
        'org.Gg.eg.db', \
        'org.Hs.eg.db', \
        'org.Mm.eg.db', \
        'org.Rn.eg.db', \
        'TxDb.Dmelanogaster.UCSC.dm3.ensGene', \
        'TxDb.Dmelanogaster.UCSC.dm6.ensGene', \
        'TxDb.Drerio.UCSC.danRer11.refGene', \
        'TxDb.Ggallus.UCSC.galGal5.refGene', \
        'TxDb.Hsapiens.UCSC.hg19.knownGene', \
        'TxDb.Hsapiens.UCSC.hg38.knownGene', \
        'TxDb.Mmusculus.UCSC.mm9.knownGene', \
        'TxDb.Mmusculus.UCSC.mm10.knownGene', \
        'TxDb.Rnorvegicus.UCSC.rn4.ensGene', \
        'TxDb.Rnorvegicus.UCSC.rn5.refGene', \
        'TxDb.Rnorvegicus.UCSC.rn6.refGene'), \
    ask = FALSE, update = TRUE); \
    devtools::install_github('rcavalcante/annotatr@RELEASE_3_9-danRer11');"
