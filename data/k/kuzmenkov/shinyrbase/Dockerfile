FROM ubuntu:trusty

ARG DEBIAN_FRONTED='noninteractive'

RUN useradd docker \
	&& mkdir /home/docker \
	&& chown docker:docker /home/docker \
	&& addgroup docker staff
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
	&& locale-gen en_US.utf8 \
	&& /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

## Install some useful tools and dependencies for MRO
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	ca-certificates \
	curl \
        wget \
	&& rm -rf /var/lib/apt/lists/*
	
# system libraries of general use
RUN apt-get update && apt-get install -y \
    sudo \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    libssl-dev \
    libssh2-1-dev \
    libssl1.0.0 \
    libxml2-dev \
    libssl-dev \
    apt-transport-https

# system library dependency for the euler app
RUN apt-get update && apt-get install -y \
    libmpfr-dev \
    gfortran \
    aptitude \
    libgdal-dev \
    libproj-dev \
    g++ \
    libicu-dev \
    libpcre3-dev\
    libbz2-dev \
    liblzma-dev \
    openjdk-7-jdk \
    libnlopt-dev \
    build-essential

RUN sudo apt-get install -y software-properties-common
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN sudo apt-get update -y
RUN sudo apt-get install -y gcc-4.9
RUN sudo apt-get install -y g++-4.9
RUN sudo apt-get update -y
RUN sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 60 --slave /usr/bin/g++ g++ /usr/bin/g++-4.9
RUN sudo update-alternatives --config gcc
RUN sudo apt-get install -y gfortran-4.9
RUN sudo update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-4.9 60
RUN sudo update-alternatives --config gfortran


WORKDIR /home/docker

# Download, valiate, and unpack and install R 3.5.2
#RUN echo "deb https://cloud.r-project.org/bin/linux/ubuntu trusty-cran35/" | sudo tee /etc/apt/sources.list
RUN sudo add-apt-repository -y 'deb https://cloud.r-project.org/bin/linux/ubuntu trusty-cran35/'
RUN sudo apt-get update -y
RUN sudo apt-get install -y r-base \
&& apt-get install -y r-base-dev

#RUN sudo R CMD javareconf
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
RUN apt-get update
RUN apt-get install -y libudunits2-dev libgdal-dev libgeos-dev 

# basic shiny functionality
RUN R -e "install.packages('shiny', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('rmarkdown', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('binom', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('dplyr', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('ggplot2', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('reshape', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('curl', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('httr', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('devtools', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('remotes', repos='https://cran.r-project.org/')" \
#&& R -e "remotes::install_url('https://cran.r-project.org/src/contrib/httpuv_1.4.3.tar.gz')" \
#&& R -e "download.file('https://github.com/rstudio/httpuv/archive/master.zip', 'httpuv-master.zip'); unlink('httpuv-master', recursive = TRUE); unzip('httpuv-master.zip', unzip = '/usr/bin/unzip'); file.mode('httpuv-master/src/libuv/configure')" \
#&& R -e "options(unzip = 'internal'); options(unzip = '/usr/bin/unzip'); devtools::install_github('rstudio/httpuv')" \
#&& R -e "options(unzip = 'internal'); devtools::install_github('rstudio/shiny')" \
&& R -e "install.packages('formattable', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('car', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('fmsb', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('igraph', repos='https://cran.r-project.org/')" \
&& sudo su - -c "R -e \"install.packages('miniUI', repos='https://cran.r-project.org/');options(unzip = 'internal'); remotes::install_github('daattali/shinyjs')\"" \
#RUN R -e "options(unzip = 'internal'); devtools::install_github('daattali/shinyjs')" \
&& R -e "install.packages('scales', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('crosstalk', repos='https://cran.r-project.org/')" \
&& sudo su - -c "R -e \"options(unzip = 'internal'); remotes::install_github('rstudio/DT')\"" \
#RUN R -e "devtools::install_github('rstudio/DT')" \
&& sudo su - -c "R -e \"install.packages(c('raster', 'sp', 'viridis'), repos='https://cran.r-project.org/');options(unzip = 'internal'); remotes::install_github('rstudio/leaflet')\"" \
&& sudo su - -c "R -e \"options(unzip = 'internal'); remotes::install_github('bhaskarvk/leaflet.extras')\"" \
&& R -e "install.packages('ggrepel', repos='https://cran.r-project.org/')" \
#RUN R -e "install.packages('leaflet', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('visNetwork', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('purrr', repos='https://cran.r-project.org/')" \
&& sudo su - -c "R -e \"options(unzip = 'internal'); remotes::install_github('kuzmenkov111/highcharter')\"" 

#COPY Rprofile.site /usr/lib64/R/etc/
EXPOSE 3838
