FROM ubuntu:14.04.5
MAINTAINER cannin

# UBUNTU
## Update Ubuntu and add extra repositories
RUN apt-get -y update && apt-get -y upgrade

# Install basic commands
RUN apt-get -y install links nano curl wget fontconfig make inkscape
#RUN apt-get install -y \
#    texlive-latex-base texlive-xetex latex-xcolor texlive-math-extra \
#    texlive-latex-extra texlive-fonts-extra

# INSTALL TEXLIVE 2015
# NOTE: https://github.com/scottkosty/install-tl-ubuntu
RUN wget https://github.com/scottkosty/install-tl-ubuntu/raw/master/install-tl-ubuntu
RUN chmod +x ./install-tl-ubuntu
RUN ./install-tl-ubuntu

# INSTALL INKSCAPE
RUN apt-get install -y --no-install-recommends inkscape

# Necessary to get the PATH sourced
#RUN source /etc/environment
