FROM ubuntu:xenial-20190515

###############################################################################
## Set up core infrastructure that supports the environments built in later
## stages
###############################################################################

# install system dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y --no-install-recommends apt-utils \
    && apt-get install -y --no-install-recommends build-essential \
    && apt-get install -y --no-install-recommends software-properties-common \
    && apt-get install -y --no-install-recommends apt-transport-https \
    && apt-get install -y --no-install-recommends wget \
    && apt-get install -y --no-install-recommends curl \
    && apt-get install -y --no-install-recommends git \
    && apt-get install -y --no-install-recommends jq \
    && apt-get install -y --no-install-recommends libcurl4-openssl-dev \
    && apt-get install -y --no-install-recommends libssl-dev \
    && apt-get install -y --no-install-recommends psmisc \
    && apt-get install -y --no-install-recommends sudo \
    && apt-get install -y --no-install-recommends wget \
    && apt-get install -y --no-install-recommends libclang-dev \
    && apt-get install -y --no-install-recommends s3fs \
    && apt-get install -y --no-install-recommends font-manager

# install conda
RUN mkdir /usr/local/bin/conda_download \
    && mkdir ~/.conda \
    && cd /usr/local/bin/conda_download \
    && wget https://repo.continuum.io/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh \
    && bash Miniconda3-4.7.10-Linux-x86_64.sh -b -p /opt/conda \
    && rm Miniconda3-4.7.10-Linux-x86_64.sh
ENV PATH="/opt/conda/bin:${PATH}"

# install RStudio
RUN wget -q "http://download2.rstudio.org/server/trusty/amd64/rstudio-server-1.2.1335-amd64.deb" \
    && dpkg -i rstudio-server-*-amd64.deb \
    && rm rstudio-server-*-amd64.deb

# Clean up APT when done (smaller image size)
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install base python dependencies (used outside of any specific conda env)
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install jupyter \
    && python3 -m pip install jupytext \
    && python3 -m pip install ipykernel \
    && python3 -m pip install awscli

# create directory for conda environment setup files
RUN mkdir /usr/local/bin/FertigComputeEnvironments

###############################################################################
## Build base conda environments, only copy core build scripts so that this
## section is run as little as possible. This is by far the longest-running
## and largest-image-producing section
###############################################################################

## R_3_5
COPY R_3_5/build_base.sh /usr/local/bin/FertigComputeEnvironments/R_3_5/build_base.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/R_3_5/ \
    && chmod +x build_base.sh && ./build_base.sh

## Python_3_6
COPY Python_3_6/build_base.sh /usr/local/bin/FertigComputeEnvironments/Python_3_6/build_base.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/Python_3_6/ \
    && chmod +x build_base.sh && ./build_base.sh

## R_3_6
COPY R_3_6/build_base.sh /usr/local/bin/FertigComputeEnvironments/R_3_6/build_base.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/R_3_6/ \
    && chmod +x build_base.sh && ./build_base.sh

## Python_3_7
COPY Python_3_7/build_base.sh /usr/local/bin/FertigComputeEnvironments/Python_3_7/build_base.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/Python_3_7/ \
    && chmod +x build_base.sh && ./build_base.sh

###############################################################################
## Install a Jupyter kernel inside each environment. This enables the Jupyter
## notebooks to find each environment.
###############################################################################

## R_3_5
COPY R_3_5/install.sh /usr/local/bin/FertigComputeEnvironments/R_3_5/install.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/R_3_5/ \
    && chmod +x install.sh && ./install.sh

## Python_3_6
COPY Python_3_6/install.sh /usr/local/bin/FertigComputeEnvironments/Python_3_6/install.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/Python_3_6/ \
    && chmod +x install.sh && ./install.sh

## R_3_6
COPY R_3_6/install.sh /usr/local/bin/FertigComputeEnvironments/R_3_6/install.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/R_3_6/ \
    && chmod +x install.sh && ./install.sh

## Python_3_7
COPY Python_3_7/install.sh /usr/local/bin/FertigComputeEnvironments/Python_3_7/install.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/Python_3_7/ \
    && chmod +x install.sh && ./install.sh

###############################################################################
## Install any core packages that are not part of the base conda environment.
## These package are installed by Python and R, any conda packages should
## installed in the first step.
###############################################################################

## R_3_5
COPY R_3_5/build_additional.sh /usr/local/bin/FertigComputeEnvironments/R_3_5/build_additional.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/R_3_5/ \
    && chmod +x build_additional.sh && ./build_additional.sh

## Python_3_6
COPY Python_3_6/build_additional.sh /usr/local/bin/FertigComputeEnvironments/Python_3_6/build_additional.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/Python_3_6/ \
    && chmod +x build_additional.sh && ./build_additional.sh

## R_3_6
COPY R_3_6/build_additional.sh /usr/local/bin/FertigComputeEnvironments/R_3_6/build_additional.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/R_3_6/ \
    && chmod +x build_additional.sh && ./build_additional.sh

## Python_3_7
COPY Python_3_7/build_additional.sh /usr/local/bin/FertigComputeEnvironments/Python_3_7/build_additional.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/Python_3_7/ \
    && chmod +x build_additional.sh && ./build_additional.sh

###############################################################################
## Additional configuration steps
###############################################################################

# create user home directory
RUN mkdir /home/fertigcompute

# set up user for RStudio
RUN useradd rstudio \
    && echo "rstudio:rstudio" | chpasswd \
    && chown rstudio:rstudio /home/fertigcompute
RUN usermod -d /home/fertigcompute rstudio

# set R_HOME in python environments that use rpy2
COPY fix_paths.sh /usr/local/bin/fix_paths.sh
RUN cd /usr/local/bin/ && chmod +x fix_paths.sh && ./fix_paths.sh

# copy and install fertigaws package in Python environments
COPY fertigaws/ /usr/local/bin/fertigaws/
RUN ["/bin/bash", "-c", "                   \
    cd /usr/local/bin/fertigaws             \
    && eval \"$(conda shell.bash hook)\"    \
    && conda activate Fertig_Python_3_6     \
    && pip install .                        \
    && conda deactivate                     \
    && conda activate Fertig_Python_3_7     \
    && pip install .                        \
    && conda deactivate                     \
"]

###############################################################################
## Configure the driver script and entry point for the environments
###############################################################################

COPY driver.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/driver.sh
CMD ["/usr/local/bin/driver.sh"]

###############################################################################
## Pull the latest versions of packages which are kept up to date with
## active development. Packages here should pull from a specified git commit
## hash. This hash may be updated often. For this reason, the packages are
## built at the end of the Dockerfile.
###############################################################################

COPY R_3_5/pull_latest.sh /usr/local/bin/FertigComputeEnvironments/R_3_5/pull_latest.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/R_3_5/ \
    && chmod +x pull_latest.sh && ./pull_latest.sh

COPY R_3_6/pull_latest.sh /usr/local/bin/FertigComputeEnvironments/R_3_6/pull_latest.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/R_3_6/ \
    && chmod +x pull_latest.sh && ./pull_latest.sh

COPY Python_3_6/pull_latest.sh /usr/local/bin/FertigComputeEnvironments/Python_3_6/pull_latest.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/Python_3_6/ \
    && chmod +x pull_latest.sh && ./pull_latest.sh

COPY Python_3_7/pull_latest.sh /usr/local/bin/FertigComputeEnvironments/Python_3_7/pull_latest.sh
RUN cd /usr/local/bin/FertigComputeEnvironments/Python_3_7/ \
    && chmod +x pull_latest.sh && ./pull_latest.sh



