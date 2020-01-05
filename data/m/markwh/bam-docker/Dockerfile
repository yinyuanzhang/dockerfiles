FROM jrnold/rstan:latest
MAINTAINER Mark Hagemann mark.hagemann@gmail.com

# Install dependencies for bamr
RUN install2.r --error \
    settings

RUN R -e "devtools::install_github('markwh/swotr', dependencies = FALSE)"
RUN R -e "devtools::install_github('markwh/bamr', ref = 'master', local = FALSE, dependencies = FALSE)"


# Get swot package and data
RUN wget https://osu.box.com/shared/static/h8gj8ugcqoxmkp9bqux9y3omszqay59t.rdata \
    -O /home/rstudio/reachdata.RData
