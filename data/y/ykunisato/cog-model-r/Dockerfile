FROM ykunisato/paper-r
MAINTAINER "Yoshihiko Kunisato" ykunisato@psy.senshu-u.ac.jp

# Install JAGS
RUN apt-get update && apt-get install -y \
    jags \
    libgsl0-dev \
    tcl8.6-dev \
    tk8.6-dev\
    openmpi-bin\
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# install R packages
RUN Rscript -e "devtools::install_github('yxlin/ggdmc')"

RUN install2.r --error --deps TRUE \
rjags \
Rsolnp \
ReinforcementLearning \
MDPtoolbox \
rtdists \
DstarM \
hBayesDM \
truncdist \
statmod \
pracma \
snowfall \
rlecuyer \
vioplot
