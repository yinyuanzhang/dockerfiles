FROM rocker/shiny-verse:3.5.1

LABEL author="Joseph Sayler" email="josephs@axioresearch.com" company="Axio Research" version="1.2" maintainer="Joseph Sayler <josephs@axioresearch.com>"

RUN Rscript -e "install.packages(c('ggplot2','Cairo','shiny','DBI','RSQLite','plotly','manhattanly','data.table','hexbin','webshot','shinyBS','htmlwidgets','DT','shinyhelper','dbplyr','shinydashboard','shinyjs','gtools','ggvis','gridExtra','magrittr','plumber','shinycssloaders','shinyWidgets','crayon'))" \
  && Rscript -e "devtools::install_github('jjsayleraxio/AxioLocusZoom@v0.1.4-alpha')" \
  && apt-get update && apt install -y curl vim \
  && curl --raw "https://raw.githubusercontent.com/jjsayleraxio/AxioShiny/devel/files/run.R" > /run.R \
  && curl --raw "https://raw.githubusercontent.com/jjsayleraxio/AxioShiny/devel/files/shiny-server.sh" > /usr/bin/shiny-server.sh \
  && chmod 755 /usr/bin/shiny-server.sh
