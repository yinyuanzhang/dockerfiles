# start with the ropensci image including debian:testing, r-base, rocker/rstudio, rocker/hadleyverse
# https://hub.docker.com/r/rocker/ropensci/
FROM rocker/rstudio:3.5.2

WORKDIR /home/eddy/eddy4R
# copy clone of GitHub source repo "NEONScience/NEON-FIU-algorithm" to the Docker image
COPY . .

# Build R dependencies using two cpu's worth of resources
ENV MAKEFLAGS='-j3'

# install OS-side dependencies: EBImage -> fftwtools -> fftw3, REddyProc -> RNetCDF -> udunits

  	# update the list of available packages and their versions
  	# required starting 2016-11-16T07:53:52Z when rocker/ropensci changed FROM rocker/hadleyverse to FROM rocker/verse
    RUN apt-get update \
    && apt-get dist-upgrade -y \
    && RUNDEPS="fftw3 \
            libudunits2-0 \
            udunits-bin \
            hdf5-helpers \
            libhdf5-cpp-100 \
            libnetcdf11 \
            libhdf5-100 \
            libsz2 \
            libmysql++3v5 \
            libmariadbclient18 \
            libpng-tools \
            libproj-dev \
			      libssl-dev \
			      # Library for git via ssh key
			      ssh \
            libxml2-dev \
            mysql-common" \
#            libtiff5 \
#            libjpeg62-turbo \
#            libnetcdf11 \
#            libpng16-16 \
#            libhdf5-100 \
#            libhdf5-cpp-100
    && BUILDDEPS="fftw3-dev \
                 libudunits2-dev \
                 libjpeg-dev \
                 libtiff5-dev \
                 libnetcdf-dev \
                 libpng-dev \
                 libhdf5-dev \
                 libmysql++-dev \
                 " \
    && apt-get install -y $BUILDDEPS $RUNDEPS \
    # create folder for dependencies of eddy4R packages
    # create directory
    && mkdir -p /home/eddy/depe \
    # provide read, write and executable access to web-hosted installation script
    # 777 is just wrong, shouldn't this be a chown?
    && chmod -R 777 /home/eddy/depe \
    # eddy4R installation
    # install eddy4R packages
    # install eddy4R packages from clone
    && R -e 'source("https://www.dropbox.com/s/xg8dxtmroo10qmm/flow.inst.eddy4r.R?dl=1")' \
    
    # Installing R package dependencies that are only workflow related (including CI combiner)
    && install2.r --error \
    Hmisc \
    parsedate \
    rowr \
    urltools \
    
    # provide read and write access for default R library location to Rstudio users
    # TODO: PERHAPS THIS SHOULD JUST CHOWN TO rstudio instead of setting 777 perms? And at the end of the file -sj
    && chmod -R 777 /usr/local/lib/R/site-library \
    # Clean up build dependencies
    && apt-get remove --purge -y $BUILDDEPS \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/* \
    # Clean up the rocker image leftovers
    && rm -rf /tmp/rstudio* \
    && rm -rf /tmp/Rtmp* 


