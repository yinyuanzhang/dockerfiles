FROM rocker/r-base:latest

RUN apt-get update \
 && apt-get install -y libgit2-dev libcurl4-openssl-dev zlib1g-dev \
                       libssl-dev libssh2-1-dev git \
 && install2.r remotes styler gh usethis withr fs knitr \
               purrr yaml base64enc tibble glue processx \
               crayon readr tidyr rlang lubridate gert \
 && installGithub.r rundel/ghclass \
 && rm -rf /tmp/* \
 && apt-get remove --purge -y $BUILDDEPS \
 && apt-get autoremove -y \
 && apt-get autoclean -y \
 && rm -rf /var/lib/apt/lists/*

CMD ["R"]
