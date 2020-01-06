FROM openanalytics/r-base

MAINTAINER Maxim Nazarov <maxim.nazarov@openanalytics.eu>

RUN apt-get update && apt-get install -y \
          sudo \
          gdebi-core \
          libcurl4-gnutls-dev \
          libcairo2-dev \
          libxt-dev \
          libssl-dev \
          libssh2-1-dev \
          tk-dev \
          libssl1.0.0 \ 
          libxml2-dev

RUN wget https://github.com/jgm/pandoc/releases/download/1.17.2/pandoc-1.17.2-1-amd64.deb
RUN dpkg -i pandoc-1.17.2-1-amd64.deb 

RUN R -e "install.packages(c('shiny', 'rmarkdown', 'flexdashboard', 'rlist', 'highcharter', 'dplyr', 'viridisLite', 'forecast', 'treemap', 'arules'), repos='https://cloud.r-project.org')"

WORKDIR /root/

COPY testflex testflex/

COPY Rprofile.site /usr/lib/R/etc/

EXPOSE 3838

ENTRYPOINT ["R", "-e"]