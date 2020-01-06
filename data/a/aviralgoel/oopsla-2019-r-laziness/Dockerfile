################################################################################
## https://hub.docker.com/_/debian/
################################################################################
FROM debian:buster

################################################################################
## Upgrade
################################################################################
RUN apt-get update
RUN apt-get -y dist-upgrade

################################################################################
## Miscellaneous
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install sudo apt-utils

################################################################################
## Locale
## https://hub.docker.com/_/debian/
## https://github.com/docker-library/postgres/blob/69bc540ecfffecce72d49fa7e4a46680350037f9/9.6/Dockerfile#L21-L24
## http://jaredmarkell.com/docker-and-locales/
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install locales
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen en_US.UTF-8
RUN /usr/sbin/update-locale LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

################################################################################
## Shell
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install fish bash zsh

################################################################################
## Editor
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install vim emacs

################################################################################
## Version Control
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install git subversion

################################################################################
## Data Transfer
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install curl wget rsync

################################################################################
## Process Monitoring
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install procps htop

################################################################################
## Latex
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install texinfo texlive texlive-fonts-extra libcairo2-dev libtiff-dev

################################################################################
## R Base
## https://cran.r-project.org/bin/linux/debian/
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install r-base r-base-dev

################################################################################
## R Package Dependencies
################################################################################
#git2r
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install libgit2-dev
#httr
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install libssl-dev
#xml2
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install libxml2-dev
#curl
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install libcurl4-openssl-dev
#rJava
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install openjdk-11-jdk default-jdk
#RMySQL
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install default-libmysqlclient-dev
#RSQLite
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install libsqlite3-dev
#odbc
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install unixodbc-dev
#rgl
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install freeglut3-dev libfreetype6-dev
# promise-dyntracing-experiment
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install xvfb expect libzstd-dev time tree pandoc xfonts-100dpi xfonts-75dpi
# latest version of GNU parallel
RUN curl -L https://bit.ly/install-gnu-parallel | sh -x

################################################################################
## Web Server
## https://www.linkedin.com/pulse/serve-static-files-from-docker-via-nginx-basic-example-arun-kumar
################################################################################
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install nginx
RUN rm -v /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/
ADD paper.pdf /var/www/
ADD small.html /var/www/
COPY small_files /var/www/small_files
ADD large.html /var/www/
COPY large_files /var/www/large_files

################################################################################
## User
################################################################################
RUN useradd -ms /bin/bash -G sudo aviral
RUN echo "aviral:aviral" | chpasswd
RUN echo "aviral ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER aviral
WORKDIR /home/aviral
RUN mkdir -p /home/aviral/library
ENV R_LIBS_USER /home/aviral/library
ENV R_KEEP_PKG_SOURCE 1
ENV R_ENABLE_JIT 0
ENV R_COMPILE_PKGS 0
ENV R_DISABLE_BYTECODE 1
ENV OMP_NUM_THREADS 1

################################################################################
## R-dyntrace
################################################################################
RUN git clone --branch oopsla-2019-study-of-laziness-v1 https://github.com/PRL-PRG/R-dyntrace.git
RUN cd R-dyntrace && ./build

################################################################################
## promisedyntracer
################################################################################
RUN git clone --branch oopsla-2019-study-of-laziness-v1 https://github.com/aviralg/promisedyntracer.git
RUN cd promisedyntracer && make

################################################################################
## promise-dyntracing-experiment
################################################################################
RUN git clone --branch r-3.5.0 https://github.com/PRL-PRG/promise-dyntracing-experiment.git
RUN cd promise-dyntracing-experiment && xvfb-run make install-dependencies DEPENDENCIES_FILEPATH=scripts/package-dependencies.txt && rm -rf *.out

ADD entrypoint.sh /home/aviral/
ENTRYPOINT ["/home/aviral/entrypoint.sh"]
