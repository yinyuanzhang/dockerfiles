FROM hawaiiteam/r-python:base-browser

LABEL maintainer="sjlee@encoredtech.com"

# install tex and some R packages
RUN sudo apt-get update && \
    sudo apt-get install -y pandoc texlive-xetex fonts-nanum fonts-nanum-extra
RUN sudo usermod -a -G staff ubuntu
RUN R -e 'install.packages(c("optparse", "rmarkdown", "knitr", "xtable", "dplyr", "magrittr", "ggplot2", "ggthemes", "lubridate", "caret"))'