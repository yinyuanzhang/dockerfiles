FROM rocker/r-ver:3.4.4

LABEL maintainer="jeffrey.hanson@uqconnect.edu.au"

## Copy files
COPY . /tmp

## Add spatial support (from rocker/geospatial)
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    jpegoptim \
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
    protobuf-compiler \
    tk-dev \
    unixodbc-dev \
    wget \
    git

## Add LaTeX, rticles and bookdown support (from rocker/verse)
RUN wget "https://travis-bin.yihui.name/texlive-local.deb" \
  && dpkg -i texlive-local.deb \
  && rm texlive-local.deb \
  && apt-get update \
  && dpkg -i /tmp/pandoc-2.7.1-1-amd64.deb \
  && rm /tmp/pandoc-2.7.1-1-amd64.deb \
  && apt-get install -y --no-install-recommends \
    ## for rJava
    default-jdk \
    ## Nice Google fonts
    fonts-roboto \
    ## used by some base R plots
    ghostscript \
    ## used to build rJava and other packages
    libbz2-dev \
    libicu-dev \
    liblzma-dev \
    ## system dependency of hunspell (devtools)
    libhunspell-dev \
    ## system dependency of hadley/pkgdown
    libmagick++-dev \
    ## rdf, for redland / linked data
    librdf0-dev \
    ## for V8-based javascript wrappers
    libv8-dev \
    ## R CMD Check wants qpdf to check pdf sizes, or throws a Warning
    qpdf \
    ## For building PDF manuals
    texinfo \
    ## for git via ssh key
    ssh \
    ## just because
    less \
    vim \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/ \
  ## Use tinytex for LaTeX installation
  && wget -qO- \
    "https://github.com/yihui/tinytex/raw/master/tools/install-unx.sh" | \
    sh -s - --admin --no-path \
  && mv ~/.TinyTeX /opt/TinyTeX \
  && /opt/TinyTeX/bin/*/tlmgr path add \
  && tlmgr install \
    ae \
    capt-of \
    changepage \
    csquotes \
    etoolbox \
    fancyhdr \
    filehook \
    float \
    inconsolata \
    lineno \
    listings \
    makecell \
    metafont \
    mfware \
    parskip \
    setspace \
    siunitx \
    subfiles \
    tabu \
    tex \
    titlesec \
    tocloft \
    varwidth \
    unicode-math \
    xcolor \
    xtab \
  && tlmgr path add \
  && Rscript -e "install.packages('/tmp/xfun_0.6.tar.gz', repos = NULL, type='source')" \
  && Rscript -e "source('http://install-github.me/yihui/tinytex'); tinytex::r_texmf()" \
  && chown -R root:staff /opt/TinyTeX \
  && chmod -R g+w /opt/TinyTeX \
  && chmod -R g+wx /opt/TinyTeX/bin

## Configure R profile and install R packages
RUN echo "options(repos = 'https://mran.microsoft.com/snapshot/2018-05-16')" \
  >> ~/.Rprofile \
  && install2.r --error --deps NA \
  assertthat \
  bookdown \
  boxr \
  clisymbols \
  crosstalk \
  data.table \
  devtools \
  digest \
  doParallel \
  dplyr \
  FNN \
  fs \
  ggplot2 \
  gh \
  ggmap \
  ggrepel \
  gridExtra \
  knitr \
  kableExtra \
  leaflet \
  lubridate \
  magrittr \
  plotly \
  plyr \
  raster \
  RcppTOML \
  readxl \
  remotes \
  rgdal \
  rgeos \
  rmarkdown \
  rnaturalearth \
  R6 \
  sf \
  smoothr \
  sp \
  tidyr \
  tictoc \
  usethis \
  viridis \
  && install2.r --error --deps NA -- "--configure-args=\"--without-liblwgeom\"" lwgeom \
  && R -e "devtools::install_github('tidyverse/ggplot2@eecc450',upgrade_dependencies=FALSE)" \
  && R -e "devtools::install_github('thomasp85/patchwork@6979eb1',upgrade_dependencies=FALSE)" \
  && R -e "devtools::install_github('ropensci/piggyback@2680151a90b1fb174cef5afa6d225036c7dd2790',upgrade_dependencies=FALSE)" \
  && R -e "devtools::install_github('r-spatial/leafem@842c3657595e814f215702f0d566eec3b3e2b9ca',upgrade_dependencies=FALSE)" \
  && R CMD INSTALL /tmp/rnaturalearthhires_0.1.0.tar.gz \
  && rm /tmp/rnaturalearthhires_0.1.0.tar.gz
