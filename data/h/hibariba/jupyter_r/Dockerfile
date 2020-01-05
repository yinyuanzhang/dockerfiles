# jupyter_r
# jupyterhub + R

FROM jupyter/jupyterhub

MAINTAINER hibariba

# install IRkernel --------

# install latest R on ubuntu trusty

#add r repo
RUN codename=$(lsb_release -c -s) \
    && echo "deb http://cran.rstudio.com/bin/linux/ubuntu $codename/" >> /etc/apt/sources.list  \
    && gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \
    && gpg -a --export E084DAB9 | apt-key add -

#install latest R
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y r-base r-base-dev \
    && apt-get install -y libxml2-dev libzmq3-dev libcurl4-openssl-dev

#install standard r packages
RUN ( echo "l <- '/usr/lib/R/site-library'" \
    && echo "r <- getOption('repos')" \
    && echo "r['CRAN'] <- 'http://cran.r-project.org'" \
    && echo "options(repos = r)" \
    && echo "install.packages('devtools', lib=l )" \
    && echo "install.packages('curl', lib=l)" \
    && echo "install.packages('RCurl', lib=l)" \
    ) | Rscript -e "source(file('stdin'))"

#install r packages from git
RUN ( echo "r <- getOption('repos')" \
    && echo "r['IRkernel'] <- 'http://irkernel.github.io/'" \
    && echo "options(repos = r)" \
    && echo "library(devtools)" \
    && echo "install_github('armstrtw/rzmq')" \
    && echo "install_github('IRkernel/repr')" \
    && echo "install_github('IRkernel/IRdisplay')"  \
    && echo "install_github('IRkernel/IRkernel')" \
    && echo "IRkernel::installspec(user = FALSE)" \
    ) | Rscript -e "source(file('stdin'))"

# -------------------------


VOLUME /data
# VOLUME /notebooks
# WORKDIR /notebooks

ENV USERNAME ""
ENV PASSWORD ""


ADD jupyterhub.sh /
RUN chmod u+x /jupyterhub.sh

CMD ["/jupyterhub.sh"]
