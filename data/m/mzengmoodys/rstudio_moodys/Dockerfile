FROM rocker/tidyverse:3.4.4

ENV WORKON_HOME /opt/virtualenvs
ENV PYTHON_VENV_PATH $WORKON_HOME/r-tensorflow

## Set up a user modifyable python3 environment
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpython3-dev \
        python3-venv \
		unixodbc \
		unixodbc-dev \
		freetds-dev \
		tdsodbc \
		odbc-postgresql && \
    rm -rf /var/lib/apt/lists/*

ENV PATH=$PATH:/opt/TinyTeX/bin/x86_64-linux/

## Add LaTeX, rticles and bookdown support
RUN wget "https://travis-bin.yihui.name/texlive-local.deb" \
  && dpkg -i texlive-local.deb \
  && rm texlive-local.deb \
  && apt-get update \
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
 ## parallelization
    libzmq3-dev \
    libopenmpi-dev \
 && apt-get clean \
  && rm -rf /var/lib/apt/lists/ \
  ## Use tinytex for LaTeX installation
  && install2.r --error --repos 'https://cran.microsoft.com/snapshot/2019-10-15/' tinytex \
 ## Admin-based install of TinyTeX:
  && wget -qO- \
    "https://github.com/yihui/tinytex/raw/master/tools/install-unx.sh" | \
    sh -s - --admin --no-path \
  && mv ~/.TinyTeX /opt/TinyTeX \
  && /opt/TinyTeX/bin/*/tlmgr path add \
  && tlmgr install ae inconsolata listings metafont mfware parskip pdfcrop tex \
  && tlmgr path add \
  && Rscript -e "tinytex::r_texmf()" \
  && chown -R root:staff /opt/TinyTeX \
  && chown -R root:staff /usr/local/lib/R/site-library \
  && chmod -R g+w /opt/TinyTeX \
  && chmod -R g+wx /opt/TinyTeX/bin \
  && echo "PATH=${PATH}" >> /usr/local/lib/R/etc/Renviron \
  ## Currently (2017-06-06) need devel PKI for ssl issue: https://github.com/s-u/PKI/issues/19
  && install2.r --error --repos 'https://cran.microsoft.com/snapshot/2019-10-15/' PKI \
  ## And some nice R packages for publishing-related stuff
  && install2.r --error --deps TRUE --repos 'https://cran.microsoft.com/snapshot/2019-10-15/'\
    bookdown rticles rmdshower rJava    
	
RUN R -e "install.packages(c('odbc', 'RPostgreSQL', 'RODBC', 'latex2exp', 'ggpmisc', 'kableExtra'), dependencies=TRUE, repos='https://cran.microsoft.com/snapshot/2019-10-15/')"
RUN R -e "devtools::install_github('moodysanalytics/RCfun', auth_token = '1a55244800a087726373c7377346aa0c5083ff8f')"
RUN R -e "devtools::install_github('moodysanalytics/MAQRG-1', auth_token = '1a55244800a087726373c7377346aa0c5083ff8f')"
RUN R -e "update.packages(ask = F, repos = 'https://cran.microsoft.com/snapshot/2019-10-15/')"

RUN chown -R root:staff /opt/TinyTeX \
  && chown -R root:staff /usr/local/lib/R/site-library \
  && chmod -R g+w /opt/TinyTeX \
  && chmod -R g+wx /opt/TinyTeX/bin

RUN python3 -m venv ${PYTHON_VENV_PATH}

RUN chown -R rstudio:rstudio ${WORKON_HOME}
ENV PATH ${PYTHON_VENV_PATH}/bin:${PATH}
## And set ENV for R! It doesn't read from the environment...
RUN echo "PATH=${PATH}" >> /usr/local/lib/R/etc/Renviron && \
    echo "WORKON_HOME=${WORKON_HOME}" >> /usr/local/lib/R/etc/Renviron && \
    echo "RETICULATE_PYTHON_ENV=${PYTHON_VENV_PATH}" >> /usr/local/lib/R/etc/Renviron && \
    MRAN=https://mran.microsoft.com/snapshot/2019-10-15 && \
    echo MRAN=$MRAN >> /etc/environment && \
    export MRAN=$MRAN && \
    echo "options(repos = c(CRAN='$MRAN'), download.file.method = 'libcurl')" >> /usr/local/lib/R/etc/Rprofile.site
    
## Because reticulate hardwires these PATHs...
RUN ln -s ${PYTHON_VENV_PATH}/bin/pip /usr/local/bin/pip && \
    ln -s ${PYTHON_VENV_PATH}/bin/virtualenv /usr/local/bin/virtualenv

## install as user to avoid venv issues later
USER rstudio
RUN pip3 install \
    h5py==2.9.0 \
    pyyaml==3.13 \
    requests==2.21.0 \
    Pillow==5.4.1 \
    tensorflow==1.12.0 \
    tensorflow-probability==0.5.0 \
    keras==2.2.4 \
    --no-cache-dir
USER root
RUN install2.r --repos 'https://cran.microsoft.com/snapshot/2019-10-15/' reticulate tensorflow keras

## Not clear why tensorflow::install_tensorflow() fails (cant find /usr/local/bin/virtualenv). 
## keras::install_keras() cannot specify a custom envname

## Not clear how we control versions...
#RUN R -e "reticulate::py_install(c( \
#  'tensorflow', \ 
#  'tensorflow-probability', \
#  'keras'))"

###RUN R -e "tensorflow::install_tensorflow(version='cpu', extra_packages = c('keras'), envname='r-tensorflow')"

# https://hub.docker.com/r/rocker/ml/dockerfile
# Python Xgboost for CPU
USER rstudio
RUN pip3 --no-cache-dir install \
    xgboost==0.81 \
    wheel==0.33.0 \
    setuptools==40.8.0 \
    scipy==1.2.1
USER root

## Get Java (for h2o R package)
RUN apt-get update -qq \
  && apt-get -y --no-install-recommends install \
    cmake \
    default-jdk \
    default-jre \
  && R CMD javareconf

## h2o requires Java
RUN install2.r --repos 'https://cran.microsoft.com/snapshot/2019-10-15/' h2o
#RUN install2.r greta
#RUN installGithub.r greta-dev/greta
RUN R -e "devtools::install_github('greta-dev/greta')"
