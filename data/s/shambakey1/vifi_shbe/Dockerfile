FROM continuumio/miniconda3

# Part of this file is copied from Dockerfile at https://hub.docker.com/r/nrel/energyplus/~/dockerfile/

# This is not ideal. The tarballs are not named nicely and EnergyPlus versioning is strange
ENV ENERGYPLUS_VERSION 8.7.0
ENV ENERGYPLUS_TAG v8.7.0
ENV ENERGYPLUS_SHA 78a111df4a

# This should be x.y.z, but EnergyPlus convention is x-y-z
ENV ENERGYPLUS_INSTALL_VERSION 8-7-0

# Downloading from Github
# e.g. https://github.com/NREL/EnergyPlus/releases/download/v8.3.0/EnergyPlus-8.3.0-6d97d074ea-Linux-x86_64.sh
ENV ENERGYPLUS_DOWNLOAD_BASE_URL https://github.com/NREL/EnergyPlus/releases/download/$ENERGYPLUS_TAG
ENV ENERGYPLUS_DOWNLOAD_FILENAME EnergyPlus-$ENERGYPLUS_VERSION-$ENERGYPLUS_SHA-Linux-x86_64.sh
ENV ENERGYPLUS_DOWNLOAD_URL $ENERGYPLUS_DOWNLOAD_BASE_URL/$ENERGYPLUS_DOWNLOAD_FILENAME

# Collapse the update of packages, download and installation into one command
# to make the container smaller & remove a bunch of the auxiliary apps/files
# that are not needed in the container
RUN apt-get update --fix-missing && apt-get install -y libgl1-mesa-glx && apt-get install -y ca-certificates curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -SLO $ENERGYPLUS_DOWNLOAD_URL \
    && chmod +x $ENERGYPLUS_DOWNLOAD_FILENAME \
    && echo "y\r" | ./$ENERGYPLUS_DOWNLOAD_FILENAME \
    && rm $ENERGYPLUS_DOWNLOAD_FILENAME \
    && cd /usr/local/EnergyPlus-$ENERGYPLUS_INSTALL_VERSION \
    && rm -rf DataSets Documentation ExampleFiles WeatherData MacroDataSets PostProcess/convertESOMTRpgm \
    PostProcess/EP-Compare PreProcess/FMUParser PreProcess/ParametricPreProcessor PreProcess/IDFVersionUpdater \
    && conda install -y python pyyaml pandas pip \
    && conda clean -y --all \
    && pip install eppy

# Remove the broken symlinks
RUN cd /usr/local/bin \
    && find -L . -type l -delete
    
