# Galaxy - BLAST+ suite
#
# VERSION       0.1

FROM bgruening/galaxy-stable:16.07

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND NCBI BLAST+ Suite

# Install deepTools
ADD blast_tools.yml $GALAXY_ROOT/tools.yaml
RUN install-tools $GALAXY_ROOT/tools.yaml
RUN apt-get install nodejs
RUN apt-get install npm
RUN npm install -g npm
RUN npm install -g n
RUN n stable
