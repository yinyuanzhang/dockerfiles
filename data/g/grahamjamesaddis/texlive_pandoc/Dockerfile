FROM ubuntu
LABEL maintainer="Graham.Addis@ndm.ox.ac.uk"
MAINTAINER Graham.Addis@ndm.ox.ac.uk
# credit to Erik Schilling for portions of the setup,
# See https://github.com/Ablu/docker-ubuntu-texlive-full

# Caveat: I reserve the right to change the packages at will, this is a work in progress.

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        texlive-full \
        make \
        imagemagick \
        inkscape \
        latexmk \
        locales \
        aspell \
        pandoc \
        pandoc-citeproc \
        python-pip \
   && pip install pandocfilters \
   && pip install pandoc-fignos
