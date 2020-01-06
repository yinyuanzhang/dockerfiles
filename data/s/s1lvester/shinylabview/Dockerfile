FROM r-base:latest

MAINTAINER Winston Chang "winston@rstudio.com"
# modified by Markus Bockhacker "hello@s1lvester.de" for study-project # "shinyLabView"

RUN apt-get update && apt-get install -y -t unstable \
    sudo \
    gdebi-core \
    pandoc \
    libssl-dev \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev/unstable \
    libxt-dev && \
    wget --no-verbose https://download3.rstudio.org/ubuntu-14.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    R -e "install.packages(c('shiny', \
                             'rmarkdown', \
                             'flexdashboard', \
                             'dplyr', \
                             'lubridate', \
                             'DT', \
                             'scales', \
                             'ggplot2', \
                             'plotly'), \
                             repos='https://cran.rstudio.com/')" && \
    cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /srv/shiny-server/manual_files

EXPOSE 3838

COPY shiny-server.sh /usr/bin/shiny-server.sh

COPY shiny-customized.config /etc/shiny-server/shiny-server.conf

RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/flexdashboard.Rmd -O /srv/shiny-server/index.Rmd
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/labData.csv -O /srv/shiny-server/labData.csv
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/labData.csv -O /srv/shiny-server/labData-Tests.csv
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/labData.csv -O /srv/shiny-server/labData-Tests-norm.csv
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/patientData.csv -O /srv/shiny-server/patientData.csv
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/normValues.csv -O /srv/shiny-server/normValues.csv
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual.htm -O /srv/shiny-server/manual.htm
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual_files/image1.jpg -O /srv/shiny-server/manual_files/image1.jpg
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual_files/image2.png -O /srv/shiny-server/manual_files/image2.png
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual_files/image3.png -O /srv/shiny-server/manual_files/image3.png
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual_files/image4.png -O /srv/shiny-server/manual_files/image4.png
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual_files/image5.png -O /srv/shiny-server/manual_files/image5.png
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual_files/image6.png -O /srv/shiny-server/manual_files/image6.png
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual_files/image7.png -O /srv/shiny-server/manual_files/image7.png
RUN wget https://raw.githubusercontent.com/s1lvester/shinyLabView/master/shinyLabView/manual_files/image8.png -O /srv/shiny-server/manual_files/image8.png

CMD ["/usr/bin/shiny-server.sh"]

