FROM mbni/shiny-base

MAINTAINER Keqiang Li "lkq@umich.edu"

RUN R -e "install.packages('viridis', repos='https://cloud.r-project.org/')"

CMD ["R", "-e", "rmarkdown::run(file='/shinyApps/markdown_example/index.Rmd')"]
