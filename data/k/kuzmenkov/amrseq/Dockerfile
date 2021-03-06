FROM kuzmenkov/docker-baseimage:latest

#Installation of nesesary package/software for this containers...
RUN echo "deb http://archive.ubuntu.com/ubuntu `cat /etc/container_environment/DISTRIB_CODENAME`-backports main restricted universe" >> /etc/apt/sources.list
RUN (echo "deb http://cran.mtu.edu/bin/linux/ubuntu `cat /etc/container_environment/DISTRIB_CODENAME`/" >> /etc/apt/sources.list && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9)

## Install some useful tools and dependencies for MRO
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	ca-certificates \
	curl \
        wget \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /home/docker
# Download, valiate, and unpack
RUN wget https://www.dropbox.com/s/uz4e4d0frk21cvn/microsoft-r-open-3.5.1.tar.gz?dl=1 -O microsoft-r-open-3.5.1.tar.gz \
&& echo "9791AAFB94844544930A1D896F2BF1404205DBF2EC059C51AE75EBB3A31B3792 microsoft-r-open-3.5.1.tar.gz" > checksum.txt \
	&& sha256sum -c --strict checksum.txt \
	&& tar -xf microsoft-r-open-3.5.1.tar.gz \
	&& cd /home/docker/microsoft-r-open \
	&& ./install.sh -a -u \
	&& ls logs && cat logs/*


# Clean up
WORKDIR /home/docker
RUN rm microsoft-r-open-3.5.1.tar.gz \
	&& rm checksum.txt \
&& rm -r microsoft-r-open


# system libraries of general use
RUN apt-get update && apt-get install -y \
    sudo \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    libssl-dev \
    libssh2-1-dev \
    libssl1.0.0 \
    libxml2-dev \
    libssl-dev \
    cron

# system library dependency for the euler app
RUN apt-get update && apt-get install -y \
    libmpfr-dev \
    gfortran \
    aptitude \
    libgdal-dev \
    libproj-dev \
    g++ \
    gdebi-core\
    libicu-dev \
    libpcre3-dev\
    libbz2-dev \
    liblzma-dev \
    libnlopt-dev \
    build-essential \
    libhiredis-dev


RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
RUN apt-get update
RUN apt-get install -y libudunits2-dev libgdal-dev libgeos-dev 


RUN sudo apt-add-repository -y ppa:webupd8team/java \
&& apt-get update && echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | sudo debconf-set-selections && apt-get install -y oracle-java8-installer \
&& R -e "Sys.setenv(JAVA_HOME = '/usr/lib/jvm/java-8-oracle/jre')"
RUN sudo java -version
#COPY Makeconf /usr/lib64/microsoft-r/3.4/lib64/R/etc/Makeconf

#wget https://www.dropbox.com/s/hl0vx1f6rpfgxrx/shiny-server-1.5.3.838-amd64.deb?dl=1 -O shiny-server-1.5.3.838-amd64.deb

RUN wget https://www.dropbox.com/s/8v07th1mur5m91n/shiny-server-1.5.9.923-amd64.deb?dl=1 -O shiny-server-1.5.9.923-amd64.deb \
&& dpkg -i --force-depends shiny-server-1.5.9.923-amd64.deb \
          && rm shiny-server-1.5.9.923-amd64.deb && \
    R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cran.rstudio.com/')" \
          && mkdir -p /srv/shiny-server; sync  \
          && mkdir -p  /srv/shiny-server/examples; sync  
   # && rm -rf /var/lib/apt/lists/*

#COPY Makeconf /usr/lib64/microsoft-r/3.3/lib64/R/etc/Makeconf

RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

##Adding Deamons to containers
RUN mkdir /etc/service/shiny-server /var/log/shiny-server ; sync 
COPY shiny-server.sh /etc/service/shiny-server/run
RUN chmod +x /etc/service/shiny-server/run  \
    && cp /var/log/cron/config /var/log/shiny-server/ \
    && chown -R shiny /var/log/shiny-server \
    && sed -i '113 a <h2><a href="./examples/">Other examples of Shiny application</a> </h2>' /srv/shiny-server/index.html



# basic shiny functionality
RUN apt-get install -y ncbi-blast+ \
&& R -e "install.packages('curl', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('httr', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('devtools', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('htmlwidgets', repos='https://cran.r-project.org/')" \
&& R -e "source('https://bioconductor.org/biocLite.R'); biocLite(); biocLite('Biostrings'); biocLite('GenomicRanges')" \
&& sudo su - -c "R -e \"install.packages('miniUI', repos='https://cran.r-project.org/');options(unzip = 'internal'); devtools::install_github('daattali/shinyjs')\"" \
&& R -e "install.packages('crosstalk', repos='https://cran.r-project.org/')" \
&& sudo su - -c "R -e \"options(unzip = 'internal'); devtools::install_github('rstudio/DT')\"" \
&& sudo su - -c "R -e \"options(unzip = 'internal'); devtools::install_github('kuzmenkov111/rBLAST')\"" \
&& R -e "install.packages('data.table', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('future', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('stringi', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('shinythemes', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('fst', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('msaR', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('shinyWidgets', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('shinyjqui', repos='https://cran.r-project.org/')"  \
&& R -e "install.packages('shinycssloaders', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('dplyr', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('RColorBrewer', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('stringr', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('ggplot2', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('ggrepel', repos='https://cran.r-project.org/')" \
&& sudo su - -c "R -e \"options(unzip = 'internal'); devtools::install_github('ropensci/plotly')\""\
&& sudo su - -c "R -e \"options(unzip = 'internal'); devtools::install_github('stefanedwards/lemon')\""\
&& sudo su - -c "R -e \"options(unzip = 'internal'); devtools::install_github('kuzmenkov111/highcharter')\""\
&& R -e "install.packages('shinyjqui', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('fs', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('gggenes', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('cronR', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('promises', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('ipc', repos='https://cran.r-project.org/')" \
&& R CMD javareconf \
&& R -e "Sys.setenv(JAVA_HOME = '/usr/lib/jvm/java-8-oracle/jre'); install.packages('rJava', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('mailR', repos='https://cran.r-project.org/')" \
&& R -e "install.packages('curl', repos='https://cran.r-project.org/')" \
&& sudo su - -c "R -e \"options(unzip = 'internal'); devtools::install_github('AdeelK93/collapsibleTree'); devtools::install_github('emitanaka/shinycustomloader')\"" 




#COPY shiny-server.conf /etc/init/shiny-server.conf
RUN mkdir /var/lib/shiny-server/bookmarks \
 && chown -R shiny:shiny /var/lib/shiny-server/bookmarks
 
#volume for Shiny Apps and static assets. Here is the folder for index.html(link) and sample apps.
VOLUME /srv/shiny-server
EXPOSE 3838



CMD ["/sbin/my_init"]
