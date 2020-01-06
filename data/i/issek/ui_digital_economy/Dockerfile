FROM rocker/shiny:3.5.1

RUN apt-get update && apt-get install libcurl4-openssl-dev libv8-3.14-dev  libxml2-dev libssl-dev libssh2-1-dev libpq-dev zlib1g-dev  -y &&\
  mkdir -p /var/lib/shiny-server/bookmarks/shiny

# Download and install library
RUN R -e "install.packages(c('shinydashboard', 'shinyjs', 'V8', 'ggthemes','ggiraph','xml2','data.table','shinythemes', 'plotly', 'shiny', 'ggplot2', 'magrittr', 'foreign', 'shinyLP', 'RPostgreSQL', 'highcharter','networkD3' ))"
RUN R -e "install.packages(c('leaflet' ))"
RUN R -e "install.packages(c('DT' ))"
RUN R -e "install.packages(c('shinyalert' ))"
# copy the app to the image COPY shinyapps /srv/shiny-server/
COPY . /srv/shiny-server/
COPY wos_colors /home/ 
# make all app files readable (solves issue when dev in Windows, but building in Ubuntu)
RUN chmod -R 777 /srv/shiny-server/

EXPOSE 3838

CMD ["/usr/bin/shiny-server.sh"] 

