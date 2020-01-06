FROM rocker/shiny-verse:3.5.3

MAINTAINER Simon Coetzee "simon.coetzee@cshs.org"

# Install dependencies and Download and install shiny server
RUN apt-get update && apt-get install -y \
    git && \
    R -e "install.packages(c('BiocManager'), repos='https://cran.rstudio.com/')"

RUN R -e "BiocManager::install(c('shinyjs', 'plotly', 'shinythemes', 'shinyBS', 'shinycssloaders', 'prettydoc', 'shinyjqui', 'shinydashboard', 'shinyWidgets'))"
RUN R -e "BiocManager::install(c('DT', 'TTR', 'rlist', 'zoo', 'xts', 'quantmod', 'highcharter'))"
RUN R -e "BiocManager::install(c('DESeq2', 'edgeR', 'iheatmapr', 'apeglm', 'ashr', 'msigdbr', 'DOSE', 'org.Hs.eg.db', 'clusterProfiler', 'enrichplot', 'GSEABase'))" \
RUN R -e "BiocManager::install('devtools')" \
RUN R -e "devtools::install_github('yang-tang/shinyjqui')" && \
    cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/alpreyes/GENAVi.git /srv/shiny-server/GENAVi && \
	mkdir /var/log/shiny-server/genavi_log && chown shiny:shiny /var/log/shiny-server/genavi_log

EXPOSE 3838

CMD ["/usr/bin/shiny-server.sh"]
