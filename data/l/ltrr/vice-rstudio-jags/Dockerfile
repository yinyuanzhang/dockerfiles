FROM ltrr/vice-rstudio-tidyverse:3.6.0

RUN set -e \
  && apt-get update \
  && apt-get install --no-install-recommends -y \
    jags \
  && rm -rf /var/lib/apt/lists/* \
  && install2.r --error \
    coda \
    rjags
