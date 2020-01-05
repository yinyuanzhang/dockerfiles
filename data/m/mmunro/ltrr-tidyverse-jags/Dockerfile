FROM rocker/tidyverse:3.6.1

RUN apt-get update \
  && apt-get install -y \
    jags \
  && install2.r \
    coda \
    rjags
