FROM rocker/shiny:3.5.1
LABEL maintainer="holken@gmail.com"
RUN export DEBIAN_FRONTEND=noninteractive; apt-get -y update \
  && apt-get install -y git-core \
	imagemagick \
	libmagic-dev \
	libmagick++-dev \
	make \
	pandoc \
	pandoc-citeproc \
	libssl-dev
RUN ["install2.r", "abind", "assertthat", "bindr", "bindrcpp", "class", "codetools", "colorspace", "CVST", "ddalpha", "DEoptimR", "dimRed", "dplyr", "DRR", "DT", "foreach", "foreign", "geometry", "ggplot2", "glmnet", "glue", "gower", "gtable", "htmltools", "htmlwidgets", "httr", "ipred", "iterators", "kernlab", "later", "lattice", "lava", "lazyeval", "lubridate", "magic", "magick", "MASS", "Matrix", "mnormt", "ModelMetrics", "munsell", "nlme", "nnet", "pillar", "pkgconfig", "plyr", "prodlim", "promises", "psych", "purrr", "RcppRoll", "recipes", "readr", "reshape2", "robustbase", "rpart", "scales", "sfsmisc", "shinythemes", "stringdist", "survival", "tibble", "tidyr", "tidyselect", "timeDate", "withr"]
RUN ["install2.r", "shinydashboard", "shinyjs", "devtools", "plotly", "flexdashboard", "zoo", "dygraphs", "xts"]
