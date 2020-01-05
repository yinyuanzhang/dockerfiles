# 3838
# /srv/shiny-server/
# /var/log/shiny-server/

FROM rocker/shiny

RUN apt-get install -y libssl-dev

COPY installpackages.r /

RUN Rscript /installpackages.r

EXPOSE 3838

CMD ["/usr/bin/shiny-server.sh"]
