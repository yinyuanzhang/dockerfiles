#    This file is part of tau-vulnerability.
#    Copyright (C) 2019  Emir Turkes
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Emir Turkes can be contacted at emir.turkes@eturkes.com

FROM rocker/rstudio:3.6.1

LABEL maintainer="Emir Turkes emir.turkes@eturkes.com"

COPY user-settings /home/rstudio/.rstudio/monitored/user-settings/

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    zlib1g-dev \
    libxml2-dev \
    libpng-dev \
 && Rscript \
    -e "install.packages('conflicted')" \
    -e "install.packages('peakRAM')" \
    -e "install.packages('rmarkdown')" \
    -e "install.packages('rprojroot')" \
    -e "install.packages('data.table')" \
    -e "install.packages('DT')" \
    -e "install.packages('dplyr')" \
    -e "install.packages('ggplot2')" \
    -e "install.packages('ggrepel')" \
    -e "install.packages('future')" \
    -e "install.packages('magrittr')" \
    -e "install.packages('knitr')" \
    -e "install.packages('Matrix')" \
    -e "install.packages('pheatmap')" \
    -e "install.packages('BiocManager')" \
    -e "install.packages('devtools')" \
    -e "BiocManager::install('BiocFileCache')" \
    -e "BiocManager::install('SingleCellExperiment')" \
    -e "BiocManager::install('biomaRt')" \
    -e "BiocManager::install('scater')" \
    -e "BiocManager::install('DropletUtils')" \
    -e "BiocManager::install('GO.db')" \
    -e "BiocManager::install('GSVA')" \
    -e "BiocManager::install('GSEABase')" \
    -e "BiocManager::install('scRNAseq')" \
    -e "BiocManager::install('multtest')" \
    -e "devtools::install_github('NathanSkene/EWCE')" \
    -e "devtools::install_github('AllenInstitute/scrattch.io')" \
    -e "install.packages('Seurat')" \
 && apt-get clean \
 && rm -Rf \
    /var/lib/apt/lists/ \
    /tmp/downloaded_packages/ \
    /tmp/*.rds
