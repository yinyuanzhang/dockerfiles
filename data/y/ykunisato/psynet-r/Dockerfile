FROM ykunisato/paper-r
MAINTAINER "Yoshihiko Kunisato" ykunisato@psy.senshu-u.ac.jp

# install R packages
RUN Rscript -e "library(devtools)"
RUN Rscript -e "install.packages('BiocManager')"
RUN Rscript -e "BiocManager::install(c('graph', 'RBGL', 'Rgraphviz'), update = TRUE, ask = FALSE)"
# RUN Rscript -e "devtools::install_github('sachaepskamp/psychonetrics')"
RUN Rscript -e "devtools::install_github('donaldRwilliams/GGMnonreg')"


RUN install2.r --error --deps TRUE \
qgraph \
IsingFit \
IsingSampler \
mlVAR \
graphicalVAR \
bootnet \
mgm \
NetworkComparisonTest \
networktools \
gimme \
NetworkToolbox \
ggraph \
pcalg \
networktree

RUN Rscript -e "install.packages('bnlearn',dependencies = TRUE)"
RUN Rscript -e "install.packages('semPlot',dependencies = TRUE)"
RUN Rscript -e "install.packages('EGAnet',dependencies = TRUE)"
RUN Rscript -e "devtools::install_github('donaldRwilliams/BGGM')"

# RUN Rscript -e "devtools::install_github('sachaepskamp/lvnet')"
