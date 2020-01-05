# This dockerfile used for DNA sequence analysis.
# VERSION 1 - EDITION 1
# Powered by ChangeGene LLC.
# A Bioinformatics Solution Provider from Harvard.
# Created by skywalker@changegene.com at 20170731.
# Offical web: https://hub.docker.com/repository/docker/changegene/
# The follow is modify log:

# ubuntu version choice the version earlier than your Software or Pipeline.  X.04 is the LTS version.
# ubuntu version list: https://wiki.ubuntu.com/Releases
# ARG  Image_VERSION=1.0
FROM bioconductor/release_base2

MAINTAINER Skywalker <skywalker@changegene.com>
RUN apt-get update -y
RUN apt-get install -y libglu1-mesa-dev

############  install MOMF   ###############

### install devtools packages (devtools package)
RUN R -e "install.packages(\"devtools\")"
RUN R -e "BiocManager::install(c(\"matlib\", \"shiny\"))"
### install MOMF package
RUN R -e "devtools::install_github(\"sqsun/MOMF\")"
