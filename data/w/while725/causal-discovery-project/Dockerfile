# Use rocker/r-ver as the base image
# This will inherit everyhing that was installed into base image already
# Documented at https://hub.docker.com/r/rocker/r-ver/~/dockerfile/
FROM ubuntu:18.04

# Configure file path
RUN mkdir /root/my-project
VOLUME /root/my-project
WORKDIR /root/my-project

# make sure the system is fully updated
RUN apt-get update && apt-get -y upgrade

# install the default GCC toolchain
RUN apt-get install -y build-essential

# a few prerequisites for building Python
RUN apt-get install -y libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev
RUN apt-get install -y libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev

RUN apt-get install -y wget
RUN wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz \
	&& tar xf Python-3.7.1.tar.xz && rm Python-3.7.1.tar.xz \
	&& cd Python-3.7.1 \
	&& ./configure --enable-optimizations \
	&& make -j 8 \
	&& make altinstall

RUN apt-get install -y apt-transport-https software-properties-common

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
	&& add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' \
	&& apt-get update \
	&& apt-get install -y r-base

RUN apt-get install -y default-jre
RUN apt-get install -y default-jdk
RUN R CMD javareconf

# Install R packages
# Install any dependencies required for the R packages
RUN apt-get update   \
    && apt-get install -y --no-install-recommends   libxml2-dev   libcurl4-openssl-dev   libssl-dev   libv8-3.14-dev

# Install lavaan dependencies
RUN apt-get install -y gfortran

RUN apt-get update   \
    && apt-get -y upgrade

# Install the R Packages from CRAN
RUN Rscript -e 'install.packages("BiocManager"); BiocManager::install(c("RBGL", "graph"), update=FALSE)'

RUN Rscript -e 'install.packages(c("pcalg", "CAM", "bnlearn"))'


# GPArotation
RUN Rscript -e 'packageurl <- "https://cran.r-project.org/src/contrib/GPArotation_2014.11-1.tar.gz"; install.packages(packageurl, repos=NULL, type="source")'

# lavaan
RUN Rscript -e 'install.packages(c("mnormt", "pbivnorm", "numDeriv")); packageurl <- "https://cran.r-project.org/src/contrib/lavaan_0.6-3.tar.gz"; install.packages(packageurl, repos=NULL, type="source")'


# semTools
RUN Rscript -e 'packageurl <- "https://cran.r-project.org/src/contrib/semTools_0.5-1.tar.gz"; install.packages(packageurl, repos=NULL, type="source")'	


# Python associated packages
# Adds metadata to the image as a key value pair example 
LABEL version="1.0"
LABEL maintainer="Wu Yu <while725@live.com>"

# Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get install -y vim

# Copying requirements.txt file
COPY requirements.txt requirements.txt

# pip install 
RUN pip3.7 install --no-cache -r requirements.txt
ENV PYTHONPATH=$PYTHONPATH:/root/my-project

# more packages
RUN Rscript -e 'install.packages(c("devtools", "psych", "doParallel", "stringr", "rJava"))'

# github repos
RUN Rscript -e 'library(devtools); install_github("bd2kccd/r-causal")'

RUN Rscript -e 'library(devtools); install_github("while519/latent-variable-models", ref = "develop", subdir="factortools")'

# add more commands here
# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \
	&& ln -s python3.7 python \
	&& ln -s pip3.7 pip

# Copying requirements_update.txt file
COPY requirements_update.txt requirements1.txt
RUN pip install --no-cache -r requirements1.txt

RUN Rscript -e 'install.packages(c("SCCI", "polychor", "sparsebn", "MASS"))'

# Exposing ports
EXPOSE 8888

# Running jupyter notebook
# --NotebookApp.token ='demo' is the password
# CMD ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token='demo'"]

COPY commands.sh /root/commands.sh
RUN ["chmod", "+x", "/root/commands.sh"]
ENTRYPOINT ["/root/commands.sh"]