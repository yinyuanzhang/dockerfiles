FROM inbobmk/rn2k

## This handle reaches Thierry
MAINTAINER "Thierry Onkelinx" thierry.onkelinx@inbo.be

## Install n2khelper from Github
RUN Rscript -e 'devtools::install_github("inbo/n2khelper", ref = "develop", upgrade_dependencies = FALSE)'

## Install n2kanalysis from Github
RUN Rscript -e 'devtools::install_github("thierryo/n2kanalysis", ref = "lincomd_list", upgrade_dependencies = FALSE)'

## Install abvanalysis from Github
RUN Rscript -e 'devtools::install_github("thierryo/abvanalysis", ref = "n2khelper_update", upgrade_dependencies = FALSE)'
