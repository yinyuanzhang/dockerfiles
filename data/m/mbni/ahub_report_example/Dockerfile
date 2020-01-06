FROM mbni/shiny-base

MAINTAINER Keqiang Li "lkq@umich.edu"

RUN R -e "install.packages(c('ggplot2movies', 'plotly', 'webshot'), repos='https://cloud.r-project.org/')" && \
    R -e "webshot::install_phantomjs()"

CMD ["R", "-e", "shiny::runApp('/shinyApps/report')"]
