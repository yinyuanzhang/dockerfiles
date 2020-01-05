FROM  r-base
ENV VERSION 0.1

RUN apt update && apt install -y procps && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo 'install.packages(c("ggplot2"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \
  && Rscript /tmp/packages.R

COPY ideel_hist.R /bin/ideel_hist.R
RUN chmod +x /bin/ideel_hist.R