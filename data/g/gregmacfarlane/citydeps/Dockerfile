####### BUILD STAGE 0
# Using a multi-stage build to protect the GITHUB_PAT key from being visible
# inside the image
FROM rocker/geospatial:3.6.2 as builder
MAINTAINER "Josie Kressner" josie@transportfoundry.com

# System libraries ------------------
# Add stretch-backports to be able to install Java 11
RUN echo "deb http://deb.debian.org/debian stretch-backports main" | tee -a /etc/apt/sources.list
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    p7zip-full \
    curl \
    gnupg \
    awscli \
    gdal-bin \
    python3-dev \
    python3-pip

RUN apt-get install -y --no-install-recommends \
  osmosis \
  osmctools \
  cmake

# citycastsim ----------------------
RUN pip3 install setuptools numpy==1.18.0 pandas==0.25.3 simpy==3.0.10
# Doppelganger dependencies
RUN pip3 install cvxpy==0.4.8 enum34==1.1.6 future==0.16.0 pomegranate==0.12.0
RUN pip3 install psycopg2==2.7.4 requests==2.12.4 six==1.10.0
RUN pip3 install wheel
RUN pip3 install doppelganger==0.1.4

# citycastr -------------------------
# Install required packages not yet available on geospatial rocker
RUN R -e "devtools::install_version('logging', version = '0.10-108', type = 'source')"
RUN R -e "devtools::install_version('pscl', version = '1.5.2', type = 'source')"
RUN R -e "devtools::install_version('RPostgres', version = '1.2.0', type = 'source')"
RUN R -e "devtools::install_version('tidycensus', version = '0.9.2', type = 'source')"
RUN R -e "devtools::install_version('tigris', version = '0.8.2', type = 'source')"
RUN R -e "devtools::install_version('aws.ec2metadata', version = '0.2.0', type = 'source')"

# citycastgtn -------------------------
RUN R -e "install.packages('geojsonio')" # v0.8.0
RUN R -e "devtools::install_version('jsonvalidate', version = '1.1.0', type = 'source')"
