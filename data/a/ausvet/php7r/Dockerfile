FROM ausvet/php7:latest
# ausvet/php7 extends php:7-apache-stretch

LABEL maintainer="ausvet <support@ausvet.com.au>"

ENV GPG_KEY 'E19F5F87128899B192B1A2C2AD5F960A256A04AF'
# Install R
RUN apt-get update || (rm -Rf /var/lib/apt/lists/* && apt-get update)
RUN apt-get install -y dirmngr --install-recommends && \
    apt-get install -y software-properties-common && \
    apt-get install -y apt-transport-https 
RUN (apt-key adv --keyserver keys.gnupg.net --recv-key "${GPG_KEY}" || \
    apt-key adv --keyserver hkp://keys.gnupg.net:80 --recv-key "${GPG_KEY}" || \
    apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-key "${GPG_KEY}" || \
    apt-key adv --keyserver pool.sks-keyservers.net --recv-key "${GPG_KEY}" )
# RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 'E19F5F87128899B192B1A2C2AD5F960A256A04AF'
RUN add-apt-repository 'deb https://cloud.r-project.org/bin/linux/debian stretch-cran35/' && \
    apt-get update && \
    apt-get install -y r-base

# install cairo and plotly dependencies
RUN apt-get install -y \
    libcairo2-dev \
    libxt-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev

# install R packages first to avoid reliving this pain unless you need to
ADD ./packages.r /packages.r
RUN Rscript /packages.r

CMD /bin/bash
