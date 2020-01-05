FROM rocker/tidyverse:3.6.0
MAINTAINER "Ed Jee" edjee96@gmail.com
USER root



RUN apt-get update \
	&& apt-get install -y --no-install-recommends apt-utils ed libnlopt-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/


# Install packages1
RUN install2.r --error --deps TRUE \
    furrr \
    zoo \
    ggridges \
    skimr \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

# Install packages2
#RUN install2.r --error --deps FALSE \
#    xgboost \
#    ggstance \
#    caret \
#    vroom \
#    glmnet \
#    testthat \
#    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

COPY install.R /home/rstudio/
RUN chown -R  rstudio /home/rstudio/

RUN if [ -f /home/rstudio/install.R ]; then R --quiet -f /home/rstudio/install.R; fi








