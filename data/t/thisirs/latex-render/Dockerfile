FROM debian:sid-slim
MAINTAINER Sylvain Rousseau <thisirs@gmail.com>

# Recreate non-existent directories
RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2 /usr/share/man/man3 /usr/share/man/man4 /usr/share/man/man5 /usr/share/man/man6 /usr/share/man/man7 /usr/share/man/man8

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        texlive-full \
        biber \
        fonts-opendyslexic \
        fonts-texgyre

# Installing pip and python-legacy modules
RUN apt-get install -y --no-install-recommends \
        python-pygments \
        python-matplotlib \
        python-numpy \
        python-scipy \
        python-pip \
        python3-pip

# Python 3 utils
RUN pip3 install \
        pygments \
        matplotlib \
        numpy \
        scipy

RUN apt-get install -y --no-install-recommends \
        git \
        make \
        gcc \
        libc6-dev \
        g++

RUN apt-get install -y --no-install-recommends r-base
RUN Rscript -e "install.packages(c('knitr', 'reticulate', 'xtable'))"
RUN apt-get install -y libpython3-dev

RUN apt-get install -y --no-install-recommends \
        default-jre \
        plantuml \
        graphviz

# Locale
RUN apt-get install -y locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen
RUN dpkg-reconfigure -fnoninteractive locales
ENV LANG en_US.UTF-8

# Slim down image
RUN apt-get --purge -y remove tex.\*-doc$
RUN apt-get --purge -y remove texlive-fonts-extra
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
