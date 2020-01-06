####### Dockerfile #######
FROM rocker/tidyverse:3.5.0

ENV DEBIAN_FRONTEND noninteractive

### install notes
	## install ed to avoid error during lme4 dependency install
	## install clang for speed and memory efficiency
	## set parameters
		# make dir
		# use clang
		# use multiple cores
	## install lme4
	## install lsmeans without suggests, to avoid the morass of rstan
	## install agricolae, ggstance, and nparLD
	## install rankFD; decline to install dependency RGtk2 because cannot get to work
	## install cowplot; decline to install dependency magick because cannot get to work

RUN sudo apt-get -y --no-install-recommends install \
		ed \
		clang \
	&& mkdir -p $HOME/.R/ \
	&& printf "CXX=clang++\n" >> $HOME/.R/Makevars \
	&& printf "options(mc.cores = parallel::detectCores())\n" >> /home/rstudio/.Rprofile \
	&& install2.r --error --deps TRUE --repos http://cran.stat.ucla.edu/ lme4 \
	&& Rscript --no-restore --no-save -e 'install.packages("lsmeans", dependencies=c("Depends","Imports"), repos=c("http://cran.stat.ucla.edu/"))' \
	&& install2.r --error --deps TRUE --repos http://cran.stat.ucla.edu/ \
		agricolae \
		ggstance \
		nparLD \
	&& Rscript --no-restore --no-save -e 'install.packages("rankFD", dependencies=c("Depends","Imports"), repos=c("http://cran.stat.ucla.edu/"))' \
	&& Rscript --no-restore --no-save -e 'install.packages("cowplot", dependencies=c("Depends","Imports"), repos=c("http://cran.stat.ucla.edu/"))'

