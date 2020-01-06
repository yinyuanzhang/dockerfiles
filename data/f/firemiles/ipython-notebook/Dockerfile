FROM jupyter/notebook
MAINTAINER firemilesxu@gmail.com firemiles

# install package nessary
RUN apt-get update && \
    apt-get install -yq --no-install-recommends libpng12-dev libfreetype6-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install extend package
RUN pip2 install --no-cache-dir numpy matplotlib && \
    pip3 install --no-cache-dir numpy matplotlib
