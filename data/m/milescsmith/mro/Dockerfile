# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
FROM milescsmith/mro:mro-verse

ENV PATH=$PATH:/opt/TinyTeX/bin/x86_64-linux/

## Taken from https://github.com/rocker-org/rocker-versioned/blob/master/tidyverse/3.5.3/Dockerfile
RUN ln -fs /usr/share/zoneinfo/America/Chicago /etc/localtime && \ 
  export DEBIAN_FRONTEND=noninteractive; apt-get -y update && \
  apt-get install -y tzdata \
    libhdf5-dev \
    libglu1-mesa-dev \
    psmisc \
    libapparmor1 \
    sudo \
    lsb-release \
    libclang-dev && \
  apt-get clean && \
  rm -rf /tmp/downloaded_packages/* && \
  rm -rf /var/lib/apt/lists/*

RUN curl https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.2.1335-amd64.deb -o /tmp/rstudio-server.deb && \
  dpkg -i /tmp/rstudio-server.deb

RUN \
  Rscript -e "BiocManager::install()" && \
  Rscript -e "BiocManager::install(c('pheatmap', \
    'kableExtra', \
    'IRdisplay', \
    'RColorBrewer', \
    'paletteer', \
    'cowplot', \
    'irlba', \
    'ggforce', \
    'uwot', \
    'rsvd', \
    'alastairrushworth/inspectdf', \
    'visNetwork', \
    'BiocParallel', \
    'clusterProfiler', \
    'DESeq2', \
    'S4Vectors', \
    'SummarizedExperiment', \
    'tximport', \
    'edgeR', \
    'limma', \
    'HGNChelper', \
    'enrichplot', \
    'furrr', \
    'future.apply', \
    'rtracklayer', \
    'ggrepel', \
    'HDF5Array', \
    'hdf5r', \
    'matrixStats', \
    'Rhdf5lib', \
    'Rtsne'))"

EXPOSE 8787

# Add image metadata
LABEL org.label-schema.license="https://mran.microsoft.com/faq/#licensing" \
    org.label-schema.vendor="Microsoft Corporation, Dockerfile provided by Daniel Nüst" \
	org.label-schema.name="Microsoft R Open (verse)" \
	org.label-schema.description="Docker images of Microsoft R Open (MRO) with the Intel® Math Kernel Libraries (MKL)." \ 
	org.label-schema.vcs-url=$VCS_URL \
	org.label-schema.vcs-ref=$VCS_REF \
	org.label-schema.build-date=$BUILD_DATE \
	org.label-schema.schema-version="rc1" \
	maintainer="Daniel Nüst <daniel.nuest@uni-muenster.de>" \
  maintainer="Miles Smith <miles-smith@omrf.org>"
