# Base image
FROM rocker/verse:3.4.3
MAINTAINER Emrah Er <eer@eremrah.com>

# Install other libraries
RUN install2.r --error \
         ggmap gam kableExtra hdm \
    && R -e "devtools::install_github('emraher/eermisc')" \
    && R -e "devtools::install_github('emraher/wildcatdown')"
