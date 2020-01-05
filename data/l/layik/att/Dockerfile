FROM ubuntu:xenial

RUN apt-get update \ 
	&& apt-get install -y --no-install-recommends \
		software-properties-common \
    ed \
		less \
		locales \
		vim-tiny \
		wget \
		ca-certificates \
    && add-apt-repository -y "ppa:marutter/rrutter" \
	  && add-apt-repository -y "ppa:marutter/c2d4u" \
    && apt-get update 

## Configure default locale, see https://github.com/rocker-org/rocker/issues/19
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
	&& locale-gen en_US.utf8 \
	&& /usr/sbin/update-locale LANG=en_US.UTF-8

## Now install R and littler, and create a link for littler in /usr/local/bin
## Default CRAN repo is now set by R itself, and littler knows about it too
## r-cran-docopt is not currently in c2d4u so we install from source
## Note: we need wget as the build env is too old for libcurl (we think, precise was)
RUN apt-get install -y --no-install-recommends \
                r-cran-littler \
		r-base \
		r-base-dev \
		r-recommended \
        && echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), download.file.method = "wget")' >> /etc/R/Rprofile.site \
	&& ln -s /usr/lib/R/site-library/littler/examples/install.r /usr/local/bin/install.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/install2.r /usr/local/bin/install2.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
	&& install.r docopt \
	&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds 

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8


RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    lbzip2 \
    libfftw3-dev \
    libgdal-dev \
    libgeos-dev \
    libgsl0-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libhdf4-alt-dev \
    libhdf5-dev \
    libjq-dev \
    liblwgeom-dev \
    libproj-dev \
    libprotobuf-dev \
    libnetcdf-dev \
    libsqlite3-dev \
    libssl-dev \
    libudunits2-dev \
    netcdf-bin \
    tk-dev \
    unixodbc-dev \
    libv8-dev \
    protobuf-compiler \ 
    git

RUN apt-get install -y --no-install-recommends \ 
    r-cran-lubridate r-cran-lubridate \
    r-cran-igraph r-cran-devtools \
    r-cran-sp r-cran-sf \
    r-cran-osmdata r-cran-stplanr \
    r-cran-v8 r-cran-plumber

RUN R -e 'install.packages(c("geojsonsf", \
        "here", "rbenchmark", "RcppParallel"), \
        dependencies=T);'

RUN git clone https://github.com/ATFutures/dodgr.git

RUN R -e "devtools::load_all('/dodgr', export_all=F)"

RUN R -e 'devtools::install_version("rgeos", version = "0.3-28")'

ADD . /app

EXPOSE 8000

ENTRYPOINT ["R", "-e", "setwd('/app'); \
 plumber::plumb(file.path(here::here(), 'server', 'plumber.R'))$run(host='0.0.0.0',port=8000)"]