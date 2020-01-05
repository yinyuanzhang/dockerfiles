FROM rocker/shiny

RUN apt-get update
RUN apt-get install -y libssl-dev libssh2-1-dev
RUN R -e 'install.packages(c("devtools","shinyBS","jsonlite","ggplot2","DT"))'
RUN R -e 'devtools::install_github("iatgen/iatgen")'
RUN mv /srv/shiny-server/ /srv/shiny-server-

ADD . /srv/shiny-server

# RUN chmod 777 /var/log/shiny-server/iatui