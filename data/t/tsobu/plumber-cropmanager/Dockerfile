FROM rocker/r-ver:3.5.1
#FROM rocker/tidyverse:3.5.1
#FROM rocker/tidyverse:latest
#FROM r-base:3.5.1

ENV CROP_USER akilimo
ENV CROP_GROUP akilimo

# Add jdk 8 runtime
#RUN apt-get update && \
#    apt-get install -y openjdk-8-jdk && \
#    apt-get install -y ant && \
#    apt-get clean;

# update some packages, including sodium and apache2, then clean
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    openjdk-8-jdk \
    file \
    libcurl4-openssl-dev \
    libedit2 \
    libssl-dev \
    lsb-release \
    libxml2-dev \
    libpq-dev \
    libpng-dev \
    libssh2-1-dev \
    libudunits2-dev \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    ca-certificates \
    libglib2.0-0 \
	libxext6 \
	libsm6  \
	libxrender1 \
	bzip2 \
	libsodium-dev \
	libcairo2-dev \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/


# Add a non-root user who will launch the apps

RUN useradd $CROP_USER \
	&& mkdir /home/$CROP_USER \
	&& mkdir /home/$CROP_USER/projects \
	&& chown $CROP_USER:$CROP_USER /home/$CROP_USER \
	&& addgroup $CROP_USER $CROP_USER

# copy the setup script, run it, then delete it
COPY setup.R /
RUN Rscript setup.R && rm setup.R

# copy all the other R files.
#COPY akilimo_recommendation /akilimo_recommendation

#Plumb your app into 8000
EXPOSE 8000
WORKDIR /home/akilimo/projects/akilimo_recommendation
#ENTRYPOINT ["Rscript","main.R"]
ENTRYPOINT ["Rscript","main-bleed.R"]
